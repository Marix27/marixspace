import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import pandas as pd 
from PIL import Image
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

st.title("Ejercicios dinámicos")
preg1 = st.text("")
puntos = pd.DataFrame({
    "x": [1, 3, 5],
    "y": [2, 4, 2],
})

st.divider()

c1, c2, c3, c4 = st.columns(4)
def crear_grafico(puntos):
    pol = Polygon(puntos.values, closed=True, fill=True, facecolor="red", edgecolor="navy")
    
    fig, ax = plt.subplots()
    ax.add_patch(pol)
    
    ax.set_xlim(puntos["x"].min() - 1, puntos["x"].max() + 1)
    ax.set_ylim(puntos["y"].min() - 1, puntos["y"].max() + 1)
    ax.set_aspect("equal")
    
    return fig

# Contenido en cada columna
with c1:
    st.subheader("Ejes A")
    puntos = st.data_editor(puntos, hide_index=True, num_rows="dynamic", key="editor1")
with c2:
    st.subheader("Polígono A")
    fig = crear_grafico(puntos)
    st.pyplot(fig)

with c3:
    st.subheader("Ejes A'")
    puntos2 = st.data_editor(puntos, hide_index=True, num_rows="dynamic", key="editor2")

with c4:
    st.subheader("Polígono A'")
    fig2 = crear_grafico(puntos2)
    st.pyplot(fig2)
st.divider()



st.text("Dado el triángulo anterior con vértices A(1,2), B(3,4), C(5,2), trasládalo 4 unidades a la derecha y 3 unidades hacia arriba.")
opciones = [
    "A′(−3,−2), B′(9,4), C′(7,1)",
    "A′(3,4), B′(0,1), C′(−3,−2)",
    "A′(5,5), B′(7,7), C′(9,5)"
]

respuesta_correcta = "A′(5,5), B′(7,7), C′(9,5)"
respuesta = st.radio("Elige una opción:", opciones)
if respuesta == respuesta_correcta:
        st.success("Correcto")
else:
        st.error("incorrecta.")




st.header("segundo ejercicio")
preg1 = st.text("")
puntos = pd.DataFrame({
    "x": [1, 3, 3, 1],
    "y": [1, 1, 3, 3],
})

st.divider()

col1, col2, col3, col4 = st.columns(4)
def crear_grafico(puntos):
    pol = Polygon(puntos.values, closed=True, fill=True, facecolor="black", edgecolor="navy")
    
    fig, ax = plt.subplots()
    ax.add_patch(pol)
    
    ax.set_xlim(puntos["x"].min() - 1, puntos["x"].max() + 1)
    ax.set_ylim(puntos["y"].min() - 1, puntos["y"].max() + 1)
    ax.set_aspect("equal")
    
    return fig

# Contenido en cada columna
with col1:
    st.subheader("Ejes A")
    puntos = st.data_editor(puntos, hide_index=True, num_rows="dynamic", key="editor3")
with col2:
    st.subheader("Polígono A")
    fig = crear_grafico(puntos)
    st.pyplot(fig)

with col3:
    st.subheader("Ejes A'")
    puntos2 = st.data_editor(puntos, hide_index=True, num_rows="dynamic", key="editor4")

with col4:
    st.subheader("Polígono A'")
    fig2 = crear_grafico(puntos2)
    st.pyplot(fig2)
st.divider()


st.text("Dado el hexágono anterior con vértices en A(2,4), B(1,3), C(1,2), D(2,1), E(3,2), F(3,3). si la figura es rotada 90° en sentido antihorario alrededor del origen (0,0), ¿cuáles serán las coordenadas de los vértices resultantes?")
opciones = ["A(2,4), B(4,3), C(1,6), D(2,1), E(3,2), F(3,3)", "A(2,4), B(1,5), C(1,3), D(2,1), E(3,2), F(3,3)", "A(-4,2), B(-3,1), C(-2,1), D(-1,2), E(-2,3), F(-3,3)"]
respuesta_correcta = "A(-4,2), B(-3,1), C(-2,1), D(-1,2), E(-2,3), F(-3,3)"
respuesta = st.radio("Elige una opción:", opciones)
if respuesta == respuesta_correcta:
        st.success("Correcto")
else:
        st.error("incorrecta.")





st.header("Tercer ejercicio")
preg1 = st.text("")
puntos = pd.DataFrame({
    "x": [2, 1, 1, 2, 3, 3],
    "y": [4, 3, 2, 1, 2, 3],
})

