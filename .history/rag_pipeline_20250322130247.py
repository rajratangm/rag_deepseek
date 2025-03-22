# "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"

from langchain_groq import ChatGroq
from vector_database import faiss_db
import os
llm_model= ChatGroq('deepseek-r1-distill-qwen-32b')

def retrive_docs(queery):
   return faiss_db.similarity_search(queery)

def get_context(documents)
