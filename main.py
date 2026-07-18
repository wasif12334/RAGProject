from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from RAG.retriver.retriver import retriver
load_dotenv()

llm=ChatMistralAI(
    model="mistral-medium-3-5"
)

template=ChatPromptTemplate.from_messages([

    ("system","""
You are an intelligent AI assistant that answers questions using the provided context.

Your responsibilities:
- Answer only using the provided context.
- If the context contains the answer, explain it clearly and accurately.
- If the answer is not present in the context, say:
  "I don't have enough information in the provided documents to answer that question."
- Do not make up facts or hallucinate.
- Keep answers concise but complete.
- If appropriate, present information as bullet points.
     """),
    ("human","""
Context:
{context}

Question:
{question}

""")
])
while True:
    userquery=input("ASK:")
    docs = retriver(userquery)

    context = "\n\n".join(doc.page_content for doc in docs)

    finalprompt=template.format_messages(

    context=context,
    question=userquery
)



    respone=llm.invoke(finalprompt)
    print(respone.content)
