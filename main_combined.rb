require "sequel"
require "benchmark"
require "fastcsv"

conn = Sequel.connect(
  adapter: "odbc",
  driver: "ODBC Driver 18 for SQL Server",
  server: "0.0.0.0",
  port: "1433",
  uid: "sa",
  pwd: "Password123",
  Encrypt: "yes",
  TrustServerCertificate: "yes",
  ConnectionTimeout: "5",
  Authentication: "SqlPassword",
  database: "TESTDB",
)

# data = conn.fetch("SELECT id FROM TESTTABLE").entries

benchmark_result = Benchmark.measure do
  result = system("python main.py save")
  rows = []
  File.open("data.csv") do |f|
    FastCSV.raw_parse(f) do |row|
      row[1] = Time.iso8601(row[1])
      rows.push(row)
    end
  end
end

puts "Time taken (total): #{benchmark_result.real}"
