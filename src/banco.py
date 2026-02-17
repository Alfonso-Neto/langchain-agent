import sqlite3
from langchain.tools import tool

DB_PATH = "data/app.db"

@tool
def consultar_banco(id: int) -> str:
    """
    Busca um usuário pelo ID no banco SQLite.
    Retorna nome e email do usuário.
    """
    try: 
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT nome, email FROM usuarios WHERE id = ?",
            (id,)
        )

        row = cursor.fetchone()
        conn.close()

        if not row:
            return f"Nenhum usuário encontrado com id {id}."
        
        nome, email = row
        return f"Usuário encontrado: nome={nome}, email={email}"
    
    except Exception as e:
        return f"Erro ao consultar o banco: {str(e)}"
    