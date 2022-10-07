require "sequel"
require "benchmark"

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

benchmark_result = Benchmark.measure do
  conn[:testtable].all
end

puts "Time taken (Sequel): #{benchmark_result.real}"
