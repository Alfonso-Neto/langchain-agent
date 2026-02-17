from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm
from agent import get_agent

def main():
    agent = get_agent()

    response = agent.invoke({
        "input": "Qual é o usuário com o ID 2 localmente, usando somente a tool buscar_usuario?"
    })
    
    print(response["output"])

if __name__ == "__main__":
    main()