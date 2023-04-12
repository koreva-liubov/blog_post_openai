import gradio as gr
import random
import time

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

persist_directory = "db"

embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory=persist_directory,
    embedding_function=embeddings,
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=False
)

qa = ConversationalRetrievalChain.from_llm(
    llm=OpenAI(temperature=0, max_tokens=-1),
    chain_type="stuff",
    retriever=db.as_retriever(),
    memory=memory,
    get_chat_history=lambda h: h,
    verbose=True,
)

res = qa(
    {
    #"question": "How does Magine tackle cold start problem in their recommendation engine?",
    "question": "How recommendation engine is implemented?",
    "chat_history": [],
    }
)

print(res)