#ATM PROJECT

import random
import datetime
amount_to_withdrawl = None
amount_to_deposit = None
#DATA OF CUSOTMERS ALREADY STORED AND ENTER BY USERS*******************************************************************************
customer_data = {
    '1' : {},
    '2' : {"NAME":"RAHUL SHARMA",   "AC/NO":"12345678", "IFSC CODE":"SBIN0001234",  "BRANCH NAME":"NAVRANGPURA BRANCH", "BRANCH CITY":"AHMEDABAD",  "DATE OF AC CREATE":"15-08-2022",   "CURRENT ADDRESS":"SATELLITE, AHMEDABAD",   "PERMANENT ADDRESS":"JAIPUR, RAJASTHAN",    "PREVIOUS BALANCE":85420.75},
    '3' : {"NAME":"PRIYA PATEL",    "AC/NO":"23456789", "IFSC CODE":"HDFC0005678",  "BRANCH NAME":"CG ROAD BRANCH",     "BRANCH CITY":"AHMEDABAD",  "DATE OF AC CREATE":"22-01-2021",   "CURRENT ADDRESS":"NARANPURA, AHMEDABAD",   "PERMANENT ADDRESS":"VADODARA, GUJARAT",    "PREVIOUS BALANCE":126500.00},
    '4' : {"NAME":"AMIT VERMA",     "AC/NO":"34567890", "IFSC CODE":"ICIC0004321",  "BRANCH NAME":"CIVIL LINES BRANCH", "BRANCH CITY":"JAIPUR",     "DATE OF AC CREATE":"10-11-2020",   "CURRENT ADDRESS":"MALVIYA NAGAR, JAIPUR",  "PERMANENT ADDRESS":"KOTA, RAJASTHAN",      "PREVIOUS BALANCE":45230.50},
    '5' : {"NAME":"SNEHA JOSHI",    "AC/NO":"45678901", "IFSC CODE":"PUNB0009876",  "BRANCH NAME":"SHIVRANJANI BRANCH", "BRANCH CITY":"AHMEDABAD",  "DATE OF AC CREATE":"05-03-2023",   "CURRENT ADDRESS":"VASTRAPUR, AHMEDABAD",   "PERMANENT ADDRESS":"SURAT, GUJARAT",       "PREVIOUS BALANCE":9800.00},
    '6' : {"NAME":"VIKAS SINGH",    "AC/NO":"56789012", "IFSC CODE":"AXIS0002468",  "BRANCH NAME":"HAZRATGANJ BRANCH",  "BRANCH CITY":"LUCKNOW",    "DATE OF AC CREATE":"18-07-2019",   "CURRENT ADDRESS":"ALIGANJ, LUCKNOW",       "PERMANENT ADDRESS":"KANPUR, UTTAR PRADESH","PREVIOUS BALANCE":240750.90},
    '7' : {"NAME":"ANKIT GUPTA",    "AC/NO":"67890123", "IFSC CODE":"SBIN0004567",  "BRANCH NAME":"ASHRAM ROAD BRANCH", "BRANCH CITY":"AHMEDABAD",  "DATE OF AC CREATE":"11-06-2021",   "CURRENT ADDRESS":"PALDI, AHMEDABAD",       "PERMANENT ADDRESS":"UDAIPUR, RAJASTHAN",   "PREVIOUS BALANCE":75890.50},
    '8' : {"NAME":"NEHA SHAH",      "AC/NO":"78901234", "IFSC CODE":"HDFC0007890",  "BRANCH NAME":"MANINAGAR BRANCH",   "BRANCH CITY":"AHMEDABAD",  "DATE OF AC CREATE":"09-02-2020",   "CURRENT ADDRESS":"MANINAGAR, AHMEDABAD",   "PERMANENT ADDRESS":"RAJKOT, GUJARAT",      "PREVIOUS BALANCE":154320.75},
    '9' : {"NAME":"ROHIT MEHTA",    "AC/NO":"89012345", "IFSC CODE":"ICIC0006543",  "BRANCH NAME":"BAPUNAGAR BRANCH",   "BRANCH CITY":"AHMEDABAD",  "DATE OF AC CREATE":"27-09-2023",   "CURRENT ADDRESS":"BAPUNAGAR, AHMEDABAD",   "PERMANENT ADDRESS":"BHAVNAGAR, GUJARAT",   "PREVIOUS BALANCE":24350.00},
    '10' : {"NAME":"KARAN SINGH",   "AC/NO":"11223344", "IFSC CODE":"PUNB0002468",  "BRANCH NAME":"MANSAROVAR BRANCH",  "BRANCH CITY":"JAIPUR",     "DATE OF AC CREATE":"30-05-2022",   "CURRENT ADDRESS":"MANSAROVAR, JAIPUR",     "PERMANENT ADDRESS":"JODHPUR, RAJASTHAN",   "PREVIOUS BALANCE":67540.10}
}
#**********************************************************************************************************************************

