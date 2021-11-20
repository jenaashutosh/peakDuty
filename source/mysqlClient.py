import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="appUser",
  password="my5qL@2021"
)

print(mydb)