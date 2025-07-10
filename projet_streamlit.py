import streamlit as st
import pandas as pd

st.title("Application Web")

st.write("Bienvenue sur notre application web interactive")

st.subheader("Téléversement de fichier CSV")

fichier_csv = st.file_uploader("Importez votre fichier CSV", type=["csv"])    #Téléversement de fichier CSV

if fichier_csv is not None:
    df = pd.read_csv(fichier_csv)
    st.write("Aperçu des données :")
    st.dataframe(df)                                                          #############################
   
import duckdb

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
st.dataframe(result_df)                     # Affichage du résultat








