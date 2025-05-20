import streamlit as st
import pandas as pd


def baseDonnee():
    try:
        donnee = pd.read_excel(
            "https://kf.kobotoolbox.org/api/v2/assets/aJnmz4mHoG9XJMMYv6pFMX/export-settings/esftSBqgXVSd5L7o8M6LUkL/data.xlsx"
        )
        # bd = donnee.copy()
        donnee["Début"] = donnee["start"].dt.date
        donnee["Envoie"] = donnee["end"].dt.date
        donnee["Date_Naissance"] = donnee["Date"].dt.date
        donnee["Téléphone"] = pd.to_numeric(donnee["Tel"])
        donnee.drop(
            columns=[
                "start",
                "end",
                "Date",
                "Tel",
                "_Localisation_latitude",
                "_Localisation_longitude",
                "_Localisation_altitude",
                "_Localisation_precision",
                "Photo",
                "Photo_URL",
                "Une petite vidéo",
                "Une petite vidéo_URL",
                "Filière spécialisé.1",
                "Filière spécialisé.2",
                "Filière spécialisé.3",
                "Filière spécialisé.4",
                "Prénom.1",
                "Région.1",
                "_uuid",
                "_submission_time",
                "_validation_status",
                "_notes",
                "_status",
                "_submitted_by",
                "__version__",
                "_tags",
                "_index",
                "_id",
            ],
            inplace=True,
        )
        return donnee
    except Exception as e:
        st.write("Erreur lors de la lecture du fichier Excel :", e)
        st.stop()


try:
    st.write("Lecture de la base")
    st.write(baseDonnee().sort_values(by="Envoie", ascending=False))
except Exception as a:
    st.write("Erreur lors de la lecture de la base :", a)
