import streamlit as st
st.divider()
st.subheader("figuras geometricas")
c1, c2 = st.columns([1,3],
vertical_alignment="center")
puntos = pd.Dataframe({
    "x":[1,1-1]
    "y":[1,-1,0.5]
})

with c1:
puntos = st.data_editor(puntos,hide_index = True,
num_rows="dynamic")
pol = patches.Polygon(puntos,
closed = True, fill = True,
facecolor="skyblue",
edgecolor = "navy")
fig, ax= plt.subplots()
ax.add_patch(pol)
ax.set_xlim(puntos["x"].min()-1,
puntos["x"].max()+1)
ax.set_ylim(puntos["y"].min()-1
pntos["y"].max()+1)
ax.set_aspect("equal")

with c2
st.pyplot(fig)
st.divider()
