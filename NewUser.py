from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import Checkbutton
from tkinter import messagebox

class NewUser:
    def __init__(self,root):
        self.root=root
        self.root.title("New User")
        self.root.geometry("1600x900+0+0")
      
        #BackGround Image
        img=Image.open(r"D:\Hotel Management System\Images\hotel images\sa_pixar_virtualbg_bugslife_16x9_d75b729e.jpeg")
        img=img.resize((1600,900))
        self.img=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.img)
        lbl_img.place(x=0,y=0,relheight=1,relwidth=1)
        
        #Second Image
        
        img2=Image.open(r"D:\Hotel Management System\Images\hotel images\developer.jpg")
        img2=img2.resize((350,450))
        self.img2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(self.root,image=self.img2)
        lbl_img2.place(x=100,y=125)
        
        #Frame
        
        new_frame=Frame(self.root,bg="white")
        new_frame.place(x=455,y=125,height=454,width=700)
        
        lbl_frame=Label(new_frame,text="New User Registration",font=("Segoi ui",15,"bold"),fg="black",bg="white",padx=2,pady=6)
        lbl_frame.place(x=0,y=5,height=40,width=270)
        
        #  Row 1 Containing First and Last name 
        
        first_name=Label(new_frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        first_name.place(x=30,y=70)
        
        self.first_name_entry=ttk.Entry(new_frame,font=("segoi ui",12,"bold"))
        self.first_name_entry.place(x=30,y=100,width=200)
        
        last_name=Label(new_frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        last_name.place(x=400,y=70)
        
        self.last_name_entry=ttk.Entry(new_frame,font=("segoi ui",12,"bold"))
        self.last_name_entry.place(x=400,y=100,width=200)
        
        # Row 2 Containing contact number and email
        contact_num=Label(new_frame,text="Contact Number",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact_num.place(x=3,y=130, width=200)
        
        self.contact_entry=ttk.Entry(new_frame,font=("segoi ui",12,"bold"))
        self.contact_entry.place(x=30,y=160,width=200)
        
        email_id=Label(new_frame,text="Email Id",font=("times new roman",15,"bold"),fg="black",bg="white")
        email_id.place(x=340,y=130,width=200)
        
        self.email_entry=ttk.Entry(new_frame,font=("segoi ui",12,"bold"))
        self.email_entry.place(x=400,y=160,width=200)
        
        #Row 3 Security Questions and Answers 
        sec_ques=Label(new_frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
        sec_ques.place(x=15,y=190,width=250)
        
        combo_ques=ttk.Combobox(new_frame,font=("times new roman",12,"bold"),width=20,state="readonly")
        combo_ques["value"]=("Select","What is your Childhood Name","Who is Your Childhood Friend Name","Who is Your Fav Pet")
        combo_ques.place(x=30,y=220,width=200)
        combo_ques.current(0)
        
        answer=Label(new_frame,text="Security Ques Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        answer.place(x=395,y=190,width=200)
        
        self.answer=ttk.Entry(new_frame,font=("segoi ui",12,"bold"))
        self.answer.place(x=400,y=220,width=200)
        
        
        # Row 4 Password and confirm Password
        password=Label(new_frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=30,y=250)
        
        self.password=ttk.Entry(new_frame,font=("segoi ui",12,"bold"),show="*")
        self.password.place(x=30,y=280,width=200)
        
        con_password=Label(new_frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        con_password.place(x=400,y=250)
        
        self.con_password=ttk.Entry(new_frame,font=("segoi ui",12,"bold"),show="*")
        self.con_password.place(x=400,y=280,width=200)
        
        
        # Row 5 Agree Terms and conditions 
        self.var_checkbtn=IntVar()
        self.checkbtn=Checkbutton(new_frame,text="I agree all terms and conditions",font=("times new roman",15,"bold"),fg="red",bg="white",onvalue=1,offvalue=0)
        self.checkbtn.place(x=30,y=310)
        
        
        #Row 6 Buttons
        btn_img=Image.open(r"D:\Hotel Management System\Images\hotel images\register-now-button1.jpg")
        btn_img=btn_img.resize((200,55))
        self.btn_img=ImageTk.PhotoImage(btn_img)
        b1=Button(new_frame,image=self.btn_img,borderwidth=0,cursor="hand2",font=("segoi ui",15,"bold"),fg="black",bg="white")
        b1.place(x=10,y=340,width=200)
        
        btn_img2=Image.open(r"D:\Hotel Management System\Images\hotel images\unnamed.png")
        btn_img2=btn_img2.resize((200,45))
        self.btn_img2=ImageTk.PhotoImage(btn_img2)
        b2=Button(new_frame,image=self.btn_img2,borderwidth=0,cursor="hand2",font=("segoi ui",15,"bold"),fg="black",bg="white")
        b2.place(x=400,y=340,width=200)     
        

        
    
        
    
if __name__=="main":
    root=Tk()
    app=NewUser(root)
    root.mainloop()
    
    
        
        
        

        
        
