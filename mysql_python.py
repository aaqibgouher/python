import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

my_db = db.cursor()

# my_db.execute("create database test")     #created a test db

my_db.execute("use test")     #using test db

# my_db.execute("create table std_details (id int auto_increment primary key,name varchar(50),house varchar(10))")  # created a table named std_details
# my_db.execute("show tables")      # using this query it will not show in terminal
# for i in my_db:                   #thats wht we have used for loop here
#     print(i)

# sql = "insert into std_details values (null,%s,%s)"
# value = ("mohan","Red")
# my_db.execute(sql,value)       #execute will use when there will be single insertion     
# db.commit()
# print(my_db.rowcount,"row inserted")      #for output in terminal

# sql = "insert into std_details values (null,%s,%s)"
# value = [
#     ("saurav","Blue"),
#     ("rohan","Yellow"),
#     ("deepa","Red"),
#     ("rahul","Green"),
#     ("ranjeet","Red"),
#     ("priya","Green"),
#     ("hari","Yellow"),
#     ("sunanda","Blue"),
#     ("rekha","Green")
# ]
# my_db.executemany(sql,value)            #executemany is used when, we have to insert more than one data at once 
# db.commit()
# print(my_db.rowcount, "inserted")

# print("last row Id is ",my_db.lastrowid)      #to get last id 

# my_db.execute("select * from std_details")        #select the all data from table the table
# data = my_db.fetchall()
# for i in data :
#     print(i)

# my_db.execute("select * from std_details")       #select the only one data i,e first one
# data = my_db.fetchone()
# for i in data :
#     print(i)

# my_db.execute("select name from std_details where house = 'Red'")        we can do this as well or
# data = my_db.fetchall()
# for i in data :
#     print(i)

# sql = "select * from std_details where house = %s"        store the query in one var and value in other and then pass in fx
# value = ("Red",)
# my_db.execute(sql,value)        
# data = my_db.fetchall()
# for i in data :
#     print(i)

# my_db.execute("select name from std_details order by name desc")        use of order by clause
# data = my_db.fetchall()
# for i in data :
#     print(i)

# my_db.execute("update std_details set house = 'Yellow' where name = 'priya'")        update the tables row 
# db.commit()
# print(my_db.rowcount,"row affected")

# my_db.execute("select * from std_details")        for checking that value is updated or not
# data = my_db.fetchall()
# for i in data :
#     print(i)

# my_db.execute("select * from std_details limit 5")
