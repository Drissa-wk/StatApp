import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram
class HistogramPlotter:
    def __init__(self, data, selected_checkboxes):
        self.data = data
        self.selected_checkboxes = selected_checkboxes
        # self.empty_container = empty_container
        self.fig, self.ax = plt.subplots()
        
        # Categorical variables in selected checkboxes
        self.selected_cat_checkboxes = [cat for cat in self.selected_checkboxes if cat in st.session_state.cat_columns]

        # Numerical variables in selected checkboxes
        self.selected_num_checkboxes = [num for num in self.selected_checkboxes if num in st.session_state.num_columns]


    def one_var_histogram(self):
        "Histogram for one numerical variable"
        if len(self.selected_num_checkboxes) == 1 and len(self.selected_cat_checkboxes) == 0:


            st.header("Histogramme")
            col1, col2, col3 = st.columns(3)
            with col1:
                color_hist = st.color_picker("Modifier la couleur", value="#F23869")
                
            with col2:
                kde = st.toggle("Distribution Normale", value=False)

            with col3:
                bins = st.slider("Bins", 10, 100, 50)
            
            self.fig.set_facecolor('#080A0D')
            sns.histplot(data=self.data, 
                            x=self.selected_num_checkboxes[0],  
                            color=color_hist, 
                            kde=kde,
                            bins=bins,
                            ax=self.ax).set_facecolor('#080A0D')
            self.ax.set_xlabel(self.selected_num_checkboxes[0], color="#D5DAE5")
            self.ax.set_ylabel("count", color="#D5DAE5")
            self.ax.grid(color="#D5DAE5", linewidth=0.2)
            self.ax.tick_params(axis="both", colors="#D5DAE5")
            st.pyplot(self.fig)

    def two_var_histogram(self):
        "Histogram for 02 variables (one numerical and one categorical)"
        if len(self.selected_num_checkboxes) == 1 and len(self.selected_cat_checkboxes) == 1:

            st.header("Histogramme")
            col1, col2 = st.columns(2)
            with col1:
                kde = st.toggle("Distribution Normale", value=False)

            with col2:
                bins = st.slider("Bins", 10, 100, 50)
            
            self.fig.set_facecolor('#080A0D')
            sns.histplot(data=self.data, 
                            x=self.selected_num_checkboxes[0],  
                            hue=self.selected_cat_checkboxes[0], 
                            kde=kde,
                            bins=bins,
                            ax=self.ax).set_facecolor('#080A0D')
            self.ax.set_xlabel(self.selected_num_checkboxes[0], color="#D5DAE5")
            self.ax.set_ylabel("count", color="#D5DAE5")
            self.ax.grid(color="#D5DAE5", linewidth=0.2)
            self.ax.tick_params(axis="both", colors="#D5DAE5")
            st.pyplot(self.fig)

    def plot(self):
        "Plot histogram"
        self.one_var_histogram()
        self.two_var_histogram()

# Boxplot
class BoxPlotter:
    def __init__(self, data, selected_checkboxes):
        self.data = data
        self.selected_checkboxes = selected_checkboxes
        # self.empty_container = empty_container
        self.fig, self.ax = plt.subplots()
        
        # Categorical variables in selected checkboxes
        self.selected_cat_checkboxes = [cat for cat in self.selected_checkboxes if cat in st.session_state.cat_columns]

        # Numerical variables in selected checkboxes
        self.selected_num_checkboxes = [num for num in self.selected_checkboxes if num in st.session_state.num_columns]


    def one_var_boxplot(self):
        "Boxplot for one numerical variable"
        if len(self.selected_num_checkboxes) == 1 and len(self.selected_cat_checkboxes) == 0:


            st.header("Boxplot")
            col1, col2 = st.columns(2)
            with col1:
                color_boxplot = st.color_picker("Modifier la couleur du boxplot", value="#F23869")
                
            with col2:
                point = st.toggle("Afficher les points", value=False)
            
            self.fig.set_facecolor('#080A0D')
            sns.boxplot(data=self.data, 
                            y=self.selected_num_checkboxes[0],
                            color=color_boxplot, 
                            ax=self.ax).set_facecolor('#080A0D')
            if point:
                sns.stripplot(
                            data=self.data, 
                            y=self.selected_num_checkboxes[0],
                            jitter=0.1,
                            ax=self.ax
                )
                
            self.ax.set_xlabel(self.selected_num_checkboxes[0], color="#D5DAE5")
            self.ax.set_ylabel("count", color="#D5DAE5")
            self.ax.grid(color="#D5DAE5", linewidth=0.2)
            self.ax.tick_params(axis="both", colors="#D5DAE5")
            st.pyplot(self.fig)

    def two_var_boxplot(self):
        "Boxplot for 02 variables (one numerical and one categorical)"
        if len(self.selected_num_checkboxes) == 1 and len(self.selected_cat_checkboxes) == 1:

            st.header("Boxplot")
            
            self.fig.set_facecolor('#080A0D')
            sns.boxplot(data=self.data, 
                            x=self.selected_cat_checkboxes[0],
                            y=self.selected_num_checkboxes[0], 
                            ax=self.ax).set_facecolor('#080A0D')
            self.ax.set_xlabel(self.selected_cat_checkboxes[0], color="#D5DAE5")
            self.ax.set_ylabel(self.selected_num_checkboxes[0], color="#D5DAE5")
            self.ax.grid(color="#D5DAE5", linewidth=0.2)
            self.ax.tick_params(axis="both", colors="#D5DAE5")
            st.pyplot(self.fig)

    def three_var_boxplot(self):
        "Boxplot for 03 variables (one numerical and two categorical)"
        if len(self.selected_num_checkboxes) == 1 and len(self.selected_cat_checkboxes) == 2:

            st.header("Boxplot")
            
            self.fig.set_facecolor('#080A0D')
            sns.boxplot(data=self.data, 
                            x=self.selected_cat_checkboxes[0],
                            y=self.selected_num_checkboxes[0], 
                            hue=self.selected_cat_checkboxes[1],
                            ax=self.ax).set_facecolor('#080A0D')
            self.ax.set_xlabel(self.selected_cat_checkboxes[0], color="#D5DAE5")
            self.ax.set_ylabel(self.selected_num_checkboxes[0], color="#D5DAE5")
            self.ax.grid(color="#D5DAE5", linewidth=0.2)
            self.ax.tick_params(axis="both", colors="#D5DAE5")
            st.pyplot(self.fig)


    def plot(self):
        "Plot boxplot"
        self.one_var_boxplot()
        self.two_var_boxplot()
        self.three_var_boxplot()

