from langchain_core.prompts import ChatPromptTemplate
from llm import get_llm

def main():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente útil."),
        ("human", "Explique o que é LangChain em uma frase.")
    ])

    chain = prompt | llm
    response = chain.invoke({})

    print(response.content)

if __name__ == "__main__":
    main()