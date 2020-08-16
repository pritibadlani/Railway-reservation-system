#Author: Priti Badlani
from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont
import time
import random
import sqlite3
global  x1,x2,x3,x4
import tkinter.ttk as ttk

global conn, cursor
conn = sqlite3.connect('Railway.db')
c = conn.cursor()

global LoginId,count
global Password
global Source
global Destination
global Date
global Name
global Age,Gender,IdProof
global variable,variable1,variable2,v2,var
global DepartureTime, TrainNumber, Number
root = Tk()
root.title("Railway reservation")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 400
height = 400
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)



w = 400
h = 400
canvas = Canvas(root, width=w, height=h)
canvas.config(bg='light blue')
canvas.pack()

my_image = PhotoImage(file='Train.gif')
my_img = canvas.create_image(0, 0, anchor=NW, image=my_image)

Label(root, text="INDIAN RAILWAYS",font=('Slab Serif',17),bg='Orange').place(x=100,y=150)
Label(root, text="LoginId",font=('Slab Serif',15),bg='green').place(x=60,y=200)
Label(root, text="Password",font=('Slab Serif',15), bg='green').place(x=60,y=240)

entry_1 = Entry(root, font=('Slab Serif',10))
entry_1.place(x=160,y=200,height=30)

entry_2 = Entry(root, font=('Slab Serif',10),show="*")
entry_2.place(x=160,y=240,height=30)

def printMsg():
    if((entry_1.get()=='priti' and entry_2.get()=='844') or (entry_1.get()=='jainam' and entry_2.get()=='844') or (entry_1.get()=='ayush' and entry_2.get()=='844') ):
        tkinter.messagebox.showinfo('login result', 'CONGRATULATIONS!! LOGIN SUCCESSFUL')
        createWindow()
    else:
        tkinter.messagebox.showinfo('login result', 'LOGIN FAILED!:( TRY AGAIN')