# Barplot
class BarPlotter:
    def __init__(self, data, selected_checkboxes):
        self.data = data
        self.selected_checkboxes = selected_checkboxes
        self.fig, self.ax = plt.subplots()
        
        # Categorical variables in selected checkboxes
        self.selected_cat_checkboxes = [cat for cat in self.selected_checkboxes if cat in st.session_state.cat_columns]

        # Numerical variables in selected checkboxes
        self.selected_num_checkboxes = [num for num in self.selected_checkboxes if num in st.session_state.num_columns]

    def plot(self):
        if len(self.selected_num_checkboxes) == 0 and len(self.selected_cat_checkboxes) == 1:

            st.header("Diagramme à Barres")

            # number of values for each categorie
            nb_per_categorie = self.data[self.selected_cat_checkboxes[0]].value_counts()

            # Bar diagram
            self.fig.set_facecolor('#080A0D')
            sns.barplot(
                                x=nb_per_categorie.index,
                                y=nb_per_categorie,
                                ax=self.ax
                            ).set_facecolor('#080A0D')
            self.ax.set_xlabel(self.selected_cat_checkboxes[0], color="#D5DAE5")
            self.ax.set_ylabel("count", color="#D5DAE5")
            self.ax.grid(color="#D5DAE5", linewidth=0.2)
            self.ax.tick_params(axis="both", colors="#D5DAE5")
            st.pyplot(self.fig)

# Pie Plot
class PiePlotter:
    def __init__(self, data, selected_checkboxes):
        self.data = data
        self.selected_checkboxes = selected_checkboxes
        self.fig, self.ax = plt.subplots()
        
        # Categorical variables in selected checkboxes
        self.selected_cat_checkboxes = [cat for cat in self.selected_checkboxes if cat in st.session_state.cat_columns]

        # Numerical variables in selected checkboxes
        self.selected_num_checkboxes = [num for num in self.selected_checkboxes if num in st.session_state.num_columns]

    def plot(self):
        if len(self.selected_num_checkboxes) == 0 and len(self.selected_cat_checkboxes) == 1:

            st.header("Diagramme Circulaire")

            # number of values for each categorie
            nb_per_categorie = self.data[self.selected_cat_checkboxes[0]].value_counts()

            # Pie diagram
            self.fig.set_facecolor('#080A0D')
            self.ax.pie(
                x=nb_per_categorie,
                labels=nb_per_categorie.index,
                autopct='%1.1f%%'
            )
            self.ax.legend(nb_per_categorie.index, title=self.selected_cat_checkboxes[0], loc="upper right")
            self.ax.axis("equal")
            st.pyplot(self.fig)

