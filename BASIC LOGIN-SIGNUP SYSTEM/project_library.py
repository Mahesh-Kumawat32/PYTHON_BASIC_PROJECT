import re

def signup():
    pattern1 = r"^[a-z0-9]+@gmail\.com$"
    pattern2 = r"^(?=.*\d)(?=.*[^a-zA-Z0-9])[a-zA-Z0-9\W]{1,8}$"
    while True:
        email = input("EMAIL ADDRESS : ")
        if re.fullmatch(pattern1, email):
            print("EMAIL IS VALID 👍")
            break
        else:
            print("YOUR EMAIL IS NOT VALID! PLEASE ENTER AGAIN")
            continue
            
    with open('credential_user.txt',"a") as f:
        f.write(f"{email}\n")
    
    while True:
        print(20*"-")
        print("PASSWORD POLICY")
        print(20*"-")
        print("1.CONTAIN AT LEAST 1 DIGIT")
        print("2.CONTAIN AT LEAST 1 SPECIAL CHARACTER")
        print("3.LENGHT SHOULD BE 8")
        print(20*"-")
        password = input("ACCORDING TO POLICY ENTER PASSWORD : ")
        
        if re.fullmatch(pattern2, password):
            print("YOUR CREDENTIAL STORED SUCCESSFULLY👍")
            break
        else:
            print("YOUR PASSWORD IS NOT ACCORDING TO OUR POLICY READ BELOW AND ENTER AGAIN")
            continue

    with open('credential_user.txt',"a") as f:
        f.write(f"{password}\n")
        f.write("----------")
    while True:
        permission = input("YOU WANT TO LOGIN (YES/NO) : ").upper()
        if permission == "YES":
            login()
            break
        else:
            break

    

def login():
    pass
                
   