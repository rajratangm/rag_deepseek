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
        chunk_overlap=200,
        add_start_index=True,
    )
    chunks=splitter.split_documents(documents)
    return chunks



file_path='universal_declaration_of_human_rights.pdf'
documen_text=load_pdf(file_path)
chunks=create_chunks(documen_text)


ollama_model_name='deepseek-r1:1.5b'

def get_embeddings(chunks):
    vector_store=FAISS(ollama_model_name)
    embeddings=vector_store.get_embeddings(chunks)
    return embeddings








print(len(chunks))
