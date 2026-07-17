from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

def load_pdfdata():
    loader = DirectoryLoader(
    "assets",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
    )

    pdfdata = loader.load()
    return pdfdata


