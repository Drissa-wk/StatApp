import streamlit as st
import os

def load_css():
    "load css"
    css_file = os.path.join("assets", "css", "style.css")
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

get_started_page = st.Page(
    page="views/get_started.py",
    title="Get Started",
    default=True
)

missing_values_page = st.Page(
    page="views/missing_values.py",
    title="Missing Values"
)

graphics_page = st.Page(
    page="views/graphics.py",
    title="Graphics"
)

correlation_page = st.Page(
    page="views/correlation.py",
    title="Correlation"
)

regression_page = st.Page(
    page="views/regression.py",
    title="Regression"
)

# --- NAVIGATION ---
pg = st.navigation(pages=[get_started_page, missing_values_page, graphics_page, correlation_page, regression_page])

# --- RUN NAVIGATION
pg.run()

