import sqlite3
from tkinter import *
from tkinter import font
from tkinter import messagebox
from turtle import bgcolor, title
# import final


root = Tk()

# configuring some ui for the main window 

root.geometry("1200x700+100+50")
root.title("Todo Application")


# establishing a connection with the database
conn = sqlite3.connect("userData.db")

c = conn.cursor()


# c.execute("""CREATE TABLE users(
#    firstName text,
#    lastName text,
#    email text,
#    password text
# )""")

conn.commit()

conn.close()


# background image for the main window
bg = PhotoImage(file = "images/groundOne.png")




# spanning the background image all across the window
backgroundImg = Label(root,image=bg)
backgroundImg.place(x=0,y=0)

# creating a center frame for the login 
centerFrame = LabelFrame(root,width=300,height=500,bg='#f1f3f5').place(x=800,y=100)

# creating various labels and entry boxes for the login form
welcome = Label(centerFrame,text="Welcome!",bg='#f1f3f5')
welcome.config(font=("Helvetica",20))
welcome.place(x=885,y=110)

email = Label(centerFrame,text="Email",bg="#f1f3f5")
email.place(x=850,y=175)

emailBox = Entry(centerFrame,width=32,border=0,background='#f1f3f5')
emailBox.place(x=850,y=205)

Frame(centerFrame, width=200, height=2, bg='black').place(x=850, y=223)

password = Label(centerFrame,text="Password",bg="#f1f3f5")
password.place(x=850,y=240)

passwordBox = Entry(centerFrame,width=32,show='*',border=0,background='#f1f3f5')
passwordBox.place(x=850,y=270)

Frame(centerFrame,width=200,height=2,bg='black').place(x=850,y=287)


# function to show the hidden password
def showPassword():
   isChecked = checkVal.get()
   if (isChecked==1):
      passwordBox.config(show='')
   else:
      passwordBox.config(show='*')   

      
# show password checkbox
checkVal = IntVar()
showPassCheckbox = Checkbutton(centerFrame,text="",bg='#f1f3f5',variable=checkVal,onvalue=1,offvalue=0,command=showPassword)
showPassCheckbox.place(y=300,x=895)

showPassLabel = Label(centerFrame,text="Show Password",bg="#f1f3f5")
showPassLabel.place(y=301,x=910)




def changePassword():
      editor = Tk()
      editor.title("Change Password")  
      editor.geometry("300x200+100+50") 


      emailLabel = Label(editor,text="Enter your email")
      emailLabel.pack()      
      editInput = Entry(editor,width=10,font=("Verdana",14))
      editInput.pack()
      
   
      passwordLabel = Label(editor,text="Old password")
      passwordLabel.pack() 
      passInput = Entry(editor,width=10,font=("Verdana",14))
      passInput.pack()


      newPasswordLabel = Label(editor,text="New password")
      newPasswordLabel.pack() 
      newPassInput = Entry(editor,width=10,font=("Verdana",14))
      newPassInput.pack()

      def save():
         newEmailValue = editInput.get()
         givenPassword = passInput.get()
         newPassword = newPassInput.get()

         if (newEmailValue in userEmails ):
                  

            conn = sqlite3.connect("userData.db")
            c = conn.cursor()
            c.execute(f"SELECT * FROM users WHERE email='{newEmailValue}'")
            currentRecord = c.fetchall()
            currentPassword = currentRecord[0][3] 

         try:
            if(givenPassword==currentPassword):
               conn = sqlite3.connect("userData.db")
               c = conn.cursor()

               c.execute(f"""UPDATE users SET 
                        password=:newPassword
                        WHERE email = '{newEmailValue}'
                     """,{
                  'newPassword':newPassword
                  })
               messagebox.showinfo("Success","Password Changed!")
               editor.destroy()
         except:
               messagebox.showerror("Error","Wrong credentials entered")   
         else:
            messagebox.showinfo("Error","Invalid Email Address")
         conn.commit()
         conn.close()     



            
      saveBtn = Button(editor,text="Save",command=save)
      saveBtn.pack()





# Defining Some Buttons
changePassword = Button(centerFrame,command=changePassword,text="Change Password",bg="#0c8599",fg="white",padx=17)
changePassword.place(x=880,y=470)

deleteAccount = Button(centerFrame,
text='Delete Account',bg="#e03131",fg="#fff",padx=24,command=deleteUser)
deleteAccount.place(x=880,y=505)

noAccountOne = Label(centerFrame,text="Don't have an account?")
noAccountOne.place(x=880,y=400)

# creating a sign up button
signUpBtn = Button(centerFrame,command=signUp,text="SignUp",fg="blue",bg="#f1f3f5",borderwidth=0)
signUpBtn.place(x=920,y=430)




root.mainloop()