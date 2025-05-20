# Importation des bibliothéques
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="ND_Dashbaord", page_icon="🎢", layout="centered")
# Page du projet
dasboaord = st.Page(
    page="dashbaord.py",
    title="Dashbaord",
    default=True,
)
accueil = st.Page(
    page="accueil.py",
    title="Données",
    icon="",
)
connexion = st.Page(
    page="connexion.py",
    title="Identification",
    icon="",
)
# Navigation des pages
pg = st.navigation({"Accueil": [accueil], "Tableau de bord": [dasboaord]})

dire = Path(__file__).parent if "__file__" in locals() else Path.cwd()
fichier_css = "styl/style.css"
titre_page = "Abdoulaye NDAO"
# icone_page = "static/Plan de travail 1.png"
with open(fichier_css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Configuration de page

# st.logo(icone_page)
pg.run()
