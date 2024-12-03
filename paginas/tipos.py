import streamlit as st
st.header("propiedades")
st.subheaderheader("1. Tansformaciones isométricas")
st.text("""Son transformaciones donde la figura resultante conserva las medidas y los ángulos de la figura inicial. 
mantiene la forma y el tamaño
    """)
st.subheader("2. Transformaciones isomórficas ")
st.text("""Son aquellas en las que la figura conserva la forma de la figura inicial, pero varía el tamaño
los ángulos se conservan y las magnitudes son distintas, pero proporcionales. 

""")
st.header("3. Trasnformaciones anamorficas")
st.text("""Son transformaciones en la que la figura es completamente diferente a la inicial varían forma, 
magnitud y sólo mantiene alguna propiedad
""")

st.header("tipos de transformaciones")

c1, c2 = st.columns(2)
with c1: 
    st.subheader("traslacion")
    st.text("""La traslación es un desplazamiento de una figura en el plano sin cambiar su forma, tamaño ni orientación""")
    st.markdown("**formula**")
    st.latex("x′=x+a")
    st.latex("y′=y+b")
   

with c2:
    st.image("https://nemdigitalstorage.blob.core.windows.net/nem-main/images/2022/10/10/d9b4d6a6-d0a9-4954-a9d8-d9451472ded6.png")

st.subheader("Ejemplo")
st.text("tenemos el punto 𝑃(2,3) y queremos trasladarlo por un vector v =(3,-2), lo que significa que queremos mover el punto 3 unidades a la derecha y 2 unidades hacia abajo.")
st.text("aplicamos la formula")
st.latex("x′=2+3=5")
st.latex("y′=3−2=1")
st.text("Resultado: El punto 𝑃(2,3) trasladado por el vector v=(3,−2) tiene nuevas coordenadas 𝑃′(5,1).")

#columnas2
c1, c2 = st.columns(2)
with c1:
    st.subheader("la reflexion")
    st.text("es una transformación que genera una imagen especular de una figura respecto a una recta o plano llamado eje de simetría")
    st.markdown("**formula**")
    st.text("reflexion sobre el eje x")
    st.latex("x′=x")
    st.latex("y′=−y")
    st.text("reflexion sobre el eje y")
    st.latex("x′=−x")
    st.latex("y′=y")
   

with c2:
    st.image("https://www.profesorenlinea.cl/imagengeometria/Semejanza_figuras_planas_image002.jpg")

st.subheader("Ejemplo")
st.text("Reflexión respecto al eje 𝑥")
st.text("Punto original 𝑃(2,3),después de la reflexión respecto al eje 𝑥, el punto reflejado será 𝑃′(2,−3).")
st.text("Reflexion respecto al eje y")
st.text("Punto original 𝑃(2,3).Después de la reflexión respecto al eje 𝑦, el punto reflejado será 𝑃′(−2,3).")

#columnas 3
c1, c2 = st.columns(2)
with c1:
   st.subheader("la dilatacion")
   st.text("""Es una transformación que cambia el tamaño de una figura, ampliándola o reduciéndola, manteniendo la forma.""")
   st.markdown("**formula**")
   st.text("x′=k⋅x")
   st.latex("y′=k⋅y")

st.subheader("Ejemplo")
st.text("Supongamos que tenemos un triángulo con las siguientes coordenadas de sus vértices:A(3,2), B(4,2), C(5,1)")
st.text("Y queremos realizar un escalamiento de factor k=3 con respecto al origen (0, 0), lo que significa que todos los puntos se moverán el triple de su distancia desde el origen.")
st.text("Para el vértice A(2,3):")
st.latex("xA′=3⋅3=9")
st.latex("yA′=3⋅2=6")
st.text("Por lo tanto, A ′(4,6).")
st.text("Para el vértice B(4,5):")
st.latex("xB′=3⋅4=12")
st.latex("yB′=2⋅3=6")
st.text("Por lo tanto, B′(12,6).")
st.text("Para el vértice C(6,1):")
st.latex("xC′=2⋅6=12")
st.latex("yC′=2⋅1=2")
st.text("Por lo tanto, C′(12,2).")

with c2:
    st.image("https://dibujotecni.com/wp-content/uploads/2020/04/Cuadrado-equivalente-a-un-poligono-regular.png")

c1,c2 = st.columns(2)
with c1:
    st.subheader("La rotacion")
    st.text("implica girar una figura alrededor de un punto fijo, llamado centro de rotación, por un ángulo determinado.")
    st.markdown("**formula**")
    st.latex("x′=x⋅cos(θ)−y⋅sin(θ)")
    st.latex("y′=x⋅sin(θ)+y⋅cos(θ)")

with c2:
    st.image("")

st.subheader("ejemplo")
st.text("Supongamos que queremos rotar el punto P(1,0) alrededor del origen por un ángulo de 60∘")
st.text("Paso 1: Convertimos el ángulo a radianes si está en grados. 60∘=𝜋/3 radianes.")
st.text("Paso 2: Aplicamos la fórmula de rotación:")
st.latex("x′=1⋅cos(π/3)−0⋅sin(π/3)=1⋅0−0⋅1=0")
st.latex("y′=1⋅sin(π/3)+0⋅cos(π/3)=1⋅1+0⋅0=1")
st.text("Entonces, después de rotar el punto P(1,0) por 60∘, las nuevas coordenadas son 𝑃′(0,1).")

  
    

