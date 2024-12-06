import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import pandas as pd 

#graficar figuras geometricas
st.divider()
st.subheader("Figuras geometricas")
c1, c2 ,c3, c4 = st.columns([1, 3, 5, 7], vertical_alignment="center")
puntos = pd.DataFrame({
    "x": [1, 1, -1],
    "y": [1, -1, 0.5],
    "x": [1, 1, -1],
    "y": [1, -1, 0.5],
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

with c3:
    
  puntos = st.data_editor(puntos, hide_index= True, num_rows="dynamic")
pol = patches.Polygon(puntos, closed= True, fill=True, facecolor="skyblue", edgecolor="navy")

fig, ax = plt.subplots()
ax.add_patch(pol)

ax.set_xlim(puntos["x"].min()-1, puntos["x"].max()+1)
ax.set_ylim(puntos["y"].min()-1, puntos["y"].max()+1)
ax.set_aspect("equal")

with c4:
  st.pyplot(fig)

st.divider()


