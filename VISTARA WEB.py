from datetime import datetime
import mysql.connector  
mydb=mysql.connector.connect(user='root',password='', host='localhost') 
mycursor=mydb.cursor()


#creating database
mycursor.execute("create database if not exists AIRLINE")
mydb.commit()
mycursor.execute("use AIRLINE")
     
#creating customer
mycursor.execute("create table if not exists customer(Name varchar(25) primary key , address varchar(30) not null, DOJ date not null, destination varchar(20) not null)")
mydb.commit()

#creating prices
mycursor.execute("create table if not exists prices(Name varchar(25) primary key, Veg_price integer, Nonveg_price integer , Class_price integer not null, Total_price integer)")
mydb.commit()

#creating non veg
mycursor.execute("drop table if exists non_veg")
mycursor.execute("create table non_veg(sno int,food_item varchar(20),price integer)")
mycursor.execute("insert into non_veg values(1,'biryani',400)")
mycursor.execute("insert into non_veg values(2,'chicken dumplings',250)")
mycursor.execute("insert into non_veg values(3,'chicken Noodles',75)")
mycursor.execute("insert into non_veg values(4,'chicken Pizza',350)")
mycursor.execute("insert into non_veg values(5,'Grilled chicken',500)")
mydb.commit()

#creating veg
mycursor.execute("drop table if exists veg")
mycursor.execute("create table veg(Sno int , food_item varchar(20) ,price integer)")
mycursor.execute('insert into veg values(1,"Burrito",300)')
mycursor.execute('insert into veg values(2,"Maggie",230)')
mycursor.execute('insert into veg values(3,"Noodles",250)')
mycursor.execute('insert into veg values(4,"Soya Chaap",200)')
mycursor.execute('insert into veg values(5,"dumplings",75)')
mydb.commit()
#global variales for calclating ticket and food prices
classprice=0 
non_vegprice=0 
vegprice=0
s=0

def main():
    print("="*90)
    print("*"," "*20," W E L C O M E   T O   V I S T A R A "," "*25,"*")
    print("="*90)
    while True :
        print("\n--------- Main Menu ---------")
        print("1. New User Register")
        print("2. Ticket Booking")
        print("3. Food Booking ")
        print("4. View total amount")
        print("5. View Bookings ")
        print("6. Print Ticket ")
        print("7. Update")
        print("8. Delete")
        print("9. Exit")
        ch= int(input("\nEnter your choice:"))
        if ch==1:
            cust_details()
        elif ch==2:
            ticket_price()
        elif ch==3:
            menuview()
        elif ch==4:
            ticket_amt()
        elif  ch==5:
            viewdetails()
        elif ch==6:
            ticketdisplay()
        elif ch==7:
            update()
        elif ch==8:
            deletebooking()    
        elif ch==9:
            print("Thanks")
            break
        else:
            print("Invalid choice ! ") 
          
def cust_details():
    Name=input('Enter Name of customer :') 
    Address=input('Enter Address:') 
    DOJ=input('Enter date of journey :') 
    Destination=input('Enter Destination:') 
    print("Your details have been recorded")
    mycursor.execute("insert into customer values('%s','%s','%s','%s')"%(Name,Address,DOJ,Destination))
    mydb.commit()

