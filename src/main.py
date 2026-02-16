from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm

def main():
    prompt = ChatPromptTemplate.from_template(
        "Explique o que é LCEL em LangChain em uma frase curta."
    )

    llm = get_llm()
    parser = StrOutputParser()

    chain = prompt | llm | parser

    response = chain.invoke({})
    print(response)

if __name__ == "__main__":
    main()