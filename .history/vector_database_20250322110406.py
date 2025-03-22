from langchain_community.documents_loader import PdfplumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS 


pdf_directory='pdfs/'

def upload_pdf(file):
    with open(pdf_directory+file.name, 'wb') as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader=PdfplumberLoader(file_path)
    documen_text=loader.load()
    return documen_text



