import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="1340",database="bookstore")
cur=con.cursor()
def admin():    #SANJIPAN
    m=input("PASSWORD:")
    if m=="1234":
        def listofbooks():
            cur.execute("""select * from booklist;""")
            r=cur.fetchall()
            print("+--------------------------------------------------------------------------------------------------------------+")
            print("|SLNo. |BOOKNAME                      |AUTHOR's NAME                 |GENRE                         |BOOKID|QTY|")
            print("+--------------------------------------------------------------------------------------------------------------+")
            s="|{:^6}|{:^30}|{:^30}|{:^30}|{:^6}|{:^3}|"
            l=[]
            for i in r:
                for j in i:
                    l.append(j)
                print(s.format(l[0],l[1],l[2],l[3],l[4],l[5]))
                l=[]
                print("+--------------------------------------------------------------------------------------------------------------+")
        def listofbookborrowers():
            cur.execute("""select * from borrowers;""")
            r=cur.fetchall()
            print("+----------------------------------------------------------------------------------------------------------------------------------------------------+")
            print("|slno.|NAME                          |PHONE NO. |ADDRESS                       |BOOKNAME                      |BOOK ID.|DATE OF BORROW|DATE OF RETURN|")
            print("+----------------------------------------------------------------------------------------------------------------------------------------------------+")
            s="|{:^5}|{:^30}|{:^10}|{:^30}|{:^30}|{:^8}|{:^14}|{:^14}|"
            l=[]
            for i in r:
                for j in i:
                    l.append(str(j))
                print(s.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7]))
                l=[]
                print("+----------------------------------------------------------------------------------------------------------------------------------------------------+")
        def addbook():  #AVANTEEKA
            while True:
                sl=int(input("ENTER THE SL NO.:"))
                b=input("ENTER THE BOOKNAME:")
                a=input("ENTER THE AUTHOR:")
                g=input("ENTER THE GENRE:")
                i=input("ENTER THE BOOKID:")
                q=input("ENTER THE QUANTITY:")
                s="""insert into booklist values(%s,%s,%s,%s,%s,%s);"""
                l=[sl,b,a,g,i,q]
                cur.execute(s,l)
                n=input("want to save?[y/n]")
                if n=="y" or n=="Y":
                    con.commit()
                k=input("want to enter more?[y/n]")
                if k=="N" or k=="n":
                    break            
        while True:
            print("+-----------------------------+")
            print("|          WELCOME            |")
            print("|         ADMIN MENU          |")
            print("|1.LIST OF THE BOOKS          |")
            print("|2.LIST OF BOOK BORROWERS     |")
            print("|3.ADD BOOKS TO THE BOOKLIST  |")
            print("|4.EXIT TO CHOICES            |")
            print("+-----------------------------+")
            n=int(input("ENTER YOUR CHOICE:"))
            if n==4:
                break
            elif n==1:
                listofbooks()
            elif n==2:
                listofbookborrowers()
            elif n==3:
                addbook()
            else:
                print("INVALID CHOICE")
    else:
        print("INVALID PASSWORD")
