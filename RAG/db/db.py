from langchain_chroma import Chroma
from RAG.spliiter.spliting import split_data
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

chunks=split_data()
embeding_model=HuggingFaceEmbeddings(
   model="sentence-transformers/all-MiniLM-L6-v2"
 )
vectorstore=Chroma.from_documents(
     documents=chunks,
     persist_directory="VectorDB",
     embedding=embeding_model,
 )