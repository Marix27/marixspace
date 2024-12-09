import streamlit as st

# crear las  paginas 
quees = st.Page("paginas/quees.py", title="descripcion general", icon = ":material/category:")
elementos = st.Page("paginas/elementos.py", title="ejemplos", icon =":material/deployed_code:")
preguntas = st.Page("paginas/preguntas.py", title="preguntas interactivas")
aplicaciones = st.Page("paginas/aplicaciones.py", title="Evaluacion", icon =":material/done_all:")
presentacion = st.Page("paginas/presentacion.py", title="presentacion")
inputs = st.Page("paginas/inputs.py", title="ejercicios")

#navigation
pg = st.navigation([quees, elementos, preguntas, aplicaciones, presentacion, inputs])
pg = st.navigation({"Introduccion": [quees, elementos], "aplicaciones": [inputs, preguntas, aplicaciones], "conclusiones": [presentacion]})

# ejecutar
pg.run()






