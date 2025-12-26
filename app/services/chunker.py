from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(txt:str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
    )
    return splitter.split_text(txt)