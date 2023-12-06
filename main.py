import psycopg2
from typing import Union, Annotated
from dotenv import load_dotenv
import os

from fastapi import FastAPI, Header

env = load_dotenv()

app = FastAPI()
database = os.getenv('database')
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
port = os.getenv('port')


def create_conn(base):
    print(f'Connection: {base}, {host}, {user}, {password}, {port}')
    conn = psycopg2.connect(
        database=base,
        host=host,
        user=user,
        password=password,
        port=port
    )
    return conn


def check_code(code):
    conn = create_conn(database)
    query = (
        "select base from token_for_the_base where code = '{}';".format(code)
    )
    with conn.cursor() as cursor:
        cursor.execute(query)
        for row in cursor.fetchone():
            print(f'Code corresponds to base: {row}')
            return row


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/query")
def read_item(
    q: Union[str, None] = None,
    code: Annotated[str | None, Header()] = None
):
    base = check_code(code)
    conn = create_conn(base)
    with conn.cursor() as cursor:
        cursor.execute(q)

        result = []
        for row in cursor.fetchall():
            result.append(row)

    return {"result": result}
