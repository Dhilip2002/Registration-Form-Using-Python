from email.headerregistry import Address
from tabnanny import check
from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")


#Heading
Label(root,text=" Registration Form",font="ar 15 bold").grid(row=0,column=3)

#Field Name
name=Label(root,text="Name")
MobileNo=Label(root,text="Mobile No")
Gender=Label(root,text="Gender")
Address=Label(root,text="Address")
PaymentMode=Label(root,text="Payment Mode")

#Packing Fields
name.grid(row=1,column=2)
MobileNo.grid(row=2,column=2)
Gender.grid(row=3,column=2)
Address.grid(row=4,column=2)
PaymentMode.grid(row=5,column=2)

#Variable for Storing Data
namevalue=StringVar
MobileNovalue=StringVar
Gendervalue=StringVar
Addressvalue=StringVar
PaymentModevalue=StringVar
checkvalue=IntVar

#Creating Entry Field
nameentry=Entry(root, textvariable=namevalue)
MobileNoentry=Entry(root, textvariable=MobileNovalue)
Genderentry=Entry(root, textvariable=Gendervalue)
Addressentry=Entry(root, textvariable=Addressvalue)
PaymentModeentry=Entry(root, textvariable=PaymentModevalue)

#Packing Entry Field 
nameentry.grid(row=1,column=3)
MobileNoentry.grid(row=2,column=3)
Genderentry.grid(row=3,column=3)
Addressentry.grid(row=4,column=3)
PaymentModeentry.grid(row=5,column=3)

#Creating Checkbox
checkbtn=Checkbutton(text="Remember Me",variable=checkvalue)
checkbtn.grid(row=6,column=3)

#Submit Button
Button (text="Submit", command=getvals).grid(row=7,column=3)





root.mainloop()