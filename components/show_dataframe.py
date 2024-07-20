import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def number_missing_values(df):
    "count the number of missing values in a dataframe"
    nb_na = df.isna().sum().sum()
    if nb_na > 0:
        st.warning("Votre jeu de données contient des valeurs manquantes.\
                   vous devrez les traiter avant de faire des analyses")
        
def show_columns(df):
    "shows the numerical and categorical variables of a dataframe"

    cat_columns = [] #categorical variables
    num_columns = [] #numerical variables

    for col in df.columns.to_list():
        if df[col].dtype == "object" or df[col].nunique() < 6:
            cat_columns.append(col)
        else:
            num_columns.append(col)

    #we save them into session variables
    st.session_state.cat_columns = cat_columns
    st.session_state.num_columns = num_columns


    #show in the app
    checkboxes_columns = {}
    with st.container():
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            st.subheader("Variables Catégorielles")
            c1, c2 = st.columns(2)
            i = 0
            for col in st.session_state.cat_columns:
                if i%2 == 0:
                    with c1:
                        checkboxes_columns[col] = st.checkbox(col)
                else:
                    with c2:
                        checkboxes_columns[col] = st.checkbox(col)
                i+=1
        with col2:
            st.subheader("Variables Numériques")
            c1, c2 = st.columns(2)
            i = 0
            for col in st.session_state.num_columns:
                if i%2 == 0:
                    with c1:
                        checkboxes_columns[col] = st.checkbox(col)
                else:
                    with c2:
                        checkboxes_columns[col] = st.checkbox(col)
                i+=1
    
    return checkboxes_columns


def show_dataframe():
    
    # Default dataframe
    df = pd.DataFrame({
        'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Age': [25, 32, 41, 20, 35, 29, 38, 33, 27, 30],
        'Salaire': [100000, 300000, 235000, 450000, 730000, 120000, 50000, 300000, 100000, 350000]
    })
    if "dataframe" not in st.session_state:
        st.session_state.dataframe = df

    with st.container():
        #header 1
        st.header("1. Dataset")

        #button to change the dataframe
        with st.expander("Importer un dataset"):
            change_df = st.file_uploader("Cliquez ici pour choisir un autre jeu de données",
                                        type=["csv"],
                                        accept_multiple_files=False)
            if change_df:
                st.session_state.dataframe = pd.read_csv(change_df)

        #show the dataframe in the app
        st.data_editor(st.session_state.dataframe, width=5000)
        st.markdown(
            f"Ce dataset possède **{st.session_state.dataframe.shape[0]}** lignes \
                et **{st.session_state.dataframe.shape[1]}** colonnes",
            unsafe_allow_html=True
        )
        number_missing_values(st.session_state.dataframe)