# SQL Challenge

O desafio tem comoo intuito copiar as tabelas com os relacionamentos preservados. Inclui solução para copiar dados e associações mantendo a integridade referencial. A lǵica foi pensada usando o PostgreSQL como banco de dados.

## Sumário

- [Instalação](#instalação)
- [Uso Local](#uso-local)
- [Usando o algoritimo](#usando-o-algoritimo)

## Instalação

Para inciar este projeto, é necessário instalar as dependências. Para fazer a instalação basta dar o seguinte comando:

```
pip install -r requirements.txt
```

## Uso Local

1. Adicionar os dados do banco de dados no inicio dos arquivos sql/models.py.

```bash
conn = psycopg2.connect(
    host="localhost",
    database="db_postgres",
    user="usuario",
    password="senha"
)
```

2. Execute a criação das tabelas:

```bash
python models.py
```

3. Popule o banco de dados.

## Usando o algoritimo

1. Adicionar os dados do banco de dados no inicio dos arquivos sql/algorithm.py:

2. Adicionar os paramêtros na função copia_de_area(area, id_area_origem, id_area_destino):

    - area = Bloco ou torre
    - id_area_origem = Id do Bloco ou Torre origem
    - id_area_destino = Id do Bloco ou Torre destino

3. Rodar o seguinte comando:

```bash
python algorithm.py
```




