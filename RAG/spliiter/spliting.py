from langchain_text_splitters import RecursiveCharacterTextSplitter
from RAG.Loader.pdfloader import load_pdfdata
from RAG.Loader.webloader import load_webdata
from langchain_huggingface import HuggingFaceEmbeddings

def split_data():
    splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
    docs=load_pdfdata()+load_webdata()
    
    chunks=splitter.split_documents(docs)
    
    return chunks


    