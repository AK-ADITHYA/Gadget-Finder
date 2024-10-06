#Import statements
from tkinter import *
from PIL import ImageTk,Image
from prettytable import PrettyTable
import mysql.connector
def creation():
    print('Please wait it will take approximately 40 sec ')
    from Gadgetfinder import Creatingdatabase
    Creatingdatabase.database()
ans=input('Are you running the pgm for the first time (y/n)')
if(ans=='y'):
    creation()    
mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="Logindetails")
mydb.is_connected()
mycursor=mydb.cursor()
mydb.commit()



def userc():
    u=input("Create username")
    p=int(input("Create Password"))
    mycursor.execute("insert into user values('{}','{}')".format(u,p))
    mydb.commit()
    print('Successfull!!')
    

def userl():
    u=input("Enter username")
    p=int(input("Enter Password"))
    mycursor.execute("select password from user where Username='{}'".format(u))
    val=list(mycursor.fetchone())
    if(len(val)==0):
         print("Wrong Credentials!!")
    for i in val:
         if(i==str(p)):
            print("Logged in successfully")
            print("")
            print("")
            from Gadgetfinder import Startingscreen
            Startingscreen.mainmenu()
                   
def adminl():
    u=input("Enter username")
    p=int(input("Enter Password"))
    mycursor.execute("select password from admin where Username='{}'".format(u))
    val=mycursor.fetchone()
    if(len(val)==0):
        print("Wrong Credentials!!")
    for i in val:
        if(i==str(p)):
            print("Logged in successfully")
            from Gadgetfinder import Admintasks
            Admintasks.admin()
yc=1
while(yc==1):
    print("Select the type of login you want")
    print("1.Admin Login ")
    print("2.User Login ")
    print("3.User Create account ")
    ch=int(input('Enter your choice'))     
    if(ch==1):
        adminl()
    if(ch==2):
        userl()
    if(ch==3):
        userc()
    yc=int(input("Enter 1 to continue or 0 to end"))
        
