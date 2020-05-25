from connection import conn, db

def register():
    try:
        print("Welcome to register")

        email = input("Email: ")
        if email == "": raise Exception("Email is required.")

        # check email exist
        conn.execute("select * from users where email='{}'".format(email))
        user = conn.fetchall()
        if user: raise Exception("Email already exist.")

        password = input("Password: ")
        if password == "": raise Exception("Password is required.")
        if len(password) < 4 and len(password) > 12: raise Exception("password should be min 4 and max 12 length")
        
        name = input("Full Name: ")
        if name == "": raise Exception("Full Name is required.")

        conn.execute("insert into users values (null, %s, %s, %s)", (name, email, password))
        db.commit()
        print("Register successfull")
    except Exception as e:
        print(e)

while True:
    register()
    break