import streamlit as st
from model import prediction

st.set_page_config(page_title = "Wine Quality Prediction", page_icon="🍷")

st.title("Wine Quality Prediction 🍷")


st.subheader("Enter the composition of your wine 🍶")
with st.form(key = "ml_form"):
    i_fixed_acidity = st.text_input("Enter fixed acidity:", "[3.8-15.9]")
    i_volatile_acidity = st.text_input("Enter volatile acidity:", "[0.08-1.58]")
    i_citric_acid = st.text_input("Enter citric acid:", "[0.0-1.66]")
    i_residual_sugar = st.text_input("Enter residual sugar:", "[0.6-65.8]")
    i_chlorides = st.text_input("Enter chlorides:", "[0.009-0.611]")
    i_total_sulfur_dioxide = st.text_input("Enter total sulfur dioxide:", "[6.0-440.0]")
    i_density = st.text_input("Enter density:", "[0.98-1.04]")
    i_ph = st.text_input("Enter pH:", "[2.72-4.01]")
    i_sulphates = st.text_input("Enter sulphates:", "[0.22-2.0]")
    i_type_white_choice = st.selectbox("Type of wine:", ['White', 'Red'])
    i_alcohol = st.text_input("Enter alcohol percentage:", "[8.0-14.9]")
    if i_type_white_choice == 'Red':
        i_type_white = 0
    else: i_type_white = 1
    if(st.form_submit_button("💠 Predict Quality")):
        answer = prediction(float(i_fixed_acidity), float(i_volatile_acidity), float(i_citric_acid), float(i_residual_sugar), float(i_chlorides), float(i_total_sulfur_dioxide), float(i_density), float(i_ph), float(i_sulphates), float(i_type_white), float(i_alcohol))
        if answer >= 6:
            st.balloons()
            st.success("Wine Quality Is Good 💎")
        else: st.error("Wine Quality Is Bad 👎")