# Boxplot
class ScatterPlotter:
    def __init__(self, data, selected_checkboxes):
        self.data = data
        self.selected_checkboxes = selected_checkboxes
        # self.empty_container = empty_container
        self.fig, self.ax = plt.subplots()
        
        # Categorical variables in selected checkboxes
        self.selected_cat_checkboxes = [cat for cat in self.selected_checkboxes if cat in st.session_state.cat_columns]

        # Numerical variables in selected checkboxes
        self.selected_num_checkboxes = [num for num in self.selected_checkboxes if num in st.session_state.num_columns]

    def two_var_scatterplot(self):
        "Scatterplot for 02 numerical variables"
        if len(self.selected_num_checkboxes) == 2 and len(self.selected_cat_checkboxes) == 0:

            st.header("Nuage de points")
            
            # Regression line
            reg_line = st.toggle("Droite de Regression", value=False)

            self.fig.set_facecolor('#080A0D')
            sns.scatterplot(data=self.data, 
                            x=self.selected_num_checkboxes[0],
                            y=self.selected_num_checkboxes[1], 
                            ax=self.ax).set_facecolor('#080A0D')
            self.ax.set_xlabel(self.selected_num_checkboxes[0], color="#D5DAE5")
            self.ax.set_ylabel(self.selected_num_checkboxes[1], color="#D5DAE5")
            self.ax.grid(color="#D5DAE5", linewidth=0.2)
            self.ax.tick_params(axis="both", colors="#D5DAE5")

            # Regression line
            if reg_line:
                sns.regplot(
                            data=self.data, 
                            x=self.selected_num_checkboxes[0],
                            y=self.selected_num_checkboxes[1], 
                            line_kws={"color": "#F23869"},
                            ax=self.ax
                )

            st.pyplot(self.fig)

    def three_var_scatterplot(self):
        "Scatterplot for 03 variables (two numerical and one categorical)"
        if len(self.selected_num_checkboxes) == 2 and len(self.selected_cat_checkboxes) == 1:

            st.header("Nuage de points")
            
            # Regression line
            reg_line = st.toggle("Droite de Regression", value=False)

            self.fig.set_facecolor('#080A0D')
            sns.scatterplot(data=self.data, 
                            x=self.selected_num_checkboxes[0],
                            y=self.selected_num_checkboxes[1], 
                            hue=self.selected_cat_checkboxes[0],
                            ax=self.ax).set_facecolor('#080A0D')
            self.ax.set_xlabel(self.selected_num_checkboxes[0], color="#D5DAE5")
            self.ax.set_ylabel(self.selected_num_checkboxes[1], color="#D5DAE5")
            self.ax.grid(color="#D5DAE5", linewidth=0.2)
            self.ax.tick_params(axis="both", colors="#D5DAE5")

            # Regression line
            if reg_line:
                sns.regplot(
                            data=self.data, 
                            x=self.selected_num_checkboxes[0],
                            y=self.selected_num_checkboxes[1], 
                            line_kws={"color": "#F23869"},
                            ax=self.ax
                )

            st.pyplot(self.fig)
    

    def plot(self):
        "Plot scatterplot"
        self.two_var_scatterplot()
        self.three_var_scatterplot()

# Boxplot
class CorrPlotter:
    def __init__(self, data, selected_checkboxes):
        self.data = data
        self.selected_checkboxes = selected_checkboxes
        # self.empty_container = empty_container
        self.fig, self.ax = plt.subplots(figsize=(8, 5))
        
        # Categorical variables in selected checkboxes
        self.selected_cat_checkboxes = [cat for cat in self.selected_checkboxes if cat in st.session_state.cat_columns]

        # Numerical variables in selected checkboxes
        self.selected_num_checkboxes = [num for num in self.selected_checkboxes if num in st.session_state.num_columns]

    def all_var_corrplot(self):
        "Corr plot for all numerical variables"
        if len(st.session_state.num_columns) > 0 and len(self.selected_cat_checkboxes) == 0:

            st.header("Corrélation pour toutes les variables numériques")
            
            self.fig.set_facecolor('#080A0D')
            sns.heatmap(data=self.data[st.session_state.num_columns].corr(), 
                            annot=True, 
                            cbar=False,
                            ax=self.ax).set_facecolor('#080A0D')
            self.ax.tick_params(axis="both", colors="#D5DAE5")
            st.pyplot(self.fig)

    def selected_var_corrplot(self):
        "Corr plot for all selected numerical variables"
        if len(self.selected_num_checkboxes) > 1 and len(self.selected_cat_checkboxes) == 0:

            st.header("Corrélation pour les variables selectionnées")
            
            self.fig.set_facecolor('#080A0D')
            sns.heatmap(data=self.data[self.selected_num_checkboxes].corr(), 
                            annot=True, 
                            cbar=False,
                            ax=self.ax).set_facecolor('#080A0D')
            self.ax.tick_params(axis="both", colors="#D5DAE5")
            st.pyplot(self.fig)

    def plot(self):
        "Plot scatterplot"
        self.selected_var_corrplot()
        self.all_var_corrplot()

