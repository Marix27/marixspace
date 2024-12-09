import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import pandas as pd 
from PIL import Image
st.title("Ejercicios dinamicos")
preg1 = st.text("")
#graficar figuras geometricas
st.divider()
st.subheader("Figuras geometricas")
c1, c2 = st.columns([1, 3], vertical_alignment="center")
puntos = pd.DataFrame({
    "x": [1, 1, -1],
    "y": [2, -1, 0.5],
 })
with c1: 
    
  puntos = st.data_editor(puntos, hide_index= True, num_rows="dynamic")
pol = patches.Polygon(puntos, closed= True, fill=True, facecolor="skyblue", edgecolor="navy")

fig, ax = plt.subplots()
ax.add_patch(pol)

ax.set_xlim(puntos["x"].min()-1, puntos["x"].max()+1)
ax.set_ylim(puntos["y"].min()-1, puntos["y"].max()+1)
ax.set_aspect("equal")
with c2: 
 st.pyplot(fig)

st.divider()

st.header("segundo ejercicio")
st.text("Abra la pagina de geogebra y cree una construccion ya sea de rotacion, traslacion, dilatacion o reflexion, tomele capture y suba el archivo aqui")
# Subir archivo
archivo = st.file_uploader("Cargar ejercicio", type=["png", "jpg", "jpeg"])

if archivo is not None:
    # Mostrar imagen cargada
    imagen = Image.open(archivo)
    st.image(imagen, caption="Imagen cargada con éxito", use_column_width=True)