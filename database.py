import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="blood_bank"
)
conn = db.cursor(dictionary=True)

# select multiple rows
conn.execute("select * from users")
users = conn.fetchall()
print(users)

for user in users:
    print(user)
    print(user["name"])

# select one orw
conn.execute("select * from users where id=1")
user = conn.fetchone()
print(user)