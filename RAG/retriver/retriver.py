from RAG.db.db import vectorstore

def retriver(userquery):
    retriver=vectorstore
    repsonse=retriver.as_retriever(
    search_type="mmr",
    search_kwargs={"k":5}
)
    result=repsonse.invoke(userquery)
    return result