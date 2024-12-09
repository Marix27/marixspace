import streamlit as st
st.title("Presentación personal")
st.subheader("Hola, mi nombre es María José Pardo Ruíz, soy estudiante de la carrera de matemáticas y actualmente estoy en primer semestre")

with st.form(key='my_form'):
    nombre = st.text_input("¿Cómo te llamas?")
    edad = st.number_input("¿Cuántos años tienes?", min_value=0, max_value=100)
    carrera = st.text_input("¿que carrera hace?")
    tema = st.text_input("¿el tema esta acorde con lo visto en el semestre?")
    mejorar = st.text_input("¿que podria haber mejorado la pagina?")
    dudas = st.text_input("la informacion fue clara y concisa?")
    submit_button = st.form_submit_button(label='Enviar')

if submit_button:
    st.write(f"Nombre: {nombre}, Edad: {edad}, Carrera: {carrera}, Tema: {tema}, Mejorar:{mejorar}, Dudas:{dudas}")

