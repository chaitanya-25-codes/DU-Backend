from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
CHROMA_DIR="chroma-db"
embedding_model=OpenAIEmbeddings(model="text-embedding-3-small")
def get_chroma_collections(collection_name:str):
    return Chroma(
        collection_name=collection_name,
        embedding_function=embedding_model,
        persist_directory=CHROMA_DIR
    )