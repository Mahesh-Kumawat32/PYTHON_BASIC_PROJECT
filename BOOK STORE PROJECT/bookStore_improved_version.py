#================================================= BOOK STORE ======================================================
#REQUIRMENTS OF PROJECT:
    #SEARCH FOR BOOK USING first_book_name GIVEN BY USER/CUSTOMER
    #IF BOOK IS AVAILBLE:
        #PRINT ALL DETAILS RELATED TO THAT BOOK LIKE : AUTHOR, first_book_name, PRICE, ALSO SHOW IN WHICH SECTION OF LIBRAY BOOK IS STORED
        #ASK USER THAT THEY WANT TO BUY BOOK OR TAKE ON RENT
        #IF BUY THEN:
            #ASK FOR SOME ESSENTIAL DETAILS LIKE: NUBMBER OF BOOK WANT TO BUY, NAME, ADDRESS, MOBILE NUMBER
            #SALE THE BOOK GIVE A SLIP TO CUSTOMER WHICH MENTION (AT TOP STORE NAME, CUSTOMER NAME,ADDRESS, MOBILE NUMBER, BOOK first_book_name, NUMBER OF BOOKS ,PRICE OF EACH BOOK, TOTAL PRICE, PRINT A GREETING MSG)
        #IF RENT THEN:
            #ASK FOR SOME ESSENTIAL DETAILS LIKE: NUBMBER OF BOOK WANT TO BUY, NAME, ADDRESS, MOBILE NUMBER
            #RENT BOOK GIVE A SLIP TO CUSTOMER WHICH MENTION (AT TOP STORE NAME, CUSTOMER NAME, ADDRESS, MOBILE NUMBER, BOOK TILTE, NUMBER OF BOOKS(IF), RENT CHARGE ACCORDING TO TIME, RENT TO EACH BOOK(IF) , TOTAL RENT, RETURNING DATE, A WARNING MSG IF NOT RETURN ON THE RETURNING DATE THEN CHARGE/EXTRA DAY, PRINT A GREETING MSG)
    #IF NOT AVAILABLE THEN:
        #PRINT BOOK IS NOT FOUND

