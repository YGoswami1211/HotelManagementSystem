from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import sqlalchemy as sqlc
from sqlalchemy import create_engine
import pandas as pd
import mysql.connector

#from roombooking import room_booking

class room_booking:
    def __init__(self,root):
        self.root=root
        self.root.title("Radisson Group of Hotels")
        self.root.geometry("1127x550+230+220")
        
        #declaring variables for table
        self.var_contact_number=StringVar()
        self.var_Checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_RoomType=StringVar()
        self.var_avl_rooms=StringVar()
        self.var_meals=StringVar()
        self.var_NOD=StringVar()
        self.var_paidTax=StringVar()
        self.var_subTotal=StringVar()
        self.var_Total=StringVar()
        
        
        # Create a label widget
        label = Label(root, text="Welcome to Raddison Blu Group of Hotels")
        label.pack()
        
        lbl_title = Label(self.root, text="RoomBooking Details", font=("Times New Roman", 20, "bold"),bg="black", fg="yellow", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=20, width=1290, height=40)
        #Logo
        #logo_image = Image.open(r"D:\Hotel Management System\Images\logo-radisson-blu.png")
        #logo_image = logo_image.resize((100, 40))
        #self.logo_photo = ImageTk.PhotoImage(logo_image)

        #logo_label = Label(self.root, image=self.logo_photo, bd=0, relief=RIDGE)
        #logo_label.place(x=5, y=25, width=100, height=65)
        
        # RoomBooking MainFrame
        label_frame_left = LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Details", font=("Times New Roman", 12, "bold"), padx=2)
        label_frame_left.place(x=5, y=60, width=380, height=415)
        
        #Room Booking Menu
        
        lbl_Phn=Label(label_frame_left,text="Contact Number :",font=("segoi ui",10,"bold"),fg="black")
        lbl_Phn.place(x=10,y=20)
        
        lbl_Phn_Entry=ttk.Entry(label_frame_left,textvariable=self.var_contact_number,font=("segoi ui",10,"bold"))
        lbl_Phn_Entry.place(x=130,y=20)
        
        
        btn_phn_entry=Button(label_frame_left,command=self.fetch_data,text="Fetch Data",bd=1,fg="black")
        btn_phn_entry.place(x=280,y=20)
        
        
        lbl_checkin=Label(label_frame_left,text="Check-In :",font=("segoi ui",10,"bold"),fg="black")
        lbl_checkin.place(x=10,y=50)
        
        lbl_checkin_Entry=ttk.Entry(label_frame_left,font=("segoi ui",10,"bold"))
        lbl_checkin_Entry.place(x=130,y=50)
        
        lbl_checkout=Label(label_frame_left,text="Check-Out :",font=("segoi ui",10,"bold"),fg="black")
        lbl_checkout.place(x=10,y=80)
        
        lbl_checkout_Entry=ttk.Entry(label_frame_left,font=("segoi ui",10,"bold"))
        lbl_checkout_Entry.place(x=130,y=80)
        
        lbl_RoomType=Label(label_frame_left,text="Room Type",font=("segoi ui",10,"bold"),fg="black")
        lbl_RoomType.place(x=10,y=110)
        
        lbl_RoomType_Entry=ttk.Combobox(label_frame_left,font=("segoi ui",10,"bold"),state="readonly")
        lbl_RoomType_Entry["value"]=("Single","Executive","Executive Suite")
        lbl_RoomType_Entry.place(x=130,y=110)
        
        lbl_avl_rooms=Label(label_frame_left,text="Available Rooms :",font=("segoi ui",10,"bold"),fg="black")
        lbl_avl_rooms.place(x=10,y=140)
        
        lbl_avl_rooms_Entry=ttk.Entry(label_frame_left,font=("segoi ui",10,"bold"))
        lbl_avl_rooms_Entry.place(x=130,y=140)
        
        lbl_meals=Label(label_frame_left,text="Meals :",font=("Segoi ui",10,"bold"),fg="black")
        lbl_meals.place(x=10,y=170)
        
        lbl_meals_Entry=ttk.Entry(label_frame_left,font=("segoi ui",10,"bold"))
        lbl_meals_Entry.place(x=130,y=170)
        
        lbl_NOD=Label(label_frame_left,text="No. Of Days :",font=("segoi ui",10,"bold"),fg="black")
        lbl_NOD.place(x=10,y=200)
        
        lbl_NOD_Entry=ttk.Entry(label_frame_left,font=("segoi ui",10,"bold"))
        lbl_NOD_Entry.place(x=130,y=200)
        
        lbl_paidTax=Label(label_frame_left,text="Paid Tax :",font=("segoi ui",10,"bold"),fg="black")
        lbl_paidTax.place(x=10,y=230)
        
        lbl_paidTax_Entry=ttk.Entry(label_frame_left,font=("segoi ui",10,"bold"))
        lbl_paidTax_Entry.place(x=130,y=230)
        
        lbl_subTotal=Label(label_frame_left,text="Sub Total :",font=("segoi ui",10,"bold"),fg="black")
        lbl_subTotal.place(x=10,y=260)
        
        lbl_subTotal_Entry=ttk.Entry(label_frame_left,font=("segoi ui",10,"bold"))
        lbl_subTotal_Entry.place(x=130,y=260)
        
        lbl_Total=Label(label_frame_left,text="Total Cost :",font=("segoi ui",10,"bold"),fg="black")
        lbl_Total.place(x=10,y=290)
        
        lbl_Total_Entry=ttk.Entry(label_frame_left,font=("segoi ui",10,"bold"))
        lbl_Total_Entry.place(x=130,y=290)
        
        
        cal_btn=Button(label_frame_left,text="Calculate Bill",font=("segoi ui",10,"bold"),fg="black",bd="1")
        cal_btn.place(x=10,y=320)
        
        # Creating Buttons for Other Fxn:
        
        
        btn_frame=Frame(label_frame_left,bd=4,relief=RIDGE)
        btn_frame.place(x=40,y=350,width=245,height=32)
        
        btnAdd= Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold")
        btnAdd.grid(row=0,column=0)
        
        btnUpdate= Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold")
        btnUpdate.grid(row=0,column=1)
        
        btnDelete= Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold")
        btnDelete.grid(row=0,column=2)
        
        btnReset= Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold")
        btnReset.grid(row=0,column=3)
        
        
        #MainFrame For right side Window 
        
        right_frame=LabelFrame(self.root,text="View Details And Search System",font=("segoi ui",10,"bold"),fg="black",bd=3)
        right_frame.place(x=400,y=275,height=200,width=725)
        
        lbl_searchby=Label(right_frame,text="SearchBy",font=("segoi ui",10,"bold","bold"),fg="black",bg="lightblue",bd=1)
        lbl_searchby.place(x=7,y=5)
        
        combo_searchby=ttk.Combobox(right_frame,font=("segoi ui",10,"bold"),state="readonly")
        combo_searchby.place(x=90,y=5)
        combo_searchby["value"]=("Select","Mobile Number","Refrence id")
        combo_searchby.current(0)
        
        txt_Entry=ttk.Entry(right_frame,font=("segoi ui",10,"bold"))
        txt_Entry.place(x=265,y=5)
        
        txt_btn1=Button(right_frame,text="Search",font=("segoi ui",9,"bold"),fg="black",bg="lightblue",bd=1)
        txt_btn1.place(x=430,y=5)
        
        txt_btn2=Button(right_frame,text="Show All",font=("segoi ui",9,"bold"),fg="black",bg="lightblue",bd=1)
        txt_btn2.place(x=490,y=5)
        
        #Data Table 
        
        data_tab=Frame(right_frame,bd=3,relief=RIDGE)
        data_tab.place(x=5,y=30,height=145,width=710)
        
        scroll_x=ttk.Scrollbar(data_tab,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(data_tab,orient=VERTICAL)
        
        self.room_details_tab=ttk.Treeview(data_tab,column=("Mobile Number","Check-In","Check-Out","Room Type","Room Number","Meals","NOD"))
        scroll_y.pack(side=BOTTOM,fill=X)
        scroll_x.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_details_tab.xview)
        scroll_y.config(command=self.room_details_tab.yview)
        
        self.room_details_tab.heading("Mobile Number",text="Mobile Number")
        self.room_details_tab.heading("Check-In",text="Check-In")
        self.room_details_tab.heading("Check-Out",text="Check-Out")
        self.room_details_tab.heading("Room Type",text="Room Type")
        self.room_details_tab.heading("Room Number",text="Room Number")
        self.room_details_tab.heading("Meals",text="Meals")
        self.room_details_tab.heading("NOD",text="NOD")
        
        
        self.room_details_tab["show"] = "headings"
        self.room_details_tab.pack(fill=BOTH, expand=1)
        
        self.room_details_tab.column("Mobile Number",width=100)
        self.room_details_tab.column("Check-In",width=100)
        self.room_details_tab.column("Check-Out",width=100)
        self.room_details_tab.column("Room Type",width=100)
        self.room_details_tab.column("Room Number",width=100)
        self.room_details_tab.column("Meals",width=100)
        self.room_details_tab.column("NOD",width=100)
        
        self.room_details_tab.pack(fill=BOTH, expand=1)    
        
        
        
        
    def fetch_data(self):
        if self.var_contact_number.get()=="":
            messagebox.showerror("error","Please Enter Contact Number",parent=self.root)
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="Addi$12112021",database="hotelmanagementsystem")
            my_cursor=con.cursor()
            query=("select Name from hotel where Mobile=%s")
            value=(self.var_contact_number.get(),)
            my_cursor.execute(query,value)
            
            row = my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("error","This Number is not found",parent=self.root)
            else:
                con.commit()
                con.close()
                
                #Creating a Data Frame:
                showDataFrame=Frame(self.root,bd=4,relief=RIDGE)
                showDataFrame.place(x=400,y=70,width=325,height=180)
                
                
                lblName=Label(showDataFrame,text="Name :",font=("segoi ui",12,"bold"))
                lblName.place(x=0,y=0)
                
                lbl=Label(showDataFrame,text=row,font=("segoi ui",12,"bold"))
                lbl.place(x=90,y=0)
             
       
                

                
            
            
 
                
                
         
            
        
        
           
        
        
        
        
        
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    
    root = Tk()
    app = room_booking(root)
    root.mainloop()
