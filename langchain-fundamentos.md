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
cd ~