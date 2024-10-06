from tkinter import *
from PIL import ImageTk,Image
def mainmenu():
    print("==========================Welcome to Gadeget finder==========================")

    
    #fuction for printing the logo
    def displaylogo():
        root=Tk()
        root.title("Welcome")


        img=ImageTk.PhotoImage(Image.open("Gadget finder logo.jpg"))
        l=Label(image=img)
        l.pack()

        root.mainloop()
    #displaylogo()


    print("This program is designed to guide the user to find the perfect gadget that fits their budget and requirements without an internet connection.\nUsing the built-in databases. ")

    print("")

    print("Select the gadget you want")
    print("1.Cameras",sep='\t')
    print("2.Smart phones",sep='\t')
    print("3.Smart watches",sep='\t')

    choice=int(input("Enter your choice "))

    if(choice==1):
        from Gadgetfinder import Camerafilter
        Camerafilter.cameras()
        
    elif(choice==2):
        from Gadgetfinder import Phonefilter
        Phonefilter.phones()
    elif(choice==3):
        from Gadgetfinder import Watchfilter
        Watchfilter.watches()
        

mainmenu()


