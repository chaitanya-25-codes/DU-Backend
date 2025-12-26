from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
def detect_intent(description:str)->str:
    prompt = f"""
    classify the users intent into one of the following:
    1. GENERAL_SUMMARY – user wants an overall brief or explanation
    2. PURPOSE_DRIVEN_ANALYSIS – user has a specific goal or criteria
    
    user description:
    {description}
    Respond with only one word: GENERAL_SUMMARY or PURPOSE_DRIVEN_ANALYSIS
    """
    response = llm.invoke(prompt).content.strip()
    return response