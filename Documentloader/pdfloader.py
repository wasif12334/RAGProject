from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.vectorstores import Chroma
load_dotenv()

#loadingthe pdf into olocal varible through pypdf loader
docs=PyPDFLoader("Documentloader/assests/resume.pdf").load()

#define the chunk size
splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
# spliting the docs into chunks
chunks=splitter.split_documents(docs)
print("Lenghts of chunks : ",len(chunks))
#emeding model define
embeding_model=HuggingFaceEmbeddings(
      model_name="sentence-transformers/all-MiniLM-L6-v2"
)
embeding_resume=embeding_model.embed_documents(chunks)

