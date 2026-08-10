import project_library
print(80*"-")
print("\t\t\t\tWELCOME TO OUT WEBSITE")
print(80*"-")
while True:
    choice = int(input("\n1.SIGN UP (PRESS) -> 1\n2.LOGIN   (PRESS) -> 2\n> "))
    match choice:
        case 1:
            project_library.signup()
            break
        case 2:
            project_library.login()
            break
        case _:
            print("YOU ENTER A WRONG CHOICE! PLEASE ENTER AGAIN")
            continue


