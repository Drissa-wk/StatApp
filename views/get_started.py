import streamlit as st
import pandas as pd
from components.show_dataframe import show_dataframe, show_columns

def descriptive_statistic(selected_checkboxes):
    "Descriptive statistic of selected variables"
    # Select the empty container
    global empty_container1

    # Remove all the elements inside the container
    empty_container1.empty()

    # Categorical variables in selected checkboxes
    selected_cat_checkboxes = [cat for cat in selected_checkboxes if cat in st.session_state.cat_columns]

    # Numerical variables in selected checkboxes
    selected_num_checkboxes = [num for num in selected_checkboxes if num in st.session_state.num_columns]
    
    # Descriptive statistic for categorical variables
    data = {}
    for cat in selected_cat_checkboxes:
        df = st.session_state.dataframe
        stat = [] # Statistic for a specific variable

        # Count non missing values
        stat.append(df[cat].shape[0] - df[cat].isna().sum()) 

        # Number of missing values
        stat.append(df[cat].isna().sum()) 

        # Percentage of non missing values
        stat.append((df[cat].shape[0] - df[cat].isna().sum())/df[cat].shape[0] * 100) 

        #Number of unique values
        stat.append(df[cat].nunique())

        data[cat] = stat

 

    with empty_container1.container():
        st.header("Statistique Descriptive")

        # Categorical variables
        if len(selected_cat_checkboxes) > 0:
            st.subheader("Variables Catégorielles")
            st.write(pd.DataFrame(
                data,
                index=[
                    "# of valid values",
                    "# of missing values",
                    "'%' of valid values",
                    "# of unique values"
                ]
            ))

        # Numerical variables
        if len(selected_num_checkboxes) > 0:
            st.subheader("Variables Numériques")
            st.write(st.session_state.dataframe[selected_num_checkboxes].describe())


# Title
st.title("Calculatrice Statistique")
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
        descriptive_statistic(selected_checkboxes)