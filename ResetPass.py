from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox



class ForgotPassword():
    def __init__(self,root):
        self.root=root
        self.root.title("Forgot Password")
        self.root.geometry("720x500+0+0")
        
        #Main Image
        img=Image.open(r"D:\Hotel Management System\Images\hotel images\developer.jpg")
        img=img.resize((720,500))
        self.img=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.img)
        lbl_img.place(x=0,y=0,relheight=1,relwidth=1)
        
        #mainFrame
        #root.wm_attributes('-transparentcolor','red')
        #frame=Frame(self.root,bg="red")
        #frame.place(x=10,y=20,height=200,width=400)
        #root.attributes('-alpha',0.5)
        
        
        
        #Creating a frame for forgot window
        Pass_frame=Frame(self.root,bg="white",height=300,width=250)
        Pass_frame.place(x=225,y=40)
        #Pass_frame.configure()
        #Now Creating a Label For Forgotting Password
        
        lbl_Pass=Label(Pass_frame,text="Forgot Password",font=("segoi ui",12,"bold"),fg="black",bg="white")
        lbl_Pass.place(x=60,y=10)
        
        # Row 1  Select Security Questions
        
        lbl_secq=Label(Pass_frame,text="Select Security Question *",font=("segoi ui",12,"bold"),padx=2,pady=6,fg="black",bg="white")
        lbl_secq.place(x=10,y=30)
        
        
        self.com_secq=ttk.Combobox(Pass_frame,font=("segoi ui",12,"bold"),state="readonly")
        self.com_secq.place(x=10,y=70)
        
        self.com_secq["value"]=("Select","What is your Childhood Name","Who is Your Childhood Friend Name","Who is Your Fav Pet")
        self.com_secq.current(0)
        
        # Row 2 Enter Your New Password
        
        lbl_newPass=Label(Pass_frame,text="Enter New Password",font=("segoi ui",12,"bold"),fg="black",bg="white",padx=2,pady=6)
        lbl_newPass.place(x=10,y=100)
        
        self.lbl_newPass_Entry=ttk.Entry(Pass_frame,font=("segoi ui",10,"bold"),show="*",width=28)
        self.lbl_newPass_Entry.place(x=10,y=130)
        
        #Row 3 Confirm Password
        
        lbl_conf_Pass=Label(Pass_frame,text="Confirm Password",font=("segoi ui",12,"bold"),padx=2,pady=6,fg="black",bg="white")
        lbl_conf_Pass.place(x=10,y=160)
        
        self.lbl_conf_Pass_entry=ttk.Entry(Pass_frame,font=("segoi ui",10,"bold"),show="*",width=28)
        self.lbl_conf_Pass_entry.place(x=10,y=190)
        
        #Row 4 Creating a reset Button 
        
        res_img=Image.open(r"D:\Hotel Management System\Images\download.jpeg") 
        res_img=res_img.resize((200,55))
        self.res_img=ImageTk.PhotoImage(res_img)
        b1=Button(Pass_frame,image=self.res_img,command=self.reset,borderwidth=0,cursor="hand2",font=("segoi ui",15,"bold"),fg="black",bg="white")
        b1.place(x=45,y=230,width=150)
        
    def reset(self):
        if self.com_secq.get()=="":
            messagebox.showerror("error","All Fields are Mandatory")
        elif self.lbl_newPass_Entry.get()!=self.lbl_conf_Pass_entry.get():
            messagebox.showerror("error","Password must be same")
        else:
            messagebox.showinfo("success","Password Successfully changed")
            
            
        
        
        

        
        
        
        
        
        
        
if __name__=="__main__":
    root = Tk()
    app=ForgotPassword(root)
    root.mainloop()