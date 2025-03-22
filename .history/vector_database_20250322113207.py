# from langchain_community.document_loaders 
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS 


pdf_directory='pdfs/'

def upload_pdf(file):
    with open(pdf_directory+file.name, 'wb') as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader=PDFPlumberLoader(file_path)
    documen_text=loader.load()
    return documen_text

def create_chunks(documents):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        overlap_size=100,
        min_chunk_size=100,
        max_chunk_size=1000
    )
    chunks=text.split(documents)
    return chunks


file_path='universal_declaration_of_human_rights.pdf'
documen_text=load_pdf(file_path)
chunks=create_chunks(documen_text)
print(len(chunks))
