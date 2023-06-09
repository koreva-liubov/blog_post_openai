from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, TextLoader


loader = DirectoryLoader(
    ".",
    glob="*.txt",
    loader_cls=TextLoader,
)

documents = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=1024,
    chunk_overlap=128,
)

persist_directory = "db"

texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory=persist_directory,
)

vectordb.persist()