def createWindow():
    root.destroy()
    window = Tk()
    window.title("Login frame")
    customFont = tkFont.Font(family="Helvetica", size=14)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width = 410
    height = 400
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.resizable(0, 0)

    window.config(bg='purple')

    entry1 =Entry(window,justify='center',font=('Slab Serif',3))
    entry1.place(x=210,y=70)

    entry2 = Entry(window, justify='center',font=('Slab Serif', 3))
    entry2.place(x=210, y=115)

    entry3 = Entry(window, justify='center',font=('Slab Serif', 3))
    entry3.place(x=210, y=205)


    def fun_1(*args):
        entry1.insert(10,variable.get())
    def fun_2(*args):
        entry2.insert(10,variable1.get())
    def fun_3(*args):
        entry3.insert(10,variable2.get())

    variable = StringVar(window)
    choices = {'Howrah', 'Ajmer'}
    variable.set('Select')
    variable.trace("w", fun_1)
    popupMenu = OptionMenu(window, variable, *choices)
    popupMenu.place(x=210, y=70,width=100)
    popupMenu.config(font=('Slab Serif',15),bg="yellow")
    Label(window, text="Source",font=('Slab Serif',14), bg="cyan").place(x=110,y=70,width=80)

    variable1 = StringVar(window)
    trains = {'New Delhi','Chandigarh'}
    variable1.set('Select')
    variable1.trace("w", fun_2)

    popupMenu1 = OptionMenu(window, variable1, *trains)
    Label(window, text="Destination",font=('Slab Serif',15), bg="cyan").place(x=100,y=115,width=100)
    popupMenu1.config(font=('Slab Serif',14),bg="yellow")
    popupMenu1.place(x=210,y=115,width=130)

    variable2 = StringVar(window)
    classes = {'1A','2A','3A'}
    variable2.set('Select')
    variable2.trace("w", fun_3)

    popupMenu1 = OptionMenu(window, variable2, *classes)
    Label(window, text="class", font=('Slab Serif', 15), bg="cyan").place(x=100, y=205, width=100)
    popupMenu1.config(font=('Slab Serif', 14), bg="yellow")
    popupMenu1.place(x=210, y=205, width=130)

    Label(window,text="Date",font=('Slab Serif',15), bg="cyan").place(x=110,y=160,width=80)
    Date=StringVar()
    e1=Entry(window,textvariable=Date)


    def Check():
        if len(e1.get()) == 0 or len(entry1.get()) == 0 or len(entry2.get()) == 0 or len(entry3.get()) == 0:
            tkinter.messagebox.showinfo('Error','enter all required fields!')
        else:
            Check1()
    def Check1():
        if (entry1.get() == "Ajmer" and entry2.get() == "Chandigarh" and entry3.get() == "3A") or (entry1.get() == "Ajmer" and entry2.get() == "New Delhi" and entry3.get() == "3A"):
            tkinter.messagebox.showinfo('Error','Sorry Train Unavailable!')
        else:
            ops = e1.get()

            len1 = len(ops)
            if len1==10:
                date1=ops[0]+ops[1]
                month1=ops[3]+ops[4]
                year11=ops[6]+ops[7]+ops[8]+ops[9]


            if(len1==10):
                if(int(date1)<=31 and int(date1)>=1):
                    if(int(month1)>=1 and int(month1)<=12):
                        if(int(year11)>=2017 and int(year11)<=2018):
                            print('')
                        else:
                            tkinter.messagebox.showinfo('Error', 'Enter Year Correctly!')
                    else:
                        tkinter.messagebox.showinfo('Error', 'Enter Month Correctly!')
                else:
                    tkinter.messagebox.showinfo('Error', 'Enter date Correctly!')
                window.destroy()
                Search()
            else:
                tkinter.messagebox.showinfo('Error', 'Enter date Correctly!')

            #print('list1 print',list1)
            #window.destroy()

            #Search()

    def Search():
        global x1

        window1=Tk()
        window1.title("RAILWAY SCHEDULE")
        window1.config(bg='purple')
        screen_width = window1.winfo_screenwidth()
        screen_height = window1.winfo_screenheight()
        width = 1160
        height = 200
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window1.geometry('%dx%d+%d+%d' % (width, height, x, y))
        window1.resizable(0, 0)

        height = 5
        width = 7
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                e1 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue",fg="white")
                e2 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
                e3 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
                e4 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
                e5 = Entry(window1, justify="center",font=('Slab Serif',10),bg="blue", fg="white")
                e6 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
                e7 = Entry(window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")

                en8 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e9 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e10 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e11 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e12 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e13 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e14 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")

                en15 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e16 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e17 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e18 = Entry(window1, justify="center",font=('Slab Serif',9),bg="light pink")
                e19 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e20 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e21 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")

                en22 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e23 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e24 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e25 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e26 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e27 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e28 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")

                en29 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e30 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e31 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e32 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e33 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e34 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")
                e35 = Entry(window1, justify="center",font=('Slab Serif',9), bg="light pink")

                e1.grid(row=0, column=0)
                e2.grid(row=0, column=1)
                e3.grid(row=0, column=2)
                e4.grid(row=0, column=3)
                e5.grid(row=0, column=4)
                e6.grid(row=0, column=5)
                e7.grid(row=0, column=6)
                en8.grid(row=1, column=0)
                e9.grid(row=1, column=1)
                e10.grid(row=1, column=2)
                e11.grid(row=1, column=3)
                e12.grid(row=1, column=4)
                e13.grid(row=1, column=5)
                e14.grid(row=1, column=6)
                en15.grid(row=2, column=0)
                e16.grid(row=2, column=1)
                e17.grid(row=2, column=2)
                e18.grid(row=2, column=3)
                e19.grid(row=2, column=4)
                e20.grid(row=2, column=5)
                e21.grid(row=2, column=6)
                en22.grid(row=3, column=0)
                e23.grid(row=3, column=1)
                e24.grid(row=3, column=2)
                e25.grid(row=3, column=3)
                e26.grid(row=3, column=4)
                e27.grid(row=3, column=5)
                e28.grid(row=3, column=6)
                en29.grid(row=4, column=0)
                e30.grid(row=4, column=1)
                e31.grid(row=4, column=2)
                e32.grid(row=4, column=3)
                e33.grid(row=4, column=4)
                e34.grid(row=4, column=5)
                e35.grid(row=4, column=6)

                e1.insert(10, "Train number")
                e2.insert(10, "Train name")
                e3.insert(10, "Source")
                e4.insert(10, "Departure time")
                e5.insert(10, "Destination")
                e6.insert(10, "Arrival")
                e7.insert(10, "class")


            if variable.get() == "Howrah" and variable1.get()== "New Delhi":
                    en8.insert(10, "12235")

                    e9.insert(10, "Rajdhani Express")
                    e10.insert(10, "Howrah")
                    e11.insert(10, "14:30")
                    e12.insert(10, "New Delhi")
                    e13.insert(10, "7:55")
                    e14.insert(10, "1A,2A,3A")

                    en15.insert(10, "12236")

                    e16.insert(10, "Howrah Juntion")
                    e17.insert(10, "Howrah")
                    e18.insert(10, "16:30")
                    e19.insert(10, "New Delhi")
                    e20.insert(10, "5:50")
                    e21.insert(10, "1A,2A,3A")

                    en22.insert(10, "12237")
                    e23.insert(10, "New Delhi Duronto")
                    e24.insert(10, "Howrah")
                    e25.insert(10, "8:35")
                    e26.insert(10, "New Delhi")
                    e27.insert(10, "15:50")
                    e28.insert(10, "1A,2A,3A")

                    en29.insert(10, "12238")
                    e30.insert(10, "Anand Vihar")
                    e31.insert(10, "Howrah")
                    e32.insert(10, "12:30")
                    e33.insert(10, "New Delhi")
                    e34.insert(10, "7:20")
                    e35.insert(10, "1A,2A,3A")


            if variable.get() == "Howrah" and variable1.get()== "Chandigarh":
                    en8.insert(10, "12239")

                    e9.insert(10, "Howrah Amritsar Express")
                    e10.insert(10, "Howrah")
                    e11.insert(10, "6:30")
                    e12.insert(10, "Chandigarh")
                    e13.insert(10, "18:20")
                    e14.insert(10, "1A,2A,3A")

                    en15.insert(10, "12240")
                    e16.insert(10, "Kalka Mail")
                    e17.insert(10, "Howrah")
                    e18.insert(10, "14:30")
                    e19.insert(10, "Chandigarh")
                    e20.insert(10, "23:30")
                    e21.insert(10, "1A,2A,3A")

                    en22.insert(10, "12241")
                    e23.insert(10, "JallianwalaBagh Express")
                    e24.insert(10, "Howrah")
                    e25.insert(10, "12:30")
                    e26.insert(10, "Chandigarh")
                    e27.insert(10, "8:40")
                    e28.insert(10, "1A,2A,3A")

                    en29.insert(10, "12242")
                    e30.insert(10, "Durgiana Express")
                    e31.insert(10, "Howrah")
                    e32.insert(10, "8:30")
                    e33.insert(10, "Chandigarh")
                    e34.insert(10, "16:20")
                    e35.insert(10, "1A,2A,3A")

            if variable.get() == "Ajmer" and variable1.get()== "Chandigarh":
                    en8.insert(10, "12243")
                    ach12243=12243
                    e9.insert(10, "Garibrath")
                    e10.insert(10, "Ajmer")
                    e11.insert(10, "9:30")
                    e12.insert(10, "Chandigarh")
                    e13.insert(10, "14:40")
                    e14.insert(10, "1A,2A")

                    en15.insert(10, "12244")
                    e16.insert(10, "Mumbai Bandra (T)")
                    e17.insert(10, "Ajmer")
                    e18.insert(10, "1:00")
                    e19.insert(10, "Chandigarh")
                    e20.insert(10, "00:45")
                    e21.insert(10, "1A,2A")

                    en22.insert(10, "12245")
                    e23.insert(10, "Pooja SF Express")
                    e24.insert(10, "Ajmer")
                    e25.insert(10, "11:05")
                    e26.insert(10, "Chandigarh")
                    e27.insert(10, "3:00")
                    e28.insert(10, "1A,2A")

                    en29.insert(10, "12246")
                    e30.insert(10, "Gandhidham")
                    e31.insert(10, "Howrah")
                    e32.insert(10, "14:05")
                    e33.insert(10, "Chandigarh")
                    e34.insert(10, "6:45")
                    e35.insert(10, "1A,2A")

            if variable.get() == "Ajmer" and variable1.get()== "New Delhi":
                    en8.insert(10, "12247")
                    and12247=12247
                    e9.insert(10, "Uttaranchal Express")
                    e10.insert(10, "Ajmer")
                    e11.insert(10, "1:40")
                    e12.insert(10, "New Delhi")
                    e13.insert(10, "10:40")
                    e14.insert(10, "1A,2A")

                    en15.insert(10, "12248")
                    e16.insert(10, "Rajkot Express")
                    e17.insert(10, "Ajmer")
                    e18.insert(10, "6:30")
                    e19.insert(10, "New Delhi")
                    e20.insert(10, "10:45")
                    e21.insert(10, "1A,2A")

                    en22.insert(10, "12249")
                    e23.insert(10, "Corbet park link Express")
                    e24.insert(10, "Ajmer")
                    e25.insert(10, "11:05")
                    e26.insert(10, "New Delhi")
                    e27.insert(10, "20:00")
                    e28.insert(10, "1A,2A")

                    en29.insert(10, "12250")
                    e30.insert(10, "Ranikhet Express")
                    e31.insert(10, "Ajmer")
                    e32.insert(10, "12:10")
                    e33.insert(10, "New Delhi")
                    e34.insert(10, "21:10")
                    e35.insert(10, "1A,2A")

        def PassengerDetails1():
            global x1

            if en8.get()=="12235":
                x1=12235
            elif en8.get()=="12239":
                x1=12239
            elif en8.get() == "12243":
                x1 = 12243
            else:
                x1 = 12247

            def PassengerDetails():
                window1.destroy()
                window2 = Tk()
                window2.title("Passenger Details")
                window2.config(bg="green")
                screen_width = window2.winfo_screenwidth()
                screen_height = window2.winfo_screenheight()
                width = 700
                height = 200
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
                window2.resizable(0, 0)

                height = 5
                width = 5
                for i in range(height):  # Rows
                    for j in range(width):  # Columns
                        e1 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn2 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn3 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn4 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        e5 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        e6 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn7 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn8 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn9 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e10 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e11 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e12 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e13 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e14 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e15 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e16 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e17 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e18 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e19 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e20 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e21 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e22 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e23 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e24 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e25 = Entry(window2, justify="center", font=('Slab Serif', 3))

                        e1.insert(10, "S.no")
                        enn2.insert(10, "Name")
                        enn3.insert(10, "Age")
                        enn4.insert(10, "Gender")
                        e5.insert(10, "IdProof")
                        e6.insert(10, "1")

                        e11.insert(10, "2")
                        e16.insert(10, "3")
                        e21.insert(10, "4")

                        e1.grid(row=0, column=0)
                        enn2.grid(row=0, column=1)
                        enn3.grid(row=0, column=2)
                        enn4.grid(row=0, column=3)
                        e5.grid(row=0, column=4)
                        e6.grid(row=1, column=0)
                        enn7.grid(row=1, column=1)
                        enn8.grid(row=1, column=2)
                        enn9.grid(row=1, column=3)
                        e10.grid(row=1, column=4)

                        e11.grid(row=2, column=0)
                        e12.grid(row=2, column=1)
                        e13.grid(row=2, column=2)
                        e14.grid(row=2, column=3)
                        e15.grid(row=2, column=4)

                        e16.grid(row=3, column=0)
                        e17.grid(row=3, column=1)
                        e18.grid(row=3, column=2)
                        e19.grid(row=3, column=3)
                        e20.grid(row=3, column=4)

                        e21.grid(row=4, column=0)
                        e22.grid(row=4, column=1)
                        e23.grid(row=4, column=2)
                        e24.grid(row=4, column=3)
                        e25.grid(row=4, column=4)

                        def fun(*args):
                            enn9.insert(10, v2.get())

                        def fun1(*args):
                            e14.insert(10, v3.get())

                        def fun2(*args):
                            e19.insert(10, v4.get())

                        def fun3(*args):
                            e24.insert(10, v5.get())

                        def fun4(*args):
                            e10.insert(10, v6.get())

                        def fun5(*args):
                            e15.insert(10, v7.get())

                        def fun6(*args):
                            e20.insert(10, v8.get())

                        def fun7(*args):
                            e25.insert(10, v9.get())

                        v2 = StringVar(window2)
                        gender = {'Male', 'Female'}
                        v2.set('Select')
                        v2.trace("w", fun)
                        popupMenu1 = OptionMenu(window2, v2, *gender)
                        popupMenu1.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu1.grid(row=1, column=3)

                        v3 = StringVar(window2)
                        gender1 = {'Male', 'Female'}
                        v3.set('Select')
                        v3.trace("w", fun1)
                        popupMenu2 = OptionMenu(window2, v3, *gender1)
                        popupMenu2.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu2.grid(row=2, column=3)

                        v4 = StringVar(window2)
                        gender2 = {'Male', 'Female'}
                        v4.set('Select')
                        v4.trace("w", fun2)
                        popupMenu3 = OptionMenu(window2, v4, *gender2)
                        popupMenu3.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu3.grid(row=3, column=3)

                        v5 = StringVar(window2)
                        gender = {'Male', 'Female'}
                        v5.set('Select')
                        v5.trace("w", fun3)
                        popupMenu4 = OptionMenu(window2, v5, *gender)
                        popupMenu4.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu4.grid(row=4, column=3)

                        v6 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v6.set('Select')
                        v6.trace("w", fun4)
                        popup = OptionMenu(window2, v6, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=1, column=4)

                        v7 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v7.set('Select')
                        v7.trace("w", fun5)
                        popup = OptionMenu(window2, v7, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=2, column=4)

                        v8 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v8.set('Select')
                        v8.trace("w", fun6)
                        popup = OptionMenu(window2, v8, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=3, column=4)

                        v9 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v9.set('Select')
                        v9.trace("w", fun7)
                        popup = OptionMenu(window2, v9, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")

                        popup.grid(row=4, column=4)

                def Check1():

                    def Show():

                        global x1,count
                        window3 = Tk()

                        window3.title("Ticket")
                        screen_width = window3.winfo_screenwidth()
                        screen_height = window3.winfo_screenheight()
                        width = 580
                        height = 480
                        x = (screen_width / 2) - (width / 2)
                        y = (screen_height / 2) - (height / 2)
                        window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                        window3.resizable(0, 0)
                        window3.config(bg='white')

                        Label(window3, text="Name",bg='white', font=('Slab Serif', 11)).place(x=90, y=50)
                        Label(window3, text="Gender",bg='white', font=('Slab Serif', 11)).place(x=320, y=50)
                        Label(window3, text="Departure time",bg='white', font=('Slab Serif', 11)).place(x=60, y=90)
                        Label(window3, text="Age",bg='white', font=('Slab Serif', 11)).place(x=320, y=90)
                        Label(window3, text="Class",bg='white', font=('Slab Serif', 11)).place(x=320, y=130)
                        Label(window3, text="Train no.",bg='white',font=('Slab Serif', 11)).place(x=90, y=130)
                        Label(window3, text="Train name",bg='white', font=('Slab Serif', 11)).place(x=90, y=170)
                        Label(window3, text="Source",bg='white', font=('Slab Serif', 11)).place(x=90, y=210)
                        Label(window3, text="Destination",bg='white', font=('Slab Serif', 11)).place(x=90, y=250)
                        Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                        Label(window3, text="PNR no",bg='white', font=('Slab Serif', 11)).place(x=320, y=170)

                        Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10)).place(x=170, y=290,  height=25)


                        Class = Label(window3, justify="center",bg='white',text=variable2.get(), font=('Slab Serif', 10)).place(x=380, y=130, height=25)
                        TrainNumber = Label(window3, justify="center",bg='white', font=('Slab Serif', 10))
                        TrainNumber.place(x=170, y=130, height=25)


                        global conn, cursor, x1, x2
                        if x1 == 12235:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12235")
                            fetch = cursor.fetchall()


                            for data in fetch:
                                Source = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[5],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)
                            a=111111
                            b=999999
                            pnr=(random.randint(a, b))

                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()),int(enn8.get()), str(enn9.get())))

                            conn.commit()


                            cursor.execute("Select * from Rail999 where pnr=?  ",(pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:

                                pnr1 = Label(window3, justify="center",bg='white',text=data[0],
                                            font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3,text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(x=170, y=50,height=25)
                                Age = Label(window3,text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(x=380, y=90, height=25)
                                Gender = Label(window3,text=data[3] ,bg='white',justify="center", font=('Slab Serif', 9)).place(x=380, y=50, height=25)



                            cursor.close()
                            conn.close()
                        elif x1 == 12239:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12239")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2], justify="center",bg='white',
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[5], justify="center",bg='white',
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)
                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))


                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:

                                pnr1 = Label(window3, justify="center", text=data[0],bg='white',
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12243:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12243")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)
                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))


                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:
                                pnr1 = Label(window3, justify="center",bg='white',text=data[0],
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12247:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12247")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5], justify="center",bg='white', font=('Slab Serif', 10)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2], justify="center",bg='white',
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1], justify="center",bg='white',
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)
                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))


                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:


                                pnr1 = Label(window3, justify="center",bg='white', text=data[0],
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()



                        Label(window3, text="Have a nice trip!!",bg='white', font=('Slab Serif', 17)).place(x=200, y=340)

                        mainloop()



                    global count
                    count=0
                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
                            e15.get()) != 0) and (
                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
                        e25.get()) != 0) and (
                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
                            e10.get()) != 0) and (
                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
                        e20.get()) != 0) and (
                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                        count=1
                        Show()
                    elif e12.get()!="" and e17.get()=="":
                        count=2
                        Show()
                    elif e17.get()!="" and e22.get()=="":
                        count=3
                        Show()
                    elif e22.get()!="":
                        count=4
                        Show()
                    else:
                        Show()

                b = Button(window2, text='Submit', bg="cyan", font=('Slab Serif', 11), command=Check1)
                b.place(x=250, y=155, width=100)

                mainloop()

            PassengerDetails()

        def PassengerDetails2():
            global x1
            if en15.get()=="12236":
                x1=12236
            elif en15.get()=="12240":
                x1=12240
            elif en15.get() == "12244":
                x1 = 12244
            else:
                x1 = 12248

            def PassengerDetails():
                window1.destroy()
                window2 = Tk()
                window2.title("Passenger Details")
                window2.config(bg="green")
                screen_width = window2.winfo_screenwidth()
                screen_height = window2.winfo_screenheight()
                width = 700
                height = 200
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
                window2.resizable(0, 0)

                height = 5
                width = 5
                for i in range(height):  # Rows
                    for j in range(width):  # Columns
                        e1 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn2 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn3 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn4 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        e5 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        e6 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn7 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn8 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn9 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e10 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e11 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e12 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e13 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e14 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e15 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e16 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e17 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e18 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e19 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e20 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e21 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e22 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e23 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e24 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e25 = Entry(window2, justify="center", font=('Slab Serif', 3))

                        e1.insert(10, "S.no")
                        enn2.insert(10, "Name")
                        enn3.insert(10, "Age")
                        enn4.insert(10, "Gender")
                        e5.insert(10, "IdProof")
                        e6.insert(10, "1")

                        e11.insert(10, "2")
                        e16.insert(10, "3")
                        e21.insert(10, "4")

                        e1.grid(row=0, column=0)
                        enn2.grid(row=0, column=1)
                        enn3.grid(row=0, column=2)
                        enn4.grid(row=0, column=3)
                        e5.grid(row=0, column=4)
                        e6.grid(row=1, column=0)
                        enn7.grid(row=1, column=1)
                        enn8.grid(row=1, column=2)
                        enn9.grid(row=1, column=3)
                        e10.grid(row=1, column=4)

                        e11.grid(row=2, column=0)
                        e12.grid(row=2, column=1)
                        e13.grid(row=2, column=2)
                        e14.grid(row=2, column=3)
                        e15.grid(row=2, column=4)

                        e16.grid(row=3, column=0)
                        e17.grid(row=3, column=1)
                        e18.grid(row=3, column=2)
                        e19.grid(row=3, column=3)
                        e20.grid(row=3, column=4)

                        e21.grid(row=4, column=0)
                        e22.grid(row=4, column=1)
                        e23.grid(row=4, column=2)
                        e24.grid(row=4, column=3)
                        e25.grid(row=4, column=4)

                        def fun(*args):
                            enn9.insert(10, v2.get())

                        def fun1(*args):
                            e14.insert(10, v3.get())

                        def fun2(*args):
                            e19.insert(10, v4.get())

                        def fun3(*args):
                            e24.insert(10, v5.get())

                        def fun4(*args):
                            e10.insert(10, v6.get())

                        def fun5(*args):
                            e15.insert(10, v7.get())

                        def fun6(*args):
                            e20.insert(10, v8.get())

                        def fun7(*args):
                            e25.insert(10, v9.get())

                        v2 = StringVar(window2)
                        gender = {'Male', 'Female'}
                        v2.set('Select')
                        v2.trace("w", fun)
                        popupMenu1 = OptionMenu(window2, v2, *gender)
                        popupMenu1.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu1.grid(row=1, column=3)

                        v3 = StringVar(window2)
                        gender1 = {'Male', 'Female'}
                        v3.set('Select')
                        v3.trace("w", fun1)
                        popupMenu2 = OptionMenu(window2, v3, *gender1)
                        popupMenu2.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu2.grid(row=2, column=3)

                        v4 = StringVar(window2)
                        gender2 = {'Male', 'Female'}
                        v4.set('Select')
                        v4.trace("w", fun2)
                        popupMenu3 = OptionMenu(window2, v4, *gender2)
                        popupMenu3.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu3.grid(row=3, column=3)

                        v5 = StringVar(window2)
                        gender = {'Male', 'Female'}
                        v5.set('Select')
                        v5.trace("w", fun3)
                        popupMenu4 = OptionMenu(window2, v5, *gender)
                        popupMenu4.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu4.grid(row=4, column=3)

                        v6 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v6.set('Select')
                        v6.trace("w", fun4)
                        popup = OptionMenu(window2, v6, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=1, column=4)

                        v7 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v7.set('Select')
                        v7.trace("w", fun5)
                        popup = OptionMenu(window2, v7, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=2, column=4)

                        v8 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v8.set('Select')
                        v8.trace("w", fun6)
                        popup = OptionMenu(window2, v8, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=3, column=4)

                        v9 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v9.set('Select')
                        v9.trace("w", fun7)
                        popup = OptionMenu(window2, v9, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=4, column=4)

                def Check1():

                    def Show():
                        global x1
                        window3 = Tk()
                        window3.title("Ticket")
                        screen_width = window3.winfo_screenwidth()
                        screen_height = window3.winfo_screenheight()
                        width = 580
                        height = 480
                        x = (screen_width / 2) - (width / 2)
                        y = (screen_height / 2) - (height / 2)
                        window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                        window3.resizable(0, 0)
                        window3.config(bg='white')

                        Label(window3, text="Name",bg='white', font=('Slab Serif', 11)).place(x=90, y=50)
                        Label(window3, text="Gender",bg='white',font=('Slab Serif', 11)).place(x=320, y=50)
                        Label(window3, text="Departure time",bg='white', font=('Slab Serif', 11)).place(x=60, y=90)
                        Label(window3, text="Age",bg='white', font=('Slab Serif', 11)).place(x=320, y=90)
                        Label(window3, text="Class",bg='white',font=('Slab Serif', 11)).place(x=320, y=130)
                        Label(window3, text="Train no.",bg='white', font=('Slab Serif', 11)).place(x=90, y=130)
                        Label(window3, text="Train name",bg='white', font=('Slab Serif', 11)).place(x=90, y=170)
                        Label(window3, text="Source",bg='white', font=('Slab Serif', 11)).place(x=90, y=210)
                        Label(window3, text="Destination",bg='white', font=('Slab Serif', 11)).place(x=90, y=250)
                        Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                        Label(window3, text="PNR no",bg='white', font=('Slab Serif', 11)).place(x=320, y=170)

                        Name = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=50, height=25)
                        Gender = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=50, height=25)
                        DepartureTime = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=90,
                                                                                                       height=25)
                        Age = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=90, height=25)
                        Class = Label(window3, justify="center",bg='white',text=variable2.get(), font=('Slab Serif', 10)).place(x=380, y=130, height=25)
                        TrainNumber = Label(window3, justify="center",bg='white', font=('Slab Serif', 10))
                        TrainNumber.place(x=170, y=130, height=25)

                        Source = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=170, height=25)
                        Destination = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=250,
                                                                                                     height=25)
                        Number = Label(window3,text=count, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=290, height=25)
                        global conn, cursor, x1, x2

                        if x1 == 12236:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12236")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5], justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2], justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1], justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3], justify="center",
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))


                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:

                                pnr1 = Label(window3, justify="center",bg='white', text=data[0],
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12240:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12240")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))


                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:

                                pnr1 = Label(window3,bg='white', justify="center", text=data[0],
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12244:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12244")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))

                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:
                                pnr1 = Label(window3,bg='white', justify="center", text=data[0],
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12248:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12248")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170,
                                    height=25)

                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))

                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:
                                pnr1 = Label(window3, justify="center",bg='white', text=data[0],
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()


                        Label(window3, text="Have a nice trip!!",bg='white', font=('Slab Serif', 17)).place(x=200, y=340)

                        mainloop()

                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
                            e15.get()) != 0) and (
                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
                        e25.get()) != 0) and (
                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
                            e10.get()) != 0) and (
                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
                        e20.get()) != 0) and (
                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                        count=1
                        Show()
                    elif e12.get()!="" and e17.get()=="":
                        count=2
                        Show()
                    elif e17.get()!="" and e22.get()=="":
                        count=3
                        Show()
                    elif e22.get()!="":
                        count=4
                        Show()
                    else:
                        Show()

                b = Button(window2, text='Submit', bg="cyan", font=('Slab Serif', 11), command=Check1)
                b.place(x=250, y=155, width=100)

                mainloop()

            PassengerDetails()

        def PassengerDetails3():
            global x1
            if en22.get() == "12237":
                x1 = 12237
            elif en22.get() == "12241":
                x1 = 12241
            elif en22.get() == "12245":
                x1 = 12245
            else:
                x1 = 12249

            def PassengerDetails():
                window1.destroy()
                window2 = Tk()
                window2.title("Passenger Details")
                window2.config(bg="green")
                screen_width = window2.winfo_screenwidth()
                screen_height = window2.winfo_screenheight()
                width = 700
                height = 200
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
                window2.resizable(0, 0)

                height = 5
                width = 5
                for i in range(height):  # Rows
                    for j in range(width):  # Columns
                        e1 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn2 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn3 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn4 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        e5 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        e6 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn7 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn8 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn9 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e10 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e11 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e12 = Entry(window2, justify="center",font=('Slab Serif', 9), bg="yellow")
                        e13 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e14 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e15 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e16 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e17 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e18 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e19 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e20 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e21 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e22 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e23 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e24 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e25 = Entry(window2, justify="center", font=('Slab Serif', 3))

                        e1.insert(10, "S.no")
                        enn2.insert(10, "Name")
                        enn3.insert(10, "Age")
                        enn4.insert(10, "Gender")
                        e5.insert(10, "IdProof")
                        e6.insert(10, "1")

                        e11.insert(10, "2")
                        e16.insert(10, "3")
                        e21.insert(10, "4")

                        e1.grid(row=0, column=0)
                        enn2.grid(row=0, column=1)
                        enn3.grid(row=0, column=2)
                        enn4.grid(row=0, column=3)
                        e5.grid(row=0, column=4)
                        e6.grid(row=1, column=0)
                        enn7.grid(row=1, column=1)
                        enn8.grid(row=1, column=2)
                        enn9.grid(row=1, column=3)
                        e10.grid(row=1, column=4)

                        e11.grid(row=2, column=0)
                        e12.grid(row=2, column=1)
                        e13.grid(row=2, column=2)
                        e14.grid(row=2, column=3)
                        e15.grid(row=2, column=4)

                        e16.grid(row=3, column=0)
                        e17.grid(row=3, column=1)
                        e18.grid(row=3, column=2)
                        e19.grid(row=3, column=3)
                        e20.grid(row=3, column=4)

                        e21.grid(row=4, column=0)
                        e22.grid(row=4, column=1)
                        e23.grid(row=4, column=2)
                        e24.grid(row=4, column=3)
                        e25.grid(row=4, column=4)

                        def fun(*args):
                            enn9.insert(10, v2.get())

                        def fun1(*args):
                            e14.insert(10, v3.get())

                        def fun2(*args):
                            e19.insert(10, v4.get())

                        def fun3(*args):
                            e24.insert(10, v5.get())

                        def fun4(*args):
                            e10.insert(10, v6.get())

                        def fun5(*args):
                            e15.insert(10, v7.get())

                        def fun6(*args):
                            e20.insert(10, v8.get())

                        def fun7(*args):
                            e25.insert(10, v9.get())

                        v2 = StringVar(window2)
                        gender = {'Male', 'Female'}
                        v2.set('Select')
                        v2.trace("w", fun)
                        popupMenu1 = OptionMenu(window2, v2, *gender)
                        popupMenu1.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu1.grid(row=1, column=3)

                        v3 = StringVar(window2)
                        gender1 = {'Male', 'Female'}
                        v3.set('Select')
                        v3.trace("w", fun1)
                        popupMenu2 = OptionMenu(window2, v3, *gender1)
                        popupMenu2.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu2.grid(row=2, column=3)

                        v4 = StringVar(window2)
                        gender2 = {'Male', 'Female'}
                        v4.set('Select')
                        v4.trace("w", fun2)
                        popupMenu3 = OptionMenu(window2, v4, *gender2)
                        popupMenu3.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu3.grid(row=3, column=3)

                        v5 = StringVar(window2)
                        gender = {'Male', 'Female'}
                        v5.set('Select')
                        v5.trace("w", fun3)
                        popupMenu4 = OptionMenu(window2, v5, *gender)
                        popupMenu4.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu4.grid(row=4, column=3)

                        v6 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v6.set('Select')
                        v6.trace("w", fun4)
                        popup = OptionMenu(window2, v6, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=1, column=4)

                        v7 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v7.set('Select')
                        v7.trace("w", fun5)
                        popup = OptionMenu(window2, v7, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=2, column=4)

                        v8 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v8.set('Select')
                        v8.trace("w", fun6)
                        popup = OptionMenu(window2, v8, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=3, column=4)

                        v9 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v9.set('Select')
                        v9.trace("w", fun7)
                        popup = OptionMenu(window2, v9, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=4, column=4)

                def Check1():

                    def Show():
                        global x1
                        window3 = Tk()
                        window3.title("Ticket")
                        screen_width = window3.winfo_screenwidth()
                        screen_height = window3.winfo_screenheight()
                        width = 580
                        height = 480
                        x = (screen_width / 2) - (width / 2)
                        y = (screen_height / 2) - (height / 2)
                        window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                        window3.resizable(0, 0)
                        window3.config(bg='white')

                        Label(window3, text="Name",bg='white', font=('Slab Serif', 11)).place(x=90, y=50)
                        Label(window3, text="Gender", bg='white',font=('Slab Serif', 11)).place(x=320, y=50)
                        Label(window3, text="Departure time",bg='white', font=('Slab Serif', 11)).place(x=60, y=90)
                        Label(window3, text="Age",bg='white', font=('Slab Serif', 11)).place(x=320, y=90)
                        Label(window3, text="Class",bg='white', font=('Slab Serif', 11)).place(x=320, y=130)
                        Label(window3, text="Train no.",bg='white', font=('Slab Serif', 11)).place(x=90, y=130)
                        Label(window3, text="Train name",bg='white', font=('Slab Serif', 11)).place(x=90, y=170)
                        Label(window3, text="Source",bg='white', font=('Slab Serif', 11)).place(x=90, y=210)
                        Label(window3, text="Destination",bg='white', font=('Slab Serif', 11)).place(x=90, y=250)
                        Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                        Label(window3, text="PNR no",bg='white', font=('Slab Serif', 11)).place(x=320, y=170)

                        Name = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=50, height=25)
                        Gender = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=50, height=25)
                        DepartureTime = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=90,
                                                                                                       height=25)
                        Age = Label(window3, justify="center",bg='white',font=('Slab Serif', 10)).place(x=380, y=90, height=25)
                        Class = Label(window3, justify="center",bg='white',text=variable2.get(),font=('Slab Serif', 10)).place(x=380, y=130, height=25)
                        TrainNumber = Label(window3, justify="center",bg='white', font=('Slab Serif', 10))
                        TrainNumber.place(x=170, y=130, height=25)

                        Source = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=170, height=25)
                        Destination = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=250,
                                                                                                     height=25)
                        Number = Label(window3,text=count, justify="center", bg='white',font=('Slab Serif', 9)).place(x=170, y=290, height=25)
                        global conn, cursor, x1, x2

                        if x1 == 12237:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12237")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))


                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:

                                pnr1 = Label(window3, justify="center", text=data[0],bg='white',
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12241:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12241")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))


                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:

                                pnr1 = Label(window3, justify="center", text=data[0],bg='white',
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12245:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12245")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2], justify="center",bg='white',
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1], justify="center",bg='white',
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))

                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:


                                pnr1 = Label(window3, justify="center", text=data[0],bg='white',
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12249:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12249")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170,
                                    height=25)

                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1], justify="center",bg='white',
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))

                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:
                                pnr1 = Label(window3, justify="center", text=data[0],bg='white',
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()


                        Label(window3, text="Have a nice trip!!", bg='white',font=('Slab Serif', 17)).place(x=200, y=340)

                        mainloop()

                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
                            e15.get()) != 0) and (
                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
                        e25.get()) != 0) and (
                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
                            e10.get()) != 0) and (
                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
                        e20.get()) != 0) and (
                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                        count=1
                        Show()
                    elif e12.get()!="" and e17.get()=="":
                        count=2
                        Show()
                    elif e17.get()!="" and e22.get()=="":
                        count=3
                        Show()
                    elif e22.get()!="":
                        count=4
                        Show()
                    else:
                        Show()

                b = Button(window2, text='Submit', bg="cyan", font=('Slab Serif', 11), command=Check1)
                b.place(x=250, y=155, width=100)

                mainloop()

            PassengerDetails()

        def PassengerDetails4():
             global x1
             if en29.get() == "12238":
                x1 = 12238
             elif en29.get() == "12242":
                x1 = 12242
             elif en29.get() == "12246":
                x1 = 12246
             else:
                x1=12250

             def PassengerDetails():
                window1.destroy()
                window2 = Tk()
                window2.title("Passenger Details")
                window2.config(bg="green")
                screen_width = window2.winfo_screenwidth()
                screen_height = window2.winfo_screenheight()
                width = 700
                height = 200
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
                window2.resizable(0, 0)

                height = 5
                width = 5
                for i in range(height):  # Rows
                    for j in range(width):  # Columns
                        e1 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn2 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn3 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        enn4 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        e5 = Entry(window2, justify="center", font=('Slab Serif', 10), bg="orange")
                        e6 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn7 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn8 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        enn9 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e10 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e11 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e12 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e13 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e14 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e15 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e16 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e17 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e18 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e19 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e20 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e21 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e22 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e23 = Entry(window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                        e24 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e25 = Entry(window2, justify="center", font=('Slab Serif', 3))

                        e1.insert(10, "S.no")
                        enn2.insert(10, "Name")
                        enn3.insert(10, "Age")
                        enn4.insert(10, "Gender")
                        e5.insert(10, "IdProof")
                        e6.insert(10, "1")

                        e11.insert(10, "2")
                        e16.insert(10, "3")
                        e21.insert(10, "4")

                        e1.grid(row=0, column=0)
                        enn2.grid(row=0, column=1)
                        enn3.grid(row=0, column=2)
                        enn4.grid(row=0, column=3)
                        e5.grid(row=0, column=4)
                        e6.grid(row=1, column=0)
                        enn7.grid(row=1, column=1)
                        enn8.grid(row=1, column=2)
                        enn9.grid(row=1, column=3)
                        e10.grid(row=1, column=4)

                        e11.grid(row=2, column=0)
                        e12.grid(row=2, column=1)
                        e13.grid(row=2, column=2)
                        e14.grid(row=2, column=3)
                        e15.grid(row=2, column=4)

                        e16.grid(row=3, column=0)
                        e17.grid(row=3, column=1)
                        e18.grid(row=3, column=2)
                        e19.grid(row=3, column=3)
                        e20.grid(row=3, column=4)

                        e21.grid(row=4, column=0)
                        e22.grid(row=4, column=1)
                        e23.grid(row=4, column=2)
                        e24.grid(row=4, column=3)
                        e25.grid(row=4, column=4)

                        def fun(*args):
                            enn9.insert(10, v2.get())

                        def fun1(*args):
                            e14.insert(10, v3.get())

                        def fun2(*args):
                            e19.insert(10, v4.get())

                        def fun3(*args):
                            e24.insert(10, v5.get())

                        def fun4(*args):
                            e10.insert(10, v6.get())

                        def fun5(*args):
                            e15.insert(10, v7.get())

                        def fun6(*args):
                            e20.insert(10, v8.get())

                        def fun7(*args):
                            e25.insert(10, v9.get())

                        v2 = StringVar(window2)
                        gender = {'Male', 'Female'}
                        v2.set('Select')
                        v2.trace("w", fun)
                        popupMenu1 = OptionMenu(window2, v2, *gender)
                        popupMenu1.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu1.grid(row=1, column=3)

                        v3 = StringVar(window2)
                        gender1 = {'Male', 'Female'}
                        v3.set('Select')
                        v3.trace("w", fun1)
                        popupMenu2 = OptionMenu(window2, v3, *gender1)
                        popupMenu2.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu2.grid(row=2, column=3)

                        v4 = StringVar(window2)
                        gender2 = {'Male', 'Female'}
                        v4.set('Select')
                        v4.trace("w", fun2)
                        popupMenu3 = OptionMenu(window2, v4, *gender2)
                        popupMenu3.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu3.grid(row=3, column=3)

                        v5 = StringVar(window2)
                        gender = {'Male', 'Female'}
                        v5.set('Select')
                        v5.trace("w", fun3)
                        popupMenu4 = OptionMenu(window2, v5, *gender)
                        popupMenu4.config(font=('Slab Serif', 9), bg="purple", fg='white')
                        popupMenu4.grid(row=4, column=3)

                        v6 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v6.set('Select')
                        v6.trace("w", fun4)
                        popup = OptionMenu(window2, v6, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=1, column=4)

                        v7 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v7.set('Select')
                        v7.trace("w", fun5)
                        popup = OptionMenu(window2, v7, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=2, column=4)

                        v8 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v8.set('Select')
                        v8.trace("w", fun6)
                        popup = OptionMenu(window2, v8, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=3, column=4)

                        v9 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v9.set('Select')
                        v9.trace("w", fun7)
                        popup = OptionMenu(window2, v9, *proof)
                        popup.config(font=('Slab Serif', 9), bg="light green")
                        popup.grid(row=4, column=4)

                def Check1():

                    def Show():
                        global x1
                        window3 = Tk()
                        window3.title("Ticket")
                        screen_width = window3.winfo_screenwidth()
                        screen_height = window3.winfo_screenheight()
                        width = 580
                        height = 480
                        x = (screen_width / 2) - (width / 2)
                        y = (screen_height / 2) - (height / 2)
                        window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                        window3.resizable(0, 0)

                        Label(window3, text="Name",bg='white', font=('Slab Serif', 11)).place(x=90, y=50)
                        Label(window3, text="Gender",bg='white', font=('Slab Serif', 11)).place(x=320, y=50)
                        Label(window3, text="Departure time",bg='white', font=('Slab Serif', 11)).place(x=60, y=90)
                        Label(window3, text="Age",bg='white', font=('Slab Serif', 11)).place(x=320, y=90)
                        Label(window3, text="Class",bg='white', font=('Slab Serif', 11)).place(x=320, y=130)
                        Label(window3, text="Train no.",bg='white', font=('Slab Serif', 11)).place(x=90, y=130)
                        Label(window3, text="Train name",bg='white', font=('Slab Serif', 11)).place(x=90, y=170)
                        Label(window3, text="Source",bg='white', font=('Slab Serif', 11)).place(x=90, y=210)
                        Label(window3, text="Destination",bg='white', font=('Slab Serif', 11)).place(x=90, y=250)
                        Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                        Label(window3, text="PNR no",bg='white', font=('Slab Serif', 11)).place(x=320, y=170)

                        Name = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=50, height=25)
                        Gender = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=50, height=25)
                        DepartureTime = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=90,
                                                                                                       height=25)
                        Age = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=90, height=25)
                        Class = Label(window3, justify="center",bg='white',text=variable2.get(), font=('Slab Serif', 10)).place(x=380, y=130, height=25)
                        TrainNumber = Label(window3, justify="center",bg='white', font=('Slab Serif', 10))
                        TrainNumber.place(x=170, y=130, height=25)

                        Source = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=170, height=25)
                        Destination = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=250,
                                                                                                     height=25)
                        Number = Label(window3,text=count, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=290, height=25)
                        global conn, cursor, x1, x2

                        if x1 == 12238:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12238")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))


                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:

                                pnr1 = Label(window3,bg='white', justify="center", text=data[0],
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3], bg='white',justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12242:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12242")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))


                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:

                                pnr1 = Label(window3,bg='white', justify="center", text=data[0],
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3], bg='white',justify="center", font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12246:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12246")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5], bg='white',justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170, height=25)
                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))

                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:


                                pnr1 = Label(window3, justify="center",bg='white', text=data[0],
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()
                        elif x1 == 12250:
                            cursor = conn.cursor()
                            TrainNumber.config(text=x1)
                            cursor.execute("Select * from Rail88 where Trainnumber=12250")
                            fetch = cursor.fetchall()
                            for data in fetch:
                                Source = Label(window3, text=data[5], bg='white',justify="center", font=('Slab Serif', 10)).place(
                                    x=170, y=170,
                                    height=25)

                                Destination = Label(window3, text=data[2],bg='white', justify="center",
                                                    font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
                                                  font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
                                                      font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                            a = 111111
                            b = 999999
                            pnr = (random.randint(a, b))

                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                            conn.commit()

                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                            fetch1 = cursor.fetchall()
                            for data in fetch1:
                                pnr1 = Label(window3, justify="center",bg='white', text=data[0],
                                             font=('Slab Serif', 9))
                                pnr1.place(x=380, y=170, height=25)
                                pnr1.config(text=data[0])
                                Name = Label(window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=170, y=50, height=25)
                                Age = Label(window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=380, y=90, height=25)
                                Gender = Label(window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
                                    x=380, y=50, height=25)

                            cursor.close()
                            conn.close()


                        Label(window3, text="Have a nice trip!!", bg='white',font=('Slab Serif', 17)).place(x=200, y=340)

                        mainloop()

                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
                            e15.get()) != 0) and (
                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
                        e25.get()) != 0) and (
                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
                            e10.get()) != 0) and (
                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
                        e20.get()) != 0) and (
                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                        count=1
                        Show()
                    elif e12.get()!="" and e17.get()=="":
                        count=2
                        Show()
                    elif e17.get()!="" and e22.get()=="":
                        count=3
                        Show()
                    elif e22.get()!="":
                        count=4
                        Show()
                    else:
                        Show()

                b = Button(window2, text='Submit', bg="cyan", font=('Slab Serif', 11), command=Check1)
                b.place(x=250, y=155, width=100)

                mainloop()

             PassengerDetails()

        def Back1():
            window1.destroy()

        button1=Button(window1,text="Book",font=('Slab Serif',9),width=10,bg="yellow",command=PassengerDetails1)
        button1.grid(row=1,column=7)
        button2 = Button(window1, text="Book",font=('Slab Serif',9),width=10, bg="yellow",command=PassengerDetails2)
        button2.grid(row=2, column=7)
        button3 = Button(window1, text="Book",font=('Slab Serif',9),width=10, bg="yellow", command=PassengerDetails3)
        button3.grid(row=3, column=7)
        button4 = Button(window1, text="Book",font=('Slab Serif',9),width=10,bg="yellow", command=PassengerDetails4)
        button4.grid(row=4, column=7)

        button5 = Button(window1, text="Back",font=('Slab Serif',15),width=60, bg="cyan", command=Back1)
        button5.place(x=450,y=150,width=100)

        mainloop()


    def Cancellation():
        window.destroy()
        window4 = Tk()
        window4.title("Cancel Ticket")

        screen_width = window4.winfo_screenwidth()
        screen_height = window4.winfo_screenheight()
        width = 410
        height = 400
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window4.geometry('%dx%d+%d+%d' % (width, height, x, y))
        window4.resizable(0, 0)

        window4.config(bg='purple')
        cancel = Label(window4, text="PNR NO", font=('Slab Serif', 15), bg="purple", fg="white").place(x=100, y=150,
                                                                                                       width=90)
        e=Entry(window4,justify="center", font=('Slab Serif', 15), bg="white")
        e.place(x=210, y=150, width=100)


        def Delete1():
            result = tkinter.messagebox.askquestion('Ask', 'Are you sure you want to delete your booked ticket?',
                                              icon="warning")
            if result == 'yes':
                cursor = conn.cursor()
                cursor.execute("Select pnr from Rail999")
                d = cursor.fetchall()

                at=str(d)
                d1=at.replace('(','')
                d2 = d1.replace(')', '')
                d3 = d2.replace(',', '')
                d4=d3.replace('[','')
                d5 = d4.replace(']', '')
                d6=d5.split(' ')


                q=0
                for i in range(1,len(d6)):
                    if e.get()==d6[i]:
                        x123=e.get()
                        q=1
                if q==1:
                    cursor.execute("Delete from Rail999 where pnr=?",(x123,))
                    tkinter.messagebox.showinfo('Success', 'Ticket Deleted Successfully')
                    window4.destroy()
                else:
                    tkinter.messagebox.showinfo('Error', 'Ticket Not Found!')

                cursor.close()
                conn.close()


        def Delete():
            if (len(e.get())==""):
                tkinter.messagebox.showinfo('Error', 'Enter required pnr no.')
            else:

                Delete1()
        def Back():
            window4.destroy()


        Button(window4, text="Back", font=('Slab Serif', 15), bg="green", fg="white",command=Back).place(x=80,y=250, width=120)

        Button(window4, text="Delete", font=('Slab Serif', 15), bg="green", fg="white",command=Delete
               ).place(x=220, y=250, width=120)
        mainloop()
    e1.config(bg="yellow")

    e1.place(x=210,y=160,height=30,width=100)
    Button(window,text="Search trains",font=('Slab Serif',15), bg="green",fg="white",command=Check).place(x=80,y=250,width=120)

    Button(window, text="Cancellation",font=('Slab Serif',15), bg="green",fg="white",command=Cancellation).place(x=220,y=250,width=120)

    mainloop()


button_1 = Button(root, text="Login",font=('Slab Serif',15),bg='blue',fg='white', command=printMsg).place(x=120,y=290)
button_2 = Button(root, text="Quit",font=('Slab Serif',15),bg='blue',fg='white', command=root.destroy).place(x=220,y=290)

for x in range(0, 60):
    canvas.move(my_img, 5, 0)
    root.update()
    time.sleep(0.05)

for x in range(0, 60):
    canvas.move(my_img, -5, 0)
    root.update()
    time.sleep(0.05)


root.mainloop()
