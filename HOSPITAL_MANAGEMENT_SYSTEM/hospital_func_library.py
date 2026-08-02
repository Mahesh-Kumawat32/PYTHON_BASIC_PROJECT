from datetime import date,timedelta
import random
from hospital_bill_payment import withdrawl_money
#FUNCTION USED FOR REGESTRATION
def regestration():
    #TAKE ESSENTIAL DETAILS FROM PATIENT
    print(40*"-")
    name = input("FULL NAME : ").upper()
    while True:
        if name.isalpha() or " " in name:
            break
        else:
            print("YOU ENTER WRONG NAME! PLEASE ENTER AGAIN")
            name = input("FULL NAME : ").upper()

    age = int(input("AGE : "))
    while True:
        if (age>0 and age<=100) or str(age).isdigit():
            break
        else:
            print("AGE IS WRONG ! PLEASE ENTER AGAIN")
            age = int(input("AGE : "))

    gender = input("GENDER (M/F) :").upper()
    while True:
        if gender=="M":
            gender = "MALE"
            break
        elif gender =="F":
            gender = "FEMALE"
            break
        else:
            print("YOU ENTER SOMETHING WRONG ! ENTER AGAIN")
            gender = input("GENDER (M/F) :").upper()


    address = input("ADDRESS : ").upper()
    while True:
        if address.isalnum() or "-" in address or "," in address or "|" in address:
            break
        else:
            print("YOU ENTER WRONG ADDRESS! PLEASE ENTER AGAIN")
            address = input("ADDRESS : ").upper()
           
    mb = int(input("MOBILE NO. : "))
    while True:
        if len(str(mb))==10 and str(mb).isdigit():
            break
        else:
            print("YOU ENTER WRONG MOBILE NO! PLEASE ENTER AGAIN")
            mb = int(input("MOBILE NO. : "))

    aadhar_no = int(input("AADHAR NO. : "))
    while True:
        if len(str(aadhar_no))==12 and str(aadhar_no).isdigit():
            break
        else:
            print("YOU ENTER WRONG AADHAR NO! PLEASE ENTER AGAIN")
            aadhar_no = int(input("AADHAR NO. : "))

    aadhar_address = input("ADDRESS AS PER AADHAR : ").upper()
    while True:
        if aadhar_address.isalnum() or "-" in aadhar_address or "," in aadhar_address or "|" in aadhar_address:
            break
        else:
            print("YOU ENTER WRONG AADHAR ADDRESS! PLEASE ENTER AGAIN")
            aadhar_address = input("ADDRESS AS PER AADHAR : ").upper()
    special_case = input("MEDICAL ISSUE : ").upper()
    while True:
        if special_case!=" ":
            break
        else:
            print("MENTIONING MEDICAL ISSUE IS MANDATORY")
            special_case = input("MEDICAL ISSUE : ")
    print(60*"-")
    print("\t\t\tDIESESE")
    print(60*"-")
    with open("hospital_text-data/diesese.txt") as f4:
        data4 = f4.read()
        print(data4)
    problem = input("PLEAE ENTER SPECIALICATION OF YOUR DIESESE : ").upper()
    while True:
        if problem!="":
            break
        else:
            print("PLEASE ENTER SPECIALIZATION ISSUE IS MANDATORY")
            problem = input("SPECIALIZATION DIESESE : ")
    match problem:
        case "GENERAL PHYSICIAN":
            doctor_name = "DR. RAJESH SHARMA"

        case "PEDIATRICIAN":
            doctor_name = "DR. PRIYA PATEL"

        case "CARDIOLOGIST":
            doctor_name = "DR. AMIT MEHTA"

        case "GYNECOLOGIST":
            doctor_name = "DR. NEHA DESAI"

        case "ORTHOPEDIC SURGEON":
            doctor_name = "DR. KUNAL SHAH"

        case "NEUROLOGIST":
            doctor_name = "DR. ROHAN JOSHI"

        case "DERMATOLOGIST":
            doctor_name = "DR. ANJALI KAPOOR"

        case "ENT SPECIALIST":
            doctor_name = "DR. VIVEK SINGH"

        case "OPHTHALMOLOGIST":
            doctor_name = "DR. POOJA VERMA"

        case "PULMONOLOGIST":
            doctor_name = "DR. SANJAY GUPTA"

        case "GASTROENTEROLOGIST":
            doctor_name = "DR. NITIN AGARWAL"

        case "ENDOCRINOLOGIST":
            doctor_name = "DR. SNEHA TRIVEDI"

        case "UROLOGIST":
            doctor_name = "DR. HARSH PATEL"

        case "PSYCHIATRIST":
            doctor_name = "DR. KAVITA IYER"

        case "DENTIST":
            doctor_name = "DR. ARJUN RAO"

        case _:
            doctor_name = "DOCTOR NOT AVAILABLE"
    #STORE DETAILS TO FILE
    with open("hospital_text-data/patient_data.txt","a") as f1:
        f1.write("\n")
        f1.write(f"PATIENT NAME         : {name}\n")
        f1.write(f"AGE                  : {age}\n")
        f1.write(f"GENDER               : {gender}\n")
        f1.write(f"ADDRESS              : {address}\n")
        f1.write(f"MOBILE NO.           : {mb}\n")
        f1.write(f"AADHAR NO.           : {aadhar_no}\n")
        f1.write(f"AADHAR ADDRESS       : {aadhar_address}\n")
        f1.write(f"MEDICAL ISSUE        : {special_case}\n")
        f1.write(f"SPECIALIZATION       : {problem}\n")
        f1.write(f"DATE OF REGESTRATION : {date.today()}\n")
        f1.write(f"DATE OF APPOINTMENT  : {date.today()+timedelta(days = 2)}\n")
        f1.write(f"DOCTOR NAME          : {doctor_name}\n")
        f1.write(f"ROOM NO              : {random.randint(1,301)}\n")
        f1.write(40*"=")
    print("\n")
    print("YOUR DATA STROED SUCCESSFULLY ✔")

