from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from sourcecode import HotelManagementSystem
from Rwin import Register 
from ResetPass import ForgotPassword
from sourcecode import HotelManagementSystem



class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        #Declaring Variables 
        self.var_Username=StringVar()
        self.var_Password=StringVar()
        
        
        self.bg=ImageTk.PhotoImage(file=r"D:\Hotel Management System\Images\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        
        login_img = Image.open(r"D:\Hotel Management System\Images\Capture.PNG")
        login_img = login_img.resize((830, 624))
        
        self.photologin_img = ImageTk.PhotoImage(login_img)
        lbl_login_img = Label(self.root, image=self.photologin_img, borderwidth=0)
        lbl_login_img.place(x=275, y=50)
        
        sec_img=Image.open(r"D:\Hotel Management System\Images\strip.PNG")
        sec_img=sec_img.resize((365,35))
        self.photosec_img=ImageTk.PhotoImage(sec_img)
        lbl_sec_img=Label(self.root,image=self.photosec_img,borderwidth=0)
        lbl_sec_img.place(x=505,y=550)
        
        #creating entry for Username:
        self.txtuser=ttk.Entry(font=("segoi ui light",15))
        self.txtuser.place(x=536,y=332,width=306,height=40)
        
        
        #creating entry for password:
        self.txtPass = ttk.Entry( font=("segoi ui light",15),show="*")
        self.txtPass.place(x=536, y=385, width=306,height=40)

        #Login Button
        
        btn_Login=Button(text="LOGIN",command=self.login,font=("segoi ui light",13,"bold"),bg="darkorchid",fg="white")
        btn_Login.place(x=540,y=443,width=302,height=36)
        
        #Forgot Password
        
        btn_forgot=Button(text="Forgot Password",command=self.ResetPass,font=("segoi ui",10,"bold"),bg="slategray3",fg="black",activebackground="slategray3")
        btn_forgot.place(x=720,y=488,height=36,width=110)
        
        #New User
        
        btn_NewUser=Button(text="New User",command=self.Rwin,font=("segoi ui",10,"bold"),bg="slategray3",fg="black",activebackground="slategray3")
        btn_NewUser.place(x=542,y=488,height=36,width=110)
        
        
        
        
        
    def login(self):
        if self.txtuser.get()=="" or self.txtPass.get()=="":
            messagebox.showerror("error","All Fields are mandatory")
        elif self.txtuser.get()=="Yash$1211" or self.txtPass.get()=="Addi$1211":
            messagebox.showinfo("Success","welcome to Blu Group of resorts")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="Addi$12112021",database="hotelmanagementsytem")
            my_cursor=conn.connect()
            my_cursor.execute("Select * from login where Username=%s and Password=%s",(self.var_Username.get(),self.var_Password.get()))
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("Yes or No","Access Admin only")
                if open_main>0:
                    self.new_main_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_main_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
        
            
    def Rwin(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    def ResetPass(self):
        self.new_win=Toplevel(self.root)
        self.app=ForgotPassword(self.new_win)
        
    
                
            
                
        
        
if __name__ == "__main__":
    root = Tk()
    app = login_window(root)
    root.mainloop()



