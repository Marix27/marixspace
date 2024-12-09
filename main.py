import streamlit as st
# crear las  paginas 
quees = st.Page("paginas/quees.py", title="Descripción general", icon = ":material/category:")
elementos = st.Page("paginas/elementos.py", title="Ejemplos", icon =":material/deployed_code:")
aplicaciones = st.Page("paginas/aplicaciones.py", title="Evaluación", icon =":material/done_all:")
presentacion = st.Page("paginas/presentacion.py", title="Presentación", icon =":material/person:")
inputs = st.Page("paginas/inputs.py", title="Ejercicios", icon =":material/fitness_center:")

#navigation
pg = st.navigation([quees, elementos, aplicaciones, presentacion, inputs])
pg = st.navigation({"Introducción": [quees, elementos], "Aplicaciones": [inputs, aplicaciones], "Conclusiones": [presentacion]})

# ejecutar
pg.run()






