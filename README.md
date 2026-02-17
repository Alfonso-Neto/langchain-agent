O que é LangChain?
É uma framework de código aberto escrito em Python e JavaScript/TypeScript, com o objetivo de facilitar a criação de aplicações que utilizam LLMs de forma encadeada. O LangChain permite criar fluxos onde a saída de um passo é a entrada do próximo.

Diferença entre LLM, Chat Moel, Tool, Chain e Agent:
1- LLM (Large Language Model)
É o "cérebro" que entende e gera texto.
Ele preve a próxima palavra, entende o contexto e gera respostas
Não executa ações, apenas gera texto

2- Chat Model
É um LLM ajustado para conversar, ele mantém histórico e o contexto de diálogo.
Diferente do LLM padrão, ele entende mensagens, mantém o contexto e responde de forma mais natural. Um exemplo de Chat Model é o ChatGPT ou até mesmo um chatbot no site de alguma empresa.

3- Tool (Ferramenta)
É qualquer função externa que o modelo pode usar.
Exemplos de tools: 
Busca de dados no banco
Consultar uma API
Criar um usuário
Enviar e-mail
Executar código

O LLM não executa a tool, ele apenas decide qual vai usar e passa os parâmetros corretos
Quem executa é o sistema

4- Chain
É uma sequência fixa de passos, onde cada etapa faz algo específico
Exemplo de chain:
- Interpretar pergunta
- Buscar dados no banco
- Processar dados
- Gerar resposta
Têm um fluxo pré-definido, ordem fixa e pouca ou nenhuma autonomia.

5- Agent
É um LLM com autonomia, tem capacidade de:
Decidir o que fazer
Escolher quais tools usar
Executar múltiplos passos
Corrigir erros
Parar quando atingir um objetivo
O agente usa:
LLM
Tools
Memória
Planejamento

O que mudou na versão 1.x?
Principalmente arquitetura, clareza e estabilidade
Visão geral 0.x vs 1.x
Antes APIs experimentais
Agora APIs estáveis
Antes tudo misturado
Agora módulos separados
Antes Chains complexas
Agora LCEL como padrão
Antes Agents confusos
Agora Agents mais explícitos
Antes Difícil ir para produção
Agora Foco em produção

O que é Runnable?
Runnable em LangChain provém uma estrutura e uma maneira modular de definir, executar e lidar com tarefas dentro de uma pipeline. Encapsulam varios componentes como models, tools chains e lógica customizada, fazendo-as serem reutilizáveis. É útil para construir workflows complexos, permitindo desenvolvedores quebrar tasks em unidades menores e administravéis.

Diagrama simples:
┌───────────────┐
│   Usuário     │
│ (Prompt/Input)│
└───────┬───────┘
        │
        ▼
┌────────────────────────┐
│   Prompt Template      │
│ (ChatPromptTemplate)  │
└────────┬──────────────┘
         │
         ▼
┌────────────────────────┐
│        LLM             │
│   (Chat Model)         │
│ ex: ChatOpenAI         │
└────────┬──────────────┘
         │
         ▼
┌────────────────────────┐
│   Output Parser        │
│ (String / JSON / etc) │
└────────┬──────────────┘
         │
         ▼
┌────────────────────────┐
│       Resposta         │
│     ao Usuário         │
└────────────────────────┘

## Clonar o repositório
git clone https://github.com/Alfonso-Neto/langchain-agent



## Configurar Ambiente
Instalar as dependências com o comando: 
pip install -r requirements.txt
Depois criar o ambiente virtual com: 
python3 -m venv venv ou python -m venv venv
Ativar o ambiente através do comando:
source venv/bin/activate

## Como conseguir sua chave API?
Acesse -> https://console.groq.com/
Faça login com sua conta
No menu lateral esquerdo, clique em "API keys"
Clique no botão "Create API key"

> Criar um arquivo .env na pasta raíz do projeto e adicione sua chave API:
GROQ_API_KEY=sua_chave_api

## Rodar o agente
Para rodar o agente utilize o comando:
python src/main.py

## Estrutura do projeto
/langchain-agent
├── /data
│   └── app.db          # Banco de dados SQLite oficial
├── /src
│   ├── agent.py        # Configuração do agente e lógica de memória
│   ├── banco.py        # Tool de consulta ao banco de dados SQLite
│   ├── config.py       # Gerenciamento de variáveis de ambiente
│   ├── llm.py          # Inicialização do modelo Groq
│   ├── main.py         # Ponto de entrada da aplicação
│   └── tools.py        # Ferramentas auxiliares (soma, busca local)
├── README.md
└── requirements.txt    # Dependências do projeto

# Como adicionar novas tools (Ferramentas)

O agente pode aprender novas habilidades facilmente. Para adicionar uma nova ferramenta, siga estes dois passos:

1. Crie a função em src/tools.py
Use o decorador @tool e escreva uma docstring (o texto entre aspas triplas) muito clara. O agente usa esse texto para entender quando e como usar a ferramenta.

2. Registre a ferramenta em src/agent.py
Importe sua nova função e adicione-a à lista de ferramentas dentro da função get_agent():