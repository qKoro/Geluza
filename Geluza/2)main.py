from tkinter import *
from pystyle import *
from allText import *
import webbrowser
from subprocess import Popen
from string import *
import random
from random_generator_tk import *


# all def


def open_ytb():
    webbrowser.open_new("https://www.youtube.com/")


def open_GitHub():
    webbrowser.open_new("https://github.com/")


def open_pyDoc3():
    webbrowser.open_new("https://docs.python.org/3/")


def open_module_installer():
    webbrowser.open_new("https://pypi.org/project/")


def open_spotify():
    p = Popen("spotify.exe", cwd=r"C:\Users\sango\AppData\Local\Programs\Python\Python310\Lib\site-packages\virtualenv\util\path")
    stdout, stderr = p.communicate()


def open_gmail():
    webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")


def open_netflix():
    webbrowser.open_new("https://www.netflix.com/browse")


def open_ascii():
    webbrowser.open_new(
        "http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20")


def open_cours_btc():
    webbrowser.open_new("https://coinmarketcap.com/currencies/bitcoin/")


def open_amazon():
    webbrowser.open_new("https://www.amazon.com/")


def open_twitch():
    webbrowser.open_new("https://www.twitch.tv/")


def open_random_passWord():
    op_ran()


# CheckBar clas

class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


# cree une fenetre

root = Tk()
root.title("Geluza")
root.geometry("1080x720")
root.minsize(360, 320)
root.maxsize(1080, 720)
root.config(background="#66FF99")

# cree les boites

frame = Frame(root, bg="#66CC99", bd=20, relief=SUNKEN)
btn = Frame(root, bg="#00CC99", bd=20, relief=RIDGE)

# ajouter un titre

Label_title = Label(frame, text=firstMsg, font=(
    "Arial", 25), bg="#66CC99", fg="white")
Label_title.pack(side=TOP)

# cree un sous titre

Label_subtitle = Label(frame, text=secondMsg, font=(
    "Arial", 17), bg="#66CC99", fg="white")
Label_subtitle.pack()

# cree des bouton

yt_button = Button(btn, text=firstBtn, font=("Courrier", 15),
                   bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_ytb)
yt_button.grid(row=0, column=0, sticky=W, pady=10, padx=20, ipadx=10)

gh_button = Button(btn, text=secondBtn, font=("Courrier", 15),
                   bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_GitHub)
gh_button.grid(row=0, column=1, sticky=W, pady=10, padx=20, ipadx=10)

pd_button = Button(btn, text=thirdBtn, font=("Courrier", 15),
                   bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_pyDoc3)
pd_button.grid(row=1, column=0, sticky=W, pady=10, padx=20, ipadx=10)

pm_button = Button(btn, text=fourthBtn, font=("Courrier", 15),
                   bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_module_installer)
pm_button.grid(row=1, column=1, sticky=W, pady=10, padx=20, ipadx=10)

spotify_button = Button(btn, text=Btn5, font=("Courrier", 15),
                        bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_spotify)
spotify_button.grid(row=0, column=2, sticky=W, pady=10, padx=20, ipadx=10)

gmail_button = Button(btn, text=Btn6, font=("Courrier", 15),
                      bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_gmail)
gmail_button.grid(row=1, column=2, sticky=W, pady=10, padx=20, ipadx=10)

netflix_button = Button(btn, text=Btn7, font=("Courrier", 15),
                        bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_netflix)
netflix_button.grid(row=0, column=3, sticky=W, pady=10, padx=20, ipadx=10)

ascii_button = Button(btn, text=Btn8, font=("Courrier", 15),
                      bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_ascii)
ascii_button.grid(row=1, column=3, sticky=W, pady=10, padx=20, ipadx=10)

btc_button = Button(btn, text=Btn9, font=("Courrier", 15),
                    bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_cours_btc)
btc_button.grid(row=2, column=3, sticky=W, pady=10, padx=20, ipadx=10)


amazon_button = Button(btn, text=Btn10, font=("Courrier", 15),
                       bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_amazon)
amazon_button.grid(row=2, column=2, sticky=W, pady=10, padx=20, ipadx=10)


twitch_button = Button(btn, text=Btn11, font=("Courrier", 15),
                       bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_twitch)
twitch_button.grid(row=2, column=1, sticky=W, pady=10, padx=20, ipadx=10)


pass_button = Button(btn, text=Btn12, font=("Courrier", 15),
                     bg="#66CC99", fg="white", border=10, width=16, height=1, command=open_random_passWord)
pass_button.grid(row=2, column=0, sticky=W, pady=10, padx=20, ipadx=10)


# enPackter la frame

frame.pack(pady=25)
btn.pack(pady=30, fill=X)

# exucute

root.mainloop()