from datetime import date, timedelta
#THIS SECTION STORES DATA OF BOOKS ***********************************************************************************************
books = {
    "THE PSYCHOLOGY OF MONEY": {"AUTHOR": "MORGAN HOUSEL", "PRICE": 399, "AVAILABLE": 12},
    "ATOMIC HABITS": {"AUTHOR": "JAMES CLEAR", "PRICE": 499, "AVAILABLE": 15},
    "RICH DAD POOR DAD": {"AUTHOR": "ROBERT KIYOSAKI", "PRICE": 350, "AVAILABLE": 18},
    "WINGS OF FIRE": {"AUTHOR": "A.P.J. ABDUL KALAM", "PRICE": 299, "AVAILABLE": 10},
    "THE ALCHEMIST": {"AUTHOR": "PAULO COELHO", "PRICE": 320, "AVAILABLE": 14},
    "THINK AND GROW RICH": {"AUTHOR": "NAPOLEON HILL", "PRICE": 450, "AVAILABLE": 20},
    "IKIGAI": {"AUTHOR": "HECTOR GARCIA", "PRICE": 420, "AVAILABLE": 16},
    "DEEP WORK": {"AUTHOR": "CAL NEWPORT", "PRICE": 520, "AVAILABLE": 11},
    "THE POWER OF NOW": {"AUTHOR": "ECKHART TOLLE", "PRICE": 410, "AVAILABLE": 13},
    "THE 5 AM CLUB": {"AUTHOR": "ROBIN SHARMA", "PRICE": 480, "AVAILABLE": 9},
    "CAN'T HURT ME": {"AUTHOR": "DAVID GOGGINS", "PRICE": 599, "AVAILABLE": 8},
    "THE SUBTLE ART OF NOT GIVING A F*CK": {"AUTHOR": "MARK MANSON", "PRICE": 399, "AVAILABLE": 17},
    "ZERO TO ONE": {"AUTHOR": "PETER THIEL", "PRICE": 499, "AVAILABLE": 10},
    "START WITH WHY": {"AUTHOR": "SIMON SINEK", "PRICE": 450, "AVAILABLE": 12},
    "HOOKED": {"AUTHOR": "NIR EYAL", "PRICE": 530, "AVAILABLE": 9},
    "THE LEAN STARTUP": {"AUTHOR": "ERIC RIES", "PRICE": 550, "AVAILABLE": 14},
    "GOOD TO GREAT": {"AUTHOR": "JIM COLLINS", "PRICE": 600, "AVAILABLE": 7},
    "THE INTELLIGENT INVESTOR": {"AUTHOR": "BENJAMIN GRAHAM", "PRICE": 699, "AVAILABLE": 6},
    "COMMON STOCKS AND UNCOMMON PROFITS": {"AUTHOR": "PHILIP FISHER", "PRICE": 650, "AVAILABLE": 5},
    "ONE UP ON WALL STREET": {"AUTHOR": "PETER LYNCH", "PRICE": 580, "AVAILABLE": 9},
    "THE WARREN BUFFETT WAY": {"AUTHOR": "ROBERT HAGSTROM", "PRICE": 620, "AVAILABLE": 8},
    "THE MILLIONAIRE NEXT DOOR": {"AUTHOR": "THOMAS STANLEY", "PRICE": 470, "AVAILABLE": 12},
    "YOUR MONEY OR YOUR LIFE": {"AUTHOR": "VICKI ROBIN", "PRICE": 430, "AVAILABLE": 10},
    "THE TOTAL MONEY MAKEOVER": {"AUTHOR": "DAVE RAMSEY", "PRICE": 510, "AVAILABLE": 11},
    "THE SIMPLE PATH TO WEALTH": {"AUTHOR": "J.L. COLLINS", "PRICE": 540, "AVAILABLE": 9},
    "THE ONE THING": {"AUTHOR": "GARY KELLER", "PRICE": 399, "AVAILABLE": 13},
    "ESSENTIALISM": {"AUTHOR": "GREG MCKEOWN", "PRICE": 460, "AVAILABLE": 10},
    "EAT THAT FROG": {"AUTHOR": "BRIAN TRACY", "PRICE": 370, "AVAILABLE": 18},
    "THE MAGIC OF THINKING BIG": {"AUTHOR": "DAVID SCHWARTZ", "PRICE": 440, "AVAILABLE": 12},
    "THE 7 HABITS OF HIGHLY EFFECTIVE PEOPLE": {"AUTHOR": "STEPHEN COVEY", "PRICE": 599, "AVAILABLE": 14},
    "HOW TO WIN FRIENDS AND INFLUENCE PEOPLE": {"AUTHOR": "DALE CARNEGIE", "PRICE": 450, "AVAILABLE": 16},
    "THE POWER OF HABIT": {"AUTHOR": "CHARLES DUHIGG", "PRICE": 510, "AVAILABLE": 10},
    "OUTLIERS": {"AUTHOR": "MALCOLM GLADWELL", "PRICE": 470, "AVAILABLE": 9},
    "BLINK": {"AUTHOR": "MALCOLM GLADWELL", "PRICE": 430, "AVAILABLE": 8},
    "TIPPING POINT": {"AUTHOR": "MALCOLM GLADWELL", "PRICE": 450, "AVAILABLE": 11},
    "GRIT": {"AUTHOR": "ANGELA DUCKWORTH", "PRICE": 520, "AVAILABLE": 10},
    "MINDSET": {"AUTHOR": "CAROL DWECK", "PRICE": 480, "AVAILABLE": 15},
    "QUIET": {"AUTHOR": "SUSAN CAIN", "PRICE": 470, "AVAILABLE": 8},
    "FLOW": {"AUTHOR": "MIHALY CSIKSZENTMIHALYI", "PRICE": 590, "AVAILABLE": 6},
    "DRIVE": {"AUTHOR": "DANIEL PINK", "PRICE": 510, "AVAILABLE": 7},
    "THE FOUR AGREEMENTS": {"AUTHOR": "DON MIGUEL RUIZ", "PRICE": 350, "AVAILABLE": 19},
    "WHO MOVED MY CHEESE": {"AUTHOR": "SPENCER JOHNSON", "PRICE": 280, "AVAILABLE": 20},
    "THE MONK WHO SOLD HIS FERRARI": {"AUTHOR": "ROBIN SHARMA", "PRICE": 390, "AVAILABLE": 12},
    "THE SECRET": {"AUTHOR": "RHONDA BYRNE", "PRICE": 420, "AVAILABLE": 11},
    "THE POWER": {"AUTHOR": "RHONDA BYRNE", "PRICE": 430, "AVAILABLE": 10},
    "THE MAGIC": {"AUTHOR": "RHONDA BYRNE", "PRICE": 410, "AVAILABLE": 9},
    "SAPIENS": {"AUTHOR": "YUVAL NOAH HARARI", "PRICE": 699, "AVAILABLE": 10},
    "HOMO DEUS": {"AUTHOR": "YUVAL NOAH HARARI", "PRICE": 720, "AVAILABLE": 8},
    "21 LESSONS FOR THE 21ST CENTURY": {"AUTHOR": "YUVAL NOAH HARARI", "PRICE": 680, "AVAILABLE": 9},
    "FACTFULNESS": {"AUTHOR": "HANS ROSLING", "PRICE": 550, "AVAILABLE": 11},
    "THE CODE BREAKER": {"AUTHOR": "WALTER ISAACSON", "PRICE": 750, "AVAILABLE": 5},
    "STEVE JOBS": {"AUTHOR": "WALTER ISAACSON", "PRICE": 799, "AVAILABLE": 6},
    "ELON MUSK": {"AUTHOR": "WALTER ISAACSON", "PRICE": 850, "AVAILABLE": 7},
    "BECOMING": {"AUTHOR": "MICHELLE OBAMA", "PRICE": 620, "AVAILABLE": 8},
    "LONG WALK TO FREEDOM": {"AUTHOR": "NELSON MANDELA", "PRICE": 580, "AVAILABLE": 6},
    "THE DIARY OF A YOUNG GIRL": {"AUTHOR": "ANNE FRANK", "PRICE": 340, "AVAILABLE": 15},
    "TO KILL A MOCKINGBIRD": {"AUTHOR": "HARPER LEE", "PRICE": 420, "AVAILABLE": 12},
    "1984": {"AUTHOR": "GEORGE ORWELL", "PRICE": 390, "AVAILABLE": 14},
    "ANIMAL FARM": {"AUTHOR": "GEORGE ORWELL", "PRICE": 250, "AVAILABLE": 18},
    "PRIDE AND PREJUDICE": {"AUTHOR": "JANE AUSTEN", "PRICE": 370, "AVAILABLE": 11},
    "JANE EYRE": {"AUTHOR": "CHARLOTTE BRONTE", "PRICE": 360, "AVAILABLE": 10},
    "THE GREAT GATSBY": {"AUTHOR": "F. SCOTT FITZGERALD", "PRICE": 330, "AVAILABLE": 13},
    "MOBY DICK": {"AUTHOR": "HERMAN MELVILLE", "PRICE": 500, "AVAILABLE": 5},
    "WAR AND PEACE": {"AUTHOR": "LEO TOLSTOY", "PRICE": 950, "AVAILABLE": 4},
    "CRIME AND PUNISHMENT": {"AUTHOR": "FYODOR DOSTOEVSKY", "PRICE": 720, "AVAILABLE": 5},
    "THE BROTHERS KARAMAZOV": {"AUTHOR": "FYODOR DOSTOEVSKY", "PRICE": 780, "AVAILABLE": 4},
    "THE HOBBIT": {"AUTHOR": "J.R.R. TOLKIEN", "PRICE": 520, "AVAILABLE": 10},
    "THE LORD OF THE RINGS": {"AUTHOR": "J.R.R. TOLKIEN", "PRICE": 1200, "AVAILABLE": 6},
    "HARRY POTTER AND THE SORCERER'S STONE": {"AUTHOR": "J.K. ROWLING", "PRICE": 550, "AVAILABLE": 15},
    "HARRY POTTER AND THE CHAMBER OF SECRETS": {"AUTHOR": "J.K. ROWLING", "PRICE": 560, "AVAILABLE": 14},
    "HARRY POTTER AND THE PRISONER OF AZKABAN": {"AUTHOR": "J.K. ROWLING", "PRICE": 570, "AVAILABLE": 13},
    "HARRY POTTER AND THE GOBLET OF FIRE": {"AUTHOR": "J.K. ROWLING", "PRICE": 620, "AVAILABLE": 12},
    "HARRY POTTER AND THE ORDER OF THE PHOENIX": {"AUTHOR": "J.K. ROWLING", "PRICE": 680, "AVAILABLE": 11},
    "HARRY POTTER AND THE HALF-BLOOD PRINCE": {"AUTHOR": "J.K. ROWLING", "PRICE": 650, "AVAILABLE": 10},
    "HARRY POTTER AND THE DEATHLY HALLOWS": {"AUTHOR": "J.K. ROWLING", "PRICE": 700, "AVAILABLE": 9},
    "THE DA VINCI CODE": {"AUTHOR": "DAN BROWN", "PRICE": 450, "AVAILABLE": 12},
    "ANGELS AND DEMONS": {"AUTHOR": "DAN BROWN", "PRICE": 430, "AVAILABLE": 11},
    "DIGITAL FORTRESS": {"AUTHOR": "DAN BROWN", "PRICE": 390, "AVAILABLE": 10},
    "DECEPTION POINT": {"AUTHOR": "DAN BROWN", "PRICE": 410, "AVAILABLE": 9},
    "THE LOST SYMBOL": {"AUTHOR": "DAN BROWN", "PRICE": 480, "AVAILABLE": 8},
    "ORIGIN": {"AUTHOR": "DAN BROWN", "PRICE": 550, "AVAILABLE": 7},
    "INFERNO": {"AUTHOR": "DAN BROWN", "PRICE": 520, "AVAILABLE": 8},
    "SHERLOCK HOLMES": {"AUTHOR": "ARTHUR CONAN DOYLE", "PRICE": 490, "AVAILABLE": 16},
    "THE ADVENTURES OF SHERLOCK HOLMES": {"AUTHOR": "ARTHUR CONAN DOYLE", "PRICE": 420, "AVAILABLE": 15},
    "THE HOUND OF THE BASKERVILLES": {"AUTHOR": "ARTHUR CONAN DOYLE", "PRICE": 380, "AVAILABLE": 12},
    "THE LITTLE PRINCE": {"AUTHOR": "ANTOINE DE SAINT-EXUPERY", "PRICE": 320, "AVAILABLE": 17},
    "THE KITE RUNNER": {"AUTHOR": "KHALED HOSSEINI", "PRICE": 460, "AVAILABLE": 10},
    "A THOUSAND SPLENDID SUNS": {"AUTHOR": "KHALED HOSSEINI", "PRICE": 470, "AVAILABLE": 9},
    "THE BOOK THIEF": {"AUTHOR": "MARKUS ZUSAK", "PRICE": 510, "AVAILABLE": 11},
    "LIFE OF PI": {"AUTHOR": "YANN MARTEL", "PRICE": 430, "AVAILABLE": 8},
    "THE FAULT IN OUR STARS": {"AUTHOR": "JOHN GREEN", "PRICE": 390, "AVAILABLE": 14},
    "PAPER TOWNS": {"AUTHOR": "JOHN GREEN", "PRICE": 360, "AVAILABLE": 9},
    "LOOKING FOR ALASKA": {"AUTHOR": "JOHN GREEN", "PRICE": 370, "AVAILABLE": 8},
    "THE GIVER": {"AUTHOR": "LOIS LOWRY", "PRICE": 340, "AVAILABLE": 12},
    "THE MARTIAN": {"AUTHOR": "ANDY WEIR", "PRICE": 580, "AVAILABLE": 7},
    "PROJECT HAIL MARY": {"AUTHOR": "ANDY WEIR", "PRICE": 650, "AVAILABLE": 6},
    "DUNE": {"AUTHOR": "FRANK HERBERT", "PRICE": 720, "AVAILABLE": 8},
    "READY PLAYER ONE": {"AUTHOR": "ERNEST CLINE", "PRICE": 520, "AVAILABLE": 9},
    "THE SILENT PATIENT": {"AUTHOR": "ALEX MICHAELIDES", "PRICE": 480, "AVAILABLE": 10},
    "VERITY": {"AUTHOR": "COLLEEN HOOVER", "PRICE": 450, "AVAILABLE": 12},
    "IT ENDS WITH US": {"AUTHOR": "COLLEEN HOOVER", "PRICE": 430, "AVAILABLE": 15},
    "REMINDERS OF HIM": {"AUTHOR": "COLLEEN HOOVER", "PRICE": 440, "AVAILABLE": 11}
}
#**********************************************************************************************************************************

