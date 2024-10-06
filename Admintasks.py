import mysql.connector
def admin():
    print("In which Device you want to make changes")
    print("1.Cameras")
    print("2.Smartphones")
    print("3.Smartwatches")
    c=int(input('Enter your choice'))
    if(c==1):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="cameras")
        mydb.is_connected()
        mycursor=mydb.cursor()
        print('1.Add')
        print('2.Modify')
        print('3.Delete')
        ch=int(input("Enter yout choice"))
        if(ch==1):
            t=1
            while(t==1):
                mycursor.execute("show tables")
                val=mycursor.fetchall()
                for i in val:
                    print(i)
                table=input("Enter tablename of which you want to update records ")
                s=int(input("Enter sl no"))
                name=input("Enter name")
                sensor=input("Enter sensor type")
                res=float(input("Enter resolution"))
                price=int(input("Enter price"))
                mycursor.execute("INSERT INTO '{}' VALUES('{}','{}','{}','{}','{}'").format(table,s,name,sensor,res,price)
                mydb.commit
                t=int(input('Do you want to continue Entering values 1 for yes and any other key(number) for no'))
        elif(ch==2):
            t=1
            while(t==1):
                mycursor.execute("show tables")
                val=mycursor.fetchall()
                for i in val:
                    print(i)
                table=input("Enter tablename of which you want to update records ")
                o=int(input("Enter slno"))
                price=int(input("Enter new price"))
                mycursor.execute("update '{}' set price='{}' where slno='{}' ").format(table,price,o)
                t=int(input('Do you want to continue updating values 1 for yes and any other key(number) for no'))
        elif(ch==3):
            t=1
            while(t==1):
                mycursor.execute("show tables")
                val=mycursor.fetchall()
                for i in val:
                    print(i)
                table=input("Enter tablename of which you want to delete records ")
                o=int(input("Enter slno"))
                mycursor.execute("delete from '{}' where slno='{}' ").format(table,o)
                t=int(input('Do you want to continue deleting 1 for yes and any other key(number) for no'))
                
    elif(c==2):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="phones")
        mydb.is_connected()
        mycursor=mydb.cursor()
        print('1.Add')
        print('2.Modify')
        print('3.Delete')
        ch=int(input("Enter yout choice"))
        if(ch==1):
            t=1
            while(t==1):
                mycursor.execute("show tables")
                val=mycursor.fetchall()
                for i in val:
                    print(i)
                table=input("Enter tablename of which you want to update records ")
                n=input("Enter MODEL NAME")
                ram=input("Enter RAM")
                rom=input("Enter ROM")
                bat=input("Enter BATTERY")
                f=input("Enter FRONT CAMERA")
                b=input("Enter BACK CAMERA")
                p=int(input("Enter PRICE"))
                mycursor.execute("INSERT INTO '{}' VALUES('{}','{}','{}','{}','{}'").format(table,n,ram,rom,bat,f,b,p)
                mydb.commit
                t=int(input('Do you want to continue Entering values 1 for yes and any other key(number) for no'))
        elif(ch==2):
            t=1
            while(t==1):
                mycursor.execute("show tables")
                val=mycursor.fetchall()
                for i in val:
                    print(i)
                table=input("Enter tablename of which you want to update records ")
                print("PRICE")
                o=int(input("Enter slno"))
                price=int(input("Enter PRICE"))
                mycursor.execute("update '{}' set price='{}' where slno='{}' ").format(table,price,o)
                t=int(input('Do you want to continue updating values 1 for yes and any other key(number) for no'))
        elif(ch==3):
            t=1
            while(t==1):
                mycursor.execute("show tables")
                val=mycursor.fetchall()
                for i in val:
                    print(i)
                table=input("Enter tablename of which you want to delete records ")
                o=int(input("Enter slno"))
                mycursor.execute("delete from '{}' where slno='{}' ").format(table,o)
                t=int(input('Do you want to continue deleting 1 for yes and any other key(number) for no'))

    elif(c==3):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="smartwatches")
        mydb.is_connected()
        mycursor=mydb.cursor()
        print('1.Add')
        print('2.Modify')
        print('3.Delete')
        ch=int(input("Enter yout choice"))
        if(ch==1):
            t=1
            while(t==1):
                mycursor.execute("show tables")
                val=mycursor.fetchall()
                for i in val:
                    print(i)
                table=input("Enter tablename of which you want to update records ")
                s=int(input("Enter slno"))
                name=input("Enter name")
                st=int(input('Enter storage'))
                g=input('Enter Heartrate sensor(YES/NO)')
                h=input('Enter SLEEPMONITOR(YES/NO)')
                i=input('Enter ECG(YES/NO)')
                j=input('Enter EMERGENCYCALLING(YES/NO)')
                k=input('Enter FALLDETECTION(YES/NO)')
                l=input('Enter GPS(YES/NO)')
                m=input('Enter COMPASS(YES/NO)')
                n=input('Enter ACCELEROMETER(YES/NO)')
                o=input('Enter SPECIALFEATURE(YES/NO)')
                p=int(input('Enter PRICE'))
                mycursor.execute("INSERT INTO '{}' VALUES('{}','{}','{}','{}','{}'").format(table,s,name,st,g,h,i,j,k,l,m,n,o,p)
                t=int(input('Do you want to continue Entering values 1 for yes and any other key(number) for no'))
        elif(ch==2):
            t=1
            while(t==1):
                mycursor.execute("show tables")
                val=mycursor.fetchall()
                for i in val:
                    print(i)
                table=input("Enter tablename of which you want to update records ")
                o=int(input("Enter slno"))
                price=int(input("Enter PRICE"))
                mycursor.execute("update '{}' set price='{}' where slno='{}' ").format(table,price,o)
                t=int(input('Do you want to continue updating 1 for yes and any other key(number) for no'))
        elif(ch==3):
            t=1
            while(t==1):
                mycursor.execute("show tables")
                val=mycursor.fetchall()
                for i in val:
                    print(i)
                table=input("Enter tablename of which you want to delete records ")
                o=int(input("Enter slno"))
                mycursor.execute("delete from '{}' where slno='{}' ").format(table,o)
                t=int(input('Do you want to continue deleting 1 for yes and any other key(number) for no'))
admin()
            
