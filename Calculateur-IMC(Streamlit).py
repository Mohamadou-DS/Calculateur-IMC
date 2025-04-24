import streamlit as st

# Calculateur d'IMC
st.title("🧮 Calculateur d'IMC")

# Entrées
weight = st.number_input("Entrez votre poids (kg)", min_value=1.0, value=70.0)
height = st.number_input("Entrez votre taille (m)", min_value=0.5, value=1.70)

# Calcul et affichage
if st.button("Calculer l'IMC"):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "Insuffisance pondérale"
    elif 18.5 <= bmi < 24.9:
        status = "Poids normal"
    elif 25 <= bmi < 29.9:
        status = "Surpoids"
    else:
        status = "Obésité"

    st.write(f"Votre IMC est de **{bmi:.2f}**, ce qui correspond à : **{status}**.")