def ticket_price():
    global s
    global classprice 
    print('These are the available class options:-') 
    print('1. type First class---> Rs6000') 
    print('2. type Business class--->Rs4000') 
    print('3. type Economy class--->Rs3000') 
    x=int(input('Enter your choice:')) 
    n=int(input('Enter No. of Passengers:')) 
    if x==1:
        s=6000*n
        Name=input("Enter Name")
        date=input("Enter the date of destination ")
        desti=input("Enter the Destination")
        print("*","="*19," B O A R D I N G   P A S S ","="*25,"*")
        print(" "*50)
        print(" "*50)
        print(" "*20,"Name: ",Name," "*25)
        print(" "*20,"Date: ",date," "*25)
        print(" "*20,"Destination: ",desti," "*25)
        print(" "*20,"You opted for FIRST CLASS")
        print(" "*20,"Price of ticket: ",s)
        print(" "*50)
        print(" "*50)
        print(" "*19," T H A N K   Y O U ")      
    elif x==2:
        s=4000*n
        Name=input("Enter Name")
        date=input("Enter the date of destination ")
        desti=input("Enter the Destination")
        print("="*19," B O A R D I N G   P A S S ","="*25)
        print(" "*50)
        print(" "*50)
        print(" "*20,"Name: ",Name," "*25,"*")
        print(" "*20,"Date: ",date," "*25,"*")
        print(" "*20,"Destination: ",desti," "*25,"*")
        print(" "*20,"You opted for BUSINESS CLASS"," "*25,"*")
        print(" "*20,"Price of ticket: ",s," "*25,"*")
        print(" "*50)
        print(" "*50)
        print(" "*19," T H A N K   Y O U ")  
    elif x==3: 
        s=3000*n
        Name=input("Enter Name")
        date=input("Enter the date of destination ")
        desti=input("Enter the Destination")
        print("="*19," B O A R D I N G   P A S S ","="*25)
        print(" "*50)
        print(" "*50)
        print(" "*20,"Name: ",Name," "*25)
        print(" "*20,"Date: ",date," "*25)
        print(" "*20,"Destination: ",desti," "*25)
        print(" "*20,"You opted for ECONOMY CLASS"," "*25)
        print(" "*20,"Price of ticket: ",s," "*25)
        print(" "*50)
        print(" "*50)
        print(" "*19," T H A N K   Y O U "," "*25) 
    else:
        print('Your total tickets cost is =',s,'\n','Please make food bookings if required- ')
    classprice+=s

def ticketdisplay():
    Name=input("Enter Name- ")
    date=input("Enter the date of destination- ")
    desti=input("Enter the Destination- ")
    print("*"," "*20," W E L C O M E   T O   V I S T A R A "," "*25,"*")
    print("-"*88)
    print("-"*88)
    print(" "*21,"Name-",Name," "*50)
    print(" "*21,"Date-",date," "*46)
    print(" "*21,"Destination-",desti," "*42)
    print("-"*88)
    print("-"*88)
    print(" "*25,"T H A N K   Y O U "," "*44)
      
def ordernon_veg():
    global s
    global non_vegprice
    print('What do you want to purchase from above list? Enter your choice.- ')
    d=int(input('Your choice:'))
    if d==1:
        print('You have ordered Biryani.')
        a=int(input('Enter quantity:'))
        s=400*a
        print('Your amount for Biryani is:',s,'\n')
    elif d==2: 
        print('You have ordered Chicken Dumplings.') 
        a=int(input('Enter quantity:')) 
        s=250*a 
        print('Your amount for Chicken Dumplings is:',s,'\n') 
    elif d==3: 
        print('You have ordered Chicken Noodles.') 
        a=int(input('Enter quantity:')) 
        s=75*a 
        print('Your amount for Chicken Noodles is:',s,'\n') 
    elif d==4:
        print('You have ordered Chicken Pizza.') 
        a=int(input('Enter quantity:')) 
        s=350*a 
        print('Your amount for Chicken Pizza is:',s,'\n') 
    elif d==5: 
        print('You have ordered Grilled Chicken.') 
        a=int(input('Enter quantity:')) 
        s=500*a 
        print('Your amount for Grilled Chicken is:',s,'\n') 
    else:
        print('Please enter your choice from the menu.') 
    non_vegprice+=s
#ordernon_veg()

def orderveg():
    global s 
    global vegprice 
    print('What do you want to purchase from above list? Enter your choice.') 
    d=int(input('Your choice:')) 
    if d==1:
        print('You have ordered Burrito.') 
        a=int(input('Enter quantity:')) 
        s=300*a 
        print('Your amount for Burrito is:',s,'\n') 
    elif d==2:
        print('You have ordered maggi.') 
        a=int(input('Enter quantity:')) 
        s=230*a 
        print('Your amount for maggi is:',s,'\n') 
    elif d==3:
        print('You have ordered Noodles.') 
        a=int(input('Enter quantity:')) 
        s=250*a 
        print('Your amount for Noodles is:',s,'\n') 
    elif d==4:
        print('You have ordered soya  chaap.') 
        a=int(input('Enter quantity:')) 
        s=200*a 
        print('Your amount for soya chaap is:',s,'\n') 
    elif d==5:
        print('You have ordered veg dumpling.') 
        a=int(input('Enter quantity:')) 
        s=75*a 
        print('Your amount for veg dumpling is:',s,'\n') 
    else:
        print('Please enter your choice from the menu.') 
    vegprice+=s
      
