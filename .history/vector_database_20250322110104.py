from langchain_community.documents_loader import PdfplumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS 


pdf_directory='pdfs/'

def upload_pdf()