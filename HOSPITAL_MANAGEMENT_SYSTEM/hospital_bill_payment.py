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

#FUNCTION HELPS USER TO WITHDRAWL MONEY FROM ACCOUNT****************************************************************************
def withdrawl_money(ac_no):
       for i in range(2,10):
            if customer_data[str(i)]['AC/NO']==ac_no:
                print(80*'-')
                print(f"YOUR RECORD FOUND SUCCESSFULLY 👍")
                global amount_to_withdrawl
                amount_to_withdrawl = float(input("AMOUNT YOU WANT TO PAY : "))
                if amount_to_withdrawl<customer_data[str(i)]['PREVIOUS BALANCE']:
                    confirm_withdrawl = input("PRESS 'CP' FOR FINALA PAYMENT : ").upper()
                    if confirm_withdrawl == "CP":
                        print(f"₹{amount_to_withdrawl} PAYED SUCCESSFULLY FROM AC/NO : {customer_data[str(i)]['AC/NO']}👍")
                        print(80*'-')
                        new_balance = (customer_data[str(i)]['PREVIOUS BALANCE']-amount_to_withdrawl)
                        customer_data[str(i)]['PREVIOUS BALANCE'] = new_balance
                    else:
                        print('WITHDRAWL CANCELLED X')
                else:
                    print(f"YOU CANNOT WITHDRAWL {amount_to_withdrawl} BECAUSE YOUR PREVIOUS BALANCE IS {customer_data[str(i)]['PREVIOUS BALANCE']}")
                    print("PLEASE TRY AGAIN")
    
            else:
                continue 
#**********************************************************************************************************************************




