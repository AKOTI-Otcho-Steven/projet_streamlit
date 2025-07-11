import streamlit as st
import pandas as pd
import duckdb
import altair as alt

st.title("Application Web")

st.write("Bienvenue sur notre application web interactive")

st.subheader("Téléversement de fichier CSV")

fichier_csv = st.file_uploader("Importez votre fichier CSV", type=["csv"])    #Téléversement de fichier CSV

if fichier_csv is not None:
    df = pd.read_csv(fichier_csv)
    st.write("Aperçu des données :")
    st.dataframe(df)                                                          #############################
   

# Chargement de data_frame
data_frame = pd.read_csv("amazon_prime_titles.csv")

# Connexion à une base DuckDB en mémoire (temporaire)
connexion = duckdb.connect(database=':memory:')

# Enregistrement de la data_frame dans le contexte DuckDB
connexion.register("data_frame_temp", data_frame)

# Création d'une table "amazon_prime_titles" avec les données du DataFrame pandas
connexion.execute("CREATE TABLE amazon_prime_titles AS SELECT * FROM data_frame_temp")

# Interrogation des données

query = """
SELECT *
FROM amazon_prime_titles
"""

result_df = connexion.execute(query).df()   # Résultat sous forme de DataFrame pandas
#st.dataframe(result_df)                     # Affichage du résultat

#######################################################


st.sidebar.markdown("## Filtres")


# — Pays (country)
all_countries = sorted(data_frame["country"].dropna().unique())
country_sel = st.sidebar.multiselect("Pays (Country)", all_countries)

# — Type
all_types = sorted(data_frame["type"].unique())
type_sel = st.sidebar.multiselect("Type", all_types)

# --------- Construction dynamique du WHERE ---------
where_clauses = []

# Région
if country_sel:
    escaped_countries = [c.replace("'", "''") for c in country_sel]
    country_list = ",".join(f"'{c}'" for c in escaped_countries)
    where_clauses.append(f"country IN ({country_list})")

# Type
if type_sel:
    escaped_types = [t.replace("'", "''") for t in type_sel]
    type_list = ",".join(f"'{t}'" for t in escaped_types)
    where_clauses.append(f"type IN ({type_list})")

if where_clauses:
    where_sql = " AND ".join(where_clauses)
    base_sql = f"SELECT * FROM data_frame_temp WHERE {where_sql}"
else:
    base_sql = "SELECT * FROM data_frame_temp"

# ---------  Application des filtres ---------
filtered_df = connexion.sql(base_sql).df()
st.success(f"✅  Filtres appliqués • {len(filtered_df):,} lignes sélectionnées")

# ---------  KPI & visualisations ---------
st.markdown("###  Indicateurs clés (4 graphes distincts)")

# KPI 1 : Movies / TV Shows par année (ligne)
year_df = connexion.sql(f"""
    WITH filt AS ({base_sql})
    SELECT release_year AS year, COUNT(*) AS nombre
    FROM filt
    GROUP BY year
    ORDER BY year
""").df()

kpi_year = alt.Chart(year_df).mark_line(point=True).encode(
    x=alt.X("year:O", title="Année de sortie"),
    y=alt.Y("nombre:Q", title="Nombre de Movies / TV Shows"),
    tooltip=["year", "nombre"]
).properties(height=300, title="📈 Movies / TV Shows par année")

# KPI 2 : Répartition Movie / TV Show (donut)
type_df = connexion.sql(f"""
    WITH filt AS ({base_sql})
    SELECT type, COUNT(*) AS nombre
    FROM filt
    GROUP BY type
""").df()

kpi_type = alt.Chart(type_df).mark_arc(innerRadius=60).encode(
    theta=alt.Theta("nombre:Q", stack=True),
    color=alt.Color("type:N", legend=None),
    tooltip=["type", "nombre"]
).properties(height=300, title="🍩 Répartition Movie / TV Show")

# KPI 3 : Top 10 pays (bulles)
country_df = connexion.sql(f"""
    WITH filt AS ({base_sql})
    SELECT country, COUNT(*) AS nombre
    FROM filt
    GROUP BY country
    ORDER BY nombre DESC
    LIMIT 10
""").df()

kpi_country = alt.Chart(country_df).mark_circle().encode(
    y=alt.Y("country:N", sort="-x", title="Pays"),
    x=alt.X("nombre:Q", title="Nombre total de Movies / TV Shows"),
    size=alt.Size("nombre:Q", legend=None),
    tooltip=["country", "nombre"]
).properties(height=300, title="🔵 Top 10 pays (bulles)")

# KPI 4 : Répartition par note (rating)
rating_df = connexion.sql(f"""
    WITH filt AS ({base_sql})
    SELECT rating, COUNT(*) AS nombre
    FROM filt
    GROUP BY rating
    ORDER BY rating
""").df()

kpi_rating = alt.Chart(rating_df).mark_area(interpolate="step-after").encode(
    x=alt.X("rating:N", title="Note"),
    y=alt.Y("nombre:Q", title="Total"),
    tooltip=["rating", "nombre"]
).properties(height=300, title="🏞️ Répartition par note")

# ---------  Affichage en grille 2×2 ---------
col1, col2 = st.columns(2)
with col1:
    st.altair_chart(kpi_year, use_container_width=True)
    st.altair_chart(kpi_country, use_container_width=True)
with col2:
    st.altair_chart(kpi_type, use_container_width=True)
    st.altair_chart(kpi_rating, use_container_width=True)
    
# ---------  Aperçu des données filtrées ---------
with st.expander("Afficher un aperçu du DataFrame filtré"):
    st.dataframe(filtered_df)

#########################################################








