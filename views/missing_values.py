import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from components.show_dataframe import show_dataframe

def missing_values(df):
    "Operations to handle missing values"

    # If there are missing values
    nb_na = df.isna().sum().sum()
    if nb_na > 0:

        # Statistics on missing values
        st.header("Statistiques sur les valeurs manquantes")
        data = {}
        for col in df.columns.to_list():
            stat_missing_values = [] # Statistic of missing values for a specific variable

            # Number of missing values
            stat_missing_values.append(df[col].isna().sum()) 

            # Percentage of non missing values
            stat_missing_values.append(round(df[col].isna().sum()/df.shape[0] * 100, 2) )
            data[col] = stat_missing_values

        stat_missing_values_df = pd.DataFrame(
                data,
                index=[
                    "# of missing values",
                    "'%' of missing values"
                ]
            )
        st.write(stat_missing_values_df)
        
        # Visualization of missing values
        st.header("Visualisation des valeurs manquantes")

        fig, ax = plt.subplots(figsize=(10, 5))
        fig.set_facecolor('#080A0D')
        sns.heatmap(df.isna(),
                            yticklabels=False,
                            cbar=False, 
                             cmap='viridis', ax=ax)
        ax.tick_params(axis="both", colors="#D5DAE5")
        st.pyplot(fig)

        # Treatment options
        st.header("Options de traitement")

        st.write("Choisissez une methode de traitement")
        st.warning("Le traitement des valeurs manquantes est une tâche \
                   très délicate car peut énormement biaiser les données. \
                   Nous vous recommandons de le faire en fonction de vos besoins \
                   et avec beaucoup de parcimonie.")

        tab1, tab2, tab3 = st.tabs(
            [
                "Delete Records With Missing Values",
                "Delete Columns with Missing Values",
                "Inputations"
            ]
        )

        with tab1:
            st.subheader("Suppression des enregistrements avec des valeurs manquantes")

            # Number of records with missing values
            nb_records_missing_values = df.isna().any(axis=1).sum()

            # Percentage of records with missing values
            per_records_missing_values = nb_records_missing_values / df.shape[0] * 100

            container1_tab1 = st.container()
            with container1_tab1:
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(
                        label="Nombre d'enregistrements",
                        value=f"{nb_records_missing_values}"
                    )
                with col2:
                    st.metric(
                        label="Pourcentage",
                        value=f"{round(per_records_missing_values, 2)} %"
                    )
            
            if per_records_missing_values > 5:
                st.error("Nous vous déconseillons fortement de supprimer ces enregistrements \
                    car cette suppression engendrera une perte considérable de données. \
                         Nous vous conseillons à la place de faire des imputations. ",
                         icon=":material/error:")
            else:
                st.warning("Ces enregistrements peuvent être supprimés mais ce processus \
                    engendrera toutefois une perte de données ",
                         icon=":material/warning:")
                
            # Suppression des enregistrements avec valeurs manquantes
            # Et redirection vers la page d'accueil   
            if st.page_link("views/get_started.py",label="Supprimer", icon=":material/delete:"):
                new_df = df.dropna()
                st.session_state.dataframe = new_df

        with tab2:
            st.subheader("Suppression des colonnes avec des valeurs manquantes")

            st.write(stat_missing_values_df)
            st.write("Vous devez sélectionner le pourcentage maximal admissible \
                     de valeurs manquantes par colonne. Si une colonne en possède plus, \
                     elle est automatiquement supprimée.")
            st.info("Ce processus n'assure pas la suppression totale des valeurs manquantes. \
                    Vous devriez sans doute ajouter à cela des imputations.",
                    icon=":material/info:")
            
            col1, col2 = st.columns(2)
            with col1:
                # Treshold of percentage of missing values
                threshold = st.slider("Choisissez le pourcentage maximal",
                                     0, 100, 20)
            with col2:
                # Select columns
                missing_values_columns = stat_missing_values_df.loc["'%' of missing values"][stat_missing_values_df.loc["'%' of missing values"] > threshold].index.to_list()
                if len(missing_values_columns) > 0:
                    st.write(f"Les variables suivantes seront supprimées :")
                    st.markdown(
                       f" **{', '.join(missing_values_columns)}**",
                       unsafe_allow_html=True
                    )

                    if st.page_link("views/get_started.py",label="Supprimer", icon=":material/delete:"):
                        new_df = df.drop(columns=missing_values_columns)
                        st.session_state.dataframe = new_df


        with tab3:
            st.subheader("Imputation")

            st.write("L'imputation est un procédé qui consiste à remplacer les valeurs manquantes \
                     d'un dataset par des valeurs estimées notamment la moyenne(mean), \
                     la médiane (median) et le mode (mode)")
            st.info("Ce processus possède des limites car ne prend pas en compte les relations \
                    potentielles entre les variables",
                    icon=":material/info:")

            st.write("Choisissez une méthode d'imputation")

            col1, col2, col3 = st.columns(3)

            with col1:
                # Mean
                if st.page_link("views/get_started.py",label="Mean", icon=":material/info:"):
                        st.session_state.dataframe = df.fillna(df.mean())
            
            with col2:
                # Median
                if st.page_link("views/get_started.py",label="Median", icon=":material/info:"):
                        st.session_state.dataframe = df.fillna(df.median())

            with col3:
                # Mode 
                if st.page_link("views/get_started.py",label="Mode", icon=":material/info:"):
                        st.session_state.dataframe = df.fillna(df.mode().iloc[0])


# Title
st.title("Missing Values")

st.write("Les valeurs manquantes peuvent avoir un impact important sur l'analyse de vos données. \
         Cette page vous permettra d'identifier et de traiter ces valeurs manquantes de manière \
         efficace. Vous pourrez choisir parmi différentes méthodes de remplacement, \
            comme la moyenne, la médiane ou l'imputation plus avancée, afin d'obtenir un \
                jeu de données complet et prêt à être analysé.")

# Dataframe
show_dataframe()
missing_values(st.session_state.dataframe)