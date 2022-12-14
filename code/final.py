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
    
    ourEmail = signIn.givenEmail
    ourName = signIn.firstName
    

    
    def clearlistbox():
        lbltask.delete(0, "end")


    def updatetask():
        clearlistbox()
        conn = sqlite3.connect("userData.db")

        c = conn.cursor()

        c.execute(f"SELECT * FROM list WHERE email='{ourEmail}'")
        records = c.fetchall()
        global tasks
        tasks = []

        for record in records:
            tasks.append(record[1])

        conn.commit()
        conn.close()

        for utask in tasks:
            lbltask.insert("end", utask)
        numtask = len(tasks)
        lbldsp_count['text'] = numtask

    
    def addtask():
        
        lbldisplay["text"] = ""
        newTask = txtinput.get()
        if newTask != "":
            # tasks.append(newTask)
            conn = sqlite3.connect("userData.db")
            c = conn.cursor()

            c.execute("INSERT INTO list VALUES(:email,:task)",{
                'email':ourEmail,
                'task':txtinput.get()
            })

            conn.commit()
            conn.close() 
            updatetask()
        else:
            lbldisplay["text"] = "please enter the text"
        txtinput.delete(0, 'end')
        
        
        
    def deleteone():
        delt = lbltask.get("active")
        

        if "'" in delt:
            ourIndex = delt.index("'")
            letters = list(delt)   
            letters.insert(ourIndex,"\\")
            delt = "".join(letters)
            



        conn = sqlite3.connect("userData.db")

        c = conn.cursor()
        c.execute(f'DELETE FROM list WHERE task="{delt}"')
        
        conn.commit()
        conn.close()
        if delt in tasks:
            tasks.remove(delt)
        updatetask()

    def editTask():
        editor = Tk()
        editor.title("Edit task")
        editor.geometry("300x100+50+50")

        editInput = tkinter.Entry(editor,width=10,font=("Verdana",14))
        editInput.pack()
        delt = lbltask.get("active")
        print(delt)

        if "'" in delt:
            ourIndex = delt.index("'")
            letters = list(delt)   
            letters.insert(ourIndex,"\\")
            delt = "".join(letters)

        def save():
            newValue = editInput.get()
            conn = sqlite3.connect("userData.db")
            print(newValue)
            c = conn.cursor()

            c.execute(f"""UPDATE list SET 
                task=:newTask
                WHERE task = '{delt}'
            """,{
                'newTask':newValue
            })

            conn.commit()
            conn.close()
            updatetask()
            editor.destroy()
            
        saveBtn = Button(editor,text="Save",command=save)
        saveBtn.pack()
        
            
    def numbertsk():
        numtask = len(tasks)
        lbldisplay["text"] = numtask



    def exitapp():
        confex = messagebox.askquestion(
            'Quit confirmation', 'Are you sure you want to quit?')
        if confex.upper() == "YES":
            root.destroy()
        else:
            pass
    
    lbltitle = tkinter.Label(root, text=f"{ourName.title()}", bg="#C0D7DF",fg="black",font=('Plateaux',60))
    lbltitle.place(x=550,y=130)

    newtitle = tkinter.Label(root,text="Welcome!",bg="#C0D7DF",fg="black",font=("Plateaux",60))
    newtitle.place(x=550,y=50)

    
    yourTask = tkinter.Label(root,text="Your tasks:",bg="#CDDBDE",font=('Plateaux',40),fg='black')
    yourTask.place(x=800,y=315)

    lbltask = tkinter.Listbox(root,width=25,height=9,font=('Verdana',20),border=2,background="white",relief="solid")
    lbltask.place(x=800,y=374)
    
    lbltitle2 = tkinter.Label(root,text='Enter Task Title :',bg='#D1DFE0',font = ('Plateaux',20))
    lbltitle2.place(x=500,y = 330)

    lbldsp_count = tkinter.Label(root, text="", bg="white",border=0,background="#D8E1E0",width=3,height=2)
    lbldsp_count.place(x = 460,y = 580)
    
    lbldisplay = tkinter.Label(root, text="0", bg="white",font=('italica',12),background='#C5D8DE')
    lbldisplay.place(x=1215,y = 353)

    txtinput = tkinter.Entry(root,width=20,font=("Verdana",14),relief='solid',border=2)
    txtinput.place(x=500,y=380)

    txtadd_button = tkinter.Button(
        root, text="Add To Do", bg="white", fg="black", width=15, command=addtask,font=('Verdana',10),padx=58,border=4)
    txtadd_button.place(x=500,y=430)

    edit_button = tkinter.Button(
        root, text="Edit", bg="white", fg="black", width=15, command=editTask,font=('Verdana',10),padx=58,border=4)
    edit_button.place(x=500,y=480)


    delonebutton = tkinter.Button(
        root, text="Done Task", bg="white", width=15, command=deleteone,font=('Verdana',10),padx=58,border=4)
    delonebutton.place(x=500,y=530)

    numbertsk = tkinter.Button(
        root, text="Number of Task", bg="white", width=15, command=numbertsk,font=('Verdana',10),padx=58,border=4)
    numbertsk.place(x=500,y=580)

    exitbutton = tkinter.Button(root, text="exit app",
                            bg="white", width=15, command=exitapp,font=('Verdana',10),padx=58,border=4)
    exitbutton.place(x=500,y=630)

    

    root.mainloop()




    