def menuview():
    print("Do you want to see menu available?") 
    ch=input("enter Y/y for yes") 
    if ch=='Y' or ch=='y':
        print("Do you want to see non-veg menu or veg menu?") 
        print("Enter 1 for Non Veg") 
        print("enter 2 for Veg") 
        L=int(input('Enter your choice'))
        if L==1:
            sql='select * from non_veg' 
            mycursor.execute(sql) 
            rows=mycursor.fetchall() 
            print(rows) 
            ordernon_veg() 
            choice=input('do you wanna continue ordering? yes/no') 
            if choice.lower()=="yes":
                menuview() 
            else:
                main() 
        elif L==2:
            sql='select * from veg' 
            mycursor.execute(sql) 
            rows=mycursor.fetchall() 
            print(rows) 
            orderveg() 
            choice=input("do you want to continue ordering? yes/no?") 
            if choice=="yes" or choice=="YES":
                menuview() 
            else:
                main() 
def ticket_amt():
    cust=()
    Name=input('Enter Name:') 
    Veg_price=vegprice 
    Nonveg_price=non_vegprice 
    Class_price=classprice 
    Total_price=vegprice+non_vegprice+classprice 
    print("Your Total Price is:", Total_price) 
    print("Thank you for choosing Vistara !") 
    print("We hope to see you again ;) ") 
    cust=(Name,Veg_price,Nonveg_price,Class_price,Total_price) 
    sql='insert into prices(Name, Veg_price, Nonveg_price, Class_price, Total_price) values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql,cust) 
    mydb.commit()
    main()
     
def viewdetails():
    sql='select Name from customer' 
    print("Customers saved in our system are:") 
    mycursor.execute(sql) 
    rows=mycursor.fetchall()
    print(rows) 
    s=input("Enter Name of customer whose details you require") 
    rl=(s,) 
    sql='select C.Name, Address, DOJ, Destination, Veg_price, Nonveg_price, Class_price, Total_price from customer c, prices p where c.Name=p.Name and c.Name=%s' 
    mycursor.execute(sql, rl) 
    rows=mycursor.fetchall() 
    for rec in rows:
        print("Name","adress","date of journey","destination","veg price","nonveg price","class price","total")
        print(rec)

def updateaddress():
    name=input("Enter name you want to update- ")
    query="select address from customer where Name = '%s'"%(name)
    mycursor.execute(query)
    d=mycursor.fetchone()
    print("OLD ADDRESS -:", d)
    ch=input("Press y to update address -: ")
    if ch=='y':
        newaddress=input("Enter New Address")
        print("NEW ADDRESS -:",newaddress)
        query="update customer set address='%s' where Name='%s'"%(newaddress,name)
        mycursor.execute(query)
        mydb.commit()
def updatedate():
    name=input("Enter name you want to update- ")
    query="select DOJ from customer where Name = '%s'"%(name)
    mycursor.execute(query)
    d=mycursor.fetchone()
    print("OLD DATE -:", d)
    ch=input("Press y to update date -: ")
    if ch=='y':
        newdate=input("Enter New Date")
        print("NEW DATE -:",newdate)
        query="update customer set DOJ='%s' where Name ='%s'"%(newdate,name)
        mycursor.execute(query)
        mydb.commit()
def updatedesti():
    name=input("Enter name you want to update- ")
    query="select destination from customer where Name = '%s'"%(name)
    mycursor.execute(query)
    d=mycursor.fetchone()
    print("OLD DESTINATION -:", d)
    ch=input("Press y to update destination -: ")
    if ch=='y':
        newdesti=input("Enter New Destination")
        print("NEW DESTINATION -:",newdesti)
        query="update customer set destination='%s' where Name='%s'"%(newdesti,name)
        mycursor.execute(query)
        mydb.commit()
def update():
    while True :
        print("What Do You Want To Update - ")
        print("1. Destination")
        print("2. Date of destination")
        print("3. Address")
        print("4. Exit")
        ch= int(input("\nEnter your choice:"))
        if ch==1:
            updatedesti()
        elif ch==2:
            updatedate()
        elif ch==3:
            updateaddress()
        elif ch==4:
            print("Thanks")
            break
        else:
            print("Invalid choice ! ") 
    
def deletebooking():
    name=input("Enter name you want to delete- ")
    query="select * from customer where Name = '%s'"%(name)
    mycursor.execute(query)
    d=mycursor.fetchone()
    print("OLD DETAILS -:", d)
    ch=input("Press y to delete this record -: ")
    if ch=='y':
        query="delete from customer where Name='%s'"%(name)
        mycursor.execute(query)
        mydb.commit()
main()