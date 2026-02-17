import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/app.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

cursor.execute("""
INSERT OR IGNORE INTO usuarios (id, nome, email)
VALUES (1, 'João Silva', 'joao@email.com')
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")