import streamlit as st
st.title("ejemplos")
st.text("1. Si tenemos el punto A(2,3) y lo trasladamos 3 unidades a la derecha y 2 unidades hacia abajo, ¿cuál será su nueva posición?")
st.text("Solución: La traslación se realiza sumando 3 unidades a la coordenada 𝑥 y restando 2 unidades a la coordenada 𝑦")
st.latex("A′(x′,y′)=(2+3,3−2)=(5,1)")
st.text("Entonces, el nuevo punto será A′(5,1).")


st.text("2. Trasladamos el triángulo △𝐴𝐵𝐶 cuyas coordenadas de los vértices son 𝐴(1,2), 𝐵(4,5), y 𝐶(7,8), 2 unidades a la izquierda y 3 unidades hacia arriba.")
st.text("Solución: Para cada punto del triángulo, realizamos la traslación sumando o restando a las coordenadas según el desplazamiento:")
st.latex("A′(1−2,2+3)=(−1,5)")
st.latex("B′(4−2,5+3)=(2,8)")
st.latex("C′(7−2,8+3)=(5,11)")
st.text("Entonces, el nuevo triángulo tiene los vértices 𝐴′(−1,5), 𝐵′(2,8) y 𝐶′(5,11).")
st.text("")
st.text("")



