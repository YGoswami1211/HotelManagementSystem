from tkinter import*
import tkinter as  ttk
#from PIL import imageTk,Image

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1600x900+0+0")
        
        font_style=("segoi ui",12,"bold")
        
        
        #user name information
        
        frame=Frame(self.root,height=200,width=500,bg="white",bd=1)
        frame.place(x=500,y=100)
        
        new_user=Label(frame,text="New User Registration",font=font_style,bg="white",fg="black")
        new_user.place(x=40,y=12)
        
        
        
        #First Name:
        
        first_name=Label(frame,text="First Name",font=font_style,bg="white",fg="black")
        first_name.place(x=40,y=50)
        
        
        first_name_entry=ttk.Entry(frame,font=font_style)
        first_name_entry.place(x=40,y=80,width=200)
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    app=login(root)
    root.mainloop()
    
        