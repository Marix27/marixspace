import streamlit as st


# crear las  paginas 
intro = st.Page("paginas/intro.py", title="Introduccion")
ejs = st.Page("paginas/ejercicios.py", title ="ejercicios")

#navigation
pg = st.navigation([intro, ejs])
# ejecutar
pg.run()