#FUNCTION USING USER CAN CREATE ACCOUNT********************************************************************************************
def create_account(name,permanent_address,current_address,amount_to_first_deposit):
    customer_name = name
    customer_ac = random.randint(10000000,99999999)
    ifsc_code = "SBIN0001234"
    branch_location = "ISANPUR"
    branch_city = "AHMEDABAD"
    customer_permanent_address = permanent_address
    customer_current_address = current_address
    customer_first_deposit = amount_to_first_deposit
    print(f"\nYOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY ✔\nYOUR DETAILS ARE AS BELOW : ")
    customer_data['1']["NAME"] = customer_name
    customer_data['1']["AC/NO"] = customer_ac
    customer_data['1']["IFSC CODE"] = ifsc_code
    customer_data['1']["BRANCH NAME"] = branch_location
    customer_data['1']["BRANCH CITY"] = branch_city
    customer_data['1']["DATE OF AC CREATE"] = datetime.date.today()
    customer_data['1']["CURRENT ADDRESS"] = customer_current_address
    customer_data['1']["PERMANENT ADDRESS"] = customer_permanent_address
    customer_data['1']["PREVIOUS BALANCE"] = customer_first_deposit
    print(80*"-")
    for a,b in customer_data['1'].items():
        print(f"{a} : {b}")
    print(80*"-")
#**********************************************************************************************************************************


#FUNCTION HELPS USER TO CREDIT/DEPOSIT MONEY TO ACCOUNT****************************************************************************
def deposit_money(ac_no):
    for i in range(2,10):
        if customer_data[str(i)]['AC/NO']==ac_no:
            print(80*'-')
            print(f"YOUR RECORD FOUND SUCCESSFULLY 👍")
            global amount_to_deposit
            amount_to_deposit = float(input("ENTER AMOUNT YOU WANT TO DEPOSIT : "))
            confirm_deposit = input("PRESS 'CD' TO CONFIRM DEPOSIT : ").upper()
            if confirm_deposit == "CD":
                print(f"AMOUNT {amount_to_deposit} CREDITED SUCCESSFULLY TO AC/NO : {customer_data[str(i)]['AC/NO']}👍")
                print(80*'-')
                new_balance = (customer_data[str(i)]['PREVIOUS BALANCE']+amount_to_deposit)
                for a,b in customer_data[str(i)].items():
                    print(f"{a} : {b}")
                print(f"CURRENT BALANCE : {new_balance}")
                customer_data[str(i)]['PREVIOUS BALANCE'] = new_balance
            else:
                print('DEPOSIT CANCELLED X')
            print(80*'-')
        else:
            continue     
#**********************************************************************************************************************************


#FUNCTION HELPS USER TO WITHDRAWL MONEY FROM ACCOUNT****************************************************************************
def withdrawl_money(ac_no):
       for i in range(2,10):
            if customer_data[str(i)]['AC/NO']==ac_no:
                print(80*'-')
                print(f"YOUR RECORD FOUND SUCCESSFULLY 👍")
                global amount_to_withdrawl
                amount_to_withdrawl = float(input("ENTER AMOUNT YOU WANT TO WITHDRAWL : "))
                if amount_to_withdrawl<customer_data[str(i)]['PREVIOUS BALANCE']:
                    confirm_withdrawl = input("PRESS 'CW' TO CONFIRM WITHDRAWL : ").upper()
                    if confirm_withdrawl == "CW":
                        print(f"AMOUNT {amount_to_withdrawl} WITHDRAWL SUCCESSFULLY FROM AC/NO : {customer_data[str(i)]['AC/NO']}👍")
                        print(80*'-')
                        new_balance = (customer_data[str(i)]['PREVIOUS BALANCE']-amount_to_withdrawl)
                        for a,b in customer_data[str(i)].items():
                            print(f"{a} : {b}")
                        print(f"CURRENT BALANCE : {new_balance}")
                        print(f"WITHDRAWL AMOUNT : {amount_to_withdrawl}")
                        customer_data[str(i)]['PREVIOUS BALANCE'] = new_balance
                    else:
                        print('WITHDRAWL CANCELLED X')
                else:
                    print(f"YOU CANNOT WITHDRAWL {amount_to_withdrawl} BECAUSE YOUR PREVIOUS BALANCE IS {customer_data[str(i)]['PREVIOUS BALANCE']}")
                    print("PLEASE TRY AGAIN")
                print(80*'-')
            else:
                continue 
