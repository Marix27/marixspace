import streamlit as st

st.header("1. Tansformaciones isométricas")
st.text("""Son transformaciones donde la figura resultante conserva las medidas y los ángulos de la figura inicial. 
mantiene la forma y el tamaño
    """)

c1, c2 = st.columns(2)
with c1: 
    st.subheader("traslacion")
    st.text("""La traslación es un desplazamiento de una figura en el plano sin cambiar su forma, tamaño ni orientación""")
    st.markdown("**formula**")
    st.latex("x′=x+a")
    st.latex("y′=y+b")
   

with c2:
    st.image("https://nemdigitalstorage.blob.core.windows.net/nem-main/images/2022/10/10/d9b4d6a6-d0a9-4954-a9d8-d9451472ded6.png")


st.header("2. Transformaciones isomórficas ")
st.text("""Son aquellas en las que la figura conserva la forma de la figura inicial, pero varía el tamaño
los ángulos se conservan y las magnitudes son distintas, pero proporcionales. 

""")

#columnas2
c1, c2 = st.columns(2)
with c1:
    st.subheader("la semejanza")
    st.text("Dos figuras son semejantes si tienen la misma forma, pero no necesariamente el mismo tamaño")
    st.markdown("**formula**")
    st.latex("area1/area2=k^2")
   

with c2:
    st.image("https://www.profesorenlinea.cl/imagengeometria/Semejanza_figuras_planas_image002.jpg")



st.header("3. Trasnformaciones anamorficas")
st.text("""Son transformaciones en la que la figura es completamente diferente a la inicial varían forma, 
magnitud y sólo mantiene alguna propiedad
""")

#columnas 3
c1, c2 = st.columns(2)
with c1:
   st.text("unas de las mas importantes son")
   st.subheader("la equivalencia")
   st.text("""Dos figuras son equivalentes si tienen la misma área, aunque su forma y orientación puedan ser diferentes""")
   st.markdown("**formula**")
   st.text("area de un triangulo")
   st.latex("A= 1/2 ×base×altura")
   st.text("area de un cuadrado")
   st.latex("A=lado^2")
   

with c2:
    st.image("https://dibujotecni.com/wp-content/uploads/2020/04/Cuadrado-equivalente-a-un-poligono-regular.png")
    
  
    

