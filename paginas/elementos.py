import streamlit as st
st.title("ejemplos de traslacion")
c1, c2 = st.columns(2, vertical_alignment="center")
with c1: 
    st.subheader("ejemplo 1")
    st.text("1. Si tenemos el punto A(2,3) y lo trasladamos 3 unidades a la derecha y 2 unidades hacia abajo, ¿cuál será su nueva posición?")
    st.latex("A′(x′,y′)=(2+3,3−2)=(5,1)")
    st.text("Entonces, el nuevo punto será A′(5,1).")
with c2:
    st.image("https://i.pinimg.com/736x/66/32/de/6632de2f1ab8fc62c58d8040be6837be.jpg")



c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.subheader("ejemplo 2")
    st.text("2. Tenemos el triángulo △𝐴𝐵𝐶 cuyas coordenadas son 𝐴(1,2), 𝐵(3,4), y 𝐶(5,2), 2 unidades a la izquierda y 3 unidades hacia arriba.")
    st.latex("A′(1−2,2+3)=(−1,5)")
    st.latex("B′(4−2,5+3)=(2,8)")
    st.latex("C′(7−2,8+3)=(5,11)")
    st.text("El nuevo triángulo vértices 𝐴′(−1,5), 𝐵′(1,7) y 𝐶′(3,5).")
   
with c2: 
    st.image("https://i.pinimg.com/736x/ae/0c/30/ae0c30190a47dfbcc5023d5e4c7224cc.jpg")




st.title("ejemplos de reflexion")
c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.subheader("ejemplo 1")
    st.text("1. Refleja sobre el eje 𝑥 el triángulo △𝐴𝐵𝐶 cuyas coordenadas son A(3,2), B(1,2), C(5,1).")
    st.latex("A(3,2)=A′(3,-2)")
    st.latex("B(1,2)=B′(1,-2)")
    st.latex("C(5,-1)=C′(5,-1)")

    st.text("Resultado: El punto transformado es A′(3,-2), B′(1,-2), C′(5,-1)")
with c2:
    st.image("https://i.pinimg.com/1200x/a1/c5/c4/a1c5c4031243332e407773eb8e0e0c08.jpg")



c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.subheader("ejemplo 2")
    st.text("2. Refleja el triángulo con vértices 𝐴(1,1), 𝐵(2,4), y 𝐶(5,6) respecto al eje 𝑥.")
    st.text("Aplicamos esta fórmula a cada vértice:")
    st.latex("Para 𝐴(1,1):  𝐴′(1,−1)")
    st.latex("Para 𝐵(2,4): 𝐵′(2,−4)")
    st.latex("Para 𝐶(5,6): 𝐶′(5,−6)")
    st.text("Los nuevos vértices del triángulo reflejado son 𝐴′(1,−1), 𝐵′(2,−4) y 𝐶′(5,−6).")
with c2:
    st.image("https://i.pinimg.com/1200x/1d/e8/af/1de8afcc758a669c6f18eac499d5e0be.jpg")



st.title("ejemplos de dilatacion")
c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.subheader("ejemplo 1")
    st.text("1. Refleja el punto 𝑃(2,3) con un factor de dilatación 2 respecto al origen")
    st.latex("P′(4,6)")
    st.text("Resultado: El punto reflejado es 𝑃′(4,6).")
with c2:
    st.image("https://i.pinimg.com/736x/4b/5f/27/4b5f2766a2f66eec812b63ec8fdfe0f4.jpg")




c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.subheader("ejemplo 2")
    st.text("2. Dilatación de un triángulo con vértices en 𝐴(2,2), 𝐵(4,1) y 𝐶(3,3) con un factor de dilatación 3.")
    st.latex("A′(2⋅3,2⋅3)=A′(6,6)")
    st.latex("B′(4⋅3,1⋅3)=B′(12,3)")
    st.latex("C′(3⋅3,3⋅3)=C′(9,9)")
    st.text("Los nuevos vértices son 𝐴′(3,6), 𝐵′(9,3) y 𝐶′(6,12).")
with c2:
    st.image("https://i.pinimg.com/736x/ee/fc/63/eefc638b2a4f67dfe5087bc565ed7bde.jpg")



st.title("ejemplos de rotacion")
c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.subheader("ejemplo 1")
    st.text("Rota el punto 𝑃(1,0) 90° en sentido horario alrededor del origen")
    st.latex("𝑃(1,0):")
    st.text("El punto rotado es 𝑃′(0,1).")
with c2:
    st.image("https://i.pinimg.com/736x/7c/64/bd/7c64bdf9b8409db6fe0a2343af43e797.jpg")



c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.subheader("ejemplo 2")
    st.text("2. Rota el triángulo con vértices 𝐴(0,3), 𝐵(-3,2) y 𝐶(3,2) 180° alrededor del origen.")
    st.text("Aplicamos esta fórmula a cada vértice:")
    st.latex("Para 𝐴(0,3):𝐴′(0,-3)")
    st.latex("Para 𝐵(-3,2):𝐵′(-3,−2)")
    st.latex("Para 𝐶(3,2):𝐶′(3,-2)")
    st.text("Los nuevos vértices del triángulo rotado son 𝐴′(0,-3), 𝐵′(-3,−2) y 𝐶′(3,-2).")
with c2:
    st.image("https://i.pinimg.com/736x/12/fd/ed/12fded709f343cbd40473793c41f581c.jpg")



