import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)


from langchain_chroma import Chroma
from RAG.spliiter.spliting import split_data
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()
chunks=split_data()
embeding_model=HuggingFaceEmbeddings(
   model="sentence-transformers/all-MiniLM-L6-v2"
 )
   
    # for ch in chunks:
    #     print(ch.page_content)
    #     print(ch.metadata)
vectorstore=Chroma.from_documents(
     documents=chunks,
     persist_directory="VectorDB",
     embedding=embeding_model,
 )
 

