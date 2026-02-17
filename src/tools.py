from langchain_core.tools import tool

@tool
def somar(a: int, b: int) -> int:
    """Soma dois números inteiros"""
    return f"{a + b}\n"

@tool
def buscar_usuario(id: int) -> str:
    """Busca um usuário APENAS na lista interna/local da memória.
    Use esta ferramenta qunado o usuário pedir uma busca simples ou local.
    """
    usuarios = {
        1: "Alfonso",
        2: "Felipe",
        3: "Kelvin",
    }
    return usuarios.get(id, "Usuário não encontrado")

