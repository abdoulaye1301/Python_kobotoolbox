import streamlit as st
import pandas as pd
from accueil import baseDonnee
import matplotlib.pyplot as plt
import seaborn as sns

try:
    donne = pd.DataFrame(baseDonnee())
    col = st.columns(2)
    varquant = donne.select_dtypes(include="number").columns.to_list()
    varquali = donne.select_dtypes(exclude="number").columns.to_list()
    varquali.remove("Début")
    varquali.remove("Envoie")
    varquali.remove("Date_Naissance")
    col[0].write(donne.describe())
    col[1].write(donne[varquali].describe().T)

    # Statistique descriptive

    # Les graphiques
    # Visualisation des variables quantitatives
    for i in range(5):
        col[0].write("\n")
    col[0].text("Représantation graphique des variables quantitatives")
    var = st.sidebar.selectbox("Choisire la variable", varquant)

    don, ax = plt.subplots()
    ax = sns.histplot(
        data=donne, x=var, stat="density", label="Histogramme", color="green"
    )
    sns.kdeplot(data=donne, x=var, label="Densité", color="red")
    plt.title(f"Histogramme de {var}")
    plt.xlabel(var)
    plt.ylabel("Densité")
    col[0].pyplot(don)

    # Visualisation des variables qualitatives
    col[1].text("Représantation graphique des variables qualitatives")
    varia = st.sidebar.selectbox("Choisire la variable", varquali)

    don, ax = plt.subplots()

    ax = sns.countplot(data=donne, x=varia)
    plt.title(f"Diagramme en barre de {varia}")
    plt.ylabel("Frequence")
    plt.xlabel(varia)
    col[1].pyplot(don)


except Exception as e:
    st.write("Erreur lors de la lecture du fichier Excel :", e)
