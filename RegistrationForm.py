from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from tkinter import ttk

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345',
    database='stu_form'
)
mycursor = mydb.cursor()

root = Tk()
root.title('Python code!')
root.geometry('450x485')

global Name
global Rollno
global Contact
global Email
global Gender
global State
global City
global message

Name = StringVar()
Rollno = IntVar()
Contact = IntVar()
Email = StringVar()
Gender = IntVar()
State = StringVar()
City = StringVar()
message = StringVar()
# Label
Label(root, text='Name * ').place(x=100, y=50)
Label(root, text='Roll no *').place(x=100, y=100)
Label(root, text='Contact * ').place(x=100, y=150)
Label(root, text='Email * ').place(x=100, y=200)
Label(root, text='Gender * ').place(x=100, y=250)
Label(root, text=' State * ').place(x=100, y=300)
Label(root, text='City * ').place(x=100, y=350)

# Enter
# Name = Entry(root,).place(x=200, y=50)
Name = Entry(root, textvariable=Name)
Name.place(x=200, y=50)
Rollno = Entry(root, textvariable=Rollno)
Rollno.place(x=200, y=100)
Contact = Entry(root, textvariable=Contact)
Contact.place(x=200, y=150)
Email = Entry(root, textvariable=Email)
Email.place(x=200, y=200)

# Radiobutton

r1 = Radiobutton(root, text='Male', variable=Gender, value=1).place(x=200, y=250)
r2 = Radiobutton(root, text='Female', variable=Gender, value=2).place(x=270, y=250)

# 1st dropdown button (States)
data = (' Madhya Pradesh',
        ' Maharashtra',
        ' Bihar',
        ' Punjab',
        ' Gujrat',
        ' Rajsthan',)
cb = Combobox(root, textvariable=State, values=data).place(x=200, y=300)

# 2nd dropdown button (City)
data1 = (' Mumbai',
         ' Bhopal',
         ' Patna',
         ' Indore',
         ' Nagpur',
         ' Motihari',
         ' Pune',
         ' Gwalior',
         ' Jabalpur',
         ' Jalandhar')
cb1 = Combobox(root, textvariable=City, values=data1).place(x=200, y=350)


# Label(root,width='100', text='Please enter detail below', bg='orange', fg='white').pack()

def Register():
    nn = Name.get()
    rr = Rollno.get()
    cc = Contact.get()
    ee = Email.get()
    gg = Gender.get()
    ss = State.get()
    ci = City.get()

    select = "INSERT INTO all_data (name_stu,roll_no,contact_stu,email,gender,state,city) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    mycursor.execute("SELECT  * FROM all_data WHERE roll_no ={}".format(rr))
    myresult = mycursor.fetchall()
    row = ''
    for row in myresult:
        print(row)
        print('break hogi')

    if not row in myresult:
        if nn == '' or rr == '' or cc == '' or ee == '' or ss == '' or ci == '':
            message.set("Fill the empty place")
            print("fill the empty field!!!")

            if gg == 1:
                data = (nn, rr, cc, ee, "Male", ss, ci)
                mycursor.execute(select, data)

            if gg == 2:
                data = (nn, rr, cc, ee, "Female", ss, ci)
                mycursor.execute(select, data)

                mydb.commit()
                message.set("Stored successfully")
            else:
                print('fill gender option   ')

    else:
        message.set("This roll no. is already exits")

    # Name.set('')
    Name.delete(0, END)
    Rollno.delete(0, END)
    Contact.delete(0, END)
    Email.delete(0, END)
    Gender.set('null')
    State.set('')
    City.set('')


Label(root, text="", textvariable=message).place(x=160, y=385)

btn = Button(root, text='Register', command=Register).place(x=190, y=420)  # fg='red'

root.mainloop()
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from tkinter import ttk

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345',
    database='stu_form'
)
mycursor = mydb.cursor()

root = Tk()
root.title('Python code!')
root.geometry('450x485')

global Name
global Rollno
global Contact
global Email
global Gender
global State
global City
global message

Name = StringVar()
Rollno = IntVar()
Contact = IntVar()
Email = StringVar()
Gender = IntVar()
State = StringVar()
City = StringVar()
message = StringVar()
# Label
Label(root, text='Name * ').place(x=100, y=50)
Label(root, text='Roll no *').place(x=100, y=100)
Label(root, text='Contact * ').place(x=100, y=150)
Label(root, text='Email * ').place(x=100, y=200)
Label(root, text='Gender * ').place(x=100, y=250)
Label(root, text=' State * ').place(x=100, y=300)
Label(root, text='City * ').place(x=100, y=350)

# Enter
# Name = Entry(root,).place(x=200, y=50)
Name = Entry(root, textvariable=Name)
Name.place(x=200, y=50)
Rollno = Entry(root, textvariable=Rollno)
Rollno.place(x=200, y=100)
Contact = Entry(root, textvariable=Contact)
Contact.place(x=200, y=150)
Email = Entry(root, textvariable=Email)
Email.place(x=200, y=200)

# Radiobutton

r1 = Radiobutton(root, text='Male', variable=Gender, value=1).place(x=200, y=250)
r2 = Radiobutton(root, text='Female', variable=Gender, value=2).place(x=270, y=250)

# 1st dropdown button (States)
data = (' Madhya Pradesh',
        ' Maharashtra',
        ' Bihar',
        ' Punjab',
        ' Gujrat',
        ' Rajsthan',)
cb = Combobox(root, textvariable=State, values=data).place(x=200, y=300)

# 2nd dropdown button (City)
data1 = (' Mumbai',
         ' Bhopal',
         ' Patna',
         ' Indore',
         ' Nagpur',
         ' Motihari',
         ' Pune',
         ' Gwalior',
         ' Jabalpur',
         ' Jalandhar')
cb1 = Combobox(root, textvariable=City, values=data1).place(x=200, y=350)


# Label(root,width='100', text='Please enter detail below', bg='orange', fg='white').pack()

def Register():
    nn = Name.get()
    rr = Rollno.get()
    cc = Contact.get()
    ee = Email.get()
    gg = Gender.get()
    ss = State.get()
    ci = City.get()

    select = "INSERT INTO all_data (name_stu,roll_no,contact_stu,email,gender,state,city) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    mycursor.execute("SELECT  * FROM all_data WHERE roll_no ={}".format(rr))
    myresult = mycursor.fetchall()
    row = ''
    for row in myresult:
        print(row)
        print('break hogi')

    if not row in myresult:
        if nn == '' or rr == '' or cc == '' or ee == '' or ss == '' or ci == '':
            message.set("Fill the empty place")
            print("fill the empty field!!!")

            if gg == 1:
                data = (nn, rr, cc, ee, "Male", ss, ci)
                mycursor.execute(select, data)

            if gg == 2:
                data = (nn, rr, cc, ee, "Female", ss, ci)
                mycursor.execute(select, data)

                mydb.commit()
                message.set("Stored successfully")
            else:
                print('fill gender option   ')

    else:
        message.set("This roll no. is already exits")

    # Name.set('')
    Name.delete(0, END)
    Rollno.delete(0, END)
    Contact.delete(0, END)
    Email.delete(0, END)
    Gender.set('null')
    State.set('')
    City.set('')


Label(root, text="", textvariable=message).place(x=160, y=385)

btn = Button(root, text='Register', command=Register).place(x=190, y=420)  # fg='red'

root.mainloop()
