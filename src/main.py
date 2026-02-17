from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm
from agent import get_agent

def main():
    agent_with_memory = get_agent()

    config = {"configurable": {"session_id": "usuario_123"}}

    print("#Pergunta 1")
    res1 = agent_with_memory.invoke(
        {"input": "Olá, meu nome é Alfonso e meu ID é 1."},
        config=config
    )
    print(res1["output"])

    print("\n#Pergunta 2")
    res2 = agent_with_memory.invoke(
        {"input": "Qual é o meu nome e o que consta localmente sobre meu ID? use a tool buscar_usuario"},
        config=config
    )
    print(res2["output"])

if __name__ == "__main__":
    main()