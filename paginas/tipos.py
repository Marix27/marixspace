import streamlit as st

#columnas
c1, c2 = st.columns(2)
with c1:
    st.header("Tansformaciones isométricas")
    st.text("""Son transformaciones donde la figura resultante conserva las medidas y los ángulos de la figura inicial. 
mantiene la forma y el tamaño, resultando una figura igual a la inicial y son:
1. traslación
2. identidad 
3. simetría.""")

with c2:
    st.image("https://nemdigitalstorage.blob.core.windows.net/nem-main/images/2022/10/10/d9b4d6a6-d0a9-4954-a9d8-d9451472ded6.png")



#columnas2
c1, c2 = st.columns(2)
with c1:
    st.header("Transformaciones isomórficas ")
    st.text("""Son aquellas en las que la figura conserva la forma de la figura inicial, pero varía el tamaño
los ángulos se conservan y las magnitudes son distintas, pero proporcionales. 
En este grupo nos encontramos con 
1. la homotecia
2. la semejanza 
3. las escalas.""")

with c2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQykvq3fRMw38dLHojrjaYHbe5Wz-DzJLVUSA&s")
    


#columnas 3
c1, c2 = st.columns(2)
with c1:
    st.header("""Transformaciones anamórficas.
Son transformaciones en la que la figura es completamente diferente a la inicial varían forma, 
magnitud y sólo mantiene alguna propiedad de la figura original como lo son:

1. la equivalencia 
2. la homología 
3. la inversión.""")
    

with c2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSDFDqDWriiuyWwoLo6JQdpoccR4NpxpYSYA&s")
