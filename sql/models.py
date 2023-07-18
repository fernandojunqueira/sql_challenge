import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="db_postgres",
    user="usuario",
    password="senha"
)

cur = conn.cursor()

create_table_blocos = """
    CREATE TABLE IF NOT EXISTS tb_blocos (
        id VARCHAR(36) DEFAULT gen_random_uuid() PRIMARY KEY,
        nome VARCHAR(50),
        criador VARCHAR(100),
        criacao TIMESTAMP DEFAULT current_timestamp
    )
"""

create_table_torres = """
    CREATE TABLE IF NOT EXISTS tb_torres (
        id VARCHAR(36) DEFAULT gen_random_uuid() PRIMARY KEY,
        id_bloco VARCHAR(36),
        nome VARCHAR(50),
        criador VARCHAR(100),
        criacao TIMESTAMP DEFAULT current_timestamp,
        FOREIGN KEY (id_bloco) REFERENCES blocos (id)
    )
"""

create_table_pavimentos = """
    CREATE TABLE IF NOT EXISTS tb_pavimentos (
        id VARCHAR(36) DEFAULT gen_random_uuid() PRIMARY KEY,
        id_torre VARCHAR(36),
        nome VARCHAR(50),
        criador VARCHAR(100),
        criacao TIMESTAMP DEFAULT current_timestamp,
        FOREIGN KEY (id_torre) REFERENCES torres (id)
    )
"""

cur.execute(create_table_blocos)
cur.execute(create_table_torres)
cur.execute(create_table_pavimentos)

conn.commit()
