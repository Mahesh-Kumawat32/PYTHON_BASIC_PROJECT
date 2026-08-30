import project_library

#FOR FORMATING---------------------------------------------------------------------
blue_bullet = "▶️"
green_bullet = "🟢"
info_bullet = "🟦"
red_bullet = "🔴"
print("="*100)
print("\t\t\t\t\tSTATE BANK OF INDIA")
#-----------------------------------------------------------------------------------

#MAIN MENU STARTS HERE--------------------------------------------------------------
while True:
    print("="*100)
    print("1 | CREATE NEW ACCOUNT")
    print("2 | WITHDRAWL MONEY")
    print("3 | DEPOSIT MONEY")
    print("4 | CHECK ACCOUNT BALANCE")
    print("5 | CHECK ACCOUNT INFORMATION")
    print("6 | REQUEST TO CHANGE PIN")
    print("7 | REQUEST TO CLOSE ACCOUNT")
    print("8 | APPLY FOR LOAN\n")
    menu_choice = int(input(f"{green_bullet} ENTER SR. NO. WHAT YOU WANT TO DO : "))
    print("="*100)
    match menu_choice:
        case 1:
            project_library.create_new_account()
        case 2:
            project_library.withdrawl_money()
        case 3:
            project_library.deposit_money()
        case 4:
            project_library.chk_account_blc()
        case 5:
            project_library.chk_account_info()
        case 6:
            project_library.change_pin()
        case 7:
            project_library.close_account()
        case 8:
            project_library.loan_details()
        case _:
            print(f"{red_bullet} INVALID CHOICE ! ENTER AGAIN")
            continue
#-----------------------------------------------------------------------------------
