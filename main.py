import streamlit as st

# crear las  paginas 
quees = st.Page("paginas/quees.py", title="¿Que son?")
tipos = st.Page("paginas/tipos.py", title="tipos")
ejemplos = st.Page("paginas/ejemplos.py", title="ejemplos")
elementos = st.Page("paginas/elementos.py", title="ejercicios")
retroalimentacion = st.Page("paginas/retroalimentacion.py", title="retroalimentacion")
presentacion = st.Page("paginas/presentacion.py", title="presentacion")
inputs = st.Page("paginas/inputs.py", title="ejercicios")

#navigation
pg = st.navigation([quees, tipos, ejemplos, elementos, retroalimentacion, presentacion])
pg = st.navigation({"Introduccion": [quees, tipos, ejemplos], "aplicaciones": [elementos, inputs]})

# ejecutar
pg.run()






