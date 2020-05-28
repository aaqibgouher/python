import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

cnnc = db.cursor()
cnnc.execute("CREATE DATABASE TEST")