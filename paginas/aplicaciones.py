import streamlit as st
import streamlit as str


preg1 = st.selectbox("¿Qué ocurre durante una rotación en geometría?", ["La figura se mueve a lo largo de una línea recta sin cambiar su forma",
                                                                       "La figura gira alrededor de un punto fijo, manteniendo su forma y tamaño, pero cambiando su orientación.",
                                                                       "La figura se amplía o reduce, pero mantiene su forma."])
c1 = st.empty()
preg2 = st.selectbox("¿Qué es una traslación en geometría?", ["Es un giro de una figura alrededor de un punto fijo.",
                                                             "Es un desplazamiento de una figura sin cambiar su forma, tamaño ni orientación.",
                                                             "Es un cambio de tamaño de la figura manteniendo su forma."])
c2 = st.empty
preg3 = st.selectbox("¿Qué son las transformaciones geométricas?",["a) Son procesos que alteran la forma de una figura, pero no su tamaño ni su posición.",
                                                                  "b) Son procesos matemáticos que permiten modificar una figura sin perder su esencia, cambiando su posición, forma o tamaño.",
                                                                  "c) Son procedimientos que solo cambian el tamaño de una figura sin afectar su forma."])
c3 = st.empty
preg4 = st.selectbox("¿Qué son las transformaciones isomórficas?",["a) Son transformaciones en las que la figura cambia su forma y tamaño, pero conserva los ángulos.",
                                                                  "b) Son transformaciones en las que la figura conserva la forma inicial, pero varía el tamaño; los ángulos se conservan y las magnitudes son proporcionales.",
                                                                  "c) Son transformaciones en las que la figura mantiene el tamaño, pero cambia su forma."])
c4 = st.empty
preg5 = st.selectbox("¿Por qué son importantes las transformaciones geométricas?",["a) Porque permiten modificar una figura sin cambiar su tamaño, lo que facilita la resolución de problemas simples.",
                                                                                  "b) Porque permiten comprender cómo las figuras y objetos se comportan al ser modificados en el espacio, y son esenciales en disciplinas como la computación gráfica, la arquitectura, la robótica y el arte.",
                                                                                  "c) Porque solo son útiles en la resolución de problemas relacionados con la simetría de las figuras."])
c5 = st.empty
preg6 = st.selectbox("Si la figura tiene un vértice en 𝐴(3,−2) y se refleja respecto al eje 𝑦, ¿cuál será la nueva coordenada de 𝐴?",["A(−3,−2)", "A(−3,−2)", "𝐴(−3,2)"])
c6 = st.empty
preg7 = st.selectbox("Dada la figura de un triángulo con vértices en P(1,2),Q(3,4),R(5,2), si la figura es rotada 90° en sentido antihorario alrededor del origen (0,0), ¿cuáles serán las coordenadas de los vértices resultantes?", ["P(−2,1),Q(−4,3),R(−2,5)","P(−2,1),Q(−4,1),R(−2,−5)","P(−2,−1),Q(−3,−4),R(−5,−2)"])
c7 = st.empty
preg8 = st.selectbox("Si un cuadrado tiene vértices en (1,1),B(3,1),C(3,3),D(1,3) y se traslada 4 unidades hacia la izquierda y 2 unidades hacia abajo, ¿qué coordenadas tendrá el vértice 𝐶?",["C(1,1)","C(1,5)","C(−1,1)"])
c8 = st.empty
preg9 = st.selectbox("Dado un triángulo con vértices A(1,1), B(2,3), y C(4,1), si se realiza una dilatación con un factor de escala de 2 respecto al origen (0, 0), ¿cuáles son las nuevas coordenadas de los vértices?", ["A(2,2), B(4,6), C(8,2)", "A(1,2), B(2,6),C(4,2)", "A(2,2), B(4,6),C(6,2)"])
c9 = st.empty
preg10 = st.selectbox("Refleja el punto Q(3,−4) respecto al eje 𝑦. ¿Dónde estará el nuevo punto?",["a) (−3,4)", "b) (4,−3)","c) (−3,−4)"])
c10 = st.empty

puntos = 0
if st.button("verificar todo"):

    if preg1 == "La figura gira alrededor de un punto fijo, manteniendo su forma y tamaño, pero cambiando su orientación.":
        st.success("Correcto")
        puntos += 1
    else:
        st.error("Esto es un error", icon="🚨")

    
    if preg2 == "Es un desplazamiento de una figura sin cambiar su forma, tamaño ni orientación.":
        st.success("Perfecto")
        puntos += 1
    else:
        st.error("Incorrecto, no es la respuesta correcta.")

    
    if preg3 == "b) Son procesos matemáticos que permiten modificar una figura sin perder su esencia, cambiando su posición, forma o tamaño.":
        st.success("Perfecto")
        puntos += 1
    else:
        st.error("Incorrecto")

    
    if preg4 == "b) Son transformaciones en las que la figura conserva la forma inicial, pero varía el tamaño; los ángulos se conservan y las magnitudes son proporcionales.":
        st.success("Perfecto")
        puntos += 1
    else:
        st.error("Incorrecto")

   
    if preg5 == "b) Porque permiten comprender cómo las figuras y objetos se comportan al ser modificados en el espacio, y son esenciales en disciplinas como la computación gráfica, la arquitectura, la robótica y el arte.":
        st.success("Perfecto")
        puntos += 1
    else:
        st.error("Incorrecto")

    
    if preg6 == "A(−3,−2)":
        st.success("Perfecto")
        puntos += 1
    else:
        st.error("Incorrecto")

    
    if preg7 == "P(−2,1),Q(−4,3),R(−2,5)":
        st.success("Perfecto")
        puntos += 1
    else:
        st.error("Incorrecto")

    
    if preg8 == "C(1,1)":
        st.success("Perfecto")
        puntos += 1
    else:
        st.error("Incorrecto")

   
    if preg9 == "a) 𝐴(2,2), 𝐵(4,6), 𝐶(8,2)":
        st.success("Perfecto")
        puntos += 1
    else:
        st.error("Incorrecto")

    
    if preg10 == "a) (−3,4)":
        st.success("Perfecto")
        puntos += 1
    else:
        st.error("Incorrecto")
    
   
