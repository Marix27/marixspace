import streamlit as st

# crear las  paginas 
quees = st.Page("paginas/quees.py", title="descripcion general", icon = ":material/category:")
elementos = st.Page("paginas/elementos.py", title="ejemplos", icon =":material/deployed_code:")
aplicaciones = st.Page("paginas/aplicaciones.py", title="Evaluacion", icon =":material/done_all:")
presentacion = st.Page("paginas/presentacion.py", title="presentacion")
inputs = st.Page("paginas/inputs.py", title="ejercicios")

#navigation
pg = st.navigation([quees, elementos, aplicaciones, presentacion, inputs])
pg = st.navigation({"Introduccion": [quees, elementos], "aplicaciones": [inputs, aplicaciones], "conclusiones": [presentacion]})

# ejecutar
pg.run()






