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

st.title("Ejercicios dinamicos")
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


preg6 = st.selectbox("Dado un triángulo con vértices A(1,2), B(3,4), C(5,2), trasládalo 4 unidades a la derecha y 3 unidades hacia arriba.",["A(−3,−2), B′(9,4), C′(7,1)", "A′(3,4), B′(0,1), C'(−3,−2)", "A′(4,5), B′(7,7), C′(9,3)"])
c6 = st.empty()

puntos = 0
if st.button("verificar todo"):
  if preg6 == "A′(4,5), B′(7,7), C′(9,3)":
        c6.success("Correcto")
        puntos += 1
  else:
        c6.error("Incorrecto")



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

preg8 = st.selectbox("Si un cuadrado tiene vértices en (1,1),B(3,1),C(3,3),D(1,3) y se traslada 4 unidades hacia la izquierda y 2 unidades hacia abajo, ¿qué coordenadas tendrá el vértice 𝐶?",["C(1,1)","C(1,5)","C(−1,1)"])
c8 = st.empty()

puntos = 0

if preg8 == "C(1,1)":
        c8.success("Correcto")
        puntos += 1
else:
        c8.error("Incorrecto")



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

preg9 = st.selectbox("Dado un triángulo con vértices A(1,1), B(2,3), y C(4,1), si se realiza una dilatación con un factor de escala de 2 respecto al origen (0, 0), ¿cuáles son las nuevas coordenadas de los vértices?", ["A(2,2), B(4,6), C(8,2)", "A(1,2), B(2,6),C(4,2)", "A(2,2), B(4,6),C(6,2)"])
c9 = st.empty()

puntos = 0
if preg9 == "a) 𝐴(2,2), 𝐵(4,6), 𝐶(8,2)":
        c9.success("Correcto")
        puntos += 1
else:
        c9.error("Incorrecto")



st.header("Cuarto ejercicio")
preg1 = st.text("")
puntos = pd.DataFrame({
    "x": [2, 2, 6, 6],
    "y": [4, 3, 4, 3],
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

preg10 = st.selectbox("Refleja el punto Q(3,−4) respecto al eje 𝑦. ¿Dónde estará el nuevo punto?",["a) (−3,4)", "b) (4,−3)","c) (−3,−4)"])
c10 = st.empty()

puntos = 0
if preg10 == "a) (−3,4)":
        c10.success("Correcto")
        puntos += 1
else:
        c10.error("Incorrecto")



st.header("segundo ejercicio")
st.text("Abra la pagina de geogebra y cree una construccion ya sea de rotacion, traslacion, dilatacion o reflexion, tomele capture y suba el archivo aqui")
# Subir archivo
archivo = st.file_uploader("Cargar ejercicio", type=["png", "jpg", "jpeg"])

if archivo is not None:
    # Mostrar imagen cargada
    imagen = Image.open(archivo)
    st.image(imagen, caption="Imagen cargada con éxito", use_column_width=True)


