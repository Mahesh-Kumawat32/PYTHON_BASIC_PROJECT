import mysql.connector

con =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = ""
)

cursor = con.cursor()

print("="*80)
print("\t\t\t\tWELCOME TO OUR WEBSITE")
print("="*80)
print("\n")

def login_system():
    login_greet = " LOGIN "
    print(login_greet.center(80,"-"))
    while True:
        try:
            username = input("USERNAME : ")
            password = input("PASSWORD : ")
            cursor.execute("SELECT * FROM user where PASSWORD = %s",(password,))
            row = cursor.fetchone()
            if row[1]==username and row[2]==password:
                print("YOU LOGGED IN SUCCESSFULLY👍")
                break
        except:
            print("WRONG CREDENTIAL! PLEASE ENTER AGAIN")
            continue

def signup():
    signup_greet = " SIGN UP "
    print(signup_greet.center(80,"-"))
    while True:
        username = input("USERNAME : ")
        if len(username)==10:
            if ('@' in username or 
                '$' in username or
                '#' in username or
                '%' in username or
                '&' in username):
                break
        else:
            print("INVALID USERNAME! PLEASE CHECK OUT THE USERNAME POLICY\n1.LENGHT WILL BE 10\n2.CONTAINS ALPHABETS\n3.AT LEAST ONE SPECIAL CHARACTER\n4.AT LEAST ONE DIGIT")
            continue
    while True:
        password = input("PASSWORD : ")
        if len(password)==8 and password.isalnum():
            print("YOU CREDENTIAL STORED SUCCESSFULLY👍")
            break
        else:
            print("INVALID PASSWORD! PLEASE CHECK OUT THE PASSWORD POLICY\n1.LENGHT WILL BE 8\n2.CONTAINS ALPHABETS\n3.NO SPECIAL CHARACTER\n4.AT LEAST ONE DIGIT")
            continue
    query = '''INSERT INTO user(USERNAME, PASSWORD) values (%s,%s)'''
    values = (username, password)
    cursor.execute(query, values)
    con.commit()

while True:
    user_choice = int(input("1. IF YOU VISTI FIRST TIME PLEASE SIGN UP!\n2. IF YOU ALREADY MEMEBER OF OUR PLATFORM PLEASE LOGIN\n> "))
    match user_choice:
        case 1:
            signup()
            break
        case 2:
            login_system()
            break
        case _:
            print("YOU ENTERED SOMETHING WRONG! RE-ENTER YOUR CHOICE ")
            continue