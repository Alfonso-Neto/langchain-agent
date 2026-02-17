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
                ("system", """Você é um assistente de busca de dados.
                REGRAS OBRIGATÓRIAS:
                1. NUNCA tente adivinhar um ID. Se o usuário não forneceu um ID nesta mensagem nem no histórico, PERGUNTE o ID antes de usar qualquer ferramenta.
                2. 'buscar_usuario' acessa a lista LOCAL.
                3. 'consultar_banco' acessa o banco SQLITE.
                4. Antes de usar uma ferramenta, verifique o histórico (chat_history) para ver se o usuário já mencionou o ID ou nome dele.
                5. Se houver conflito entre a busca Local e o SQLite, apenas reporte os dois resultados de forma objetiva."""
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
                max_iterations=5,
        )

        return RunnableWithMessageHistory(
                agent_executor,
                get_session_history,
                input_messages_key="input",
                history_messages_key="chat_history",
        )