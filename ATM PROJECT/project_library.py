#IMPORTANT LIBRARIES AND PACKAGES TO PROJECT==========================================
import mysql.connector
import random
import atm_project
from datetime import date,timedelta
#DATABASE CONNECTIVITY================================================================
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bank"
)
cursor = con.cursor()

#FORMATING ICONS FOR PROGRAMMING=======================================================
blue_bullet = "▶️ "
green_bullet = "🟢 "
info_bullet = "🟦 "
red_bullet = "🔴 "

#TO CREATE NEW ACCOUNT=================================================================
def create_new_account_at_bank():
    while True:
        firstname = input(f"{green_bullet} FIRST NAME : ").upper().strip()
        if firstname.isalpha():
            break
        else:
            print(f"{red_bullet} ENTER VALID FIRST NAME!")
            continue
    while True:
        secondname = input(f"{green_bullet} SECOND NAME : ").upper().strip()
        if secondname.isalpha():
            break
        else:
            print(f"{red_bullet} ENTER VALID SECOND NAME!")
            continue

    while True:
        mobile = int(input(f"{green_bullet} MOBILE NO : "))
        if len(str(mobile))==10:
            break
        else:
            print(f"{red_bullet} ENTER VALID MOBILE NO!")
            continue
    
    while True:
        per_address = input(f"{green_bullet} PERMANENT ADDRESS : ").upper().strip()
        if (" " in per_address or
            "-" in per_address or
            "/" in per_address or
            "|" in per_address or
            "," in per_address or
            per_address.isalnum()
            ):
            break
        else:
            print(f"{red_bullet} ENTER VALID ADDRESS! ONLY SYMBOLS(-/,|) ARE ALLOWED")
            continue

    while True:
          cur_address = input(f"{green_bullet} CURRENT ADDRESS : ").upper().strip()
          if (" " in per_address or
              "-" in per_address or
              "/" in per_address or
              "|" in per_address or
              "," in per_address or
              cur_address.isalnum()
              ):
              break
          else:
            print(f"{red_bullet} ENTER VALID ADDRESS! ONLY SYMBOLS(-/,|) ARE ALLOWED")
            continue
    
    ac_no = random.randint(10000000,99999999)
    date_of_create = date.today()
    fullname = firstname+" "+secondname

    while True:
        try:
            balance = float(input(f"{green_bullet} SUBMIT MONEY TO OPEN ACCOUNT (MININUM ₹500) : "))
            if balance>=500:
                another_ac = (input(f"{green_bullet} ENTER AC/NO : "))
                atm_project.withdrawl_money(another_ac)
                break
        except ValueError:
            print("INVALID AMOUNT! ENTER AGAIN")
            continue

    query = "INSERT INTO customers(ac_no,cst_first_name,cst_second_name,full_name,mobile_num,current_address,permanent_addresss,current_balance,date_of_create) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (ac_no,firstname,secondname,fullname,mobile,cur_address,per_address,balance,date_of_create)
    cursor.execute(query,values)
    con.commit()
    print(f"{info_bullet} ACCOUNT CREATED SUCCESSFULLY")
    print("-"*50)

    #AUTHENTICATION SMALL SYSTEM TO GIVE A REAL TOUCH TO PROJECT
    print(f"{blue_bullet} COLLECT YOUR BANK DETAILS VIA OTP")
    otp = random.randint(1000,9999)
    while True:
        request_otp = input(f"{green_bullet} REQUEST OTP (R) : ").upper()
        if request_otp=='R':
            print(f"{info_bullet} YOUR ONE TIME PASSWORD FOR ACCOUNT DETAILS IS : {otp} DO NOT SHARE IT WITH ANY ONE")
            otp_authe = int(input(f"{green_bullet} ENTER OTP : "))
            if otp_authe==otp:
                cursor.execute("SELECT * from customers where ac_no = %s",(ac_no,))
                user_details = cursor.fetchone()
                cursor.execute("SELECT * from bank_info")
                bank_details = cursor.fetchone()
                print("="*50)
                print(f"BANK                : {bank_details[0]}")
                print(f"BRANCH             : {bank_details[1]}")
                print(f"BRANCH CODE         : {bank_details[2]}")
                print(f"EMAIL               : {bank_details[5]}")
                print(f"IFSC                : {bank_details[3]}")
                print("_"*50)
                print(f"NAME                : {user_details[3]}")
                print(f"AC/NO               : {user_details[0]}")
                print(f"MOBILE NO.          : {user_details[4]}")
                print(f"PERMANENT ADDRESS   : {user_details[6]}")
                print(f"CURRENT ADDRESS     : {user_details[5]}")
                print(f"A/C OPENING DATE    : {user_details[8]}")
                print("="*50)
                print(f"{info_bullet} PASSBOOK, CHEQUE-BOOK, DEBIT CARD ETC. FROM MAIN BRANCH USING ABOVE DETAILS")
                break
            else:
                print(f"{red_bullet} INVALID OTP")
                continue
           
        else:
            ReferenceNum = random.randint(1000,9999)
            print("-"*80)
            print(f"{info_bullet} COLLECT BANK DETAILS AND PASSBOOK FROM MAIN BRANCH USING REFFERENCE ID : {ReferenceNum}")
            cursor.execute("UPDATE customers SET refer_id = %s where ac_no = %s",(ReferenceNum,ac_no))
            con.commit()
            break

def create_new_account():
    print(f"{blue_bullet} TO CREATE NEW ACCOUNT TELL FIRST YOU HAVE")
    print("-"*50)
    print("1 | ONLINE TRANSACTION WITH ANY OTHER ACCOUNT")
    print("2 | NO ONLINE TRANSACTION\n")
    while True:
        try:
            choice = int(input(f"{green_bullet} ENTER ONE OF ABOVE : "))
            print("-"*50)
            if choice==1:
                create_new_account_at_bank()
                break
            else:
                print(f"{info_bullet} PLEASE VISIT OUR BANK BRANCH TO OPEN NEW ACCOUNT")
                print("-"*50)
                break
        except ValueError:
            print(f'{red_bullet} ENTER A VALID CHOICE')
            continue
    
#TO WITHDRAWL AMOUNT===================================================================
def withdrawl_money():
    pass

#TO DEPOSIT AMOUNT=====================================================================
def deposit_money():
    pass

#TO CHECK ACCOUNT BALANCE AMOUNT=======================================================
def chk_account_blc():
    pass

#TO CHECK ACCOUNT INFORMATION AMOUNT===================================================
def chk_account_info():
    pass

#TO CHANGE PIN OF ACCOUNT==============================================================
def change_pin():
    pass

#TO REMOVE ACCOUNT FROM BANK==========================================================
def close_account():
    pass

#LOAN DETAILS TAKEN FROM BANK=========================================================
def loan_details():
    pass