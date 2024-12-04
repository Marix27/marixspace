import streamlit as st

# crear las  paginas 
quees = st.Page("paginas/quees.py", title="descripcion general")
tipos = st.Page("paginas/tipos.py", title="teoria")
elementos = st.Page("paginas/elementos.py", title="ejemplos interactivos")
preguntas = st.Page("paginas/preguntas.py", title="preguntas interactivas")
aplicaciones = st.Page("paginas/aplicaciones.py", title="Evaluacion")
presentacion = st.Page("paginas/presentacion.py", title="presentacion")
inputs = st.Page("paginas/inputs.py", title="ejercicios")

#navigation
pg = st.navigation([quees, tipos, elementos, preguntas, aplicaciones, presentacion, inputs])
pg = st.navigation({"Introduccion": [quees, tiposs], "aplicaciones": [elementos, inputs, preguntas, aplicaciones], "conclusiones": [presentacion]})

# ejecutar
pg.run()






