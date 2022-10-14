import csv
import sys
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

# Write data to csv
if "save" in sys.argv:
    with open("data.csv", "w") as f:
        writer = csv.writer(f)
        # isoformat
        for i in data:
            i[1] = i[1].isoformat()
        writer.writerows(data)

end = time.time()
print(f"Time taken (Pyodbc): {end - start}")
