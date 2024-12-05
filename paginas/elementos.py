import streamlit as st
st.title("ejemplos de traslacion")
st.subheader("ejemplo 1")
st.text("1. Si tenemos el punto A(2,3) y lo trasladamos 3 unidades a la derecha y 2 unidades hacia abajo, ¿cuál será su nueva posición?")
st.text("Solución: La traslación se realiza sumando 3 unidades a la coordenada 𝑥 y restando 2 unidades a la coordenada 𝑦")
st.latex("A′(x′,y′)=(2+3,3−2)=(5,1)")
st.text("Entonces, el nuevo punto será A′(5,1).")
st.subheader("ejemplo 2")
st.text("2. Trasladamos el triángulo △𝐴𝐵𝐶 cuyas coordenadas de los vértices son 𝐴(1,2), 𝐵(4,5), y 𝐶(7,8), 2 unidades a la izquierda y 3 unidades hacia arriba.")
st.text("Solución: Para cada punto del triángulo, realizamos la traslación sumando o restando a las coordenadas según el desplazamiento:")
st.latex("A′(1−2,2+3)=(−1,5)")
st.latex("B′(4−2,5+3)=(2,8)")
st.latex("C′(7−2,8+3)=(5,11)")
st.text("Entonces, el nuevo triángulo tiene los vértices 𝐴′(−1,5), 𝐵′(2,8) y 𝐶′(5,11).")



st.title("ejemplos de reflexion")
st.text("1. Refleja el punto 𝑃(3,4) respecto al eje 𝑦.")
st.text("Para 𝑃(2,3) y 𝑘=2:")
st.latex("P′(2⋅2),(2⋅3)=P′(4,6)")
st.text("Resultado: El punto transformado es 𝑃′(4,6).")
st.text("2. Refleja el triángulo con vértices 𝐴(1,2), 𝐵(4,5), y 𝐶(6,7) respecto al eje 𝑥.")
st.text("Aplicamos esta fórmula a cada vértice:")
st.latex("Para 𝐴(1,2):  𝐴′(1,−2)")
st.latex("Para 𝐵(4,5): 𝐵′(4,−5)")
st.latex("Para 𝐶(6,7): 𝐶′(6,−7)")
st.text("Los nuevos vértices del triángulo reflejado son 𝐴′(1,−2), 𝐵′(4,−5) y 𝐶′(6,−7).")



st.title("ejemplos de dilatacion")
st.text("1. Refleja el punto 𝑃(2,3) con un factor de dilatación 2 respecto al origen, para 𝑃(3,4):")
st.latex("P′(−3,4)")
st.text("Resultado: El punto reflejado es 𝑃′(−3,4).")
st.text("2. Dilatación de un triángulo con vértices en 𝐴(1,2), 𝐵(3,1) y 𝐶(2,4) con un factor de dilatación 3 respecto al origen.")
st.text("Solución: Aplicamos la fórmula de dilatación a cada uno de los vértices:")
st.latex("A′(1⋅3,2⋅3)=A′(3,6)")
st.latex("B′(3⋅3,1⋅3)=B′(9,3)")
st.latex("C′(2⋅3,4⋅3)=C′(6,12)")
st.text("Los nuevos vértices del triángulo son 𝐴′(3,6), 𝐵′(9,3) y 𝐶′(6,12).")



st.title("ejemplos de rotacion")
st.text("Rota el punto 𝑃(2,3) 90° en sentido horario alrededor del origen, para 𝑃(2,3):")
st.latex("𝑃(2,3):")
st.text("El punto rotado es 𝑃′(3,−2).")
st.text("2. Rota el triángulo con vértices 𝐴(1,0), 𝐵(0,1) y 𝐶(−1,0) 180° alrededor del origen.")
st.text("Aplicamos esta fórmula a cada vértice:")
st.latex("Para 𝐴(1,0):𝐴′(−1,0)")
st.latex("Para 𝐵(0,1):𝐵′(0,−1)")
st.latex("Para 𝐶(−1,0):𝐶′(1,0)")
st.text("Los nuevos vértices del triángulo rotado son 𝐴′(−1,0), 𝐵′(0,−1) y 𝐶′(1,0).")