def bookborrower():
    while True:
        print("+--------------------------------------------+")
        print("|                 WELCOME                    |")
        print("|           BOOK BORROWER's CHOICE           |")
        print("|1.LIST OF THE BOOKS CAN BE BORROWED         |")
        print("|2.EXIT TO CHOICES                           |")
        print("+--------------------------------------------+")
        n=int(input("ENTER YOUR CHOICE:"))
        def bookshowcase():
            def b1():     #AKSHETA
                cur.execute("""select * from booklist;""")
                m=cur.fetchall()
                print("+--------------------------------------------------------------------------------------------------------------+")
                print("|SLNo. |BOOKNAME                      |AUTHOR's NAME                 |GENRE                         |BOOKID|QTY|")
                print("+--------------------------------------------------------------------------------------------------------------+")
                s="|{:^6}|{:^30}|{:^30}|{:^30}|{:^6}|{:^3}|"
                l=[]
                for i in m:
                    for j in i:
                        l.append(j)
                    print(s.format(l[0],l[1],l[2],l[3],l[4],l[5]))
                    l=[]
                    print("+--------------------------------------------------------------------------------------------------------------+")
                print()
                print("########################################################")
                print("# THE BOOKS WITH QUANTITY 0 ARE NOT AVAILABLE FOR NOW  #")
                print("# CHOOSE BY BOOKID                                     #")
                print("# A BORROWER CAN BORROW ONE BOOK AT A TIME             #")
                print("########################################################")
                list=[]
                while True:
                    book=input("ENTER BOOKID TO BORROW:")
                    list.append(book)
                    n=input("WANT TO CHANGE THE BOOK?[Y/N]:")
                    if n=="n" or n=="N":
                        break
                def bookfinal(list):
                    def updateborrowerlist(h):
                        qry="""select slno from borrowers;"""
                        cur.execute(qry)
                        sl=cur.fetchall()
                        c=0
                        for i in sl:
                            for j in i:
                                c=j
                        slno=c+1
                        name=input("ENTER YOUR NAME:")
                        phone=int(input("ENTER PHONE NO(10 DIGITS):"))
                        addr=input("ENTER YOUR ADDRESS(30 LETTERS LIMIT):")
                        bookn,bookid=h[1],h[4]
                        date=input("ENTER BORROWING DATE (YYYY-MM-DD):")
                        d=date.split("-")
                        w=""
                        for jj in d:
                            if int(d[1])>1 and int(d[1])<12:
                                if int(d[2])+15<30:
                                    w=str(d[0]+"-"+d[1]+"-"+str((int(d[2])+15)))
                                else:
                                    w=str(d[0]+"-"+str(int(d[1])+1)+"-"+str((int(d[2])+15)-30))
                        qry2="""insert into borrowers values(%s,%s,%s,%s,%s,%s,%s,%s);"""
                        l3=[slno,name,phone,addr,bookn,bookid,date,w]
                        cur.execute(qry2,l3)
                        con.commit()
                        print("|_______________________|")
                        print("+-----------------------------------------------------------------+")
                        print("|                 BOOK STORE                                      |")
                        print("|                                                                 |")
                        print("|NAME:{:^30}   DATE:{:^10}            |".format(name,date))
                        print("|BOOKID:{:^5}                                                     |".format(bookid))
                        print("|BOOKBORROWED:{:^30}                      |".format(bookn))
                        print("|                                                                 |")
                        print("|DATE OF RETURN:{:^10}                                        |".format(w))
                        print("|*AFTER COMPLITION OF RETURNING DATE A FINE OF Rs.15 WILL BE      |")
                        print("|CHARGED PER DAY.                                                 |")
                        print("|*INCASE OF BOOK LOST OR DAMAGE THE FULL PRICE OF BOOK WILL BE    |")
                        print("|CHARGED AS FINE                                                  |")
                        print("+-----------------------------------------------------------------+")
                        print("|_______________________|")
                    while True:    
                        qry="""select * from booklist where bookid=%s;"""
                        print("THE BOOK YOU CHOOSE:")
                        h=[]
                        for l in list:
                            cur.execute(qry,[str(l)])
                            k=cur.fetchall()
                            for j in k:
                                for o in j:
                                    h.append(o)
                                    print(o,end=" | ")
                                print()
                        ll=input("DO YOU WANT TO CONFIRM[y/n]")
                        if ll=="n" or ll=="N":
                            list=[]
                            break
                        elif ll=="Y" or ll=="y":
                            updateborrowerlist(h)
                            break
                        else:
                            print("INVALID CHOICE")
                bookfinal(list)
            def b2():      #KSHITIJ
                g=input("ENTER GENRE:")
                cur.execute("""select * from booklist where genre like "{}%";""".format(g))
                m=cur.fetchall()
                print("+--------------------------------------------------------------------------------------------------------------+")
                print("|SLNo. |BOOKNAME                      |AUTHOR's NAME                 |GENRE                         |BOOKID|QTY|")
                print("+--------------------------------------------------------------------------------------------------------------+")
                s="|{:^6}|{:^30}|{:^30}|{:^30}|{:^6}|{:^3}|"
                l=[]
                for i in m:
                    for j in i:
                        l.append(j)
                    print(s.format(l[0],l[1],l[2],l[3],l[4],l[5]))
                    l=[]
                    print("+--------------------------------------------------------------------------------------------------------------+")
                print()
                print("########################################################")
                print("# THE BOOKS WITH QUANTITY 0 ARE NOT AVAILABLE FOR NOW  #")
                print("# CHOOSE BY BOOKID                                     #")
                print("# A BORROWER CAN BORROW ONE BOOK AT A TIME             #")
                print("########################################################")
                list=[]
                while True:
                    book=input("ENTER BOOKID TO BORROW:")
                    list.append(book)
                    n=input("WANT TO CHANGE THE BOOK?[Y/N]:")
                    if n=="n" or n=="N":
                        break
                def bookfinal(list):
                    def updateborrowerlist(h):
                        qry="""select slno from borrowers;"""
                        cur.execute(qry)
                        sl=cur.fetchall()
                        c=0
                        for i in sl:
                            for j in i:
                                c=j
                        slno=c+1
                        name=input("ENTER YOUR NAME:")
                        phone=int(input("ENTER PHONE NO(10 DIGITS):"))
                        addr=input("ENTER YOUR ADDRESS(30 LETTERS LIMIT):")
                        bookn,bookid=h[1],h[4]
                        date=input("ENTER BORROWING DATE (YYYY-MM-DD):")
                        d=date.split("-")
                        w=""
                        for jj in d:
                            if int(d[1])>1 and int(d[1])<12:
                                if int(d[2])+15<30:
                                    w=str(d[0]+"-"+d[1]+"-"+str((int(d[2])+15)))
                                else:
                                    w=str(d[0]+"-"+str(int(d[1])+1)+"-"+str((int(d[2])+15)-30))
                        qry2="""insert into borrowers values(%s,%s,%s,%s,%s,%s,%s,%s);"""
                        l3=[slno,name,phone,addr,bookn,bookid,date,w]
                        cur.execute(qry2,l3)
                        con.commit()
                        print("|_______________________|")
                        print("+-----------------------------------------------------------------+")
                        print("|                 BOOK STORE                                      |")
                        print("|                                                                 |")
                        print("|NAME:{:^30}   DATE:{:^10}            |".format(name,date))
                        print("|BOOKID:{:^5}                                                     |".format(bookid))
                        print("|BOOKBORROWED:{:^30}                      |".format(bookn))
                        print("|                                                                 |")
                        print("|DATE OF RETURN:{:^10}                                        |".format(w))
                        print("|*AFTER COMPLITION OF RETURNING DATE A FINE OF Rs.15 WILL BE      |")
                        print("|CHARGED PER DAY.                                                 |")
                        print("|*INCASE OF BOOK LOST OR DAMAGE THE FULL PRICE OF BOOK WILL BE    |")
                        print("|CHARGED AS FINE                                                  |")
                        print("+-----------------------------------------------------------------+")
                        print("|_______________________|")
                    while True:    
                        qry="""select * from booklist where bookid=%s;"""
                        print("THE BOOK YOU CHOOSE:")
                        h=[]
                        for l in list:
                            cur.execute(qry,[str(l)])
                            k=cur.fetchall()
                            for j in k:
                                for o in j:
                                    h.append(o)
                                    print(o,end=" | ")
                                print()
                        ll=input("DO YOU WANT TO CONFIRM[y/n]")
                        if ll=="n" or ll=="N":
                            list=[]
                            break
                        elif ll=="Y" or ll=="y":
                            updateborrowerlist(h)
                            break
                        else:
                            print("INVALID CHOICE")
                bookfinal(list)
            def b3():    #DIVYANSH
                g=input("ENTER BOOKNAME:")
                cur.execute("""select * from booklist where bookname like "{}%";""".format(g))
                m=cur.fetchall()
                print("+--------------------------------------------------------------------------------------------------------------+")
                print("|SLNo. |BOOKNAME                      |AUTHOR's NAME                 |GENRE                         |BOOKID|QTY|")
                print("+-------------------------------------------------------------------------------------------------------------+")
                s="|{:^6}|{:^30}|{:^30}|{:^30}|{:^6}|{:^3}|"
                l=[]
                for i in m:
                    for j in i:
                        l.append(j)
                    print(s.format(l[0],l[1],l[2],l[3],l[4],l[5]))
                    l=[]
                    print("+--------------------------------------------------------------------------------------------------------------+")
                print()
                print("########################################################")
                print("# THE BOOKS WITH QUANTITY 0 ARE NOT AVAILABLE FOR NOW  #")
                print("# CHOOSE BY BOOKID                                     #")
                print("# A BORROWER CAN BORROW ONE BOOK AT A TIME             #")
                print("########################################################")
                list=[]
                if len(list)!=0:
                    while True:
                        book=input("ENTER BOOKID TO BORROW:")
                        list.append(book)
                        n=input("WANT TO CHANGE THE BOOK?[Y/N]:")
                        if n=="n" or n=="N":
                            break
                    def bookfinal(list):
                        def updateborrowerlist(h):
                            qry="""select slno from borrowers;"""
                            cur.execute(qry)
                            sl=cur.fetchall()
                            c=0
                            for i in sl:
                                for j in i:
                                    c=j
                            slno=c+1
                            name=input("ENTER YOUR NAME:")
                            phone=int(input("ENTER PHONE NO(10 DIGITS):"))
                            addr=input("ENTER YOUR ADDRESS(30 LETTERS LIMIT):")
                            bookn,bookid=h[1],h[4]
                            date=input("ENTER BORROWING DATE (YYYY-MM-DD):")
                            d=date.split("-")
                            w=""
                            for jj in d:
                                if int(d[1])>1 and int(d[1])<12:
                                    if int(d[2])+15<30:
                                        w=str(d[0]+"-"+d[1]+"-"+str((int(d[2])+15)))
                                    else:
                                        w=str(d[0]+"-"+str(int(d[1])+1)+"-"+str((int(d[2])+15)-30))
                            qry2="""insert into borrowers values(%s,%s,%s,%s,%s,%s,%s,%s);"""
                            l3=[slno,name,phone,addr,bookn,bookid,date,w]
                            cur.execute(qry2,l3)
                            con.commit()
                            print("|_______________________|")
                            print("+-----------------------------------------------------------------+")
                            print("|                 BOOK STORE                                      |")
                            print("|                                                                 |")
                            print("|NAME:{:^30}   DATE:{:^10}            |".format(name,date))
                            print("|BOOKID:{:^5}                                                     |".format(bookid))
                            print("|BOOKBORROWED:{:^30}                      |".format(bookn))
                            print("|                                                                 |")
                            print("|DATE OF RETURN:{:^10}                                        |".format(w))
                            print("|*AFTER COMPLITION OF RETURNING DATE A FINE OF Rs.15 WILL BE      |")
                            print("|CHARGED PER DAY.                                                 |")
                            print("|*INCASE OF BOOK LOST OR DAMAGE THE FULL PRICE OF BOOK WILL BE    |")
                            print("|CHARGED AS FINE                                                  |")
                            print("+-----------------------------------------------------------------+")
                            print("|_______________________|")
                        while True:    
                            qry="""select * from booklist where bookid=%s;"""
                            print("THE BOOK YOU CHOOSE:")
                            h=[]
                            for l in list:
                                cur.execute(qry,[str(l)])
                                k=cur.fetchall()
                                for j in k:
                                    for o in j:
                                        h.append(o)
                                        print(o,end=" | ")
                                    print()
                            ll=input("DO YOU WANT TO CONFIRM[y/n]")
                            if ll=="n" or ll=="N":
                                list=[]
                                break
                            elif ll=="Y" or ll=="y":
                                updateborrowerlist(h)
                                break
                            else:
                                print("INVALID CHOICE")
                else:
                    print("NO BOOK FOUND PLEASE TRY AGAIN")
                bookfinal(list)
            while True:  #PRAKHAR
                print("+-------------------------------------+")
                print("|1.ALL BOOKS                          |")
                print("|2.FILTER BY GENRE                    |")
                print("|3.SEARCH BY BOOK NAME                |")
                print("|4.EXIT TO BOOK BORROWER's CHOICE     |")
                print("+-------------------------------------+")
                m=int(input("ENTER YOUR CHOICE:"))
                if m==4:
                    break
                elif m==1:
                    b1()
                elif m==2:
                    b2()
                elif m==3:
                    b3()
                else:
                    print("INVALID CHOICE")
        if n==2:
            break
        elif n==1:
            bookshowcase()
        else:
            print("INVALID CHOICE")
while True:
    print("+------------------------------+")
    print("|           BOOKSTORE          |")
    print("|1.ADMIN                       |")
    print("|2.BOOK BORROWER               |")
    print("|3.EXIT                        |")
    print("+------------------------------+")
    n=int(input("ENTER YOUR CHOICE:"))
    if n==3:
        print("~~~~~~~THANKYOU~~~~~~~~")
        con.close()
        break
    elif n==1:
        admin()
    elif n==2:
        bookborrower()
    else:
        print("INVALID CHOICE")