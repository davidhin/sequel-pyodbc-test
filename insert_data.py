import datetime
import uuid

import pyodbc
from tqdm import tqdm

conn = pyodbc.connect(
    "Driver=ODBC Driver 18 for SQL Server;"
    "Server=0.0.0.0;"
    "Port=1433;"
    "uid=sa;"
    "pwd=Password123;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
    "ConnectionTimeout=5;"
    "Authentication=SqlPassword;"
    "Database=TESTDB;",
    autocommit=True,
)


with conn.cursor() as cursor:
    cursor.execute("delete from TESTTABLE")

# Insert dummy data
with conn.cursor() as cursor:
    for i in tqdm(range(200)):
        value_string = [
            "('{}','{}')".format(uuid.uuid4(), datetime.datetime.now())
            for _ in range(1000)
        ]
        cursor.execute("insert into TESTTABLE values {}".format(",".join(value_string)))
