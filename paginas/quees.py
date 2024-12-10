import streamlit as st

# título de la página
c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
 st.title("Las transformaciones geométricas")
with c2:
    st.image("https://i.pinimg.com/736x/6c/30/ed/6c30edebdef3ed9ad6346b621d3246ff.jpg")


# Subtítulo
st.subheader("¿Qué son?")

# texto
st.write(
    """
   Las transformaciones geométricas son procesos matemáticos que permiten modificar una figura sin perder su esencia. Cambian su posición, forma, o tamaño. A través de estas transformaciones, podemos entender cómo las figuras pueden interactuar en el espacio y cómo se utilizan en áreas como la informática, la arquitectura, la animación y más.

    """)

st.subheader("¿Para qué nos sirven las transformaciones geométricas?")
st.text("Las transformaciones geométricas son fundamentales en muchas ramas de las matemáticas y las ciencias aplicadas. Permiten comprender cómo las figuras y objetos se comportan al ser modificados en el espacio.")

st.header("Tipos de transformaciones")
st.subheader("Tansformaciones isométricas")
st.text("""Son transformaciones donde la figura resultante conserva las medidas y los ángulos de la figura inicial. 
mantiene la forma y el tamaño
    """)
st.subheader("Transformaciones isomórficas")
st.text("""Son aquellas en las que la figura conserva la forma de la figura inicial, pero varía el tamaño
los ángulos se conservan y las magnitudes son distintas, pero proporcionales. 

""")
st.subheader("Transformaciones anamorficas")
st.text("""Son transformaciones en la que la figura es completamente diferente a la inicial varían forma, 
magnitud y sólo mantiene alguna propiedad
""")

st.header("Propiedades")

c1, c2 = st.columns(2, vertical_alignment="center")
with c1: 
    st.subheader("Traslación")
    st.text("""La traslación es un desplazamiento de una figura en el plano sin cambiar su forma, tamaño ni orientación""")
    st.markdown("**Fórmula**")
    st.latex("x′=x+a")
    st.latex("y′=y+b")
   

with c2:
    st.image("https://nemdigitalstorage.blob.core.windows.net/nem-main/images/2022/10/10/d9b4d6a6-d0a9-4954-a9d8-d9451472ded6.png")


#columnas2
c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.subheader("La reflexión")
    st.text("es una transformación que genera una imagen especular de una figura respecto a una recta o plano llamado eje de simetría")
    st.markdown("**formula**")
    st.text("Reflexión sobre el eje x")
    st.latex("x′=x")
    st.latex("y′=−y")
    st.text("Reflexión sobre el eje y")
    st.latex("x′=−x")
    st.latex("y′=y")
   

with c2:
    st.image("https://www.profesorenlinea.cl/imagengeometria/Semejanza_figuras_planas_image002.jpg")



#columnas 3
c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
   st.subheader("La dilatación")
   st.text("""Es una transformación que cambia el tamaño de una figura, ampliándola o reduciéndola, manteniendo la forma.""")
   st.markdown("**Fórmula**")
   st.latex("x′=k⋅x")
   st.latex("y′=k⋅y")


with c2:
    st.image("https://dr282zn36sxxg.cloudfront.net/datastreams/f-d%3A068abef32c5a49e7e8ba6b0104cad264316527716ecca70fa4aeff14%2BIMAGE_TINY%2BIMAGE_TINY.1")

c1,c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.subheader("La rotación")
    st.text("implica girar una figura alrededor de un punto fijo, llamado centro de rotación, por un ángulo determinado.")
    st.markdown("**Fórmula**")
    st.latex("x′=x⋅cos(θ)−y⋅sin(θ)")
    st.latex("y′=x⋅sin(θ)+y⋅cos(θ)")

with c2:
    st.image("https://calculo.cc/temas/temas_geometria/movimiento_plano/imagenes/teoria/giro/t_1_2.gif")







