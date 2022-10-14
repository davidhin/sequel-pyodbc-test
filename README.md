# Sequel Performance Testing

1. Create a mssql database in a table with the following schema:
   - id: integer
   - date: datetime2
2. Select all rows from the table using Pyodbc/Sequel

## Local results

| Rows      | Python + Pyodbc | Ruby + Sequel | Ruby + Python (Method1) |
| --------- | --------------- | ------------- | ----------------------- |
| 50,000    | 0.12s           | 2.65s         | 0.65s                   |
| 100,000   | 0.31s           | 6.19s         | 1.28s                   |
| 200,000   | 0.57s           | 16.95s        | 2.60s                   |
| 1,000,000 | 1.29s           |               | 13.96s                  |

## Ruby + Python

### Method1

1. Serialize datetime.datetime in python as iso8601
2. Use fastcsv to read csv in ruby
3. Deserialize using Time.iso8601
