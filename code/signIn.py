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

userEmails = []

conn = sqlite3.connect("userData.db")

c = conn.cursor()

c.execute("SELECT *, oid FROM users")
ourRecord = c.fetchall()

for record in ourRecord:
   userEmails.append(record[2])

print(userEmails)
conn.close()


def loginValidity():
   global givenEmail
   givenEmail = emailBox.get()
   givenPassword = passwordBox.get()

   if(givenEmail in userEmails):
         conn = sqlite3.connect("userData.db")
         c = conn.cursor()

         c.execute(f"SELECT * FROM users WHERE email='{givenEmail}'")
         
         
         currentRecord = c.fetchall()
         global firstName
         firstName = currentRecord[0][0]

         currentPassword = currentRecord[0][3] 

         if(givenPassword==currentPassword):
            messagebox.showinfo("Success","Logged in successfully")
            root.destroy()
            final.openWindow()
         else:
            messagebox.showinfo("Error","Wrong credentials entered")   
         conn.commit()
         conn.close()
   else:
         messagebox.showinfo("Error","Please enter a valid email address") 



loginBtn = Button(centerFrame,borderwidth=0,text="Login",bg="#0c8599",fg="white",padx=50,command=loginValidity)
loginBtn.place(y=340,x=880)


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


def deleteUser():
      editor = Tk()
      editor.title("Edit task")
      editor.geometry("300x140+100+50")


      emailLabel = Label(editor,text="Enter your email")
      emailLabel.pack()    

      editInput = Entry(editor,width=10,font=("Verdana",14))
      editInput.pack()

      passwordLabel = Label(editor,text="Enter your password")
      passwordLabel.pack()    

      passInput = Entry(editor,width=10,font=("Verdana",14))
      passInput.pack()
   
      def save():
               newEmailValue = editInput.get()
               givenPassword = passInput.get()

               if (newEmailValue in userEmails ):
                  conn = sqlite3.connect("userData.db")
                  c = conn.cursor()
                  c.execute(f"SELECT * FROM users WHERE email='{newEmailValue}'")
                  currentRecord = c.fetchall()

                  c.execute(f'DELETE FROM users WHERE email="{newEmailValue}"')


                  currentPassword = currentRecord[0][3] 
               try:
                  if(givenPassword==currentPassword):
                     conn.commit()
                     conn.close()     
                     messagebox.showinfo("Success","User Deleted")
                     editor.destroy()
               except:
                     messagebox.error("Error","Wrong credentials entered")   
               else:
                  messagebox.showinfo("Error","Invalid Email Address")
      saveBtn = Button(editor,text="Okay",command=save)
      saveBtn.pack()




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


# code to show up a new window and various widgets for the signup form
def signUp():


   
   top = Toplevel()
   top.title("Sign Up Form")
   top.geometry("600x700+100+50")
   top.config(bg="#fff")
   bgcolor="red"
   signUpFrame = LabelFrame(top,width=300,height=500,bg="#f1f3f5")
   signUpFrame.place(x=150,y=100)

   # inserting various widgets into the sign up form
   fName = Label(signUpFrame,text="First Name",bg="#f1f3f5")
   fName.place(x=30,y=25)

   fNameBox = Entry(signUpFrame,width=30,border=0,bg='#f1f3f5')
   fNameBox.place(x=30,y=50)

   Frame(signUpFrame, width=200, height=2, bg='black').place(x=30, y=68)

   lName = Label(signUpFrame,text="Last Name",bg="#f1f3f5")
   lName.place(x=30,y=75)

   lNameBox = Entry(signUpFrame,width=30,border=0,bg='#f1f3f5')
   lNameBox.place(x=30,y=100)

   Frame(signUpFrame, width=200,height=2,bg='black').place(x=30,y=118)
   
   newEmail = Label(signUpFrame,text="Email",bg="#f1f3f5")
   newEmail.place(x=30,y=125)

   newEmailBox = Entry(signUpFrame,width=30,border=0,bg='#f1f3f5')
   newEmailBox.place(x=30,y=150)
   
   Frame(signUpFrame, width=200,height=2,bg='black').place(x=30,y=168)

   newPassword = Label(signUpFrame,text="New Password",bg="#f1f3f5")
   newPassword.place(x=30,y=175)

   newPasswordBox = Entry(signUpFrame,width=30,border=0,bg='#f1f3f5')
   newPasswordBox.place(x=30,y=200)
   
   Frame(signUpFrame, width=200,height=2,bg='black').place(x=30,y=218)
   
   confirmNewPassword = Label(signUpFrame,text="Confirm new password",bg="#f1f3f5")
   confirmNewPassword.place(x=30,y=225)

   confirmNewPasswordBox = Entry(signUpFrame,width=30,border=0,bg='#f1f3f5')
   confirmNewPasswordBox.place(x=30,y=250)

   Frame(signUpFrame, width=200,height=2,bg='black').place(x=30,y=268)


   
   def registerUser():
      conn = sqlite3.connect("userData.db")

      c = conn.cursor()
      if (newPasswordBox.get()==confirmNewPasswordBox.get()):

         c.execute("INSERT INTO users VALUES(:f_name,:l_name,:email,:password)",{
            'f_name':fNameBox.get(),
            'l_name':lNameBox.get(),
            'email':newEmailBox.get(),
            'password':confirmNewPasswordBox.get()
         })
         conn.commit()
         conn.close()

         fNameBox.delete(0,END)
         lNameBox.delete(0,END)
         newEmailBox.delete(0,END)
         newPasswordBox.delete(0,END)
         confirmNewPasswordBox.delete(0,END)
         messagebox.showinfo("Success!","Signed up successfully")

         top.destroy()
      else:
         messagebox.showinfo("Error","Password don't match. Please try again!")   

   signBtn = Button(signUpFrame,text="SignUp",bg="#12b886",fg="white",padx=50,command=registerUser)
   signBtn.place(x=51,y=300)





noAccountOne = Label(centerFrame,text="Don't have an account?")
noAccountOne.place(x=880,y=400)

# creating a sign up button
signUpBtn = Button(centerFrame,command=signUp,text="SignUp",fg="blue",bg="#f1f3f5",borderwidth=0)
signUpBtn.place(x=920,y=430)




root.mainloop()