from tkinter import *
from tkinter import font
from pystyle import *
from allText import *
import webbrowser
from subprocess import Popen
from string import *
import random

def op_ran():
    def open_random_passWord():
        password_min = 8
        password_max = 16
        all_chras = ascii_letters + punctuation + digits

        password = "".join(random.choice(all_chras)
                        for x in range(random.randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)


    randomwin = Tk()
    randomwin.title("Random PassWord Generator")
    randomwin.geometry("480x360")
    randomwin.minsize(360, 320)
    randomwin.maxsize(720, 480)
    randomwin.iconbitmap("logo.ico")
    randomwin.config(background="#66FF99")

    frame = Frame(randomwin, bg="#66CC99", bd=20, relief=SUNKEN)
    btn = Frame(randomwin, bg="#00CC99", bd=20, relief=RIDGE)
    password_entry = Entry(frame, font=("Courrier", 20), bg="#66FF99", fg="black")
    password_entry.pack()

    generate_btn = Button(btn, text='Generate', font=(
        "Courrier", 15), bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_random_passWord)
    generate_btn.pack()

    frame.pack(pady=30)
    btn.pack(pady=30)


    randomwin.mainloop()
