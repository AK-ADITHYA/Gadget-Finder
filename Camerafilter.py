import mysql.connector
from prettytable import PrettyTable

def cameras():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="hello123",database="cameras")
        mycursor=mydb.cursor()
        c=1
        while(c==1):
            w=int(input("Select a brand 1.Canon 2.Nikon 3.Sony"))
            if(w==1):
                ch=1
                while(ch==1):
                    t=int(input("1.DSLR or 2.Mirrorless??"))
                    if(t==1):
                        print('Filter search ')
                        print('Select the criterion for filter searching')
                        print("1.Resolution")
                        print("2.Price ")
                        ans=int(input("Enter your choice"))
                        if(ans==1):
                            
                            print("===========DSLR - FULL FRAME===========")
                            l=int(input("Enter lower value"))
                            h=int(input("Enter higher value"))
                            mycursor.execute("select * from Canondslrfull where Resolution >'{}' and Resolution <'{}'".format(l,h))
                            val=mycursor.fetchall()
                            table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                            for i in val:
                                table.add_row(i)
                            print('')
                            print('Cameras Available are')
                            print('')
                            print(table)
                            print('')
                            print('')
                        
                            print("===========DSLR - APSC===========")
                            mycursor.execute("select * from Canondslrapsc where Resolution >'{}' and Resolution <'{}'".format(l,h))
                            val=mycursor.fetchall()
                            table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                            for i in val:
                                table.add_row(i)
                            print('')
                            print('Cameras Available are')
                            print('')
                            print(table)

                            
                        if(ans==2):
                            l=int(input("Enter lower value"))
                            h=int(input("Enter higher value"))
                            mycursor.execute("select * from Canondslrfull where price >'{}' and price <'{}'".format(l,h))
                            val=mycursor.fetchall()
                            table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                            for i in val:
                                table.add_row(i)
                            print('')
                            print('Cameras Available are')
                            print('')
                            print(table)


                            print('')
                            print('')
                        
                            print("===========DSLR - APSC===========")
                            mycursor.execute("select * from Canondslrapsc where price >'{}' and price <'{}'".format(l,h))
                            val=mycursor.fetchall()
                            table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                            for i in val:
                                table.add_row(i)
                            print('')
                            print('Cameras Available are')
                            print('')
                            print(table)


                    elif(t==2):
                            print('Filter search ')
                            print('Select the criterion for filter searching')
                            print("1.Resolution")
                            print("2.Price ")
                            ans=int(input("Enter your choice"))
                            
                            if(ans==1):
                                l=int(input("Enter lower value"))
                                h=int(input("Enter higher value"))
                                print("===========MIRRORLESS - FULLFRAME===========")
                                mycursor.execute("select * from CanonmirrorlesseosR where Resolution >'{}' and Resolution <'{}'".format(l,h))
                                val=mycursor.fetchall()
                                table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                                for i in val:
                                    table.add_row(i)
                                print('')
                                print('Cameras Available are')
                                print(table)

                                print('')
                                print('')
                            
                                print("===========MIRRORLESS - APSC===========")
                                mycursor.execute("select * from Canonmirrorlesseosm where Resolution >'{}' and Resolution <'{}'".format(l,h))
                                val=mycursor.fetchall()
                                table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                                for i in val:
                                    table.add_row(i)
                                print('')
                                print('Cameras Available are')
                                print('')
                                print(table)                        


                            if(ans==2):
                                l=int(input("Enter lower value"))
                                h=int(input("Enter higher value"))
                                print("===========MIRRORLESS - FULLFRAME===========")
                                mycursor.execute("select * from Canonmirrorlesseosr where price >'{}' and price <'{}'".format(l,h))
                                val=mycursor.fetchall()
                                table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                                for i in val:
                                    table.add_row(i)
                                print('')
                                print('Cameras Available are')
                                print('')
                                print(table)

                        
                                print('')
                                print('')
                            
                                print("===========MIRRORLESS - APSC===========")
                                mycursor.execute("select * from Canonmirrorlesseosm where price >'{}' and price <'{}'".format(l,h))
                                val=mycursor.fetchall()
                                table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                                for i in val:
                                    table.add_row(i)
                                print('')
                                print('Cameras Available are')
                                print('')
                                print(table)

                        
                    ch=int(input("Do you want to continues searching  1 for YES and any other key(Number) for NO"))
                    
            if(w==2):
                ch=1         
                while(ch==1):
                    

                    t=int(input("1.DSLR or 2.Mirrorless??"))
                    if(t==1):
                        print('Filter search ')
                        print('Select the criterion for filter searching')
                        print("1.Resolution")
                        print("2.Price ")
                        ans=int(input("Enter your choice"))
                        if(ans==1):
                            l=int(input("Enter lower value"))
                            h=int(input("Enter higher value"))
                            print("===========DSLR - FULL FRAME===========")
                            mycursor.execute("select * from Nikondslrfull where Resolution >'{}' and Resolution <'{}'".format(l,h))
                            val=mycursor.fetchall()
                            table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                            for i in val:
                                table.add_row(i)
                            print('')
                            print('Cameras Available are')
                            print('')
                            print(table)
                            
                            print("===========DSLR - APSC===========")
                            mycursor.execute("select * from Nikondslrapsc where Resolution >'{}' and Resolution <'{}'".format(l,h))
                            val=mycursor.fetchall()
                            table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                            for i in val:
                                table.add_row(i)
                            print('')
                            print('Cameras Available are')
                            print('')
                            print(table)

                        if(ans==2):
                            l=int(input("Enter lower value"))
                            h=int(input("Enter higher value"))
                            print("===========DSLR - FULL FRAME===========")
                            mycursor.execute("select * from Nikondslrfull where price >'{}' and price <'{}'".format(l,h))
                            val=mycursor.fetchall()
                            table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                            for i in val:
                                table.add_row(i)
                            print('')
                            print('Cameras Available are')
                            print('')
                            print(table)
                            print("===========DSLR - APSC===========")
                            mycursor.execute("select * from Nikondslrapsc where price >'{}' and price <'{}'".format(l,h))
                            val=mycursor.fetchall()
                            table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                            for i in val:
                                table.add_row(i)
                            print('')
                            print('Cameras Available are')
                            print('')
                            print(table)
                    elif(t==2):
                        print('Filter search ')
                        print('Select the criterion for filter searching')
                        print("1.Resolution")
                        print("2.Price ")
                        ans=int(input("Enter your choice"))
                        print("=========== MIRRORLESS ===========")
                        if(ans==1):
                            l=int(input("Enter lower value"))
                            h=int(input("Enter higher value"))
                            mycursor.execute("select * from Nikonmirrorless where Resolution >'{}' and Resolution <'{}'".format(l,h))
                            val=mycursor.fetchall()
                            table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                            for i in val:
                                table.add_row(i)
                            print('')
                            print('Cameras Available are')
                            print('')
                            print(table)
                            
                        if(ans==2):
                            l=int(input("Enter lower value"))
                            h=int(input("Enter higher value"))      
                            mycursor.execute("select * from Nikonmirrorless where price >'{}' and price <'{}'".format(l,h))
                            val=mycursor.fetchall()
                            table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                            for i in val:
                                table.add_row(i)
                            print('')
                            print('Cameras Available are')
                            print('')
                            print(table)


                    ch=int(input("Do you want to continues searching  1 for YES and any other key(Number) for NO"))

            if(w==3):
                ch=1
                while(ch==1):
                    print('Filter search ')
                    print('Select the criterion for filter searching')
                    print("1.Resolution")
                    print("2.Price ")
                    ans=int(input("Enter your choice"))
                    if(ans==1):
                        l=int(input("Enter lower value"))
                        h=int(input("Enter higher value"))
                        print("=========== MIRRORLESS - FULL FRAME ===========")
                        mycursor.execute("select * from Sonymirrorlessfull where Resolution >'{}' and Resolution <'{}'".format(l,h))
                        val=mycursor.fetchall()
                        table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                        for i in val:
                            table.add_row(i)
                        print('')
                        print('Cameras Available are')
                        print('')
                        print(table)
                        
                        print("Almost all of the APS-C cameras offered by sony has tha same resoution")
                        print("=========== MIRRORLESS - APSC ===========")
                        mycursor.execute("select * from Sonymirrorlessapsc")
                        val=mycursor.fetchall()
                        table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                        for i in val:
                            table.add_row(i)
                        print(table)
                    if(ans==2):
                        l=int(input("Enter lower value"))
                        h=int(input("Enter higher value"))
                        print("=========== MIRRORLESS - FULL FRAME ===========")
                        mycursor.execute("select * from Sonymirrorlessfull where price >'{}' and price <'{}'".format(l,h))
                        val=mycursor.fetchall()
                        table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                        for i in val:
                            table.add_row(i)
                        print('')
                        print('Cameras Available are')
                        print('')
                        print(table)
                        

                        print("=========== MIRRORLESS - APSC ===========")
                        mycursor.execute("select * from Sonymirrorlessapsc where price >'{}' and price <'{}'".format(l,h))
                        val=mycursor.fetchall()
                        table=PrettyTable(['Slno','Name','Sensortype','Resolution','Price'])
                        for i in val:
                            table.add_row(i)
                        print('')
                        print('Cameras Available are')
                        print('')
                        print(table)

                    
                    ch=int(input("Do you want to continues searching  1 for YES and any other key(Number) for NO"))


            c=int(input("Do you want to go to selecting brand 1 for YES and any other key for NO"))


