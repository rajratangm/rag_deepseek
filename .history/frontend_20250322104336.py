import streamlit as st 

uploaded_file = st.file_uploader("Choose a file", type="pdf",
                                 accept_multiple_files=False)