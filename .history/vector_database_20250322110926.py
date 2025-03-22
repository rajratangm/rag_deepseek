# from langchain_community.document_loaders import PdfPlumberLoader
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


file_path='universal_declaration_of_human_rights.pdf'
documen_text=load_pdf(file_path)
print(len(documen_text))
