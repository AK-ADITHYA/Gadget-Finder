from prettytable import PrettyTable
import mysql.connector
def watches():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="smartwatches")
    mydb.is_connected()
    mycursor=mydb.cursor()
    print("Available Brands Are:")
    print("****************************************************************************************")
    print("1.APPLE")
    print("........................................................................................")
    print("2.FOSSIL")
    print("........................................................................................")
    print("3.NOISE")
    print("........................................................................................")
    b=input("do you want to start browsing?yes/no")
    while b=="yes":
        n=int(input("enter product number:1.APPLE 2.FOSSIL 3.NOISE"))
        if n==1:
            print("~~APPLE SMARTWATCHES~~")
            print("*******************************************************************************************")
            f=input("Apply Filters?(y/n):")
            while f=="y":
                print("1.Price")
                print("2.Storage")
                print("3.Features")
                a=int(input("Enter Filter Number:"))
                if a==1:
                    print("PLEASE NOTE THAT THE STARTING VALUE IS 20900")
                    l=int(input("Enter Lowest Value:"))
                    h=int(input("enter highest Value:"))
                    mycursor.execute("select * from APPLE where PRICE >'{}' and PRICE <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                    for i in val:                
                        table.add_row(i)
                    print(table)  
                elif a==2:
                    print("PLEASE NOTE THAT THE LOWEST STORAGE SPACE AVAILABLE IS 8 GB ")
                    l=int(input("Enter Lowest Value:"))
                    h=int(input("enter highest Value:"))
                    mycursor.execute("select * from APPLE where STORAGE>'{}' and STORAGE<'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                    for i in val:                
                        table.add_row(i)
                    print(table)  
                elif a==3:
                    print("PLEASE NOTE THAT THE ONLY FILTER FOR FEATURES IS EMERGENCY CALLING(OTHER FEATURES ARE ALL COMMON FOR ALL)")
                    q=input("Emergency Calling(yes/no):")
                    if q=="yes":
                        mycursor.execute("select * from APPLE where EMERGENCYCALLING='YES'")
                        val=mycursor.fetchall()
                        table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                        for i in val:
                            table.add_row(i)
                        print(table)
                    elif q=="no":
                        mycursor.execute("select * from apple where EMERGENCYCALLING='NO'")
                        val=mycursor.fetchall()
                        table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                        for i in val:
                            table.add_row(i)
                        print(table)
                    else:
                        print("wrong format")
                else:
                    print("not available")
                f=input("if you want to continue checking filters press y or if n you want to view all the data ")
    
            if f=="n":
                print("Printing all the data")
                mycursor.execute("select * from apple")
                val=mycursor.fetchall()
                table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                for i in val:
                    table.add_row(i)
                print(table)
        elif n==2:
            print("~~FOSSIL SMARTWATCHES~~")
            print("*******************************************************************************************")
            f=input("Apply Filters?(y/n):")
            while f=="y":
                print("1.Price")
                print("2.Features")
                a=int(input("Enter Filter Number:"))
                if a==1:
                    print("PLEASE NOTE THAT THE STARTING VALUE IS 10728")
                    l=int(input("Enter Lowest Value:"))
                    h=int(input("enter highest Value:"))
                    mycursor.execute("select * from FOSSIL where PRICE >'{}' and PRICE <'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                    for i in val:                
                        table.add_row(i)
                    print(table)

                    
                elif a==2:
                    print("PLEASE NOTE THAT THE ONLY FILTER FOR FEATURES IS SLEEP TRACKER")
                    q=input("SPLEEP TRACKER(yes/no):")
                    if q=="yes":
                        mycursor.execute("select * from FOSSIL where SLEEPMONITOR='YES'")
                        val=mycursor.fetchall()
                        table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])

                        for i in val:                
                            table.add_row(i)
                        print(table)  
                        
                    elif q=="no":
                        mycursor.execute("select * from FOSSIL where SLEEPMONITOR='NO'")
                        val=mycursor.fetchall()
                        table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])

                        for i in val:                
                            table.add_row(i)
                        print(table)
                    else:
                        print("wrong format")
                else:
                    print("not available")
                f=input("if you want to continue checking filters press y or if n you want to view all the data ")      
            if f=="n":
                mycursor.execute("select * from FOSSIL")
                val=mycursor.fetchall()
                table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                for i in val:
                    table.add_row(i)
                print(table)
                    
        elif n==3:
            print("~~NOISE SMARTWATCHES~~")
            print("*******************************************************************************************")
            f=input("Apply Filters?(y/n):")
            while f=="y":
                print("1.Price")
                print("2.Special Features")
                a=int(input("Enter Filter Number:"))
                if a==1:
                    print("PLEASE NOTE THAT THE STARTING VALUE IS 4999")
                    l=int(input("Enter Lowest Value:"))
                    h=int(input("enter highest Value:"))
                    mycursor.execute("select * from NOISE where PRICE>'{}' and PRICE<'{}'".format(l,h))
                    val=mycursor.fetchall()
                    table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                    for i in val:
                        table.add_row(i)
                    print(table)  
                elif a==2:
                    print("PLEASE NOTE THAT THE ONLY FILTER FOR SPECIAL FEATURES IS HAND WASH REMINDER(OTHER FEATURES ARE ALL COMMON FOR ALL)")
                    q=input("HAND WASH REMINDER(yes/no):")
                    if q=="yes":
                        mycursor.execute("select * from NOISE where SPECIALFEATURE='HAND WASH REMINDER'")
                        val=mycursor.fetchall()
                        table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                        for i in val:
                            table.add_row(i)
                        print(table)  
                    elif q=="no":
                        mycursor.execute("select * from NOISE where SPECIALFEATURE='NO'")
                        val=mycursor.fetchall()
                        table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                        for i in val:
                            table.add_row(i)
                        print(table)  
                    else:
                        print("not available")
                f=input("if you want to continue checking filters press y or if n you want to view all the data ")
            if f=="n":
                mycursor.execute("select * from NOISE")
                val=mycursor.fetchall()
                table=PrettyTable(['Slno','NAME','STORAGE','HEARTRATESENSOR','SLEEPMONITOR','ECG','EMERGENCYCALLING','FALLDETECTION','GPS','COMPASS','ACCELEROMETER','SPECIALFEATURE','PRICE'])
                for i in val:
                    table.add_row(i)
                print(table)
        b=input("if you want to continue browsing type yes or type no")
       

watches()        



