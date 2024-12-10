import streamlit as st
st.title("Presentación personal")
st.text("Hola, mi nombre es María José Pardo Ruíz, soy estudiante de la carrera de matemáticas y actualmente estoy en primer semestre")
st.subheader("¿Cúales son mis intereses?")
st.text("Me gusta mucho el arte y todo lo que lo involucra, como pintar, coser, bordar, escribir y leer, además de eso amo escuchar música y bailar")
st.subheader("¿Cúal es el área de matemáticas con mayor afinidad?")
st.text("Realmente no hay ninguna")
st.subheader("¿Qúe aprendizaje me dejó la materia de programación?")
st.text("Más que aprendizaje me dejó un gusto por programar, en el colegio me parecía algo tedioso y sin sentido, pero ahora me parece interesante")

st.title("Formulario")
st.text("Ahora llena este formulario con tus datos")
with st.form(key='my_form'):
    nombre = st.text_input("¿Cómo te llamas?")
    edad = st.number_input("¿Cuántos años tienes?", min_value=0, max_value=100)
    carrera = st.text_input("¿Qúe carrera hace?")
    tema = st.text_input("¿El tema esta acorde con lo visto en el semestre?")
    mejorar = st.text_input("¿Qúe podria haber mejorado la pagina?")
    dudas = st.text_input("La información fue clara y concisa?")
    submit_button = st.form_submit_button(label='Enviar')

if submit_button:
    st.write(f"Nombre: {nombre}, Edad: {edad}, Carrera: {carrera}, Tema: {tema}, Mejorar:{mejorar}, Dudas:{dudas}")

