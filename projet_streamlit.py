import streamlit as st 
import pandas as pd

st.title("Application Web")

st.write("Bienvenue sur notre application web interactive")

st.subheader("Téléversement de fichier CSV")

fichier_csv = st.file_uploader("Importez votre fichier CSV", type=["csv"])

if fichier_csv is not None:
    df = pd.read_csv(fichier_csv)
    st.write("Aperçu des données :")
    st.dataframe(df)



