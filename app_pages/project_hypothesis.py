import streamlit as st
import matplotlib.pyplot as plt

def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* Cherry leaves inficted by powdery mildew shows visual patterns compared to healthy uninfected cherry leaves. "
        f"These patterns are typically on the edges of the leaf, compared to a healthy leaf with no patterns. \n\n"
        f"* An Image Montage shows typical patterns on the edges."
        f"Validate the hypothesis by conducting exploratory data analysis (EDA) on the dataset. "
        f"Visualize samples of healthy and infected cherry leaves to identify any noticeable patterns or differences."
    )