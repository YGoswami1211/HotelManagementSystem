from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import sqlalchemy as sqlc
import pandas as pd
import mysql.connector






class cust_win:
    
    def __init__(self, root):
        
        global x
        self.root = root
        self.root.title("Raddison Blu Group of Hotels")
        self.root.geometry("1132x520+220+205")
        
        #Variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_idProof=StringVar()
        self.var_Iden_Number=StringVar()
        self.var_nationality=StringVar()
        self.var_email_id=StringVar()
        self.var_mobile_number=StringVar()
        self.var_address=StringVar()
        
        
        
        
        # Create a label widget
        label = Label(root, text="Welcome to Blu Group of Resorts")
        label.pack()
        
        lbl_title = Label(self.root, text="Customer Details", font=("Times New Roman", 40, "bold"),bg="lightblue", fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=20, width=1290, height=50)
        
        #Logo
        logo_image = Image.open(r"D:\Hotel Management System\Images\download.png")
        logo_image = logo_image.resize((100, 40))
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = Label(self.root, image=self.logo_photo, bd=0, relief=RIDGE)
        logo_label.place(x=5, y=25, width=100, height=40)
        
        # Customer MainFrame
        label_frame_left = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("Times New Roman", 12, "bold"), padx=2)
        label_frame_left.place(x=5, y=70, width=400, height=430)
        
        #Labels And Entries
        #custRef:
        label_cust_ref=Label(label_frame_left,text="Customer Ref :",font=("arial",12,"bold"),padx=2,pady=6)
        label_cust_ref.grid(row=0,column=0,sticky=W)
        
        cust_entry=ttk.Entry(label_frame_left,textvariable=self.var_ref,width=25,font=("arial",10,"bold"))
        cust_entry.grid(row=0,column=1)
        
        #CustName
        cust_name = Label(label_frame_left, text="Customer Name :", font=("arial", 12, "bold"), padx=2, pady=6)
        cust_name.grid(row=1, column=0, sticky=W)  

        txtcust_name = ttk.Entry(label_frame_left,textvariable=self.var_cust_name, width=25, font=("arial", 10, "bold"))
        txtcust_name.grid(row=1, column=1) 
        
        #Fathers Name
        Fath_name = Label(label_frame_left, text="Father's Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        Fath_name.grid(row=2, column=0, sticky=W) 

        txtFath_name = ttk.Entry(label_frame_left,textvariable=self.var_father_name, width=25, font=("arial", 10, "bold"))
        txtFath_name.grid(row=2, column=1) 
        #Gender 
        cust_gen=Label(label_frame_left,text="Gender :",font=("arial",12,"bold"),padx=2,pady=6)
        cust_gen.grid(row=3,column=0,sticky=W) 
        combo_gen=ttk.Combobox(label_frame_left,textvariable=self.var_gender,font=("arial",10,"bold"),width=23,state="readonly")
        combo_gen["value"]=("Male","Female","Other")
        combo_gen.grid(row=3,column=1)
        #id proof type
        id_proof = Label(label_frame_left, text="id Proof Type :", font=("arial", 12, "bold"), padx=2, pady=6)
        id_proof.grid(row=4, column=0, sticky=W)
        
        combo_id=ttk.Combobox(label_frame_left,textvariable=self.var_idProof,font=("arial",10,"bold"),width=23,state="readonly")
        combo_id["value"]=("Passport","Aadhar Card","Ration Card","Driving Liscence","Any other id issue by the Government")
        combo_id.grid(row=4,column=1)

        
        
        #identification Number
        iden_num = Label(label_frame_left, text="Identification Number :", font=("arial", 12, "bold"), padx=2, pady=6)
        iden_num.grid(row=5, column=0, sticky=W)

        txtiden_num = ttk.Entry(label_frame_left,textvariable=self.var_Iden_Number, width=25, font=("arial", 10, "bold"))
        txtiden_num.grid(row=5, column=1)
        #MobileNumber
        cust_mobile_num=Label(label_frame_left,text="Mobile Number :",font=("arial",12,"bold"),padx=2,pady=6)
        cust_mobile_num.grid(row=6,column=0,sticky=W)
        
        txtcust_mobile_num=ttk.Entry(label_frame_left,textvariable=self.var_mobile_number,width=25,font=("arial",10,"bold"))
        txtcust_mobile_num.grid(row=6,column=1)
        #Email id
        cust_email=Label(label_frame_left,text="E-mail id :",font=("arial",12,"bold"),padx=2,pady=6)
        cust_email.grid(row=7,column=0,sticky=W)
        
        txtcust_email=ttk.Entry(label_frame_left,textvariable=self.var_email_id,width=25,font=("arial",10,"bold"))
        txtcust_email.grid(row=7,column=1)
        #Nationality
        cust_nationality=Label(label_frame_left,text="Nationality :",font=("arial",12,"bold"),padx=2,pady=6)
        cust_nationality.grid(row=8,column=0,sticky=W)
        
        combo_nationality=ttk.Combobox(label_frame_left,textvariable=self.var_nationality,font=("arial",10,"bold"),width=23,state="readonly")
        combo_nationality["value"]=("Indian","Russian","Canadian")
        combo_nationality.grid(row=8,column=1)
        
        
        #Address
        cust_add=Label(label_frame_left,text="Address :",font=("arial",12,"bold"),padx=2,pady=6)
        cust_add.grid(row=9,column=0,sticky=W)
        
        txtcust_add=ttk.Entry(label_frame_left,textvariable=self.var_address,width=25,font=("arial",10,"bold"))
        txtcust_add.grid(row=9,column=1)
        
        #Button frame
        btn_frame=Frame(label_frame_left,bd=4,relief=RIDGE)
        btn_frame.place(x=75,y=360,width=245,height=32)
        
        btnAdd= Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold")
        btnAdd.grid(row=0,column=0)
        
        btnUpdate= Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold")
        btnUpdate.grid(row=0,column=1)
        
        btnDelete= Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold")
        btnDelete.grid(row=0,column=2)
        
        btnReset= Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold")
        btnReset.grid(row=0,column=3)
        
        #Table Frame
        tab_frame=LabelFrame(self.root,relief=RIDGE,text="View details and Search system", font=("arial",12,"bold"),padx=2)
        tab_frame.place(x=400,y=70,width=800,height=430)
        
        label_searchBy=Label(tab_frame,font=("arial",10,"bold"),text="Search By:",bg="red",fg="white")
        label_searchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        combo_searchBy=ttk.Combobox(tab_frame,font=("arial",10,"bold"),width=23,state="readonly")
        combo_searchBy["value"]=("Mobile Number","Refrence id")
        combo_searchBy.grid(row=0,column=1)
        
        txt_search=ttk.Entry(tab_frame,font=("arial",10,"bold"),width=23)
        txt_search.grid(row=0,column=2,padx=2)
        
        
        btn_search=Button(tab_frame,text="Search",font=("arial",8,"bold",),bg="blue",fg="black",width=10)
        btn_search.grid(row=0,column=3,padx=1)
        
        btn_showall=Button(tab_frame,text="Show All",font=("arial",8,"bold",),bg="blue",fg="black",width=10)
        btn_showall.grid(row=0,column=4,padx=1)
        
        #Data Table
        data_table=Frame(tab_frame,bd=4,relief=RIDGE)
        data_table.place(x=0,y=40,width=720,height=350)
        
        scroll_x=ttk.Scrollbar(data_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(data_table,orient=VERTICAL)
        
        self.cust_details_table=ttk.Treeview(data_table,column=("Ref id","Name","Father's Name","Gender","id ProofType","Id.Number","email id","Nationality","Mobile Number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)
        
        self.cust_details_table.heading("Ref id",text="Ref No")
        self.cust_details_table.heading("Name",text="Name")
        self.cust_details_table.heading("Father's Name",text="Father's Name")
        self.cust_details_table.heading("Gender",text="Gender")
        self.cust_details_table.heading("id ProofType",text="id Proof Type")
        self.cust_details_table.heading("Id.Number",text="identification Number")
        self.cust_details_table.heading("email id",text="email id")
        self.cust_details_table.heading("Nationality",text="Nationality")
        self.cust_details_table.heading("Mobile Number",text="Mobile Number")
        self.cust_details_table.heading("Address",text="Address")
        
        self.cust_details_table["show"] = "headings"
        self.cust_details_table.pack(fill=BOTH, expand=1)
        
        self.cust_details_table.column("Ref id",width=100)
        self.cust_details_table.column("Name",width=100)
        self.cust_details_table.column("Father's Name",width=100)
        self.cust_details_table.column("Gender",width=100)
        self.cust_details_table.column("id ProofType",width=100)
        self.cust_details_table.column("Id.Number",width=100)
        self.cust_details_table.column("Nationality",width=100)
        self.cust_details_table.column("email id",width=100)
        self.cust_details_table.column("Mobile Number",width=100)
        self.cust_details_table.column("Address",width=100)
        self.cust_details_table.pack(fill=BOTH, expand=1)
       # self.fetch_data()
        
        
        
    def add_data(self):
        if self.var_mobile_number.get() == "" or self.var_cust_name.get() == "":
            messagebox.showerror("Error", "All Fields are Mandatory")
        else:
            #try:
                conn = mysql.connector.connect(host="127.0.0.1",user="root",password="Addi$12112021",database="hotelmanagementsystem")
                my_cursor = conn.cursor()

            
                query = "INSERT INTO hotel VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                data = (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_idProof.get(),
                    self.var_Iden_Number.get(),
                    self.var_nationality.get(),
                    self.var_mobile_number.get(),
                    self.var_email_id.get(),
                    self.var_address.get()
             )

                my_cursor.execute(query, data)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "User Successfully Added", parent=self.root)
            #except Exception as es:
                #messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)


            
            
            
            
if __name__ == "__main__":
    root = Tk()
    app = cust_win(root)
    root.mainloop()


    
