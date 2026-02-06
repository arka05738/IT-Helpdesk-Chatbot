from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def get_qa_chain(retriever):
    """
    Creates Retrieval-Augmented QA chain
    """
    llm = OpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    return qa_chain
