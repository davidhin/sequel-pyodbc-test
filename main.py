import time

import pyodbc

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
    "Database=TESTDB;"
)

start = time.time()
with conn.cursor() as cursor:
    cursor.execute("select * from TESTTABLE")
    data = cursor.fetchall()
    print(len(data))
end = time.time()

print(f"Time taken (Pyodbc): {end - start}")