#**********************************************************************************************************************************


#FUNCTION HELPS USER TO CHECK THEIR ACCOUNT STATUS ACCOUNT*************************************************************************
def check_balance(ac_no):
    cnt = 0
    for i in range(2,10):
            if customer_data[str(i)]['AC/NO']==ac_no:
                global base
                base = str(i)
                cnt = cnt +1
            else:
                continue
    if cnt == 1:
        print(80*"-")
        for a,b in customer_data[base].items():
            print(f"{a} : {b}")
        print(80*"-")
    else:
        print("CHECK YOUR AC/NO")
#**********************************************************************************************************************************


#FUNCTION HELPS USER TO CHECK THEIR TRANSACTION HISTORY OF ACCOUNT****************************************************************
transaction_details = {}
def transaction_history(ac_no):
    cnt = 0
    for i in range(2,10):
        if customer_data[str(i)]['AC/NO']==ac_no:
            cnt = cnt +1
            transaction_details["DATE"]=datetime.date.today()
            transaction_details["CREDITED AMOUNT"] = amount_to_deposit
            transaction_details["WITHDRAWL AMOUNT"] = amount_to_withdrawl
        else:
            continue
    if cnt == 1:
        print(80*"-")
        for a,b in transaction_details.items():
            print(f"{a} : {b}")
        print(f"AC/NO : {ac_no}")
        print(80*"-")
    else:
        print("SOMETHING WRONG IN AC/NO OR SOMETHING ELSE")
#**********************************************************************************************************************************


#PROGRAM EXECUTION STARTS FROM HERE ***********************************************************************************************
heading = " STATE BANK OF INDIA "
print(heading.center(100,"*"))
while True:
    permission_to_create_ac = input("TO PROCEED FURTHER ENTER => (YES/NO): ").upper()
    if permission_to_create_ac=="YES":
        print("\n")
        choice = input("> TO CREATE A NEW ACCOUNT (PRESS) => A\n> TO DEPOSIT MONEY (PRESS) => D\n> TO WITHDRAWL MONEY (PRESS) => W\n> TO CHECHING BALANCE (PRESS) => CB\n> TO CHECK TRANSACTION HISTORY (PRESS) => H\n=>").upper()
        match choice:
            case 'A':
                name = input("ENTER YOUR FULL NAME : ").upper()
                permanent_address = input('ENTER YOUR PERMANENT ADDRESS : ').upper()
                current_address = input("ENTER YOUR CURRENT ADDRESS : ").upper()
                amount_to_first_deposit = float(input("ENTER AMOUNT YOU WANT TO DEPOSIT FIRST (MINIMUM 500/-) : "))
                create_account(name,permanent_address,current_address,amount_to_first_deposit)
            case 'D':
                print("\n")
                ac_no = input("ENTER YOUR AC/NO : ")
                deposit_money(ac_no)
            case 'W':
                ac_no = input("ENTER YOUR 8 DIGIT AC/NO : ")
                withdrawl_money(ac_no)
            case 'CB':
                ac_no = input("ENTER YOUR 8 DIGIT AC/NO : ")
                check_balance(ac_no)
            case 'H':
                ac_no = input("ENTER YOUR 8 DIGIT AC/NO : ")
                transaction_history(ac_no)
            case _:
                print("YOU ENTER SOMETHING WRONG! PLEASE TRY AGAIN")
    else:
        break
print(100*"*")
#*********************************************************************************************************************************