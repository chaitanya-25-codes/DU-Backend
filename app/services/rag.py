from app.services.intent import detect_intent
from langchain_openai import ChatOpenAI
from app.services.chunker import chunk_text
from app.services.chroma import get_chroma_collections
llm = ChatOpenAI(model_name="gpt-4o-mini")
def run_rag(description:str,text:str,doc_id:str):
    chunks=chunk_text(text)
    vectordb=get_chroma_collections(doc_id)
    vectordb.add_texts(chunks)
    vectordb.persist()
    
    if detect_intent(description)=='PURPOSE_DRIVEN_ANALYSIS':
        docs=vectordb.similarity_search(description,k=5)
        context="\n\n".join([doc.page_content for doc in docs])
        prompt = f"""
        User purpose:
        {description}
        Based on the following content,answer clearly
        {context}
        """
    else:
        prompt = f"""
        Provide a brief summary based on the following content:
        {text}
        """
    response = llm.invoke(prompt).content.strip()
    return response