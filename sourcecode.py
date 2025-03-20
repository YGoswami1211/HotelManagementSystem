from tkinter import *
from PIL import ImageTk, Image
from customer import cust_win
import random
import sqlalchemy as sqlc
from roombooking import room_booking
from Details import Details








class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Blu Group of Resorts")
        self.root.geometry("1920x1080+0+0")
        

        # First Image (Banner)
        myImage = Image.open(r"D:\Hotel Management System\Images\1ADE85CD0AD8428AFA2DF0DD7C73E2D3B26709EA1644170105165.jpg")
        myImage = myImage.resize((1550, 140))
        self.photo = ImageTk.PhotoImage(myImage)

        lblmyImage = Label(self.root, image=self.photo, bd=4, relief=RIDGE)
        lblmyImage.place(x=0, y=0, width=1550, height=140)


        # Logo
        logo_image = Image.open(r"D:\Hotel Management System\Images\download.png")
        logo_image = logo_image.resize((230, 140))
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = Label(self.root, image=self.logo_photo, bd=4, relief=RIDGE)
        logo_label.place(x=0, y=0, width=230, height=140)

        # Title
        dark_brown_hex = "#46322D"
        lbl_title = Label(self.root, text="Blu-Moon Resorts", font=("Times New Roman", 20, "bold"),bg="lightblue", fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=40)

        # Mainframe
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=180, width=1550, height=620)

        # Menu
        dark_brown_hex = "FFBA5E"
        lbl_menu = Label(main_frame, text="MENU", font=("Times New Roman", 20, "bold"), bg="light blue", fg="black", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # btn_Frame
        btn_frame = Frame(main_frame, bd=4 ,relief=RIDGE)
        btn_frame.place(x=0, y=42, width=230, height=230)
        
        cust_btn=Button(btn_frame,text="Customer Report",command=self.cust_details,width=22, font=("Times New Roman", 14, "bold"), bg="lightblue", fg="black", bd=4,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="Room",width=22,command=self.room_booking,font=("Times New Roman", 14, "bold"), bg="lightblue", fg="black", bd=4,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="Details",width=22,command=self.Details,font=("Times New Roman", 14, "bold"), bg="lightblue", fg="black", bd=4,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="Report",width=22,font=("Times New Roman", 14, "bold"), bg="lightblue", fg="black", bd=4,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LogOut",width=22,font=("Times New Roman", 14, "bold"), bg="lightblue", fg="black", bd=4,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
        
       # Main Image
        main_image = Image.open(r"D:\Hotel Management System\Images\PMI_69653_pirates_village_1117_08.jpg")
        main_image = main_image.resize((1310, 590),)
        self.main_photo = ImageTk.PhotoImage(main_image)

        main_image_label = Label(self.root, image=self.main_photo, bd=4, relief=RIDGE)
        main_image_label.place(x=225, y=180, width=1140, height=550)
       # Down Image
        down_image = Image.open(r"D:\Hotel Management System\Images\326361564.jpg")
        down_image = down_image.resize((230, 210))
        self.down_photo = ImageTk.PhotoImage(down_image)

        down_image_label = Label(main_frame,image=self.down_photo, bd=4, relief=RIDGE)
        down_image_label.place(x=0, y=270, width=230, height=210)
        



    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)
    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=room_booking(self.new_window)
    def Details(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)
        
        
        
        
        

       

        

        

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()


        