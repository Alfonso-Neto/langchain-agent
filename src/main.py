from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm
from agent import get_agent

def main():
    agente = get_agent()

    config = {"configurable": {"session_id": "usuario_123"}}

    print("#Passo 1 - Identificação")
    agente.invoke(
        {"input": "Olá, estamos analisando o usuário de ID 3."},
        config=config
    )


    print("\n#Passo 2 - Testar memória")
    res = agente.invoke(
        {"input": "Busque este usuário localmente e também no banco oficial. Existem divergências?"},
        config=config
    )
    print(res["output"])

    print("#Passo 3 - Cálculo")
    res_soma = agente.invoke(
        {"input": "O usuário 3 disse que tem 10 pontos. O usuário 2 tem 15. Qual o total?"},
        config=config
    )
    print(res_soma["output"])

if __name__ == "__main__":
    main()