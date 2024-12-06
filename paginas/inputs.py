import streamlit as st

rta1 = st.selectbox("cual wa la respuesta", ["si","no"])
c1 = st.empty()
rta2 = st.selectbox("elegir", ["si","no"])
c2 = st.empty

if st.button("verificar"):
    ptos = 0
    if rta1 == "no":
          c1.info("perfecto")
          ptos += 1
    else:
          c1.error("incorrecto")

        
    if rta2 == "arquimedes"
          c2.info("perfecto")
          ptos += 1
    else:
          c2.error("incorrecto")