from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

class Details:
    def __init__(self, root):
        self.root = root
        self.root.title("Blu Group of Resorts")
        self.root.geometry("1132x520+220+205")
        
        #Label Widget
        label = Label(root, text="Blu Group of resorts")
        label.pack()
        
        lbl_title = Label(self.root, text="Details", font=("Times New Roman", 15, "bold"),bg="black", fg="yellow", bd=3, relief=RIDGE)
        lbl_title.place(x=0, y=20, width=1240, height=30)

if __name__ == '__main__':
    root = Tk()
    app = Details(root)
    root.mainloop()
    
    
    