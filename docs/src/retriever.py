from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()

def get_retriever():
    """
    Loads FAISS vector store and returns a retriever
    """
    embeddings = OpenAIEmbeddings()

    # Load FAISS index (created by ingest.py)
    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    return retriever
