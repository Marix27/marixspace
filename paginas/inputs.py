import streamlit as st
import numpy as st

st.title("selectbox")

contact_options = ["email", "phone", "text"]
st.header("selectbox from a list")
contact_selected = st.selectbox("why would you like to be contacted?",
                                options = contact_options)

st.write("selectbox returns:", contact_selected,
          "of type", type(contact_selected))

if contact_selected == "Email":
    st.write("**confirm your email address by clicking the link sen to you**")
else:
    st.write("**thank you, we will be in touch soon")

