import streamlit as st


rta1 = st.selectbox("¿Qué ocurre durante una rotación en geometría?", ["La figura se mueve a lo largo de una línea recta sin cambiar su forma",
                                                                       "La figura gira alrededor de un punto fijo, manteniendo su forma y tamaño, pero cambiando su orientación.",
                                                                       "La figura se amplía o reduce, pero mantiene su forma."])
c1 = st.empty()
rta2 = st.selectbox("¿Qué es una traslación en geometría?", ["Es un giro de una figura alrededor de un punto fijo.",
                                                             "Es un giro de una figura alrededor de un punto fijo.",
                                                             "Es un cambio de tamaño de la figura manteniendo su forma."])
c2 = st.empty
rta3 = st.selectbox("¿Qué son las transformaciones geométricas?",["a) Son procesos que alteran la forma de una figura, pero no su tamaño ni su posición.",
                                                                  "b) Son procesos matemáticos que permiten modificar una figura sin perder su esencia, cambiando su posición, forma o tamaño.",
                                                                  "c) Son procedimientos que solo cambian el tamaño de una figura sin afectar su forma."])
c3 = st.empty
rta4 = st.selectbox("¿Qué son las transformaciones isomórficas?",["a) Son transformaciones en las que la figura cambia su forma y tamaño, pero conserva los ángulos.",
                                                                  "b) Son transformaciones en las que la figura conserva la forma inicial, pero varía el tamaño; los ángulos se conservan y las magnitudes son proporcionales.",
                                                                  "c) Son transformaciones en las que la figura mantiene el tamaño, pero cambia su forma."])
c4 = st.empty
rta5 = st.selectbox("¿Por qué son importantes las transformaciones geométricas?",["a) Porque permiten modificar una figura sin cambiar su tamaño, lo que facilita la resolución de problemas simples.",
                                                                                  "b) Porque permiten comprender cómo las figuras y objetos se comportan al ser modificados en el espacio, y son esenciales en disciplinas como la computación gráfica, la arquitectura, la robótica y el arte.",
                                                                                  "c) Porque solo son útiles en la resolución de problemas relacionados con la simetría de las figuras."])
c5 = st.empty
rta6 = st.selectbox("Si la figura tiene un vértice en 𝐴(3,−2) y se refleja respecto al eje 𝑦, ¿cuál será la nueva coordenada de 𝐴?",["A(−3,−2)", "A(−3,−2)", "𝐴(−3,2)"])
c6 = st.empty
rta7 = st.selectbox("Dada la figura de un triángulo con vértices en P(1,2),Q(3,4),R(5,2), si la figura es rotada 90° en sentido antihorario alrededor del origen (0,0), ¿cuáles serán las coordenadas de los vértices resultantes?", ["P(−2,1),Q(−4,3),R(−2,5)","P(−2,1),Q(−4,1),R(−2,−5)","P(−2,−1),Q(−3,−4),R(−5,−2)"])
c7 = st.empty
rta8 = st.selectbox("Si un cuadrado tiene vértices en (1,1),B(3,1),C(3,3),D(1,3) y se traslada 4 unidades hacia la izquierda y 2 unidades hacia abajo, ¿qué coordenadas tendrá el vértice 𝐶?",["C(1,1)","C(1,5)","C(−1,1)"])
c8 = st.empty
rta9 = st.selectbox("Dado un triángulo con vértices A(1,1), B(2,3), y C(4,1), si se realiza una dilatación con un factor de escala de 2 respecto al origen (0, 0), ¿cuáles son las nuevas coordenadas de los vértices?", ["A(2,2), B(4,6), C(8,2)", "A(1,2), B(2,6),C(4,2)", "A(2,2), B(4,6),C(6,2)"])
c9 = st.empty
rta10 = st.selectbox("Refleja el punto Q(3,−4) respecto al eje 𝑦. ¿Dónde estará el nuevo punto?",["a) (−3,4)", "b) (4,−3)","c) (−3,−4)"])
c10 = st.empty

if st.button("verificar"):
    ptos = 0
    if rta1 == "La figura gira alrededor de un punto fijo, manteniendo su forma y tamaño, pero cambiando su orientación.":
          c1.info("perfecto")
          ptos += 1
    else:
          c1.error("incorrecto")

        
    if rta2 == "Es un desplazamiento de una figura sin cambiar su forma, tamaño ni orientación.":
          c2.info("perfecto")
          ptos += 1
    else:
          c2.error("incorrecto")
      
    if rta3 == "b) Son procesos matemáticos que permiten modificar una figura sin perder su esencia, cambiando su posición, forma o tamaño.":
          c3.info("perfecto")
          ptos += 1
    else:
          c3.error("incorrecto")

    if rta4 == "b) Son transformaciones en las que la figura conserva la forma inicial, pero varía el tamaño; los ángulos se conservan y las magnitudes son proporcionales.":
          c4.info("perfecto")
          ptos += 1
    else: 
          c4.error("")

    if rta5 == "b) Porque permiten comprender cómo las figuras y objetos se comportan al ser modificados en el espacio, y son esenciales en disciplinas como la computación gráfica, la arquitectura, la robótica y el arte.":
          c5.info("perfecto")
          ptos += 1
    else:
          c5.error("incorrecto")


    if rta6 == "A(−3,−2)":
          c6.info("perfecto")
          ptos += 1
    else: 
          c6.error("")

    
    if rta7 == "P(−2,1),Q(−4,3),R(−2,5)":
          c7.info("perfecto")
          ptos += 1
    else:
          c7.error("incorrecto")

    
    if rta8 == "C(1,1)":
          c8.info("perfecto")
          ptos += 1
    else:
          c8.error("incorrecto")

    
    if rta9 == "a) 𝐴(2,2), 𝐵(4,6), 𝐶(8,2)":
          c9.info("perfecto")
          ptos += 1
    else:
          c9.error("incorrecto")

    
    if rta10 == "a) (−3,4)":
          c10.info("perfecto")
          ptos += 1
    else:
          c10.error("incorrecto")

    
   
