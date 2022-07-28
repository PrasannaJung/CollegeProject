import sqlite3
from tkinter import *
import tkinter
from tkinter import messagebox
from turtle import bgcolor, left
from tkinter import font
import signIn


def openWindow():
    root = Tk()
    root.configure(bg="white")
    root.title("Todo List")
    root.geometry("1920x1080")
    root.configure(bg='#FFE5B4')
    
    # tasks = []

    bg = PhotoImage(file="images/bg_4.png")

    canvas1 = Canvas(root,width=1920,height=1080)
    canvas1.pack(fill='both',expand=False)
    canvas1.create_image(0,0,image=bg,anchor="nw")



    conn = sqlite3.connect('userData.db')
    c = conn.cursor()


    # c.execute("""CREATE TABLE list(
    #     email text,
    #     task text
    # )""")
    conn.commit()
    conn.close()

    

    root.mainloop()




    
