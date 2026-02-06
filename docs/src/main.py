import streamlit as st
from retriever import get_retriever
from llm import get_qa_chain

st.set_page_config(page_title="IT Helpdesk Chatbot")

st.title("🛠️ IT Helpdesk Chatbot")
st.write("Describe your IT issue and get instant support")

user_query = st.text_input("Enter your problem:")

if user_query:
    retriever = get_retriever()
    qa_chain = get_qa_chain(retriever)

    response = qa_chain.run(user_query)

    if response:
        st.success(response)
    else:
        st.warning("Issue could not be resolved. Please raise a support ticket.")

