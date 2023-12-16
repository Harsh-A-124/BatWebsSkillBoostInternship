initial_name=input("Enter Name:")
designation=input("Enter Designation:")
location=input("Enter Location:")
m_no=int(input("Enter Mobile No.:"))


#Importing required modules
import tkinter as tk
from tabulate import tabulate
from PIL import Image,ImageTk
from tkinter import messagebox
import threading

window=tk.Tk()
window.title("IN STOCK IMAGES")
window.geometry("960x540")
window.attributes("-topmost", True)
frame=tk.Frame(master=window,bd=0)
frame.place(x=0,y=0,relwidth=1,relheight=1)
panel=tk.Label(master=frame)
panel.place(x=0,y=0,relwidth=1,relheight=1)

#Image list
images=["audi r8.jpg","bentayga.jpg","bmw 520d.jpg","bmw s1000rr.jpg","bmw x6.jpg","ford_mustang.jpg","gwagon.jpg","hayabusa.jpg","jaguar xjl.jpg","kaasaki ninja.jpg","porsche 911.jpg","q7.jpg","urus.jpg","volvo xc90.jpg"]

#Image format conversion
i=1
for image in images:
    FTimgpath = image
    FTimg = Image.open(FTimgpath)
    FTimg = FTimg.resize((960,540))
    FTimg = ImageTk.PhotoImage(FTimg)
    globals()["image" + str(i)] = FTimg
    i += 1
j=1

#Slideshow function
def slides():
    global j
    if j in range(0,14):
        j+=1
        panel["image"]= globals()["image"+str(j)]
    else:
        j=0
        j+=1
        panel["image"]= globals()["image"+str(j)]
    window.after(2000,slides)

#Thread creation
thread1=threading.Thread(target=slides)
thread1.daemon = 1
thread1.start()

window.after(28000,lambda:window.destroy())
window.mainloop()

#MySQL connection
import mysql.connector as sqltor 
mycon=sqltor.connect(host="localhost",user="root",passwd="")
if mycon.is_connected():
    print("Connection Successful")
else:
    print("Connection Failed")
    exit()

#Database creation
cursor=mycon.cursor()
cursor.execute("Create Database IF NOT EXISTS DEMO")
mycon.commit()
mycon.close()

#Connecting to database
mycon=sqltor.connect(host="localhost",user="root",passwd="",database="DEMO")
if mycon.is_connected():
    print("Connection to DB Successful")
else:
    print("Connection to DB Failed")
    exit()

#Stock Table
cursor=mycon.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS IN_STOCK(SR_NO int,NAME varchar(20),MODEL varchar(20),COMPANY varchar(20),QUANTITY int,PRICE int)")
print("Table created successfully")

#Initial data for demonstration
cursor.execute("SHOW TABLES LIKE 'IN_STOCK'")
data0=cursor.fetchall()
count0= cursor.rowcount
cursor.execute("SELECT * FROM IN_STOCK")
data1=cursor.fetchall()
count1=cursor.rowcount

if count0 == 1 and count1 == 0:
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(1,'G-WAGON','G-50AMG','MERCEDES',5,15000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(2,'MUSTANG','GT','FORD',3,5000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(3,'X6','M','BMW',7,7500000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(4,'XJ','L','JAGUAR',9,6000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(5,'R8','V8','AUDI',3,8000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(6,'911','TURBO','PORSCHE',5,5000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(7,'XC','90','VOLVO',2,4500000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(8,'URUS','SPORTZ','LAMBORGINI',3,30000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(9,'530D','LUXURY LINE','BMW',5,5000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(10,'BENTAYGA','V8','BENTLEY',2,18000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(11,'Q7','SUV','AUDI',4,5000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(12,'HAYABUSA','GSXR 1350','SUZUKI',4,1000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(13,'S1000','RR','BMW',2,2000000))
    cursor.execute("INSERT INTO IN_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(14,'NINJA','H2','KAWASAKI',3,5000000))
mycon.commit()
print("Stock Updated Successfully")

#Customer Details Table
cursor=mycon.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMER_DETAILS(SR_NO int,NAME varchar(20),ADDRESS varchar(100),OWNER int,M_NO bigint,NO_OF_CARS int)")
print("Table created successfully")

cursor.execute("SHOW TABLES LIKE 'CUSTOMER_DETAILS'")
data2=cursor.fetchall()
count2= cursor.rowcount
cursor.execute("SELECT * FROM CUSTOMER_DETAILS")
data3=cursor.fetchall()
count3=cursor.rowcount

if count2 == 1 and count3 == 0:
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(1,'PRANAY','10/5 VIMAL NAGAR RAJKOT ',1,4684635,1))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(2,'VIPUL','199 LAXMI NARAYAN DELHI ',2,68464664,2))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(3,'ROHIT','44 VILAS BHAVAN KANPUR',2,95153646,1))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(4,'DEVRAJ','78 KALAVAD ROAD RAIPUR',1,70006465,1))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(5,'YURAJ','12/3 JUHU BEACH MUMBAI',3,7065815,2))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(6,'MRIDUL','34/58 UNA HIMACHAL PRADESH',2,76546815,1))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(7,'PRASHIK','911 KOCHI KERALA',1,70654815,1))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(8,'PRIYANSH','14 MANDI HIMACHAL PRADESH',3,84500815,2))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(9,'HARSH','90 JAIPUR RAJASTHAN',1,6884765,1))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(10,'JAY','78 PERIYAR STREET CHENNAI',2,7448646,2))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(11,'TEJUS','31 GAUTAM BUDDHA NAGAR BHOPAL',3,76455865,2))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(12,'HARSH','32 AMRAVATI HYDRABAD',2,78486415,1))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(13,'JAYESH','99/2 AIRPORT ROAD CHANDIGARH',1,7458258015,2))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(14,'AKASH','10/89 SANTA STREET PUNE',1,79846815,1))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(15,'JAYRAJ','40 VISHNU VIHAR AGRA',2,7000815545,1))
    cursor.execute("INSERT INTO CUSTOMER_DETAILS(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS)\
                    values({},'{}','{}',{},'{}',{})".format(16,'CYRIL','45 STYLE STREET NAGPUR',2,70008148465,2))

