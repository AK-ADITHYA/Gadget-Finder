import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123")
mydb.is_connected()
mycursor=mydb.cursor()
def database():
    from Gadgetfinder import Creatingtables
    def c():
        #Database-cameras
        mycursor.execute("CREATE DATABASE cameras")
        mydb.commit()
        Creatingtables.camera()
    def p():
        #Database-smartphones
        mycursor.execute("CREATE DATABASE PHONES")
        mydb.commit()
        Creatingtables.phones()
        #Database-Smartwatches
    def s():
        mycursor.execute("create database Smartwatches")
        mydb.commit()
        Creatingtables.smartwatches()
    def l():
        #Database-Logindetails
        mycursor.execute("CREATE DATABASE Logindetails")
        mydb.commit()
    c()
    p()
    s()


