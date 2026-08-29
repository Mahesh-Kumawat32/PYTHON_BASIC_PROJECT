import project_function
while True:
    print("="*90)
    print("\t\t\t\tSTUDENT MANAGEMENT SYSTEM")
    print("="*90)
    print("1. ADD STUDENT ")
    print("2. VIEW STUDENT")
    print("3. SEARCH STUDENT")
    print("4. UPDATE STUDENT")
    print("5. DELETE STUDENT ")
    print("6. EXIT")    
   
    choice = int(input("ENTER SERIES NO. : "))
    print("="*90)
    match choice:
        case 1:
            project_function.add_student()
        case 2:
            project_function.view_student()
        case 3:
            project_function.search_student()
        case 4:
            project_function.update_student()
        case 5:
            project_function.delete_student()
        case 6:
            print("\t\t\t\tTODAY WORK IS DONE 👍 SEE YOU TOMMOROW 😊")
            break
        case _:
            print("INVALID INPUT! PLEASE ENTER AGAIN")
           
