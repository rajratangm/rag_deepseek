import streamlit as st 

uploaded_file = st.file_uploader("Choose a file", type="pdf",
                                 accept_multiple_files=False)
if uploaded_file is not None:
    st.write(uploaded_file)
    st.write(uploaded_file.getvalue())


user_query = st.text_area("Enter your query here", height=100, placeholder="Enter your query here")
ask_question=st.button("Ask Question")
if ask_question:
    fixed_response='This is a fixed response'
    st.chat_message('hi rajratan').write(fixed_response)