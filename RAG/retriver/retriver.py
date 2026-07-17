from RAG.db.db import vectorstore

def retriver():
    retriver=vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k":5}
)

    response=retriver.invoke("What is the addmision policy for the new student ")
    for r in response:
        print(r.page_content)