from prettytable import PrettyTable
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="PHONES")
mycursor=mydb.cursor()
#search PHONES
def phones():
    c=1
    while(c==1):
        print("AVAILABLE BRANDS ARE")
        print("********************")
        print("1.SAMSUNG")
        print("*********")
        print("2.APPLE")
        print("*******")
        print("3.GOOGLE")
        print("********")
        c=int(input("ENTER YOUR CHOICE: "))
        if c==1:
            n=input("do you want to apply filters?y/n")
            if n=="y":
                print("1.price")
                print("2.battery")
                print("3.ram")
                m=int(input("enter your filter: "))
                if m==1:
                    l=int(input("enter lower value: "))
                    h=int(input("enter higher value: "))
                    mycursor.execute("select * from SAMSUNG where price >'{}' and price <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['MODEL_NAME','RAM','ROM','BATTERY','FRONT_CAMERA','REAR_CAMERA','PRICE'])
                    for i in val:
                        table.add_row(i)
                    print(table)
                elif m==2:
                    l=int(input("enter lower value: "))
                    h=int(input("enter higher value: "))
                    mycursor.execute("select * from SAMSUNG where battery >'{}' and battery <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['MODEL_NAME','RAM','ROM','BATTERY','FRONT_CAMERA','REAR_CAMERA','PRICE'])
                    for i in val:
                        table.add_row(i)
                    print(table)
                elif m==3:
                    l=int(input("enter lower value: "))
                    h=int(input("enter higher value: "))
                    mycursor.execute("select * from SAMSUNG where ram >'{}' and ram <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['MODEL_NAME','RAM','ROM','BATTERY','FRONT_CAMERA','REAR_CAMERA','PRICE'])
                    for i in val:
                        table.add_row(i)
                    print(table)
                else:
                    print("invalid choice")
        elif c==2:

            n=input("do you want to apply filters?y/n")
            if n=="y":
                print("1.price")
                print("2.battery")
                print("3.ram")
                m=int(input("enter your filter: "))
                if m==1:
                    l=int(input("enter lower value: "))
                    h=int(input("enter higher value: "))
                    mycursor.execute("select * from APPLE where price >'{}' and price <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['MODEL_NAME','RAM','ROM','BATTERY','FRONT_CAMERA','REAR_CAMERA','PRICE'])
                    for i in val:                
                        table.add_row(i)
                    print(table)
                elif m==2:
                    l=int(input("enter lower value: "))
                    h=int(input("enter higher value: "))
                    mycursor.execute("select * from APPLE where battery >'{}' and battery <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['MODEL_NAME','RAM','ROM','BATTERY','FRONT_CAMERA','REAR_CAMERA','PRICE'])
                    for i in val:                
                        table.add_row(i)
                    print(table)
                elif m==3:
                    l=int(input("enter lower value: "))
                    h=int(input("enter higher value: "))
                    mycursor.execute("select * from APPLE where ram >'{}' and ram <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['MODEL_NAME','RAM','ROM','BATTERY','FRONT_CAMERA','REAR_CAMERA','PRICE'])
                    for i in val:                
                        table.add_row(i)
                    print(table)
                else:
                    print("invalid choice")
        elif c==3:
            
            n=input("do you want to apply filters?y/n")
            if n=="y":
                print("1.price")
                print("2.battery")
                print("3.ram")
                m=int(input("enter your filter: "))
                if m==1:
                    l=int(input("enter lower value: "))
                    h=int(input("enter higher value: "))
                    mycursor.execute("select * from GOOGLE where price >'{}' and price <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['MODEL_NAME','RAM','ROM','BATTERY','FRONT_CAMERA','REAR_CAMERA','PRICE'])
                    for i in val:                
                        table.add_row(i)
                    print(table)
                    
                elif m==2:
                    l=int(input("enter lower value: "))
                    h=int(input("enter higher value: "))
                    mycursor.execute("select * from GOOGLE where battery >'{}' and battery <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['MODEL_NAME','RAM','ROM','BATTERY','FRONT_CAMERA','REAR_CAMERA','PRICE'])
                    for i in val:                
                        table.add_row(i)
                    print(table)
                elif m==3:
                    l=int(input("enter lower value: "))
                    h=int(input("enter higher value: "))
                    mycursor.execute("select * from GOOGLE where ram >'{}' and ram <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['MODEL_NAME','RAM','ROM','BATTERY','FRONT_CAMERA','REAR_CAMERA','PRICE'])
                    for i in val:                
                        table.add_row(i)
                    print(table)
                else:
                    print("invalid choice")
        else:
            print("INVALID CHOICE")
        c=int(input("Do you want to go to selecting brand 1 for YES and any other key for NO"))

                    
                    
