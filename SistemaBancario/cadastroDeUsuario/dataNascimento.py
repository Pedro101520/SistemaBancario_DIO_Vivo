from tkinter import *
from tkcalendar import *

def pick_date(event, txtData):
    global cal, date_window

    date_window = Toplevel()
    date_window.grab_set()
    date_window.title("Choose Date of Birth")
    date_window.geometry("250x220+590+370")
    cal = Calendar(date_window, selectmode="day", date_pattern="dd/mm/yyyy")
    cal.place(x=0, y=0)

    submit_btn = Button(date_window, text="Submit", command=lambda: grab_date(txtData))
    submit_btn.place(x=80, y=190)

def grab_date(txtData):
    txtData.delete(0, END)
    txtData.insert(0, cal.get_date())
    date_window.destroy()

def block_entry(event):
    return 'break'