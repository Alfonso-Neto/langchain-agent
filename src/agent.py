from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from llm import get_llm
from tools import somar, buscar_usuario
from banco import consultar_banco

def get_agent():
        llm = get_llm()

        tools = [somar, buscar_usuario, consultar_banco]

        prompt = ChatPromptTemplate.from_messages([
                ("system", "Você é um assistente que pode usar ferramentas quando necessário."),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
        ])

        agent = create_tool_calling_agent(
                llm=llm,
                tools=tools,
                prompt=prompt,
        )

        return AgentExecutor(
                agent=agent,
                tools=tools,
                verbose=True,
                max_iterations=2,
        )