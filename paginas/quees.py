import streamlit as st

# título de la página
st.title("Transformaciones geometricas")

# Subtítulo
st.header("¿Que son?")

# texto
st.write(
    """
   Las transformaciones geométricas son procesos matemáticos que permiten modificar una figura sin perder su esencia. Cambian su posición, forma, o tamaño. A través de estas transformaciones, podemos entender cómo las figuras pueden interactuar en el espacio y cómo se utilizan en áreas como la informática, la arquitectura, la animación y más.

    """)

st.header("propiedades")
st.subheader("1. Tansformaciones isométricas")
st.text("""Son transformaciones donde la figura resultante conserva las medidas y los ángulos de la figura inicial. 
mantiene la forma y el tamaño
    """)
st.subheader("2. Transformaciones isomórficas ")
st.text("""Son aquellas en las que la figura conserva la forma de la figura inicial, pero varía el tamaño
los ángulos se conservan y las magnitudes son distintas, pero proporcionales. 

""")
st.subheader("3. Trasnformaciones anamorficas")
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



#columnas 3
c1, c2 = st.columns(2)
with c1:
   st.subheader("la dilatacion")
   st.text("""Es una transformación que cambia el tamaño de una figura, ampliándola o reduciéndola, manteniendo la forma.""")
   st.markdown("**formula**")
   st.latex("x′=k⋅x")
   st.latex("y′=k⋅y")


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
    st.image("https://calculo.cc/temas/temas_geometria/movimiento_plano/imagenes/teoria/giro/t_1_2.gif")




