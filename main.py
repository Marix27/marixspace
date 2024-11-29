import streamlit as st

# crear las  paginas 
quees = st.Page("paginas/quees.py", title="descripcion general")
tipos = st.Page("paginas/tipos.py", title="teoria")
ejemplos = st.Page("paginas/ejemplos.py", title="ejemplos")
elementos = st.Page("paginas/elementos.py", title="ejemplos interactivos")
preguntas = st.Page("paginas/preguntas.py", title="preguntas interactivas")
aplicaciones = st.Page("paginas/aplicaciones.py", title="aplicaciones en la vida")
retroalimentacion = st.Page("paginas/retroalimentacion.py", title="retroalimentacion")
presentacion = st.Page("paginas/presentacion.py", title="presentacion")
inputs = st.Page("paginas/inputs.py", title="ejercicios")

#navigation
pg = st.navigation([quees, tipos, ejemplos, elementos, preguntas, aplicaciones, retroalimentacion, presentacion, inputs])
pg = st.navigation({"Introduccion": [quees, tipos, ejemplos], "aplicaciones": [elementos, inputs, preguntas, aplicaciones], "conclusiones":
[retroalimentacion,presentacion]})

# ejecutar
pg.run()






