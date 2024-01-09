import tkinter
from tkinter import messagebox
top=tkinter.Tk()
top.title("maths")
top.geometry("400x500")
top.config(background="black")
def sum():
    num1=int(en.get())
    num2=int(en1.get())
    sum=num1+num2
    messagebox.showinfo("alert",sum)
    print("sum=",sum)

def sub():
    num1=int(en.get())
    num2=int(en1.get())
    sub=num1-num2
    messagebox.showinfo("alert",sub)
    print("sub",sub)
def mul():
    num1=int(en.get())
    num2=int(en1.get())
    mul=num1*num2
    messagebox.showinfo("alert",mul)
    print("mul",mul)
def div():
    num1=int(en.get())
    num2=int(en1.get())
    div=num1/num2
    messagebox.showinfo("alert",div)
    print("div",div)
def mod():
    num1=int(en.get())
    num2=int(en1.get())
    mod=num1%num2
    messagebox.showinfo("alert",mod)
    print("mod",mod)

lb=tkinter.Label(text="num1")
lb.place(x=10,y=20)

en=tkinter.Entry()
en.place(x=70,y=20)

lb1=tkinter.Label(text="num2")
lb1.place(x=10,y=60)

en1=tkinter.Entry()
en1.place(x=70,y=60)

btn=tkinter.Button(text="sum",command=sum)
btn.place(x=10,y=120)

btn1=tkinter.Button(text="sub",command=sub)
btn1.place(x=70,y=120)

btn2=tkinter.Button(text="mul",command=mul)
btn2.place(x=130,y=120)

btn3=tkinter.Button(text="div",command=div)
btn3.place(x=190,y=120)

btn4=tkinter.Button(text="mod",command=mod)
btn4.place(x=250,y=120)