cursor.execute("SELECT SR_NO FROM customer_details ORDER BY SR_NO DESC LIMIT 1;")
result0=cursor.fetchall()
for output0 in result0:
    for val0 in output0:
        srno0=val0
srno0+=1
cursor.execute("INSERT INTO customer_details(SR_NO,NAME,ADDRESS,OWNER,M_NO,NO_OF_CARS) Values(%d,'%s','%s',%d,'%s',%d)"%(srno0,initial_name,location,1,m_no,0))
mycon.commit()


#Ordered Stock Table
cursor=mycon.cursor() 
cursor.execute("CREATE TABLE IF NOT EXISTS ORDERED_STOCK(SR_NO int,NAME varchar(20),MODEL varchar(20),COMPANY varchar(20),QUANTITY int,PRICE int)")
print("Table created successfully")

cursor.execute("SHOW TABLES LIKE 'ORDERED_STOCK'")
data4=cursor.fetchall()
count4= cursor.rowcount
cursor.execute("SELECT * FROM ORDERED_STOCK")
data5=cursor.fetchall()
count5=cursor.rowcount

if count4 == 1 and count5 == 0:
    cursor.execute("INSERT INTO ORDERED_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(1,'G-WAGON','G-50AMG','MERCEDES',2,10000000))
    cursor.execute("INSERT INTO ORDERED_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(2,'HAYABUSA','GSXR 1350','SUZUKI',3,4000000))
    cursor.execute("INSERT INTO ORDERED_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(3,'MUSTANG','GT','FORD',5,2000000))
    cursor.execute("INSERT INTO ORDERED_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(4,'XJ','L','JAGUAR',5,5000000))
    cursor.execute("INSERT INTO ORDERED_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(5,'R8','V8','AUDI',2,7000000))
    cursor.execute("INSERT INTO ORDERED_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(6,'911','TURBO','PORSCHE',4,4000000))
    cursor.execute("INSERT INTO ORDERED_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(7,'Q7','SUV','AUDI',3,4000000))
    cursor.execute("INSERT INTO ORDERED_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(8,'S1000','RR','BMW',2,1500000))
    cursor.execute("INSERT INTO ORDERED_STOCK(SR_NO,NAME,MODEL,COMPANY,QUANTITY,PRICE)\
                           values({},'{}','{}','{}',{},{})".format(9,'NINJA','H2','KAWASAKI',3,4000000))
mycon.commit()
print("Stock Updated Successfully")

#Promo Codes Table
cursor=mycon.cursor() 
cursor.execute("CREATE TABLE IF NOT EXISTS PROMO_CODES(SR_NO int,CODE varchar(10),DISCOUNT int)")
print("Table created successfully")

cursor.execute("SHOW TABLES LIKE 'PROMO_CODES'")
data6=cursor.fetchall()
count6= cursor.rowcount
cursor.execute("SELECT * FROM PROMO_CODES")
data7=cursor.fetchall()
count7=cursor.rowcount

if count6 == 1 and count7 == 0:
    cursor.execute("INSERT INTO PROMO_CODES(SR_NO,CODE,DISCOUNT)\
                           values({},'{}',{})".format(1,'ASDQW12',10))
    cursor.execute("INSERT INTO PROMO_CODES(SR_NO,CODE,DISCOUNT)\
                           values({},'{}',{})".format(2,'ZXCV22',15))
    cursor.execute("INSERT INTO PROMO_CODES(SR_NO,CODE,DISCOUNT)\
                           values({},'{}',{})".format(3,'QWER11',30))
    cursor.execute("INSERT INTO PROMO_CODES(SR_NO,CODE,DISCOUNT)\
                           values({},'{}',{})".format(4,'ZDTHJ22',25))
    cursor.execute("INSERT INTO PROMO_CODES(SR_NO,CODE,DISCOUNT)\
                           values({},'{}',{})".format(5,'CVVBB33',40))
mycon.commit()
cursor=mycon.cursor()
print("Main Menu")
#Menu
Q=input("\nWould you like to use this program? ")
    
while Q == "Yes" or Q == "yes":
    print("\nList of Operations")
    print("1. View Stock")
    print("2. Buying Options")
    print("3. Promo Codes")
    print("4. View Customer Details")
    print("5. Exit")
    ch=int(input("Enter your choice(1-4) : "))
    if ch==1:
        print("Processing...")
        cursor.execute("SELECT * FROM IN_STOCK")
        stock=cursor.fetchall()
        print(tabulate(stock,headers=["Sr.No.","Name", "Model","Company","Quantity", "Price"]))
            
    elif ch==2:
        print("Processing...")
        company=input("Enter Name Of Company: ")
        cursor.execute("SELECT Name,Model,Quantity,Price FROM in_stock WHERE Company='%s'"%company)
        result1=cursor.fetchall()
        print(tabulate(result1,headers=["Name","Model","Quantity","Price"]))
        name=input("\nEnter Name of The Vehicle You Want To Purchase: ")
        model=input("Enter Model Name: ")
        cursor.execute("SELECT Quantity FROM in_stock WHERE Company = '%s' AND Name = '%s' AND Model = '%s'"%(company,name,model))
        qres=cursor.fetchall()
        for qout in qres:
            for qval in qout:
                quant=qval
        if quant == 0:
            print("OUT OF STOCK!")
            continue
        quantity=int(input("Enter Quantity: "))
        cursor.execute("SELECT Price FROM in_stock WHERE Company = '%s' AND Name = '%s' AND Model = '%s'"%(company,name,model))
        result2=cursor.fetchall()
        for value in result2:
            for val in value:
                result2_final=val
        final_cost0=result2_final*quantity
        print("Sub-Total: ",final_cost0)
        promoq=input("Do you want to enter a promo code? ")
        if promoq == "Yes" or promoq == "yes":
            promo=input("Enter Promo Code: ")
            cursor.execute("SELECT EXISTS(SELECT * FROM promo_codes WHERE CODE = '%s')"%promo)
            result_promo=cursor.fetchall()
            for promo_output in result_promo:
                for promo_val in promo_output:
                    promo_check = promo_val
            if promo_check == 1:
                cursor.execute("SELECT DISCOUNT FROM promo_codes WHERE CODE = '%s'"%promo)
                disc_result=cursor.fetchall()
                for disc_output in disc_result:
                    for disc_val in disc_output:
                        discount=disc_val
                discount= discount/100
                sub_final_cost=final_cost0*discount
                final_cost= final_cost0-sub_final_cost
                cursor.execute("DELETE FROM promo_codes WHERE CODE = '%s'"%promo)
            else:
                print("Invalid Promo Code")
                final_cost = final_cost0
        else:
            final_cost = final_cost0
        print("Final Amount To Be Paid: ",final_cost)
        cont=input("\nPress Enter To Continue")
        print("Order Successfully Placed!")
        cursor.execute("UPDATE customer_details SET NO_OF_CARS = NO_OF_CARS + %d WHERE Name = '%s'"%(quantity,initial_name))
        cursor.execute("UPDATE in_stock SET Quantity = Quantity - '%d' WHERE Company = '%s' AND Name = '%s' AND Model = '%s'"%(quantity,company,name,model))
        cursor.execute("SELECT EXISTS(SELECT Name,Model FROM ordered_stock WHERE Company = '%s' AND Name = '%s' AND Model = '%s')"%(company,name,model))
        result3=cursor.fetchall()
        for output in result3:
            for val1 in output:
                check=val1
        if check == 0:
            cursor.execute("SELECT SR_NO FROM ordered_stock ORDER BY SR_NO DESC LIMIT 1;")
            result4=cursor.fetchall()
            for output1 in result4:
                for val2 in output1:
                    srno=val2
            srno+=1
            cursor.execute("INSERT INTO ordered_stock(SR_NO,Name,Model,Company,Quantity,Price) Values(%d,'%s','%s','%s',%d,%d)"%(srno,name,model,company,quantity,final_cost))
        else:
            cursor.execute("UPDATE ordered_stock SET Quantity = Quantity + %d AND Price = Price + %d"%(quantity,final_cost))
        mycon.commit()
        cursor=mycon.cursor()

    elif ch == 3:
        print("Processing...")
        cursor.execute("SELECT * FROM PROMO_CODES")
        promo_code=cursor.fetchall()
        print(tabulate(promo_code,headers=["Sr.No.","Code", "Discount"]))

    elif ch == 4:
        print("Processing...")
        cursor.execute("SELECT * FROM CUSTOMER_DETAILS")
        customers=cursor.fetchall()
        print(tabulate(customers,headers=["Sr.No.","Name", "Location", "Owner", "Mo.No.", "NO.OF_CARS"]))

    elif ch == 5:
        if messagebox.askyesno("Exit", "Do You Really Wanna Exit The Program Now?"):
            if messagebox.showinfo(title="Thanks A Lot!", message="Thank You For Using My Program! I Hope You Enjoyed! Have A Good Day!"):
                mycon.commit()
                mycon.close()
                quit()

