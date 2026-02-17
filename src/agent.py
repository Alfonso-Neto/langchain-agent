from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from llm import get_llm
from tools import somar, buscar_usuario
from banco import consultar_banco

store = {}

def get_session_history(session_id: str):
        if session_id not in store:
                store[session_id] = ChatMessageHistory()
        return store[session_id]

def get_agent():
        llm = get_llm()
        tools = [somar, buscar_usuario, consultar_banco]

        prompt = ChatPromptTemplate.from_messages([
                ("system", """Você é um Especialista em Auditoria de Sistemas.
                Sua missão é cruzar dados locais com o banco de dados oficial.

                REGRAS DE OPERAÇÃO:
                1. MEMÓRIA: Antes de usar qualquer ferramenta, verifique se o usuário já mencionou o ID ou nome no histórico.
                2. PRECISÃO: NUNCA use o ID 1 a menos que o usuário peça explicitamente ou que esse ID esteja no histórico recente.
                3. FERRAMENTAS: Use 'buscar_usuario' para dados preliminares/locais e 'consultar_banco' para dados oficiais do SQLite.
                4. CÁLCULOS: Use a ferramenta 'somar' para qualquer operação matemática, não faça de cabeça.
                5. Se houver diferença entre o nome local e o nome no banco, aponte isso como uma 'Divergência de Auditoria'."""
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
        ])

        agent = create_tool_calling_agent(
                llm=llm,
                tools=tools,
                prompt=prompt,
        )

        agent_executor = AgentExecutor(
                agent=agent,
                tools=tools,
                verbose=True,
                max_iterations=1,
        )

        return RunnableWithMessageHistory(
                agent_executor,
                get_session_history,
                input_messages_key="input",
                history_messages_key="chat_history",
        )