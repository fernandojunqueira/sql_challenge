import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="db_postgres",
    user="usuario",
    password="senha"
)
cur = conn.cursor()


def procurar_bloco_por_id(id):
    cur.execute("SELECT * FROM blocos WHERE id = %s", (id,))

    return cur.fetchall()


def procurar_torre_por_id(id):
    cur.execute("SELECT * FROM torres WHERE id = %s", (id,))

    return cur.fetchall()


def copia_de_area(area, id_area_origem, id_area_destino):

    if area.lower() == 'torre':

        torre_origem = procurar_torre_por_id(id_area_origem)
        torre_destino = procurar_torre_por_id(id_area_destino)

        if len(torre_origem) == 0 or len(torre_destino) == 0:
            return 'As duas torres precisam existir.'

        query_copia_dos_pavimentos = """
        INSERT INTO pavimentos  (id_torre , nome, criador)
        SELECT %s, p.nome, p.criador
        FROM torres t
        INNER JOIN pavimentos p ON t.id = p.id_torre
        WHERE t.id = %s;
        """

        cur.execute(
            query_copia_dos_pavimentos, (id_area_destino, id_area_origem)
            )

        conn.commit()

        return 'Dados copiados'
    else:

        bloco_origem = procurar_bloco_por_id(id_area_origem)
        bloco_destino = procurar_bloco_por_id(id_area_destino)

        if len(bloco_origem) == 0 or len(bloco_destino) == 0:
            return 'Os dois blocos precisam existir.'

        query_copia_das_torres = """
        INSERT INTO torres (id_bloco, nome, criador)
        SELECT %s, t.nome, t.criador
        FROM blocos b
        INNER JOIN torres t ON b.id = t.id_bloco
        WHERE b.id = %s;
        """

        cur.execute(
            query_copia_das_torres, (id_area_destino, id_area_origem)
            )

        conn.commit()

        return 'Dados copiados'


copia_de_area(
    'bloco',
    '8f995d4d-084f-4602-b86e-bb32eb915eaa',
    '80627ed2-6af0-4b11-9931-50d0062fcac2'
    )
