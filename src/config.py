from dotenv import load_dotenv
import os

load_dotenv()

settings = {
    "MODEL_NAME": "llama-3.1-8b-instant",
    "TEMPERATURE": 0.2,
    "GROQ_API_KEY": os.getenv("GROQ_API_KEY"),
}