st.divider()

col1, col2, col3, col4 = st.columns(4)
def crear_grafico(puntos):
    pol = Polygon(puntos.values, closed=True, fill=True, facecolor="green", edgecolor="navy")
    
    fig, ax = plt.subplots()
    ax.add_patch(pol)
    
    ax.set_xlim(puntos["x"].min() - 1, puntos["x"].max() + 1)
    ax.set_ylim(puntos["y"].min() - 1, puntos["y"].max() + 1)
    ax.set_aspect("equal")
    
    return fig

# Contenido en cada columna
with col1:
    st.subheader("Ejes A")
    puntos = st.data_editor(puntos, hide_index=True, num_rows="dynamic", key="editor5")
with col2:
    st.subheader("Polígono A")
    fig = crear_grafico(puntos)
    st.pyplot(fig)

with col3:
    st.subheader("Ejes A'")
    puntos2 = st.data_editor(puntos, hide_index=True, num_rows="dynamic", key="editor6")

with col4:
    st.subheader("Polígono A'")
    fig2 = crear_grafico(puntos2)
    st.pyplot(fig2)
st.divider()



st.text("Si un cuadrado tiene vértices en A(1,1), B(3,1), C(3,3), D(1,3) y se traslada 2 unidades hacia la derecha y 3 unidades hacia arriba, ¿qué coordenadas tendrá el vértice B?")
opciones = ["B(5,4)", "B(3,6)", "B(5,1)"]
respuesta_correcta = "B(5,4)"
respuesta = st.radio("Elige una opción:", opciones)
if respuesta == respuesta_correcta:
        st.success("Correcto")
else:
        st.error("incorrecta.")



st.header("Cuarto ejercicio")
preg1 = st.text("")
puntos = pd.DataFrame({
    "x": [3, 2, 3, 4],
    "y": [4, 2, 1, 2],
})

st.divider()

col1, col2, col3, col4 = st.columns(4)
def crear_grafico(puntos):
    pol = Polygon(puntos.values, closed=True, fill=True, facecolor="blue", edgecolor="navy")
    
    fig, ax = plt.subplots()
    ax.add_patch(pol)
    
    ax.set_xlim(puntos["x"].min() - 1, puntos["x"].max() + 1)
    ax.set_ylim(puntos["y"].min() - 1, puntos["y"].max() + 1)
    ax.set_aspect("equal")
    
    return fig

# Contenido en cada columna
with col1:
    st.subheader("Ejes A")
    puntos = st.data_editor(puntos, hide_index=True, num_rows="dynamic", key="editor7")
with col2:
    st.subheader("Polígono A")
    fig = crear_grafico(puntos)
    st.pyplot(fig)

with col3:
    st.subheader("Ejes A'")
    puntos2 = st.data_editor(puntos, hide_index=True, num_rows="dynamic", key="editor8")

with col4:
    st.subheader("Polígono A'")
    fig2 = crear_grafico(puntos2)
    st.pyplot(fig2)
st.divider()

st.text("Dado el triangulo anterior con vértices en A(3,4), B(2,2), C(3,1), D(4,2), si se realiza una dilatación con un factor de escala de 3 respecto al origen (0, 0), ¿cuáles son las nuevas coordenadas de los vértices? ")
opciones = ["a)A′(9,12),B′(6,6),C′(9,3),D′(12,6)", "b)A′(6,8),B′(4,4),C′(6,2),D′(8,4)", "c)A′(12,16),B′(8,8),C′(12,4),D′(16,8)"]
respuesta_correcta = "a)A′(9,12),B′(6,6),C′(9,3),D′(12,6)"
respuesta = st.radio("Elige una opción:", opciones)
if respuesta == respuesta_correcta:
        st.success("Correcto")
else:
        st.error("incorrecta.")


st.header("segundo ejercicio")
st.text("Abra la pagina de geogebra y cree una construccion ya sea de rotacion, traslacion, dilatacion o reflexion, tomele capture y suba el archivo aqui")
# Subir archivo
archivo = st.file_uploader("Cargar ejercicio", type=["png", "jpg", "jpeg"])

if archivo is not None:
    # Mostrar imagen cargada
    imagen = Image.open(archivo)
    st.image(imagen, caption="Imagen cargada con éxito", use_column_width=True)


