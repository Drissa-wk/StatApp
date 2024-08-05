import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from components.show_dataframe import show_dataframe, show_columns
from components.graphs import CorrPlotter

def draw_graphics(selected_checkboxes):
    # Select the empty container
    global empty_container1

    # Remove all the elements inside the container
    empty_container1.empty()

    # Categorical variables in selected checkboxes
    selected_cat_checkboxes = [cat for cat in selected_checkboxes if cat in st.session_state.cat_columns]

    # Numerical variables in selected checkboxes
    selected_num_checkboxes = [num for num in selected_checkboxes if num in st.session_state.num_columns]

    with empty_container1.container():
        CorrPlotter(st.session_state.dataframe, selected_checkboxes).plot()




# Title
st.title("Corrélation De Pearson")

st.write("L'analyse des corrélations de Pearson vous permet d'explorer les relations \
    linéaires entre vos variables numériques. Sur cette page, vous pourrez calculer \
         la matrice de corrélation de Pearson et visualiser les résultats\
         . Cette information sera cruciale pour comprendre quelles \
         variables sont étroitement liées et pourront être utilisées dans vos futurs modèles.")

# Dataframe
show_dataframe()

#list of columns
checkboxes_columns = show_columns(st.session_state.dataframe, cat_disabled=True)


# We create an empty container. It'll be updated any time the 
# user select a column of the dataset
empty_container1 = st.empty()


selected_checkboxes = []
for label, checkbox in checkboxes_columns.items():
    if checkbox:
        selected_checkboxes.append(label)
draw_graphics(selected_checkboxes)