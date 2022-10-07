# Sequel Performance Testing

1. Create a mssql database in a table with the following schema:
   - id: integer
   - date: datetime2
2. Select all rows from the table using Pyodbc/Sequel

## Local results

| Rows    | Python + Pyodbc | Ruby + Sequel |
| ------- | --------------- | ------------- |
| 50,000  | 0.001s          | 2.65s         |
| 100,000 | 0.002s          | 6.19s         |
| 200,000 | 0.002s          | 16.95s        |
