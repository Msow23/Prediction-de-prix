import streamlit as st
import joblib
import numpy as np

# Charger le modèle
model = joblib.load("model_ordinateur_prix.pkl")

# Titre de l'application
st.title("💻 Estimation du Prix d’un Ordinateur")
st.write("Remplis les caractéristiques ci-dessous pour obtenir une estimation du prix.")

# Interface utilisateur
ram = st.slider("RAM (Go)", 4, 64, step=4, value=8)
ssd = st.slider("Stockage SSD (Go)", 128, 2048, step=128, value=512)
cpu_speed = st.number_input("Vitesse CPU (GHz)", min_value=1.0, max_value=5.0, step=0.1, value=2.5)
gpu = st.selectbox("Carte Graphique Dédiée ?", ["Oui", "Non"])
gpu_flag = 1 if gpu == "Oui" else 0

marque = st.selectbox("Marque", ["HP", "Dell", "Asus", "Lenovo", "Acer", "Apple", "MSI", "Autre"])

# Encodage simple de la marque (à ajuster selon ton encodage réel)
marques_connues = ["HP", "Dell", "Asus", "Lenovo", "Acer", "Apple", "MSI"]
marque_encoded = [1 if marque == m else 0 for m in marques_connues]  # one-hot encoding
if marque == "Autre":
    marque_encoded.append(1)
else:
    marque_encoded.append(0)

screen_size = st.slider("Taille de l’écran (pouces)", 11.0, 20.0, step=0.1, value=15.6)

# Préparation des features pour la prédiction
features = [ram, ssd, cpu_speed, gpu_flag, screen_size] + marque_encoded

if st.button("Prédire le prix 💰"):
    prediction = model.predict([features])
    st.success(f"Prix estimé : {prediction[0]:,.2f} €")
