from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import datetime

root = Tk()

root.geometry("1000x900")
root.wm_minsize(1780, 1700)
root.wm_maxsize(1700, 11000)
root.title("NewsPaper")

title = Label(text="Welcome To ", bg="black", fg="white", font="Consolas 25 bold", padx=50)
title.grid(column=0)

title = Label(text="Jay News", bg="black", fg="white", font="Consolas 25 bold", padx=50)
title.grid(row=0, column=1, pady=5)


# Topic 1: Hacking

with open("files/hacking.txt") as hack:
    for h in hack:
        data = h

HImage = Image.open("images/hacking.png")
HPhoto = ImageTk.PhotoImage(HImage)

hacking = Label(text="Hacking", font='Consolas 20 bold', bg="red", width=50)
Photo = Label(image=HPhoto)
Info = Text(root, wrap=WORD, bg="orange", font="Consolas 12 bold", pady=20, padx=20)
Info.insert(INSERT, data)
Info.config(height=12)

hacking.grid(row=1, column=0, padx=50)
Photo.grid(row=2, column=0)
Info.grid(row=3, column=0)

# Topic 2: Cricket

with open("files/cricket.txt") as crick:
    for c in crick:
        data = c

CImage = Image.open("images/cricket.png")
CPhoto = ImageTk.PhotoImage(CImage)

cricket = Label(text="Cricket", font='Consolas 20 bold', bg="red", width=50)
cPhoto = Label(image=CPhoto)
CInfo = Text(root, wrap=WORD, bg="orange", font="Consolas 12 bold", pady=20, padx=20)
CInfo.insert(INSERT, data)
CInfo.config(height=12)

cricket.grid(row=1, column=1)
cPhoto.grid(row=2, column=1)
CInfo.grid(row=3, column=1)

# Topic 3: Programming
with open("files/programming.txt") as pro:
    for pr in pro:
        data = pr

PrImage = Image.open("images/programming.png")
PrPhoto = ImageTk.PhotoImage(PrImage)

programming = Label(text="Programming", font='Consolas 20 bold', bg="red", width=50)
pPhoto = Label(image=PrPhoto)
PInfo = Text(root, wrap=WORD, bg="orange", font="Consolas 12 bold", pady=20, padx=20)
PInfo.insert(INSERT, data)
PInfo.config(height=8)

programming.grid(row=4, column=0, pady=20)
pPhoto.grid(row=5, column=0)
PInfo.grid(row=6, column=0, pady=5)

# Topic 4: Space

SImage = Image.open("images/space.png")
SPhoto = ImageTk.PhotoImage(SImage)

space = Label(text="Space", font='Consolas 20 bold', bg="red", width=50)
sPhoto = Label(image=SPhoto)
SInfo = Text(root, wrap=WORD, bg="orange", font="Consolas 12 bold", pady=20, padx=20)
SInfo.insert(INSERT,
             '''The new findings match Andrea Dupree’s previous observations of Betelgeuse using the Hubble Space Telescope. Dupree, an astronomer at the Center for Astrophysics | Harvard & Smithsonian and a co-author on the new paper, captured signs of dense, heated material moving through the star’s atmosphere in the months leading up to the great dimming.“With Hubble, we could see the material as it left the star’s surface and moved out through the atmosphere, before the dust formed that caused the star to appear to dim,” Dupree says.Dupree found that the material moved about 200,000 miles per hour as it traveled from the star’s surface to its outer atmosphere. Once the gas bubble was millions of miles from the hot star, it cooled and formed a dust cloud that temporarily blocked the star’s light.The star returned to its normal brightness by April 2020.Dupree, who has been studying Betelgeuse since 1985, hopes to continue studying the star in hopes of catching it eject another gas bubble.''')
SInfo.config(height=8)

space.grid(row=4, column=1, pady=20)
sPhoto.grid(row=5, column=1)
SInfo.grid(row=6, column=1, pady=5)

root.mainloop()