from langchain_groq import ChatGroq
from config import settings

def get_llm():
    return ChatGroq(
        model=settings["MODEL_NAME"],
        temperature=settings["TEMPERATURE"],
        api_key=settings["GROQ_API_KEY"],
    )