#THE SECTION WHICH STORES DATA WHEN USER ENTER*************************************************************************************
customer_data = {}
#**********************************************************************************************************************************

#MAIN FUCNTION THAT WORKS ACCORDING TO CUSTOMER NEED*******************************************************************************
def find_book(first_book_name):
    book_rent_days_for_any_book = 30
    charge_per_day = 10
    extra_charge_per_day = 20
    if first_book_name in books:
        print(f"✔ BOOK IS AVAILBLE")
        print(f"BOOK TITLE : {first_book_name}")
        print(f"TOTAL BOOKS AVAILABLE : {books[first_book_name]['AVAILABLE']}")
        print(f"BOOK AUTHOR : {books[first_book_name]['AUTHOR']}")
        print(f"BOOK PRICE : {books[first_book_name]['PRICE']}")
        print(f"BOOK RENT/DAY : {charge_per_day}")
        print(f"BOOK ON RENT MAX DAY : {book_rent_days_for_any_book}")
        print(80*"-")
        rent_or_buy = input("BUY (PRESS) : 'B'\nRENT (PRESS) : 'R'\n:").upper()

        #IF CUSTOMER SAY TO BUY BOOK THEN THIS SECTION IS HELPFULL*****************************************************************
        if rent_or_buy=="B":
            #TAKING DATA FROM USER
            customer_name = input("CUSTOMER NAME : ")
            customer_address = input("CUSTOMER ADDRESS : ")
            customer_mb = input("CUSTOMER MOBILE NUMBER : ")
            number_books = int(input(f"NUMBER OF BOOK \'{first_book_name}\' YOU WANT TO BUY : "))
            #STORE DATA OF USER
            customer_data['NAME'] = customer_name
            customer_data['ADDRESS'] = customer_address
            customer_data['MOBILE NO'] = customer_mb
            customer_data['BOOK NAME'] = first_book_name
            customer_data[f"TOTAL BOOK"] = number_books
            customer_data[f"BOOK-PRICE"] = books[first_book_name]['PRICE']
            customer_data[f"TOTAL AMOUNT"] = ( customer_data["TOTAL BOOK"] * customer_data[f"BOOK-PRICE"])
            customer_data[f"DATE"] = date.today()
            #PRINT DATA OF USER
            print(100*"=")
            for a,b in customer_data.items():
                    print(f"{a} : {b}")
            print("\t\t\t\tTHANK YOU 😀 VISIT AGAIN 👍")
            print(100*"=")
            customer_data.clear()
        #**************************************************************************************************************************

        #IF CUSTOMER SAY TO RENT A BOOK THEN THIS SECTION IS HELPFULL**************************************************************
        elif rent_or_buy=="R":
            #TAKING DATA FROM USER
            customer_name = input("CUSTOMER NAME : ")
            customer_address = input("CUSTOMER ADDRESS : ")
            customer_mb = input("CUSTOMER MOBILE NUMBER : ")
            day_for_rent = int(input(f"FOR HOW MANY DAYS YOU WANT TO RENT \'{first_book_name}\' : "))
            if day_for_rent<=30:
                #STORES DATA OF USER
                number_books = int(input(f"NUMBER OF BOOK \'{first_book_name}\' YOU WANT TO RENT : "))
                customer_data['NAME'] = customer_name
                customer_data['ADDRESS'] = customer_address
                customer_data['MOBILE NO'] = customer_mb
                customer_data['BOOK NAME'] = first_book_name
                customer_data[f"TOTAL BOOK"] = number_books
                customer_data[f"DAYS FOR YOU RENT \'{first_book_name}\'"] = day_for_rent
                customer_data[f"CHARGE FOR {day_for_rent} DAYS"] = (customer_data[f"TOTAL BOOK"]*customer_data[f"DAYS FOR YOU RENT \'{first_book_name}\'"]*charge_per_day)
                customer_data[f"DATE OF ISSUE"] = date.today()
                customer_data[f"DATE OF RENEW"] = date.today()+timedelta(days=30)
                customer_data[f"NOTE"] = (f"IF YOU RENEW LATE THEN YOU HAVE TO PAY EXTRA CHARGE PER DAY {extra_charge_per_day}/-")
                #PRINT DATA OF USER
                print(100*"=")
                for a,b in customer_data.items():
                    print(f"{a} : {b}")
                print("\n\t\t\t\tTHANK YOU 😀 VISIT AGAIN 👍")
                print(100*"=")
                customer_data.clear()
            else:
                print(f"YOU CANNOT RENT BOOK MORE THAN 30 DAYS")
        #**************************************************************************************************************************

        #IF CUSTOMER ENTER SOMETHIGNG WRONG THEN THIS SECTION IS HELPFULL*****************************************************************
        else:
            print("YOU ENTERED SOMETHING WRONG🤨! PLEASE TRY AGAIN 😡")
        #**************************************************************************************************************************

    else:
        print(f"BOOKS \'{first_book_name}\' IS NOT FOUND")



#PROGRAM EXECUTION STARTS FROM HERE************************************************************************************************
#GREETING SECTION====================
store_name = " GYAN BOOK STORE "
print(store_name.center(100,"*"))
#====================================

#THIS SECTION ASK PEOPLE ABOUT THE NAME OR TITLE OF THE BOOK THEY NEED
while True:
    first_book_name = input("ENTER BOOK NAME YOU WANT : ").upper()
    print(102*"-")
    find_book(first_book_name)
    print(102*"-")
    permission = input("PROCEED AGAIN (YES/NO) : ").upper()
    if permission=="YES":
        continue
    else:
        print("TODAY WORK IS DONE 🙂 MEET YOU TOMMOROW 👍")
        print(102*"-")
        break
#=====================================================================
#**********************************************************************************************************************************