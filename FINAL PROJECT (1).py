#Rohit Rai
#Vidhik Dang
#Class X11-B
print()
print("                           ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
print("                           █      ██████████      █              █      █████████              █              █      ██████████      █              █")
print("                           █  ▄▀  ██████████  ▄▀  █  ▄▀▄▀▄▀▄▀▄▀  █  ▄▀  █████████  ▄▀▄▀▄▀▄▀▄▀  █  ▄▀▄▀▄▀▄▀▄▀  █  ▄▀              ▄▀  █  ▄▀▄▀▄▀▄▀▄▀  █")
print("                           █  ▄▀  ██████████  ▄▀  █  ▄▀          █  ▄▀  █████████  ▄▀          █  ▄▀      ▄▀  █  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  █  ▄▀          █")
print("                           █  ▄▀  ██████████  ▄▀  █  ▄▀  █████████  ▄▀  █████████  ▄▀  █████████  ▄▀  ██  ▄▀  █  ▄▀      ▄▀      ▄▀  █  ▄▀  █████████")
print("                           █  ▄▀  ██      ██  ▄▀  █  ▄▀          █  ▄▀  █████████  ▄▀  █████████  ▄▀  ██  ▄▀  █  ▄▀  ██  ▄▀  ██  ▄▀  █  ▄▀          █")
print("                           █  ▄▀  ██  ▄▀  ██  ▄▀  █  ▄▀▄▀▄▀▄▀▄▀  █  ▄▀  █████████  ▄▀  █████████  ▄▀  ██  ▄▀  █  ▄▀  ██  ▄▀  ██  ▄▀  █  ▄▀▄▀▄▀▄▀▄▀  █")
print("                           █  ▄▀  ██  ▄▀  ██  ▄▀  █  ▄▀          █  ▄▀  █████████  ▄▀  █████████  ▄▀  ██  ▄▀  █  ▄▀  ██      ██  ▄▀  █  ▄▀          █")
print("                           █  ▄▀      ▄▀      ▄▀  █  ▄▀  █████████  ▄▀  █████████  ▄▀  █████████  ▄▀  ██  ▄▀  █  ▄▀  ██████████  ▄▀  █  ▄▀  █████████")
print("                           █  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  █  ▄▀          █  ▄▀          █  ▄▀          █  ▄▀      ▄▀  █  ▄▀  ██████████  ▄▀  █  ▄▀          █")
print("                           █  ▄▀      ▄▀      ▄▀  █  ▄▀▄▀▄▀▄▀▄▀  █  ▄▀▄▀▄▀▄▀▄▀  █  ▄▀▄▀▄▀▄▀▄▀  █  ▄▀▄▀▄▀▄▀▄▀  █  ▄▀  ██████████  ▄▀  █  ▄▀▄▀▄▀▄▀▄▀  █")
print("                           █      ██      ██      █              █              █              █              █      ██████████      █              █")
print("                           ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
print()
print()
import mysql.connector
from time import gmtime, strftime
def cont():
    y=int(input("                                                                 DO YOU WANT TO GO BACK TO MENU\n                                                                 PRESS 1 FOR YES\n                                                                 PRESS 2 TO EXIT:"))
    print()
    if(y==1):
        print("                                                                 OK")
        print()
        i=1
    elif(y==2):
        print("                                                                 GOOD BYE")
        print()
        exit()
    else:
        print("                                                                 WRONG OPTION SELECTED")
        print()
r=0
while r==0:
    try:
        rt=0
        while rt==0:
            try:
                x12=input("                                                                 ENTER YOUR MySQL USERNAME:")
                print()
                x23=input("                                                                 ENTER YOUR MySQL PASSWORD:")
                print()
                f=mysql.connector.connect(host="localhost",user=x12,passwd=x23)
                break
            except:
                print()
                print("                                                                 USERNAME OR PASSWORD IS INCORRECT!!!PLEASE TRY AGAIN")
                print()
                continue
        c=f.cursor()
        c.execute("CREATE DATABASE eshop")
        c.execute("USE eshop")
        c.execute("CREATE TABLE REVIEW(Name char(30) not null, E_Mail char(30) Primary Key, Star_Rating int not null, Review char(50) not null)")
        c.execute("CREATE TABLE SMARTPHONE(Model_Name char(30) Primary Key, Brand_Name char(30) not null, Mrp int not null, Processor_CPU char(10) not null, RAM char(20) not null, ROM char(20) not null, Front_Camera char(20) not null, Rear_Camera char(20) not null, Bluetooth char(20) not null, Screen_Size char(10) not null, OS char(10) not null, Battery char(30) not null, MISC_Colors char(70) not null, Sim char(10) not null, Network char(70) not null, Sim_size char(20) not null, Packaging_Content char(100) not null)")
        c.execute("CREATE TABLE LAPTOP(Model_Name char(30) Primary Key, Brand_Name char(30) not null, Mrp int not null, Laptop_Type char(30) not null, Screen_Size char(30) not null, Screen_Resolution char(30) not null, Hard_Drive char(30) not null, RAM char(20) not null, Graphic_Card char(50) not null, Processor char(50) not null, OS char(30) not null, Connectivity char(60) not null, Battery char(40) not null, Built_in char(80) not null, Environmental_Features char(60) not null, Colors char(50) not null, Packaging_Content char(100) not null)")
        c.execute("CREATE TABLE HEADPHONES(Model_Name char(30) Primary Key, Brand_Name char(30) not null, Wired_Or_Wireless char(10) not null, Colour char(50) not null, Mrp int not null, Play_Time int not null, Bluetooth char(20) not null, Packaging_Content char(100) not null)")
        c.execute("CREATE TABLE EARPHONES(Model_Name char(30) Primary Key, Brand_Name char(30) not null, Wired_Or_Wireless char(10) not null, Colour char(50) not null, Mrp int not null, Play_Time int not null, Bluetooth char(20) not null, Packaging_Content char(100) not null)")
        c.execute("CREATE TABLE SMARTWATCH(Model_Name char(30) Primary Key, Brand_Name char(30) not null, Mrp int not null, OS char(50) not null, Bluetooth char(40) not null, Display_Size char(50) not null, Display_Technology char(50) not null, Processor_CPU char(30) not null, Connectivity char(100) not null, Ram char(30) not null, Rom char(30) not null, Sensors char(100) not null, Network char(100) not null, Battery char(30) not null, COLORS char(50) not null, Packaging_Content char(100) not null)")
        c.execute("CREATE TABLE TABLETS(Model_Name char(30) Primary Key, Brand_Name char(30) not null, Mrp int not null, Processor_CPU char(10) not null, Display_Size char(50) not null, Display_technology char(50) not null, SPen_Support char(30) not null, RAM char(20) not null, ROM char(20) not null, Front_Camera char(20) not null, Rear_Camera char(20) not null, Bluetooth char(20) not null, OS char(30) not null, Battery char(30) not null, Colors char(70) not null, Connectivity char(100) not null, Sim char(10) not null, Network char(100) not null, Sim_size char(20) not null, Packaging_Content char(100) not null)")
        c.execute("CREATE TABLE BOOKING(Name char(30) not null, E_Mail char(30) Primary Key, Passwd char(10) not null, Model_Name char(20) not null, Pno char(11) not null, Address char(50) not null, Date char(10) not null)")
        break
    except:
        break
i=0
while i<=0:
    j=0
    print("                                                                             █▀▄▀█ █▀▀ █▀▀▄ █  █                                                       ")      
    print("                      ----------------------------------------------------   █ █ █ █▀▀ █  █ █  █  -----------------------------------------------------") 
    print("                     |                                                       █   █ ▀▀▀ ▀  ▀  ▀▀▀                                                       |")
    print("                     |                                       1. OPTIONS FOR STAFF                                                                      |")
    print("                     |                                       2. TO CHECK FOR AN ITEM AND BOOKING                                                       |")
    print("                     |                                       3. CANCELLING ORDER                                                                       |")
    print("                     |                                       4. READ AND WRITE REVIEW                                                                  |")
    print("                     |                                       5. EXIT                                                                                   |")
    print("                      ---------------------------------------------------------------------------------------------------------------------------------")
    print()
    t=0
    while(t==0):
        try:
            x=int(input("                                                                 ENTER THE OPTION NUMBER:"))
            print()
            break
        except ValueError:
            print("                                                                 ONLY INTEGER OPTIONS!!!")
            print()
            continue
        except:
            print("                                                                 SOME ERROR HAS OCCURED PLEASE ENTER AGAIN!!!")
            print()
            continue
    if(x==1):
        for c in range(2,-1,-1):
            if(j==0):
                a=input("                                                                 ENTER THE PASSWORD(HINT-TWO ALPHABETS):")
                print()
                if(a=="vr"):
                    print("                                                                 WELCOME!!!")
                    print()
                else:
                    if(c>0):
                        print("                                                                 WRONG PASSWORD!!!")
                        print()
                        print("                                                                 YOU ARE STILL LEFT WITH",c,"TRIES!!!")
                        print()
                        o=input("                                                                 PRESS 1 TO RETRY\n                                                                 PRESS 2 TO EXIT TO MENU\n                                                                 PRESS ANY KEY TO EXIT THE PROGRAM:")
                        print()
                        if(o=="1"):
                            print("                                                                 OK")
                            print()
                            continue
                        elif(o=="2"):
                            print("                                                                 OK")
                            print()
                            break
                        else:
                            print("                                                                 GOOD BYE!!!")
                            print()
                            exit()
                    elif(c==0):
                        print("                                                                 WRONG PASSWORD!!!")
                        print()
                        print("                                                                 LOCKING")
                        print()
                        j=1
                        break
            elif(j==0.9999969):
                break
            else:
                print("                                                                 SORRY!!! MANY ATTEMPTS MADE.....")
                print()
                break
            ty=0
            while ty==0:
                print("                      --------------------------------  █▀ ▀█▀ ▄▀█ █▀▀ █▀▀   █▀▄▀█ █▀▀ █▄ █ █ █  -----------------------------------------------")
                print("                     |                                  ▄█  █  █▀█ █▀  █▀    █ ▀ █ ██▄ █ ▀█ █▄█                                                 | ")
                print("                     |                                            1. TO ADD AN ITEM                                                                    | ")
                print("                     |                                            2. TO DELETE AN ITEM                                                                 | ")
                print("                     |                                            3. TO DELETE AN ORDER                                                                | ")
                print("                     |                                            4. TO DELETE A REVIEW                                                                | ")
                print("                     |                                            5. EXIT TO MENU                                                                      | ")
                print("                      ---------------------------------------------------------------------------------------------------------------------------------")
                print()
                so=int(input("                                                                 ENTER OPTION NUMBER:"))
                print()
                if(so==1):
                    print("                      ---------------------------------------------------------------------------------------------------------------------------------")
                    print("                     |                                                                                                                                |")                     
                    print("                     |    █▀ █▀▀ █   █▀▀ █▀▀ ▀█▀   █▀▀ █▀█ █▀█ █▀▄▀█   ▀█▀ █ █ █▀▀   █▄▄ █▀▀ █   █▀█ █ █ █   █ ▀█▀ █▀▀ █▀▄▀█ █▀    |")
                    print("                     |    ▄█ ██▄ █▄▄ ██▄ █▄▄  █    █▀  █▀▄ █▄█ █ ▀ █    █  █▀█ ██▄   █▄█ ██▄ █▄▄ █▄█ ▀▄▀▄▀   █  █  ██▄ █ ▀ █ ▄█    |")
                    print("                     |                                                                                                                                |")                                            
                    print("                     |                                            1. SMARTPHONE                                                                       |")
                    print("                     |                                            2. LAPTOP                                                                           |")
                    print("                     |                                            3. HEADPHONES                                                                       |")
                    print("                     |                                            4. EARPHONES                                                                        |")
                    print("                     |                                            5. SMARTWATCH                                                                       |")
                    print("                     |                                            6. TABLETS                                                                          |")                                              
                    print("                      ---------------------------------------------------------------------------------------------------------------------------------")
                    print()
                    g=input("                                                                 ENTER THE TYPE NUMBER:")
                    print()
                    if(g=="1"):
                        #ENTERING ITEMS FOR SMARTPHONE
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        yt=0
                        while yt==0:
                            try:
                                mn=input("                                                                 ENTER MODEL NAME:")
                                print()
                                bn=input("                                                                 ENTER BRAND NAME:")
                                print()
                                type1="SMARTPHONE"
                                mrp=float(input("                                                                 ENTER THE PRICE OF SMARTPHONES:"))
                                print()
                                cpu=input("                                                                 ENTER CPU SPEED (in GHz):")
                                print()
                                ram=input("                                                                 ENTER RAM (in GB):")
                                print()
                                rom=input("                                                                 ENTER ROM (in GB):")
                                print()
                                fc=int(input("                                                                 ENTER FRONT CAMERA (in MP):"))
                                print()
                                rc=int(input("                                                                 ENTER REAR CAMERA (in MP):"))
                                print()
                                blu=input("                                                                 ENTER THE BLUETOOTH VERSION:")
                                print()
                                ss=input("                                                                 ENTER SCREEN SIZE (in inches):")
                                print()
                                os=float(input("                                                                 ENTER OPERATING SYSTEM:"))
                                print()
                                ba =input("                                                                 ENTER BATTERY CAPACITY:")
                                print()
                                misc=input("                                                                 ENTER VARIANT COLOURS:")
                                print()
                                ne=input("                                                                 ENTER NO. OF SIM:")
                                print()
                                net=input("                                                                 ENTER NETWORK/BEARER:")
                                print()
                            
                                y1=0
                                while y1==0:
                                    si=input("                                                                 PRESS 1 IF SIM IS MICRO-SIM OR PRESS 2 IF SIM IS NANO-SIM:")
                                    print()
                                    if(si=="2"):
                                        si="MICRO-SIM"
                                        break
                                    elif(si=="1"):
                                        si="NANO-SIM"
                                        break
                                    else:
                                        print("                                                                 PLEASE ENTER A VALID OPTION!!!")
                                        print()
                                        continue
                                pk=input("                                                                 ENTER PACKAGING CONTENT:")
                                print()
                                break
                            except ValueError:
                                print()
                                print("                                                                 PLEASE ENTER PROPER VALUES!!!")
                                print()
                                continue
                            except:
                                print()
                                print("                                                                 SOMETHING WENT WRONG!!! PLEASE ENTER AGAIN")
                                print()
                                continue
                        t=(mn,bn,mrp,cpu,ram,rom,fc,rc,blu,ss,os,ba,misc,ne,net,si,pk)
                        str1="""INSERT INTO SMARTPHONE (Model_Name, Brand_Name, Mrp, Processor_CPU, RAM, ROM, Front_Camera, Rear_Camera, Bluetooth, Screen_Size, OS, Battery, MISC_Colors, Sim, Network, Sim_size, Packaging_Content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        c.execute(str1,t)
                        f.commit()
                        print("                                                                 DONE!!!")
                        continue
                    if(g=="2"):
                        #ENTERING ITEM FOR LAPTOP
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        yop=0
                        while yop==0:
                            try:
                                mn=input("                                                                 ENTER MODEL NAME:")
                                print()
                                bn=input("                                                                 ENTER BRAND NAME:")
                                print()
                                type1="Laptop"
                                mrp=int(input("                                                                 ENTER THE PRICE OF Laptop:"))
                                print()
                                lt=input("                                                                 ENTER LAPTOP TYPE:")
                                print()
                                ss=input("                                                                 ENTER SCREEN SIZE:")
                                print()
                                sr=input("                                                                 ENTER SCREEN RESOLUTION:")
                                print()
                                hd=input("                                                                 ENTER HARD DRIVE (in GB):")
                                print()
                                ra=input("                                                                 ENTER RAM (in GB):")
                                print()
                                gc=input("                                                                 ENTER GRAPHIC CARD DETAILS:")
                                print()
                                pr=input("                                                                 ENTER PROCESSOR DETAILS:")
                                print()
                                os=input("                                                                 ENTER OPERATING SYSTEM:")
                                print()
                                co=input("                                                                 ENTER CONNECTIVITY FEATURES:")
                                print()
                                ba=input("                                                                 ENTER BATTERY DETAILS:")
                                print()
                                bi=input("                                                                 ENTER BUILT_IN FUNCTIONS:")
                                print()
                                ef=input("                                                                 ENTER ENVIRONMENTAL FEATURES:")
                                print()
                                co=input("                                                                 ENTER VARIANT COLOURS:")
                                print()
                                pk=input("                                                                 ENTER PACKAGING CONTENTS:")
                                print()
                                break
                            except ValueError:
                                print()
                                print("                                                                 PLEASE ENTER CORRECT VALUES!!!")
                                print()
                                continue
                            except:
                                print()
                                print("                                                                 SOME ERROR HAS OCCURED PLEASE RETRY!!!")
                                print()
                                continue
                        t=(mn,bn,mrp,lt,ss,sr,hd,ra,gc,pr,os,co,ba,bi,ef,co,pk)
                        str1="""INSERT INTO LAPTOP (Model_Name, Brand_Name, Mrp, Laptop_Type, Screen_Size, Screen_Resolution, Hard_Drive, RAM, Graphic_Card, Processor, OS, Connectivity, Battery, Built_in, Environmental_Features, Colors, Packaging_Content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        c.execute(str1,t)
                        f.commit()
                        print("                                                                 DONE!!!")
                        print()
                        cont()
                        continue                   
                    if(g=="3"):
                        #ENTERING ITEMS FOR HEADPHONES
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        yu=0
                        while yu==0:
                            try:
                                mn=input("                                                                 ENTER MODEL NAME:")
                                print()
                                bn=input("                                                                 ENTER BRAND NAME:")
                                print()
                                type3="HEADPHONES"
                                yu1=0
                                while yu1==0:
                                    w=input("                                                                 PRESS 1 IF HEADPHONES ARE WIRED OR PRESS 2 IF HEADPHONES ARE WIRELESS:")
                                    print()
                                    if(w=="1"):
                                        w1="WIRED"
                                        break
                                    elif(w=="2"):
                                        w1="WIRELESS"
                                        break
                                    else:
                                        print("                                                                 PLEASE ENTER A VALID OPTION!!!")
                                        print()
                                        continue
                                col=input("                                                                 ENTER THE COLOUR OF HEADPHONES:")
                                print()
                                mrp=float(input("                                                                 ENTER THE PRICE OF HEADPHONES:"))
                                print()
                                pt=int(input("                                                                 ENTER THE PLAY TIME OF HEADPHONES IN MINUTES:"))
                                print()
                                blu=input("                                                                 ENTER THE BLUETOOTH VERSION:")
                                print()
                                pk=input("                                                                 ENTER THE PACKAGING CONTENT:")
                                print()
                                break
                            except ValueError:
                                print()
                                print("                                                                 PLEASE ENTER PROPER VALUES!!!")
                                print()
                                continue
                            except:
                                print()
                                print("                                                                 SOMETHING WENT WRONG!!! PLEASE ENTER AGAIN")
                                print()
                                continue
                        t=(mn,bn,w1,col,mrp,pt,blu,pk)
                        str1="""INSERT INTO HEADPHONES (Model_Name, Brand_Name, Wired_or_Wireless, Colour, Mrp, Play_Time, Bluetooth, Packaging_Content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
                        c.execute(str1,t)
                        f.commit()
                        print("                                                                 DONE!!!")
                        print()
                        cont()
                        continue
                    elif(g=="4"):
                        #ENTERING ITEMS FOR EARPHONES
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        yi=0
                        while yi==0:
                            try:
                                mn=input("                                                                 ENTER MODEL NAME:")
                                print()
                                bn=input("                                                                 ENTER BRAND NAME:")
                                print()
                                yi1=0
                                while yi1==0:
                                    w=input("                                                                 PRESS 1 IF EARPHONES ARE WIRED OR PRESS 2 IF EARPHONES ARE WIRELESS:")
                                    print()
                                    if(w=="1"):
                                        w1="WIRED"
                                        break
                                    elif(w=="2"):
                                        w1="WIRELESS"
                                        break
                                    else:
                                        print("                                                                 PLEASE ENTER VALID OPTION!!!")
                                        print()
                                        continue
                                col=input("                                                                 ENTER THE COLOUR OF EARPHONES:")
                                print()
                                mrp=float(input("                                                                 ENTER THE PRICE OF EARPHONES:"))
                                print()
                                pt=int(input("                                                                 ENTER THE PLAY TIME OF EARPHONES IN MINUTES:"))
                                print()
                                blu=input("                                                                 ENTER THE BLUETOOTH VERSION:")
                                print()
                                pk=input("                                                                 ENTER THE PACKAGING CONTENT:")
                                print()
                                break
                            except ValueError:
                                print()
                                print("                                                                 PLEASE ENTER PROPER VALUES!!!")
                                print()
                                continue
                            except:
                                print()
                                print("                                                                 SOMETHING WENT WRONG!!! PLEASE ENTER AGAIN")
                                print()
                                continue
                        t=(mn,bn,w1,col,mrp,pt,blu,pk)
                        str1="""INSERT INTO EARPHONES (Model_Name, Brand_Name, Wired_or_Wireless, Colour, Mrp, Play_Time, Bluetooth, Packaging_Content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
                        c.execute(str1,t)
                        f.commit()
                        print("                                                                 DONE!!!")
                        print()
                        cont()
                        continue
                    elif(g=="5"):
                        #ENTERING ITEMS FOR SMARTWATCH
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        yt=0
                        while yt==0:
                            try:
                                mn=input("                                                                 ENTER MODEL NAME:")
                                print()
                                bn=input("                                                                 ENTER BRAND NAME:")
                                print()
                                type1="SMARTWATCH"
                                mrp=float(input("                                                                 ENTER THE PRICE OF SMARTWATCH:"))
                                print()
                                os=input("                                                                 ENTER OPERATING SYSTEM:")
                                print()
                                blu=input("                                                                 ENTER THE BLUETOOTH VERSION:")
                                print()
                                ds=input("                                                                 ENTER DISPLAY SIZE (in Inches):")
                                print()
                                dt=input("                                                                 ENTER DISPLAY TECHNOLOGY:")
                                print()
                                cpu=input("                                                                 ENTER CPU SPEED (in GHz):")
                                print()
                                con=input("                                                                 ENTER CONNECTIVITY DETAILS:")
                                print()                                
                                ram=input("                                                                 ENTER RAM (in GB):")
                                print()
                                rom=input("                                                                 ENTER ROM (in GB):")
                                print()
                                ss=input("                                                                 ENTER TYPE OF SENSORS:")
                                print()
                                net=input("                                                                 ENTER NETWORK/BEARER:")
                                print()                                
                                ba =input("                                                                 ENTER BATTERY CAPACITY:")
                                print()
                                misc=input("                                                                 ENTER VARIANT COLOURS:")
                                print()
                                pk=input("                                                                 ENTER PACKAGING CONTENTS:")
                                print()
                                break
                            except ValueError:
                                print()
                                print("                                                                 PLEASE ENTER CORRECT VALUES!!!")
                                print()
                                continue
                            except:
                                print()
                                print("                                                                 SOME ERROR HAS OCCURED PLEASE RETRY!!!")
                                print()
                                continue
                        t=(mn,bn,mrp,os,blu,ds,dt,cpu,con,ram,rom,ss,net,ba,misc,pk)
                        str1="""INSERT INTO SMARTWATCH (Model_Name, Brand_Name, Mrp, OS, Bluetooth, Display_Size, Display_Technology, Processor_CPU, Connectivity, Ram, Rom, Sensors, Network, Battery, COLORS, Packaging_Content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        c.execute(str1,t)
                        f.commit()
                        print("                                                                 DONE!!!")
                        print()
                        continue               

                    if(g=="6"):
                        #ENTERING ITEMS FOR TABLETS
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        yt=0
                        while yt==0:
                            try:
                                mn=input("                                                                 ENTER MODEL NAME:")
                                print()
                                bn=input("                                                                 ENTER BRAND NAME:")
                                print()
                                type1="TABLETS"
                                mrp=float(input("                                                                 ENTER THE PRICE OF TABLET:"))
                                print()
                                cpu=input("                                                                 ENTER CPU SPEED (in GHz):")
                                print()
                                ds=input("                                                                 ENTER DISPLAY SIZE (in Inches):")
                                print()
                                dt=input("                                                                 ENTER DISPLAY TECHNOLOGY")
                                print()
                                sps=input("                                                                 ENTER SMART PEN SUPPORT:")
                                print()
                                ram=input("                                                                 ENTER RAM (in GB):")
                                print()
                                rom=input("                                                                 ENTER ROM (in GB):")
                                print()                                
                                fc=int(input("                                                                 ENTER FRONT CAMERA (in MP):"))
                                print()
                                rc=int(input("                                                                 ENTER REAR CAMERA (in MP):"))
                                print()
                                blu=input("                                                                 ENTER THE BLUETOOTH VERSION:")
                                print()
                                os=float(input("                                                                 ENTER OPERATING SYSTEM:"))
                                print()
                                ba =input("                                                                 ENTER BATTERY CAPACITY:")
                                print()
                                misc=input("                                                                 ENTER VARIANT COLOURS:")
                                print()
                                con=input("                                                                 ENTER CONNECTIVITY DETAILS:")
                                print()
                                ne=input("                                                                 ENTER NO. OF SIM:")
                                print()
                                net=input("                                                                 ENTER NETWORK/BEARER:")
                                print()
                                y1=0
                                while y1==0:
                                    si=input("                                                                 PRESS 1 IF SIM IS MICRO-SIM OR PRESS 2 IF SIM IS NANO-SIM")
                                    print()
                                    if(si=="2"):
                                        si="MICRO-SIM"
                                        break
                                    elif(si=="1"):
                                        si="NANO-SIM"
                                        break
                                    else:
                                        print("                                                                 PLEASE ENTER A VALID OPTION!!!")
                                        print()
                                        continue
                                pk=input("                                                                 ENTER PACKAGING CONTENT:")
                                print()
                                break
                            except ValueError:
                                print()
                                print("                                                                 PLEASE ENTER PROPER VALUES!!!")
                                print()
                                continue
                            except:
                                print()
                                print("                                                                 SOMETHING WENT WRONG!!! PLEASE ENTER AGAIN")
                                print()
                                continue
                        t=(mn,bn,mrp,cpu,ds,dt,sps,ram,rom,fc,rc,blu,os,ba,misc,con,ne,net,si,pk)
                        str1="""INSERT INTO TABLETS (Model_Name, Brand_Name, Mrp, Processor_CPU, Display_Size, Display_technology, SPen_Support, RAM, ROM, Front_Camera, Rear_Camera, Bluetooth, OS, Battery, Colors, Connectivity, Sim, Network, Sim_size, Packaging_Content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        c.execute(str1,t)
                        f.commit()
                        print("                                                                 DONE!!!")
                        print()
                        continue
                elif(so==2):
                    #DELETING AN ITEM
                    f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                    c=f.cursor()
                    print("                      ---------------------------------------------------------------------------------------------------------------------------------")
                    print("                     |                                                                                                                                 |")                     
                    print("                     |    █▀ █▀▀ █   █▀▀ █▀▀ ▀█▀   █▀▀ █▀█ █▀█ █▀▄▀█   ▀█▀ █ █ █▀▀   █▄▄ █▀▀ █   █▀█ █ █ █   █ ▀█▀ █▀▀ █▀▄▀█ █▀     |")
                    print("                     |    ▄█ ██▄ █▄▄ ██▄ █▄▄  █    █▀  █▀▄ █▄█ █ ▀ █    █  █▀█ ██▄   █▄█ ██▄ █▄▄ █▄█ ▀▄▀▄▀   █  █  ██▄ █ ▀ █ ▄█     |")
                    print("                     |                                                                                                                                 |")                                            
                    print("                     |                                            1. SMARTPHONE                                                                        |")
                    print("                     |                                            2. LAPTOP                                                                            |")
                    print("                     |                                            3. HEADPHONES                                                                        |")
                    print("                     |                                            4. EARPHONES                                                                         |")
                    print("                     |                                            5. SMARTWATCH                                                                        |")
                    print("                     |                                            6. TABLETS                                                                           |")
                    print("                      ---------------------------------------------------------------------------------------------------------------------------------")
                    print()                    
                    g=input("                                                                 ENTER THE TYPE NUMBER:")
                    if(g=="1"):
                        #DELETING AN ITEM FROM SMARTPHONES
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        stris="SELECT Model_Name,Brand_Name,Mrp FROM SMARTPHONE"
                        c.execute(stris)
                        r=c.fetchall()
                        for z in r:
                            print("                                                                 --------------------------")
                            print("                                                                 MODEL NAME=",z[0])
                            print("                                                                 BRAND NAME=",z[1])
                            print("                                                                 PRICE=Rs",z[2])
                            print("                                                                 --------------------------")
                        mr=input("                                                                 ENTER THE MODEL NAME OF ITEM WHICH YOU WANT TO DELETE:")
                        ste="DELETE FROM SMARTPHONE WHERE MODEL_NAME=%s"
                        c.execute(ste,(mr,))
                        print("                                                                 DONE!!!")
                        f.commit()
                        cont()
                        continue
                    if(g=="2"):
                        #DELETING AN ITEM FROM LAPTOP
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        stris="SELECT Model_Name,Brand_Name,Mrp FROM LAPTOP"
                        c.execute(stris)
                        r=c.fetchall()
                        for z in r:
                            print("                                                                 --------------------------")
                            print("                                                                 MODEL NAME=",z[0])
                            print("                                                                 BRAND NAME=",z[1])
                            print("                                                                 PRICE=Rs",z[2])
                            print("                                                                 --------------------------")
                        vb="SELECT COUNT(*) FROM LAPTOP"
                        c.execute(vb)
                        r=c.fetchall()
                        no1=r[0]
                        no=no1[0]
                        if(no==0):
                            print("SORRY!!! NO ITEMS ADDED")
                            cont()
                            continue
                        mr=input("                                                                 ENTER THE MODEL NAME OF ITEM WHICH YOU WANT TO DELETE:")
                        for wer in range(0,no+1):
                            if(wer<=no):
                                ste="DELETE FROM LAPTOP WHERE Model_Name=%s"
                                c.execute(ste,(mr,))
                                f.commit()
                                jk=0
                                JKL="SELECT * FROM LAPTOP WHERE Model_Name=%s"
                                c.execute(JKL,(mr,))
                                r=c.fetchall()
                                l=[]
                                print(r)
                                if r==l:
                                    print("DONE")
                                    break
                                if(wer==no):
                                    jk=1
                                    break
                        print(jk)
                        if(jk==0):
                            print("DONE")
                        cont()
                        continue                    
                    if(g=="3"):
                        #DELETING AN ITEM FROM HEADPHONES
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        stris="SELECT Model_Name,Brand_Name,Mrp FROM HEADPHONES"
                        c.execute(stris)
                        r=c.fetchall()
                        for z in r:
                            print("                                                                 --------------------------")
                            print("                                                                 MODEL NAME=",z[0])
                            print("                                                                 BRAND NAME=",z[1])
                            print("                                                                 PRICE=Rs",z[2])
                            print("                                                                 --------------------------")
                        mr=input("                                                                 ENTER THE MODEL NAME OF ITEM WHICH YOU WANT TO DELETE:")
                        ste="DELETE FROM HEADPHONES WHERE Model_Name=%s"
                        c.execute(ste,(mr,))
                        print("                                                                 DONE!!!")
                        f.commit()
                        cont()
                        continue
                    elif(g=="4"):
                        #DELETING AN ITEM FROM EARPHONES
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        stris="SELECT Model_Name,Brand_Name,Mrp FROM EARPHONES"
                        c.execute(stris)
                        r=c.fetchall()
                        for z in r:
                            print("                                                                 --------------------------")
                            print("                                                                 MODEL NAME=",z[0])
                            print("                                                                 BRAND NAME=",z[1])
                            print("                                                                 PRICE=Rs",z[2])
                            print("                                                                 --------------------------")
                        mr=input("                                                                 ENTER THE MODEL NAME OF ITEM WHICH YOU WANT TO DELETE:")
                        ste="DELETE FROM EARPHONES WHERE Model_Name=%s"
                        c.execute(ste,(mr,))
                        print("                                                                 DONE!!!")
                        f.commit()
                        cont()
                        continue
                    elif(g=="5"):
                        #DELETING AN ITEM FROM SMARTWATCH
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        stris="SELECT Model_Name,Brand_Name,Mrp FROM SMARTWATCH"
                        c.execute(stris)
                        r=c.fetchall()
                        for z in r:
                            print("                                                                 --------------------------")
                            print("                                                                 MODEL NAME=",z[0])
                            print("                                                                 BRAND NAME=",z[1])
                            print("                                                                 PRICE=Rs",z[2])
                            print("                                                                 --------------------------")
                        mr=input("                                                                 ENTER THE MODEL NAME OF ITEM WHICH YOU WANT TO DELETE:")
                        ste="DELETE FROM SMARTWATCH WHERE Model_Name=%s"
                        c.execute(ste,(mr,))
                        print("                                                                 DONE!!!")
                        f.commit()
                        cont()
                        continue
                    if(g=="6"):
                        #DELETING AN ITEM FROM TABLETS
                        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                        c=f.cursor()
                        stris="SELECT Model_Name,Brand_Name,Mrp FROM TABLETS"
                        c.execute(stris)
                        r=c.fetchall()
                        for z in r:
                            print("                                                                 --------------------------")
                            print("                                                                 MODEL NAME=",z[0])
                            print("                                                                 BRAND NAME=",z[1])
                            print("                                                                 PRICE=Rs",z[2])
                            print("                                                                 --------------------------")
                        mr=input("                                                                 ENTER THE MODEL NAME OF ITEM WHICH YOU WANT TO DELETE:")
                        ste="DELETE FROM TABLETS WHERE MODEL_NAME=%s"
                        c.execute(ste,(mr,))
                        print("                                                                 DONE!!!")
                        f.commit()
                        cont()
                        continue                    
                elif(so==3):
                    f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                    c=f.cursor()
                    print("                                                                 ALL PENDING ORDERS--")
                    print()
                    c.execute("                                                                 SELECT * FROM BOOKING")
                    r=c.fetchall()
                    for z in r:
                        print("                                                                 --------------------------")
                        print("                                                                 NAME=",z[0])
                        print("                                                                 E-MAIL=",z[1])
                        print("                                                                 MODEL NAME=",z[2])
                        print("                                                                 --------------------------")
                    yu7=0
                    while yu7==0:
                        try:
                            eml=input("                                                                 ENTER THE E-MAIL ID OF THE PERSON WHOSE ORDER YOU WANT TO DELETE:")
                            print()
                            break
                        except:
                            print()
                            print("                                                                 SOME ERROR HAS OCCURED!!!")
                            print()
                            continue
                    ste="DELETE FROM BOOKING WHERE E_Mail=%s"
                    if eml in z:
                        c.execute(ste,(eml,))
                        print("                                                                 DONE!!!")
                        print()
                        f.commit()
                        break
                    else:
                        print("                                                                 SORRY!!!MAIL ID NOT FOUND...")
                        print()
                    cont()
                    continue
                elif(so==4):
                    #DELETING A REVIEW
                    f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
                    c=f.cursor()
                    print("                                                                 ALL REVIEWS--")
                    print()
                    c.execute("                                                                 SELECT * FROM REVIEW")
                    r=c.fetchall()
                    for z in r:
                        print("                                                                 --------------------------")
                        print("                                                                 NAME=",z[0])
                        print("                                                                 E-MAIL=",z[1])
                        print("                                                                 STAR RATING=",z[2])
                        print("                                                                 REVIEW=",z[3])
                        print("                                                                 --------------------------")
                    yo=0
                    while yo==0:
                        try:
                            eml=input("                                                                 ENTER THE E-MAIL ID OF THE PERSON WHOSE REVIEW YOU WANT TO DELETE:")
                            print()
                            break
                        except:
                            print()
                            print("                                                                 SOME ERROR HAS OCCURED!!! PLEASE ENTER AGAIN")
                            print()
                            continue
                    ste="DELETE FROM REVIEW WHERE E_Mail=%s"
                    if eml in z:
                        c.execute(ste,(eml,))
                        print("                                                                 DONE!!!")
                        print()
                        f.commit()
                        break
                    else:
                        print("                                                                 SORRY!!!MAIL ID NOT FOUND...")
                        print()
                    cont()
                    continue
                elif(so==5):
                    print("                                                                 OK")
                    print()
                    j=0.9999969
                    break
    elif(x==2):
        #CHECKING AN ITEM
        print("                      ---------------------------------------------------------------------------------------------------------------------------------")
        print("                     |                                                                                                                                |")                     
        print("                     |    █▀ █▀▀ █   █▀▀ █▀▀ ▀█▀   █▀▀ █▀█ █▀█ █▀▄▀█   ▀█▀ █ █ █▀▀   █▄▄ █▀▀ █   █▀█ █ █ █   █ ▀█▀ █▀▀ █▀▄▀█ █▀    |")
        print("                     |    ▄█ ██▄ █▄▄ ██▄ █▄▄  █    █▀  █▀▄ █▄█ █ ▀ █    █  █▀█ ██▄   █▄█ ██▄ █▄▄ █▄█ ▀▄▀▄▀   █  █  ██▄ █ ▀ █ ▄█    |")
        print("                     |                                                                                                                                |")                                            
        print("                     |                                            1. SMARTPHONE                                                                       |")
        print("                     |                                            2. LAPTOP                                                                           |")
        print("                     |                                            3. HEADPHONES                                                                       |")
        print("                     |                                            4. EARPHONES                                                                        |")
        print("                     |                                            5. SMARTWATCH                                                                       |")
        print("                     |                                            6. TABLETS                                                                          |")
        print("                      ---------------------------------------------------------------------------------------------------------------------------------")
        print()                
        m=input("                                                                 ENTER THE ITEM FROM ABOVE LIST WHOSE MODELS YOU WANT TO SEE:")
        if(m=="1"):
            #CHECKING AN ITEM FROM SMARTPHONE
            f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
            c=f.cursor()
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM SMARTPHONE")
            r=c.fetchall()
            for z in r:
                print("                                                                 --------------------------")
                print("                                                                 MODEL NAME=",z[0])
                print("                                                                 BRAND NAME=",z[1])
                print("                                                                 PRICE=Rs",z[2])
                print("                                                                 --------------------------")
            km=input("                                                                 ENTER THE MODEL NAME OF SMARTPHONE ABOUT WHICH YOU WANT TO KNOW MORE:")
            print()
            str2nd="SELECT * FROM SMARTPHONE WHERE Model_Name=%s"
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM SMARTPHONE")
            r=c.fetchall()
            for z in r:
                if km in z:
                    c.execute(str2nd,(km,))
                    r=c.fetchall()
                    for z in r:
                        print("                                                                 --------------------------")
                        print("                                                                 MODEL NAME=",z[0])
                        print("                                                                 BRAND NAME=",z[1])
                        print("                                                                 PRICE=Rs",z[2])
                        print("                                                                 CPU SPEED=",z[3],"Ghz")
                        print("                                                                 RAM=",z[4],"GB")
                        print("                                                                 ROM=",z[5],"GB")
                        print("                                                                 FRONT CAMERA=",z[6],"MP")
                        print("                                                                 REAR CAMERA=",z[7],"MP")
                        print("                                                                 BLUETOOTH VERSION=v",z[8])
                        print("                                                                 SCREEN SIZE=",z[9],"Inch")
                        print("                                                                 OPERATING SYSTEM=ANDROID",z[10])
                        print("                                                                 BATTERY=",z[11],"mAh")
                        print("                                                                 VARIANT COLOUR=",z[12])
                        print("                                                                 NO. OF SIM=",z[13])
                        print("                                                                 MICRO OR NANO SIM=",z[14])
                        print("                                                                 PACKAGING CONTENT=",z[15])
                        book=int(input("                                                                 DO YOU WANT TO BOOK THIS ITEM\n                                                                 PRESS 1 FOR YES\n                                                                 PRESS 2 FOR NO:"))
                        print()
                        if(book==1):
                            ui=0
                            while ui==0:
                                try:
                                    name=input("                                                                 ENTER YOUR NAME:")
                                    print()
                                    email=input("                                                                 ENTER YOUR E-MAIL ID:")
                                    print()
                                    pas=input("                                                                 ENTER YOUR EMAIL ID PASSWORD:")
                                    print()
                                    pno=input("                                                                 ENTER YOUR PHONE NUMBER:")
                                    print()
                                    add=input("                                                                 ENTER YOUR ADDRESS:")
                                    print()
                                    break
                                except:
                                    print()
                                    print("                                                                 SOME ERROR HAS OCCURED!!!PLEASE ENTER AGAIN")
                                    print()
                                    continue
                            op=strftime("%Y-%m-%d", gmtime())
                            modelname=z[0]
                            t=(name, email, pas, modelname, pno, add, op)
                            str=("INSERT INTO BOOKING(Name, E_Mail, Passwd, Model_Name, Pno, Address, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)")
                            c.execute(str,t)
                            f.commit()
                            print("                                                                 YOUR ORDER HAS BEEN BOOKED")
                            print()
                            drt="SELECT * FROM BOOKING WHERE E_Mail=%s"
                            c.execute(drt,(email,))
                            r=c.fetchall()
                            for z in r:
                                print()
                                print("                                            █▄█ █▀█ █░█ █▀█   █▀█ █▀█ █▀▄ █▀▀ █▀█")
                                print("                     -----------------------░█░ █▄█ █▄█ █▀▄   █▄█ █▀▄ █▄▀ ██▄ █▀▄----------------------------")
                                print("                    |                                                                                               ")
                                print("                    |                             NAME :",z[0],"                                                    ")
                                print("                    |                             EMAIL :",z[1],"                                                   ")
                                print("                    |                             PASSWORD:",z[2],"                                                 ")
                                print("                    |                             MODEL NAME:",z[3],"                                               ")
                                print("                    |                             PHONE NUMBER:",z[4],"                                             ")
                                print("                    |                             ADDRESS :",z[5],"                                                 ")
                                print("                    |                             DATE OF ORDER:",z[6],"                                            ")
                                print("                    |-----------------------------------------------------------------------------------------------")

                            print("                                                                 1. YOU WILL RECEIVE YOUR ORDER IN 3 WORKING DAYS\n                                                                 2. YOU WILL HAVE TO PAY CASH ON DELIVERY\n                                                                 3. YOU CAN CANCEL YOUR ORDER ANYTINE BEFORE DELIVRY")
                            print()
                    cont()
        if(m=="2"):
            #CHECKING AN ITEM FROM LAPTOP
            f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
            c=f.cursor()
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM LAPTOP")
            r=c.fetchall()
            for z in r:
                print("                                                                 --------------------------")
                print("                                                                 MODEL NAME=",z[0])
                print("                                                                 BRAND NAME=",z[1])
                print("                                                                 PRICE=Rs",z[2])
                print("                                                                 --------------------------")
            km=input("                                                                 ENTER THE MODEL NAME OF LAPTOP ABOUT WHICH YOU WANT TO KNOW MORE:")
            print()
            str2nd="SELECT * FROM LAPTOP WHERE Model_Name=%s"
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM LAPTOP")
            r=c.fetchall()
            for z in r:
                if km in z:
                    c.execute(str2nd,(km,))
                    r=c.fetchall()
                    for z in r:
                        print("                                                                 --------------------------")
                        print("                                                                 MODEL NAME=",z[0])
                        print("                                                                 BRAND NAME=",z[1])
                        print("                                                                 PRICE=Rs",z[2])
                        print("                                                                 LAPTOP TYPE=",z[3])
                        print("                                                                 SCREEN SIZE=",z[4],"Inch")
                        print("                                                                 SCREEN RESOLUTION=",z[5],"FHD")
                        print("                                                                 HARD DRIVE=",z[6],"GB")
                        print("                                                                 RAM=",z[7],"GB")
                        print("                                                                 GRAPHIC CARD DETAILS=",z[8])
                        print("                                                                 PROCESSOR DETAILS=",z[9])
                        print("                                                                 OPERATING SYSTEM=",z[10])
                        print("                                                                 CONNECTIVITY FEATURES=",z[11])
                        print("                                                                 BATTERY DETAILS=",z[12])
                        print("                                                                 BUILT_IN FUNCTIONS=",z[13])
                        print("                                                                 ENVIRONMENTAL FEATURES=",z[14])
                        print("                                                                 VARIANT DETAILS=",z[15])
                        print("                                                                 PACKAGING CONTENTS=",z[16])
                        book=int(input("                                                                 DO YOU WANT TO BOOK THIS ITEM\n                                                                 PRESS 1 FOR YES\n                                                                 PRESS 2 FOR NO:"))
                        print()
                        if(book==1):
                            ui=0
                            while ui==0:
                                try:
                                    name=input("                                                                 ENTER YOUR NAME:")
                                    print()
                                    email=input("                                                                 ENTER YOUR E-MAIL ID:")
                                    print()
                                    pas=input("                                                                 ENTER YOUR EMAIL ID PASSWORD:")
                                    print()
                                    pno=input("                                                                 ENTER YOUR PHONE NUMBER:")
                                    print()
                                    add=input("                                                                 ENTER YOUR ADDRESS:")
                                    print()
                                    break
                                except:
                                    print()
                                    print("                                                                 SOME ERROR HAS OCCURED!!!PLEASE ENTER AGAIN")
                                    print()
                                    continue
                            op=strftime("%Y-%m-%d", gmtime())
                            modelname=z[0]
                            t=(name, email, pas, modelname, pno, add, op)
                            str=("INSERT INTO BOOKING(Name, E_Mail, Passwd, Model_Name, Pno, Address, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)")
                            c.execute(str,t)
                            f.commit()
                            print("                                                                 YOUR ORDER HAS BEEN BOOKED")
                            print()
                            drt="SELECT * FROM BOOKING WHERE E_Mail=%s"
                            c.execute(drt,(email,))
                            r=c.fetchall()
                            for z in r:
                                print()
                                print("                                            █▄█ █▀█ █░█ █▀█   █▀█ █▀█ █▀▄ █▀▀ █▀█")
                                print("                     -----------------------░█░ █▄█ █▄█ █▀▄   █▄█ █▀▄ █▄▀ ██▄ █▀▄----------------------------")
                                print("                    |                                                                                               ")
                                print("                    |                             NAME :",z[0],"                                                    ")
                                print("                    |                             EMAIL :",z[1],"                                                   ")
                                print("                    |                             PASSWORD:",z[2],"                                                 ")
                                print("                    |                             MODEL NAME:",z[3],"                                               ")
                                print("                    |                             PHONE NUMBER:",z[4],"                                             ")
                                print("                    |                             ADDRESS :",z[5],"                                                 ")
                                print("                    |                             DATE OF ORDER:",z[6],"                                            ")
                                print("                    |-----------------------------------------------------------------------------------------------")
                            print("                                                                 1. YOU WILL RECEIVE YOUR ORDER IN 3 WORKING DAYS\n                                                                 2. YOU WILL HAVE TO PAY CASH ON DELIVERY\n                                                                 3. YOU CAN CANCEL YOUR ORDER ANYTINE BEFORE DELIVRY")
                            print()
                    cont()
            
        if(m=="3"):
            #CHECKING AN ITEM FROM HEADPHONES
            f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
            c=f.cursor()
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM HEADPHONES")
            r=c.fetchall()
            for z in r:
                print("                                                                 --------------------------")
                print("                                                                 MODEL NAME=",z[0])
                print("                                                                 BRAND NAME=",z[1])
                print("                                                                 PRICE=Rs",z[2])
                print("                                                                 --------------------------")
            km=input("                                                                 ENTER THE MODEL NAME OF HEADPHONES ABOUT WHICH YOU WANT TO KNOW MORE:")
            print()
            str2nd="SELECT * FROM HEADPHONES WHERE Model_Name=%s"
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM HEADPHONES")
            r=c.fetchall()
            for z in r:
                if km in z:
                    c.execute(str2nd,(km,))
                    r=c.fetchall()
                    for z in r:
                        print("                                                                 --------------------------")
                        print("                                                                 MODEL NAME=",z[0])
                        print("                                                                 BRAND NAME=",z[1])
                        print("                                                                 WIRED OR WIRELESS=",z[2])
                        print("                                                                 COLOUR=",z[3])
                        print("                                                                 PRICE=Rs",z[4])
                        print("                                                                 PLAY TIME=",z[5],"HOURS")
                        print("                                                                 BLUETOOTH VERSION=v",z[6])
                        print("                                                                 PACKAGING CONTENT=",z[7])
                        print("                                                                 --------------------------")
                        book=int(input("                                                                 DO YOU WANT TO BOOK THIS ITEM\n                                                                 PRESS 1 FOR YES\n                                                                 PRESS 2 FOR NO:"))
                        print()
                        if(book==1):
                            ui=0
                            while ui==0:
                                try:
                                    name=input("                                                                 ENTER YOUR NAME:")
                                    print()
                                    email=input("                                                                 ENTER YOUR E-MAIL ID:")
                                    print()
                                    pas=input("                                                                 ENTER YOUR EMAIL ID PASSWORD:")
                                    print()
                                    pno=input("                                                                 ENTER YOUR PHONE NUMBER:")
                                    print()
                                    add=input("                                                                 ENTER YOUR ADDRESS:")
                                    print()
                                    break
                                except:
                                    print()
                                    print("                                                                 SOME ERROR HAS OCCURED!!!PLEASE ENTER AGAIN")
                                    print()
                                    continue
                                
                            op=strftime("%Y-%m-%d", gmtime())
                            modelname=z[0]
                            t=(name, email, pas, modelname, pno, add, op)
                            str=("INSERT INTO BOOKING(Name, E_Mail, Passwd, Model_Name, Pno, Address, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)")
                            c.execute(str,t)
                            f.commit()
                            print("                                                                 YOUR ORDER HAS BEEN BOOKED")
                            drt="SELECT * FROM BOOKING WHERE E_Mail=%s"
                            c.execute(drt,(email,))
                            r=c.fetchall()
                            for z in r:
                                print()
                                print("                                            █▄█ █▀█ █░█ █▀█   █▀█ █▀█ █▀▄ █▀▀ █▀█")
                                print("                     -----------------------░█░ █▄█ █▄█ █▀▄   █▄█ █▀▄ █▄▀ ██▄ █▀▄----------------------------")
                                print("                    |                                                                                               ")
                                print("                    |                             NAME :",z[0],"                                                    ")
                                print("                    |                             EMAIL :",z[1],"                                                   ")
                                print("                    |                             PASSWORD:",z[2],"                                                 ")
                                print("                    |                             MODEL NAME:",z[3],"                                               ")
                                print("                    |                             PHONE NUMBER:",z[4],"                                             ")
                                print("                    |                             ADDRESS :",z[5],"                                                 ")
                                print("                    |                             DATE OF ORDER:",z[6],"                                            ")
                                print("                    |-----------------------------------------------------------------------------------------------")
                            print("                                                                 1. YOU WILL RECEIVE YOUR ORDER IN 3 WORKING DAYS\n                                                                 2. YOU WILL HAVE TO PAY CASH ON DELIVERY\n                                                                 3. YOU CAN CANCEL YOUR ORDER ANYTINE BEFORE DELIVRY")
                            print()
                    cont()
            
        elif(m=="4"):
            #CHECKING AN ITEM FROM EARPHONES
            f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
            c=f.cursor()
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM EARPHONES")
            r=c.fetchall()
            for z in r:
                print("                                                                 --------------------------")
                print("                                                                 MODEL NAME=",z[0])
                print("                                                                 BRAND NAME=",z[1])
                print("                                                                 PRICE=Rs",z[2])
                print("                                                                 --------------------------")
            km=input("                                                                 ENTER THE MODEL NAME OF EARPHONES ABOUT WHICH YOU WANT TO KNOW MORE:")
            print()
            str2nd="SELECT * FROM EARPHONES WHERE Model_Name=%s"
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM EARPHONES")
            r=c.fetchall()
            for z in r:
                if km in z:
                    c.execute(str2nd,(km,))
                    r=c.fetchall()
                    for z in r:
                        print("                                                                 --------------------------")
                        print("                                                                 MODEL NAME=",z[0])
                        print("                                                                 BRAND NAME=",z[1])
                        print("                                                                 WIRED OR WIRELESS=",z[2])
                        print("                                                                 COLOUR=",z[3])
                        print("                                                                 PRICE=Rs",z[4])
                        print("                                                                 PLAY TIME=",z[5],"HOURS")
                        print("                                                                 BLUETOOTH VERSION=v",z[6])
                        print("                                                                 PACKAGING CONTENT=",z[7])
                        print("                                                                 --------------------------")
                        book=int(input("                                                                 DO YOU WANT TO BOOK THIS ITEM\n                                                                 PRESS 1 FOR YES\n                                                                 PRESS 2 FOR NO:"))
                        print()
                        if(book==1):
                            ui=0
                            while ui==0:
                                try:
                                    name=input("                                                                 ENTER YOUR NAME:")
                                    print()
                                    email=input("                                                                 ENTER YOUR E-MAIL ID:")
                                    print()
                                    pas=input("                                                                 ENTER YOUR EMIAL ID PASSWORD:")
                                    print()
                                    pno=input("                                                                 ENTER YOUR PHONE NUMBER:")
                                    print()
                                    add=input("                                                                 ENTER YOUR ADDRESS:")
                                    print()
                                    break
                                except:
                                    print()
                                    print("                                                                 SOME ERROR HAS OCCURED!!!PLEASE ENTER AGAIN")
                                    print()
                                    continue
                            op=strftime("%Y-%m-%d", gmtime())
                            modelname=z[0]
                            t=(name, email, pas, modelname, pno, add, op)
                            str=("INSERT INTO BOOKING(Name, E_Mail, Passwd, Model_Name, Pno, Address, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)")
                            c.execute(str,t)
                            f.commit()
                            print("                                                                 YOUR ORDER HAS BEEN BOOKED")
                            print()
                            drt="SELECT * FROM BOOKING WHERE E_Mail=%s"
                            c.execute(drt,(email,))
                            r=c.fetchall()
                            for z in r:
                                print()
                                print("                                            █▄█ █▀█ █░█ █▀█   █▀█ █▀█ █▀▄ █▀▀ █▀█")
                                print("                     -----------------------░█░ █▄█ █▄█ █▀▄   █▄█ █▀▄ █▄▀ ██▄ █▀▄----------------------------")
                                print("                    |                                                                                               ")
                                print("                    |                             NAME :",z[0],"                                                    ")
                                print("                    |                             EMAIL :",z[1],"                                                   ")
                                print("                    |                             PASSWORD:",z[2],"                                                 ")
                                print("                    |                             MODEL NAME:",z[3],"                                               ")
                                print("                    |                             PHONE NUMBER:",z[4],"                                             ")
                                print("                    |                             ADDRESS :",z[5],"                                                 ")
                                print("                    |                             DATE OF ORDER:",z[6],"                                            ")
                                print("                    |-----------------------------------------------------------------------------------------------")
                            print("                                                                 1. YOU WILL RECEIVE YOUR ORDER IN 3 WORKING DAYS\n                                                                 2. YOU WILL HAVE TO PAY CASH ON DELIVERY\n                                                                 3. YOU CAN CANCEL YOUR ORDER ANYTINE BEFORE DELIVRY")
                            print()
                    cont()
        elif(m=="5"):
            #CHECKING AN ITEM FROM SMARTWATCH
            f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
            c=f.cursor()
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM SMARTWATCH")
            r=c.fetchall()
            for z in r:
                print("                                                                 --------------------------")
                print("                                                                 MODEL NAME=",z[0])
                print("                                                                 BRAND NAME=",z[1])
                print("                                                                 PRICE=Rs",z[2])
                print("                                                                 --------------------------")
            km=input("                                                                 ENTER THE MODEL NAME OF SMARTWATCH ABOUT WHICH YOU WANT TO KNOW MORE:")
            print()
            str2nd="SELECT * FROM SMARTWATCH WHERE Model_Name=%s"
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM SMARTWATCH")
            r=c.fetchall()
            for z in r:
                if km in z:
                    c.execute(str2nd,(km,))
                    r=c.fetchall()
                    for z in r:
                        print("                                                                 --------------------------")
                        print("                                                                 MODEL NAME=",z[0])
                        print("                                                                 BRAND NAME=",z[1])
                        print("                                                                 PRICE=Rs",z[2])
                        print("                                                                 OPERATING SYSTEM=",z[3])
                        print("                                                                 BLUETOOTH VERSION=v",z[4])
                        print("                                                                 MAIN DISPLAY SIZE=",z[5],"Inches")
                        print("                                                                 DISPLAY TECHNOLOGY=",z[6])
                        print("                                                                 PROCESSOR(CPU SPEED)=",z[7],"gHz")
                        print("                                                                 CONNECTIVITY=",z[8])
                        print("                                                                 RAM=",z[9],"GB")
                        print("                                                                 ROM=",z[10],"GB")
                        print("                                                                 SENSORS=",z[11])
                        print("                                                                 NETWORK=",z[12])
                        print("                                                                 BATTERY CAPACITY=",z[13],"mAh")
                        print("                                                                 COLOUR=",z[14])
                        print("                                                                 PACKAGING CONTENT=",z[15])
                        print("                                                                 --------------------------")
                        book=int(input("                                                                 DO YOU WANT TO BOOK THIS ITEM\n                                                                 PRESS 1 FOR YES\n                                                                 PRESS 2 FOR NO:"))
                        print()
                        if(book==1):
                            ui=0
                            while ui==0:
                                try:
                                    name=input("                                                                 ENTER YOUR NAME:")
                                    print()
                                    email=input("                                                                 ENTER YOUR E-MAIL ID:")
                                    print()
                                    pas=input("                                                                 ENTER YOUR EMAIL ID PASSWORD:")
                                    print()
                                    pno=input("                                                                 ENTER YOUR PHONE NUMBER:")
                                    print()
                                    add=input("                                                                 ENTER YOUR ADDRESS:")
                                    print()
                                    break
                                except:
                                    print()
                                    print("                                                                 SOME ERROR HAS OCCURED!!!PLEASE ENTER AGAIN")
                                    print()
                                    continue
                            op=strftime("%Y-%m-%d", gmtime())
                            modelname=z[0]
                            t=(name, email, pas, modelname, pno, add, op)
                            str=("INSERT INTO BOOKING(Name, E_Mail, Passwd, Model_Name, Pno, Address, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)")
                            c.execute(str,t)
                            f.commit()
                            print("                                                                 YOUR ORDER HAS BEEN BOOKED")
                            print()
                            drt="SELECT * FROM BOOKING WHERE E_Mail=%s"
                            c.execute(drt,(email,))
                            r=c.fetchall()
                            for z in r:
                                print()
                                print("                                            █▄█ █▀█ █░█ █▀█   █▀█ █▀█ █▀▄ █▀▀ █▀█")
                                print("                     -----------------------░█░ █▄█ █▄█ █▀▄   █▄█ █▀▄ █▄▀ ██▄ █▀▄----------------------------")
                                print("                    |                                                                                               ")
                                print("                    |                             NAME :",z[0],"                                                    ")
                                print("                    |                             EMAIL :",z[1],"                                                   ")
                                print("                    |                             PASSWORD:",z[2],"                                                 ")
                                print("                    |                             MODEL NAME:",z[3],"                                               ")
                                print("                    |                             PHONE NUMBER:",z[4],"                                             ")
                                print("                    |                             ADDRESS :",z[5],"                                                 ")
                                print("                    |                             DATE OF ORDER:",z[6],"                                            ")
                                print("                    |-----------------------------------------------------------------------------------------------")
                            print("                                                                 1. YOU WILL RECEIVE YOUR ORDER IN 3 WORKING DAYS\n                                                                 2. YOU WILL HAVE TO PAY CASH ON DELIVERY\n                                                                 3. YOU CAN CANCEL YOUR ORDER ANYTINE BEFORE DELIVRY")
                            print()
                    cont()
                    
        elif(m=="6"):
            #CHECKING AN ITEM FROM TABLETS
            f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
            c=f.cursor()
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM TABLETS")
            r=c.fetchall()
            for z in r:
                print("                                                                 --------------------------")
                print("                                                                 MODEL NAME=",z[0])
                print("                                                                 BRAND NAME=",z[1])
                print("                                                                 PRICE=Rs",z[2])
                print("                                                                 --------------------------")
            km=input("                                                                 ENTER THE MODEL NAME OF TABLETS ABOUT WHICH YOU WANT TO KNOW MORE:")
            print()
            str2nd="SELECT * FROM TABLETS WHERE Model_Name=%s"
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM TABLETS")
            r=c.fetchall()
            for z in r:
                if km in z:
                    c.execute(str2nd,(km,))
                    r=c.fetchall()
                    for z in r:
                        print("                                                                 --------------------------")
                        print("                                                                 MODEL NAME=",z[0])
                        print("                                                                 BRAND NAME=",z[1])
                        print("                                                                 PRICE=Rs",z[2])
                        print("                                                                 CPU SPEED=",z[3],"Ghz")
                        print("                                                                 DISPLAY_SIZE=",z[4],"Inches")
                        print("                                                                 DISPLAY TECHNOLOGY=",z[5])
                        print("                                                                 SMART PEN SUPPORT=",z[6])
                        print("                                                                 RAM=",z[7],"GB")
                        print("                                                                 ROM=",z[8],"GB")
                        print("                                                                 FRONT CAMERA=",z[9],"MP")
                        print("                                                                 REAR CAMERA=",z[10],"MP")
                        print("                                                                 BLUETOOTH VERSION=v",z[11])
                        print("                                                                 OPERATING SYSTEM=ANDROID ",z[12])
                        print("                                                                 BATTERY=",z[13],"mAh")
                        print("                                                                 VARIANT COLOUR=",z[14])
                        print("                                                                 CONNECTIVITY DETAILS=",z[15])
                        print("                                                                 NO. OF SIM=",z[16])
                        print("                                                                 NETWORK/BEARER=",z[17])
                        print("                                                                 MICRO OR NANO SIM=",z[18])
                        print("                                                                 PACKAGING CONTENT=",z[19])
                        print("                                                                 --------------------------")
                        book=int(input("                                                                 DO YOU WANT TO BOOK THIS ITEM\n                                                                 PRESS 1 FOR YES\n                                                                 PRESS 2 FOR NO:"))
                        if(book==1):
                            ui=0
                            while ui==0:
                                try:
                                    name=input("                                                                 ENTER YOUR NAME:")
                                    print()
                                    email=input("                                                                 ENTER YOUR E-MAIL ID:")
                                    print()
                                    pas=input("                                                                 ENTER YOUR EMAIL ID PASSWORD:")
                                    print()
                                    pno=input("                                                                 ENTER YOUR PHONE NUMBER:")
                                    print()
                                    add=input("                                                                 ENTER YOUR ADDRESS:")
                                    print()
                                    break
                                except:
                                    print()
                                    print("                                                                 SOME ERROR HAS OCCURED!!!PLEASE ENTER AGAIN")
                                    print()
                                    continue
                            op=strftime("%Y-%m-%d", gmtime())
                            modelname=z[0]
                            t=(name, email, pas, modelname, pno, add, op)
                            str=("INSERT INTO BOOKING(Name, E_Mail, Passwd, Model_Name, Pno, Address, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)")
                            c.execute(str,t)
                            f.commit()
                            print("                                                                 YOUR ORDER HAS BEEN BOOKED")
                            print()
                            drt="SELECT * FROM BOOKING WHERE E_Mail=%s"
                            c.execute(drt,(email,))
                            r=c.fetchall()
                            for z in r:
                                print()
                                print("                                            █▄█ █▀█ █░█ █▀█   █▀█ █▀█ █▀▄ █▀▀ █▀█")
                                print("                     -----------------------░█░ █▄█ █▄█ █▀▄   █▄█ █▀▄ █▄▀ ██▄ █▀▄----------------------------")
                                print("                    |                                                                                               ")
                                print("                    |                             NAME :",z[0],"                                                    ")
                                print("                    |                             EMAIL :",z[1],"                                                   ")
                                print("                    |                             PASSWORD:",z[2],"                                                 ")
                                print("                    |                             MODEL NAME:",z[3],"                                               ")
                                print("                    |                             PHONE NUMBER:",z[4],"                                             ")
                                print("                    |                             ADDRESS :",z[5],"                                                 ")
                                print("                    |                             DATE OF ORDER:",z[6],"                                            ")
                                print("                    |-----------------------------------------------------------------------------------------------")
                            print("                                                                 1. YOU WILL RECEIVE YOUR ORDER IN 3 WORKING DAYS\n                                                                 2. YOU WILL HAVE TO PAY CASH ON DELIVERY\n                                                                 3. YOU CAN CANCEL YOUR ORDER ANYTINE BEFORE DELIVRY")
                            print()
                    cont()




    elif(x==3):
        #BOOKING CANCELLATION
        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
        c=f.cursor()
        er=0
        while er==0:
            try:
                email=input("                                                                 ENTER YOUR EMAIL ID:")
                print()
                pas=input("                                                                 ENTER YOUR EMAIL ID PASSWORD:")
                print()
                pno=input("                                                                 ENTER YOUR PHONE NUMBER:")
                print()
                break
            except:
                print()
                print("                                                                 SOME ERROR HAS OCCURED!!!PLEASE ENTER AGAIN")
                print()
                continue
        str1="SELECT * FROM BOOKING WHERE E_Mail=%s"
        c.execute(str1,(email,))
        r=c.fetchall()
        tp=1
        for z in r:
            print("                                                                 --------------------------")
            print("                                                                 Name=",z[0])
            print("                                                                 E Mail=",z[1])
            print("                                                                 Password=",z[2])
            print("                                                                 Model Name=",z[3])
            print("                                                                 Phone Number=",z[4])
            print("                                                                 Address=",z[5])
            print("                                                                 --------------------------")
            tp=0
        if(tp==0):

            d=input("                                                                 DO YOU WANT TO DELETE YOUR BOOKING!!!\n                                                                 PRESS 1 FOR YES\n                                                                 PRESS 2 FOR NO:")
            print()
            if(d=="1"):
                print("                                                                 DELETING!!!")
                print()
                ste="DELETE FROM BOOKING WHERE E_Mail=%s"
                if email in z:
                    c.execute(ste,(email,))
                    print("                                                                 DONE!!!")
                    print()
                    f.commit()
                    cont()
                else:
                    print("                                                                 SORRY!!!MAIL ID NOT FOUND...")
                    print()
            elif(d=="2"):
                print("                                                                 OK")
                print()
            else:
                print("                                                                 OK")
                print()
        else:
            print("                                                                 SORRY!!! MAIL ID NOT FOUND")
            print()
        cont()
    elif(x==4):
        #REVIEW
        f=mysql.connector.connect(host="localhost",user=x12,passwd=x23,database="eshop")
        c=f.cursor()
        rev=input("                                                                 PRESS 1 TO WRITE A REVIEW\n                                                                 PRESS 2 TO READ REVIEWS:")
        print()
        if(rev=="1"):
            #ENTERING A REVIEW
            ty=0
            while ty==0:
                try:
                    nam=input("                                                                 ENTER YOUR NAME:")
                    print()
                    email=input("                                                                 ENTER YOUR E-MAIL ID:")
                    print()
                    star=int(input("                                                                 ENTER STAR RATING BY 5:"))
                    print()
                    rev=input("                                                                 ENTER YOUR REVIEW ABOUT THIS PROGRAM:")
                    print()
                    break
                except ValueError:
                    print()
                    print("                                                                 STAR RATING CAN BE INTEGER ONLY!!!PLEASE ENTER AGAIN")
                    print()
                    continue
                except:
                    print()
                    print("                                                                 SOME ERROR HAS OCCURED!!! PLEASE ENTER AGAIN")
                    print()
                    continue
            print("                                                                 REGISTERING....")
            print()
            t=(nam,email,star,rev)
            str1="""INSERT INTO REVIEW(Name, E_Mail, Star_Rating, Review) VALUES(%s,%s,%s,%s)"""
            c.execute(str1,t)
            f.commit()
            print("                                                                 REGISTERED SUCCESSFULLY!!!")
            print()
            cont()
        elif(rev=="2"):
            #DISPLAYING A REVIEW
            c.execute("SELECT * FROM REVIEW")
            r=c.fetchall()
            for z in r:
                print("                                                                 --------------------------")
                print("                                                                 NAME=",z[0])
                print("                                                                 E-MAIL=",z[1])
                print("                                                                 STAR RATNG=",z[2])
                print("                                                                 REVIEW=",z[3])
                print("                                                                 --------------------------")
            cont()
    elif(x==5):
        print("                                                                 GOOD BYE!!!")
        print()
        exit()
    else:
        print("                                                                 WRONG OPTION SELECTED PLEASE TRY AGAIN!!!")
        print()
        continue
            
            
            
