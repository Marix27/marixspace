import streamlit as st
st.title(" pagina de inputs")


st.text("practica")
st.text("¿Cuántos ejes de simetría tiene un cuadrado?")
respuesta = st.text_input("digite su respuesta")
st.markdown(f"el numero de ejes de simetría es: {respuesta}")
