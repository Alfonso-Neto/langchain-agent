import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from config import MODEL_NAME, TEMPERATURE

load_dotenv()

def get_llm():
    return ChatOpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )
