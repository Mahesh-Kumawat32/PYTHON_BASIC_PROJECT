import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Password",
    database = "student_management_system"
)

cursor = con.cursor()

def add_student():
    name = input("STUDENT NAME : ").strip().upper()
    city = input("CITY : ").upper().strip()
    marks = float(input("MARKS : "))
    confirm_add = input("SUBMIT (S) : ").upper()
    query = "INSERT INTO student_record(name,city,marks) values (%s,%s,%s)"
    values = (name, city, marks)

    if confirm_add=='S':
        cursor.execute(query,values)
        con.commit()
        print("STUDENT ADDED SUCCESSFULLY ✔")
    else:
        print("STUDENT RECORD DOES NOT ADDED ❌")

def view_student():
    choice = input("YOU WANT TO SEE ALL STUDENT RECORD (YES/NO) : ").upper()
    if choice == "YES":
        cursor.execute("SELECT * FROM student_record")
        rows = cursor.fetchall()
        print("-"*80)
        print(f"{'ID' : <5} | {'NAME' : <20} | {'CITY' : <20} | {'MARKS' : <5}")
        print("-"*80)
        for row in rows:
            print(f"{row[0] : <5} | {row[1] : <20} | {row[2] : <20} | {row[3] : <5}")
        print("-"*80)
        

def search_student():
    name = input("STUDENT NAME : ").upper().strip()
    cursor.execute("SELECT * FROM student_record where name = %s",(name,))
    row = cursor.fetchone()
    try:
        print("-"*80)
        print(f"STUDENT ID   : {row[0]}")
        print(f"STUDENT NAME : {row[1].upper()}")
        print(f"CITY         : {row[2].upper()}")
        print(f"MARKS        : {row[3]}")
        print("-"*80)
    except:
        print("STUDENT NOT FOUND")
    

def update_student():
    oldname = input("ENTER STUDENT NAME : ").strip().upper()
    cursor.execute("SELECT * from student_record where name = %s",(oldname,))
    row = cursor.fetchone()
    while True:
        print("-"*50)
        print("1. NAME")
        print("2. CITY")
        print("3. MARKS")
        choice = int(input("ENTER SERIES NO. WHAT YOU WANT TO CHANGE : "))
        print("-"*50)
        match choice:
            case 1:
                newname = input("ENTER NEW NAME : ").upper()
                cursor.execute("UPDATE student_record SET name = %s where id = %s",(newname,row[0]))
                confirm = input("YOU WANT TO CHANGE RECORD ? (YES/NO) : ").upper()
                if confirm == 'YES':
                    con.commit()
                    print("RECORD UPDATED SUCCESSFULLY")
                else:
                    print('UPDATION IS CANCELLED!')
            case 2:
                newcity = input("NEW CITY NAME : ").upper()
                cursor.execute("UPDATE student_record SET city = %s where id = %s",(newcity,row[0]))
             
                confirm = input("YOU WANT TO CHANGE RECORD ? (YES/NO) : ").upper()
                if confirm == 'YES':
                    con.commit()
                    print("RECORD UPDATED SUCCESSFULLY")
                else:
                    print('UPDATION IS CANCELLED!')
               
            case 3:
                newmarks = float(input("NEW MARKS : "))
                cursor.execute("UPDATE student_record SET marks = %s where id = %s",(newmarks,row[0]))
                confirm = input("YOU WANT TO CHANGE RECORD ? (YES/NO) : ").upper()
                if confirm == 'YES':
                    con.commit()
                    print("RECORD UPDATED SUCCESSFULLY ✔")
                else:
                    print('UPDATION IS CANCELLED!')
            case _:
                print("INVALID INPUT! PLEASE ENTER AGAIN")
                continue
        permission = input("YOU WANT TO UPDATE MORE DETAILS (YES/NO) : ").upper()
        if permission== 'YES':
            continue
        else:
            break

def delete_student():
    name = input("STUDENT NAME WANT TO DELETE : ").upper()
    cursor.execute('SELECT * FROM student_record where name = %s',(name,))
    row = cursor.fetchone()
    if row[1]==name:
        print('RECORD FOUND SUCCESSFULLY 👍')
        confirm = input("CONFIRM DELETE (CD) : ").upper()
        if confirm == 'CD':
            cursor.execute('DELETE FROM student_record where name = %s',(name,))
            con.commit()
            print("RECORD DELETED SUCCESSFULLY ✔")
        else:
            print('DELETE OPERATION IS CANCELLED')
    else:
        print("RECORD NOT FOUND")


    