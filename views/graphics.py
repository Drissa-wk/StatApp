import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from components.show_dataframe import show_dataframe, show_columns
from components.graphs import HistogramPlotter, PiePlotter, BoxPlotter, BarPlotter

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
        HistogramPlotter(st.session_state.dataframe, selected_checkboxes).plot()
        BoxPlotter(st.session_state.dataframe, selected_checkboxes).plot()
        BarPlotter(st.session_state.dataframe, selected_checkboxes).plot()
        PiePlotter(st.session_state.dataframe, selected_checkboxes).plot()



# Title
st.title("Graphiques")
show_dataframe()

#list of columns
checkboxes_columns = show_columns(st.session_state.dataframe)
# We create an empty container. It'll be updated any time the 
# user select a column of the dataset
empty_container1 = st.empty()


selected_checkboxes = []
for label, checkbox in checkboxes_columns.items():
    if checkbox:
        selected_checkboxes.append(label)
draw_graphics(selected_checkboxes)