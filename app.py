import streamlit as st
import helper

st.title("Similarity Calculator")

col1,col2=st.columns(2)

with col1:
    text1=st.text_input("Text 1")
with col2:
    text2=st.text_input("Text 2")

if st.button("Calculate Similarity"):
    similarity=helper.cal_similarity(text1,text2)
    st.header("Similarity between the two texts is:")
    st.header(round(similarity,3))