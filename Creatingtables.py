import mysql.connector

#Table for cameras
def camera():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="cameras")
    mydb.is_connected()
    mycursor=mydb.cursor()

    mycursor.execute('CREATE TABLE Canondslrfull(Slno int(2),Name varchar(100),Sensortype varchar(10),Resolution decimal(4, 2),Price int(10))')
    mydb.commit()
    mycursor.execute('CREATE TABLE Canondslrapsc(Slno int(2),Name varchar(100),Sensortype varchar(10),Resolution decimal(4, 2),Price int(10))')
    mydb.commit()
    mycursor.execute('CREATE TABLE CanonmirrorlesseosR(Slno int(2),Name varchar(100),Sensortype varchar(10),Resolution decimal(4, 2),Price int(10))')
    mydb.commit()
    mycursor.execute('CREATE TABLE CanonmirrorlesseosM(Slno int(2),Name varchar(100),Sensortype varchar(10),Resolution decimal(4, 2),Price int(10))')
    mydb.commit()
    mycursor.execute('CREATE TABLE Sonymirrorlessfull(Slno int(2),Name varchar(100),Sensortype varchar(10),Resolution decimal(4, 2),Price int(10))')
    mydb.commit()
    mycursor.execute('CREATE TABLE Sonymirrorlessapsc(Slno int(2),Name varchar(100),Sensortype varchar(10),Resolution decimal(4, 2),Price int(10))')
    mydb.commit()
    mycursor.execute('CREATE TABLE Nikondslrfull(Slno int(2),Name varchar(100),Sensortype varchar(10),Resolution decimal(4, 2),Price int(10))')
    mydb.commit()
    mycursor.execute('CREATE TABLE Nikondslrapsc(Slno int(2),Name varchar(100),Sensortype varchar(10),Resolution decimal(4, 2),Price int(10))')
    mydb.commit()
    mycursor.execute('CREATE TABLE Nikonmirrorless(Slno int(2),Name varchar(100),Sensortype varchar(10),Resolution decimal(4, 2),Price int(10))')
    mydb.commit()
    mydb.close()
    from Gadgetfinder import Enteringvalues
    Enteringvalues.camerain()
    
    


def login():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="logindetails")
    mydb.is_connected()
    mycursor=mydb.cursor()
    mycursor.execute('CREATE TABLE admin(Username varchar(20) Primary key,password varchar(8))')
    mydb.commit()
    mycursor.execute('CREATE TABLE user(Username varchar(20) Primary key,password varchar(8))')
    mydb.commit()
    mydb.close()
    

#Table for smartphones
def phones():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="phones")
    mydb.is_connected()
    mycursor=mydb.cursor()           
    mycursor.execute("CREATE TABLE SAMSUNG(model_name varchar(10),ram int(3),rom int(3),battery int(3),front_camera varchar(20),rear_camera varchar(20),price int(6))")
    mydb.commit()
    mycursor.execute("CREATE TABLE APPLE(model_name varchar(10),ram int(3),rom int(3),battery int(3),front_camera varchar(20),rear_camera varchar(20),price int(6))")
    mydb.commit()
    mycursor.execute("CREATE TABLE GOOGLE(model_name varchar(10),ram int(3),rom int(3),battery int(3),front_camera varchar(20),rear_camera varchar(20),price int(6))")
    mydb.commit()
    from Gadgetfinder import Enteringvalues
    Enteringvalues.phonein()




#Table for smartwatches

def smartwatches():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="smartwatches")
    mydb.is_connected()
    mycursor=mydb.cursor()
    mycursor.execute('CREATE TABLE APPLE(Slno int(2),NAME varchar(100),STORAGE int(6),HEARTRATESENSOR varchar(10),SLEEPMONITOR VARCHAR(10),ECG varchar(10),EMERGENCYCALLING varchar(10),FALLDETECTION varchar(10),GPS varchar(10),COMPASS varchar(10),ACCELEROMETER varchar(10),SPECIALFEATURE varchar(100),PRICE int(10))')
    mydb.commit()
    mycursor.execute('CREATE TABLE NOISE(Slno int(2),NAME varchar(100),STORAGE int(6),ACCELEROMETER varchar(10),HEARTRATESENSOR varchar(10),SLEEPMONITOR varchar(10),ECG varchar(10),GPS varchar(10),FALLDETECTION varchar(10),EMERGENCYCALLING varchar(10),COMPASS varchar(10),SPECIALFEATURE varchar(100),Price int(10))')
    mydb.commit() 
    mycursor.execute('CREATE TABLE FOSSIL(Slno int(2),NAME varchar(100),STORAGE int(6),ACCELEROMETER varchar(10),HEARTRATESENSOR varchar(10),SLEEPMONITOR varchar(10),ECG varchar(10),GPS varchar(10),FALLDETECTION varchar(10),EMERGENCYCALLING varchar(10),COMPASS varchar(10),SPECIALFEATURE varchar(100),Price int(10))')
    mydb.commit()
    from Gadgetfinder import Enteringvalues
    Enteringvalues.watchin()
    




