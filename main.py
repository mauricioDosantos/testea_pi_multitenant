import psycopg2
from typing import Union
from dotenv import load_dotenv
import os

from fastapi import FastAPI

env = load_dotenv()

app = FastAPI()
database = os.getenv('database')
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
port = os.getenv('port')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/query/base/{base}")
def read_item(base: str, q: Union[str, None] = None):
    conn = psycopg2.connect(
        database=base,
        host=host,
        user=user,
        password=password,
        port=port
    )
    with conn.cursor() as cursor:
        print(base, host, user, password, port)
        cursor.execute(q)

        result = []
        for row in cursor.fetchall():
            result.append(row)

    return {"result": result}
