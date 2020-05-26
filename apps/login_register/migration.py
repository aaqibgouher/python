import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="aaqib_python"
)
conn = db.cursor()

conn.execute("""
create table if not exists users(
    id int auto_increment primary key,
    name varchar(50),
    email varchar(100),
    password varchar(100)
)
""")
