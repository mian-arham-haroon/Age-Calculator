from tkinter import *
from datetime import date

root=Tk()
root.geometry("800x600")
root.title("Age Calculator")
# root.configure("")
root.resizable(False,False)

def calculateage ():
    today=date.today()
    birthday=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year - birthday.year - ((today.month,today.day)<(birthday.month,birthday.day))
    # day=today.day-birthday.day
    # month=today.month-birthday.month
    day=age*365
    second=age*365*86400        #month*day
    Label(text=f"{namevalue.get()} your age {age} , in the day {day}\nand in the second:{second}",font=30).place(x=300,y=500)

photo=PhotoImage(file=("Age calculator  .png"))
myimage=Label(image=photo)
myimage.pack(pady=15,padx=15)

Label(text="Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Day",font=23).place(x=200,y=400)

namevalue=StringVar()
yearvalue=StringVar()
monthvalue=StringVar()
dayvalue=StringVar()

nameEntry=Entry(root,textvariable=namevalue,width=30,bd=3,font=20)
nameEntry.place(x=300,y=250)
yearEntry=Entry(root,textvariable=yearvalue,width=30,bd=3,font=20)
yearEntry.place(x=300,y=300)
monthEntry=Entry(root,textvariable=monthvalue,width=30,bd=3,font=20)
monthEntry.place(x=300,y=350)
dayEntry=Entry(root,textvariable=dayvalue,width=30,bd=3,font=20)
dayEntry.place(x=300,y=400)

Button(text="Age Calaculator",font=20,width=13,height=2,bg="black",fg="white",command=calculateage).place(x=300,y=450)


root.mainloop()