#FUNCTION USED TO GET APPOINTMENT DETAILS
def appointment():
    print(40*"-")
    name = input("PATIENT NAME : ").upper()
    print(40*"=")
    found = False
    with open("hospital_text-data/patient_data.txt","r") as f2:
        for line in f2:
            if f"PATIENT NAME         : {name}" == line.strip():
                found = True
            if found:
                if (line.startswith("PATIENT NAME")
                    or line.startswith("DATE OF REGESTRATION")
                    or line.startswith("DATE OF APPOINTMENT")
                    or line.startswith('DOCTOR NAME')
                    or line.startswith('ROOM NO')
                    ):
                        print(line,end = "")
                if line.startswith("="):
                    break
    
#FUNCTION USED TO SEARCH PATIENT
def search_patient():
    print(40*"-")
    name = input("PATIENT NAME : ").upper()
    print(40*"=")
    found = False
    with open("hospital_text-data/patient_data.txt","r") as f2:
        for line in f2:
            if f"PATIENT NAME         : {name}" == line.strip():
                found = True
            if found:
                print(line,end = "")
                if line.startswith("="):
                        break

#FUNCTION USED TO CREATE BILL
def create_bill():
    print(100*"-")
    name = input("FULL NAME : ")
    way_of_payment = int(input("PAYMENT WAY\n\t1.UPI\n\t2.Paytm\n\t3.UPI-BHIM\n\t4.PhonePay\n\t5.PayPal\n\t6.Cash\n>SELECT PAYMENT WAY (ENTER SERIES NUMBER) : "))
    match way_of_payment:
        case 1:
            ac_no = input("ENTER YOUR AC/NO : ")
            withdrawl_money(ac_no)
            payment_way = "UPI"
        case 2:
            ac_no = input("ENTER YOUR AC/NO : ")
            withdrawl_money(ac_no)
            payment_way = "Paytm"
        case 3:
            ac_no = input("ENTER YOUR AC/NO : ")
            withdrawl_money(ac_no)
            payment_way = "UPI-BHIM"
        case 4:
            ac_no = input("ENTER YOUR AC/NO : ")
            withdrawl_money(ac_no)
            payment_way = "PhonePay"
        case 5:
            ac_no = input("ENTER YOUR AC/NO : ")
            withdrawl_money(ac_no)
            payment_way = "PayPal"
        case 6:
            payment_way = "Cash"
    print(100*"=")
    with open("hospital_text-data/hospital_details.txt","r") as f3:
        data3 = f3.read()
        print(data3)
    found = False 
    print(100*"-")
    with open("hospital_text-data/patient_data.txt","r") as f4:
        for line in f4:
            if f"PATIENT NAME         : {name}" == line.strip():
                found = True
            if found:
                if (line.startswith("PATIENT NAME")
                    or line.startswith("DATE OF REGESTRATION")
                    or line.startswith("DATE OF APPOINTMENT")
                    or line.startswith("MEDICAL ISSUE")
                    or line.startswith("SPECIALIZATION")
                    or line.startswith("DOCTOR NAME")
                ):
                    print(line,end="")
                if line.startswith("="):
                    break
    print(100*"-")
    print(f"TREATMENT CHARGE    : ₹50")
    print(f"MEDICINE CHARGE     : ₹100")
    print(f"TOTAL BILL          : ₹150")
    print(f"PAYMENT WAY         : {payment_way}")
    print(100*"=")
   

    search = False
    with open("hospital_text-data/patient_data.txt", "r") as f4, \
        open("hospital_text-data/bills_data.txt", "a", encoding="utf-8") as f6:

        f6.write(data3 + "\n")      # Hospital details
        f6.write(50*"="+"\n")
        for line in f4:

            if f"PATIENT NAME         : {name.upper()}" == line.strip():
                search= True

            if search:
                f6.write(line)      # Seedha bill file me likh do

            if search and line.startswith("="):
                break
        print(50*"=")

        f6.write("\nTREATMENT CHARGE    : ₹50\n")
        f6.write("MEDICINE CHARGE     : ₹100\n")
        f6.write("TOTAL BILL          : ₹150\n")
        f6.write(f"PAYMENT WAY         : {payment_way}\n")
        f6.write("-" * 60 + "\n")
                
#FUNCTION USED TO UPDATE DETAILS
def update_patient_details():
    pass

#FUNCTION USED TO DELETE PATIENT
def delete_patient():
    print(80 * "-")
    name = input("ENTER PATIENT NAME TO DELETE : ").upper()

    # Read all lines
    with open("hospital_text-data/patient_data.txt", "r") as f:
        lines = f.readlines()

    new_data = []
    delete_record = False
    found = False

    for line in lines:

        # Patient found
        if line.strip() == f"PATIENT NAME         : {name}":
            delete_record = True
            found = True
            continue

        # Skip all lines of that patient
        if delete_record:
            if line.startswith("="):
                delete_record = False
            continue

        # Keep remaining data
        new_data.append(line)

    if found:
        confirm = input("PRESS 'D' TO CONFIRM DELETE : ").upper()

        if confirm == "D":
            with open("hospital_text-data/patient_data.txt", "w") as f:
                f.writelines(new_data)

            print("\nPATIENT RECORD DELETED SUCCESSFULLY ✔")
        else:
            print("\nDELETE CANCELLED.")
    else:
        print("\nPATIENT RECORD NOT FOUND.")

            