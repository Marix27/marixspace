import streamlit as st



st.subheader("Ejemplo")
st.text("tenemos el punto 𝑃(2,3) y queremos trasladarlo por un vector v =(3,-2), lo que significa que queremos mover el punto 3 unidades a la derecha y 2 unidades hacia abajo.")
st.text("aplicamos la formula")
st.latex("x′=2+3=5")
st.latex("y′=3−2=1")
st.text("Resultado: El punto 𝑃(2,3) trasladado por el vector v=(3,−2) tiene nuevas coordenadas 𝑃′(5,1).")



st.subheader("Ejemplo")
st.text("Reflexión respecto al eje 𝑥")
st.text("Punto original 𝑃(2,3),después de la reflexión respecto al eje 𝑥, el punto reflejado será 𝑃′(2,−3).")
st.text("Reflexion respecto al eje y")
st.text("Punto original 𝑃(2,3).Después de la reflexión respecto al eje 𝑦, el punto reflejado será 𝑃′(−2,3).")



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



st.subheader("ejemplo")
st.text("Supongamos que queremos rotar el punto P(1,0) alrededor del origen por un ángulo de 60∘")
st.text("Paso 1: Convertimos el ángulo a radianes si está en grados. 60∘=𝜋/3 radianes.")
st.text("Paso 2: Aplicamos la fórmula de rotación:")
st.latex("x′=1⋅cos(π/3)−0⋅sin(π/3)=1⋅0−0⋅1=0")
st.latex("y′=1⋅sin(π/3)+0⋅cos(π/3)=1⋅1+0⋅0=1")
st.text("Entonces, después de rotar el punto P(1,0) por 60∘, las nuevas coordenadas son 𝑃′(0,1).")

  
    

