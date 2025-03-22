# "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"

from langchain_groq import ChatGroq
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate
import os
llm_model= ChatGroq('deepseek-r1-distill-qwen-32b')

def retrive_docs(queery):
   return faiss_db.similarity_search(queery)

def get_context(documents):
    context="/n/n".join([doc.page_content for doc in documents])
    return context

custom_prompt_template="""
give correct asnwer make it funny as funny as possible
Context:{context}
Question:{question}
Answer:
"""

def asnwer_query(documents):
    context=get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    