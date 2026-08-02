#HOSPITAL MANAGEMENT SYSTEM
import hospital_func_library
while True:
    print("\n")
    print(100*"-")
    print("\t\t\t\tGOVERMENT HOSPITAL OF GUJARAT")
    print(100*"-")
    choice = input("1. PATIENT REGISTRATION\n2. SEARCH PATIENT\n3. APPOINTMENT DETAILS\n4. CREATE BILL\n5. DELETE PATIENT\n6. EXIT\n\nTO PROCEED ENTER SERIES NO. : ")
    match choice:
        case '1':
            hospital_func_library.regestration()
        case '2':
            hospital_func_library.search_patient()
        case '3':
            hospital_func_library.appointment()
        case '4':
            hospital_func_library.create_bill()
        case '5':
            hospital_func_library.delete_patient()
        case _:
            continue