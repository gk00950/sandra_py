import time
import tkinter
import serial
from PIL import ImageTk, Image
from pprint import pprint


def close(event):
    tkinter.sys.exit()


def onKeyPress(key):
    updateMouth(key.char)


def updateMouth(which):
    if which in mouths:
        canvas.delete("lips")
        canvas.create_image(mouthX, mouthY, anchor=tkinter.NW, tags="lips", image=img[which])
    if which == "1":
        jaSicher()
    if which == "2":
        amStandLaufen()
    if which == "3":
        hallokinder()
    if which == "4":
        dribbeln()



# initialize
root = tkinter.Tk()
root.bind("<Escape>", close)
root.bind("<Key>", onKeyPress)
root.attributes("-fullscreen", True)
root.config(cursor="none")

height = root.winfo_screenheight()
width = root.winfo_screenwidth()

mouthHeight = int(height*600/1024)
mouthWidth = int(width*900/1024)
mouthX = int((width-mouthWidth)/2)
mouthY = int((height/14)*6)


file = {"smile": Image.open("smile.png").resize((width, height), Image.ANTIALIAS),
        "smile2": Image.open("smile2.png").resize((mouthWidth, mouthHeight), Image.ANTIALIAS)}

img = {"smile": ImageTk.PhotoImage(file["smile"]),
       "smile2": ImageTk.PhotoImage(file["smile2"])}

mouths = ["m", "a", "e", "i", "o", "l", "f", "r", "s"]
for m in mouths:
    file[m] = Image.open(m+".png").resize((mouthWidth, mouthHeight), Image.ANTIALIAS);
    img[m] = ImageTk.PhotoImage(file[m])


canvas = tkinter.Canvas(root, width=width, height=height, highlightthickness=0)
canvas.pack(side="bottom", fill="both", expand="yes")
canvas.configure(background="black")
canvas.create_image(0, 0, anchor=tkinter.NW, image=img["smile"])
canvas.create_image(mouthX, mouthY, anchor=tkinter.NW, tags="lips", image=img["m"])



# Set 1 : Hallo Kinder das ist der Franz...
def hallokinder():
    updateMouth("a")  # hA
    root.after(200, lambda: updateMouth("o"))  # llO
    root.after(350, lambda: updateMouth("i"))  # kI
    root.after(600, lambda: updateMouth("a"))  # ndEr
    root.after(800, lambda: updateMouth("m"))  # --

    root.after(1000, lambda: updateMouth("a"))  # dAs
    root.after(1200, lambda: updateMouth("i"))  # Ist
    root.after(1400, lambda: updateMouth("e"))  # dEr
    root.after(1600, lambda: updateMouth("f"))  # Fr
    root.after(1750, lambda: updateMouth("a"))  # Anz
    root.after(2000, lambda: updateMouth("m"))  # --

    root.after(2200, lambda: updateMouth("o"))  # Und
    root.after(2500, lambda: updateMouth("i"))  # Ich
    root.after(2650, lambda: updateMouth("m"))  # BiN
    root.after(2850, lambda: updateMouth("i"))  # dIe
    root.after(3000, lambda: updateMouth("a"))  # sA
    root.after(3120, lambda: updateMouth("f"))  # Nd
    root.after(3320, lambda: updateMouth("a"))  # rA
    root.after(3500, lambda: updateMouth("m"))  # --

    root.after(3700, lambda: updateMouth("a"))  # dA
    root.after(3780, lambda: updateMouth("f"))  # s
    root.after(4000, lambda: updateMouth("m"))  # sPr
    root.after(4150, lambda: updateMouth("e"))  # EchE
    root.after(4300, lambda: updateMouth("m"))  # Nd
    root.after(4400, lambda: updateMouth("e"))  # E
    root.after(4500, lambda: updateMouth("f"))  # Schl
    root.after(4650, lambda: updateMouth("a"))  # Ag
    root.after(4900, lambda: updateMouth("f"))  # Z
    root.after(5000, lambda: updateMouth("e"))  # Eug
    root.after(5400, lambda: updateMouth("m"))  # --
    return 5400

# Set 1 : Ja Sicher.
def jaSicher():
    updateMouth("e")  # J
    root.after(140, lambda: updateMouth("a"))  # A

    root.after(400, lambda: updateMouth("f"))  # S
    root.after(526, lambda: updateMouth("i"))  # Ich
    root.after(750, lambda: updateMouth("e"))  # Er
    root.after(1100, lambda: updateMouth("m"))  # --
    return 1100

# Set 1 : Tschuess Kinder, bis zum naechsten Mal
def tschuessKinder():
    updateMouth("f")  # tsch
    root.after(100, lambda: updateMouth("o"))  # u
    root.after(200, lambda: updateMouth("f"))  # SS

    root.after(350, lambda: updateMouth("i"))  # kI
    root.after(450, lambda: updateMouth("m"))  # Nd
    root.after(520, lambda: updateMouth("e"))  # Er
    root.after(800, lambda: updateMouth("m"))  # --

    root.after(950, lambda: updateMouth("i"))  # bI
    root.after(1130, lambda: updateMouth("o"))  # Um

    root.after(1300, lambda: updateMouth("e"))  # naechstE
    root.after(1500, lambda: updateMouth("m"))  # N _ M
    root.after(1650, lambda: updateMouth("a"))  # A
    root.after(2000, lambda: updateMouth("m"))  # -
    return 2000


# Set 2 : Drehen
def drehen():
    updateMouth("o")  # dr
    root.after(150, lambda: updateMouth("e"))  # Eh
    root.after(550, lambda: updateMouth("l"))  # eN
    root.after(1000, lambda: updateMouth("m"))  # --
    return 1000

# Set 2 : Dribbeln
def dribbeln():
    updateMouth("o")  # dr
    root.after(150, lambda: updateMouth("i"))  # I
    root.after(300, lambda: updateMouth("m"))  # BB
    root.after(400, lambda: updateMouth("e"))  # E
    root.after(600, lambda: updateMouth("l"))  # Ln
    root.after(1100, lambda: updateMouth("m"))  # --
    return 1100

# Set 2 : Werfen
def werfen():
    updateMouth("o")  # W
    root.after(100, lambda: updateMouth("e"))  # Er
    root.after(280, lambda: updateMouth("f"))  # F
    root.after(400, lambda: updateMouth("e"))  # E
    root.after(1000, lambda: updateMouth("m"))  #
    return 1000


# Set 3 : Am Stand Laufen
def amStandLaufen():
    updateMouth("a")  # A
    root.after(80, lambda: updateMouth("m"))  # m

    root.after(180, lambda: updateMouth("f"))  # SCHt
    root.after(350, lambda: updateMouth("a"))  # A
    root.after(500, lambda: updateMouth("i"))  # Nd  # war 't'

    root.after(680, lambda: updateMouth("l"))  # L
    root.after(760, lambda: updateMouth("a"))  # A
    root.after(880, lambda: updateMouth("o"))  # U
    root.after(960, lambda: updateMouth("f"))  # F
    root.after(1080, lambda: updateMouth("e"))  # eN

    root.after(1600, lambda: updateMouth("m"))  # m
    return 1600

def allesGuteZumGeburtstag():
    updateMouth("a")  #
    root.after(200, lambda: updateMouth("l"))  #
    root.after(400, lambda: updateMouth("e"))  #
    root.after(500, lambda: updateMouth("f"))  #

    root.after(700, lambda: updateMouth("m"))  #
    root.after(800, lambda: updateMouth("o"))  #
    root.after(1100, lambda: updateMouth("e"))  #

    root.after(1400, lambda: updateMouth("m"))  #
    root.after(1500, lambda: updateMouth("f"))  #
    root.after(1600, lambda: updateMouth("o"))  #
    root.after(1800, lambda: updateMouth("m"))  #

    root.after(2100, lambda: updateMouth("e"))  #
    root.after(2300, lambda: updateMouth("m"))  #
    root.after(2400, lambda: updateMouth("o"))  #
    root.after(2600, lambda: updateMouth("r"))  #
    root.after(2700, lambda: updateMouth("f"))  #
    root.after(2900, lambda: updateMouth("a"))  #
    root.after(3300, lambda: updateMouth("i"))  #
    return 3300


ser = serial.Serial("/dev/ttyACM0", 9600, timeout=0, writeTimeout=0)

def serialRead():
    c = ser.readline().decode("ascii")

    if c != "":    
        serialInput(c)
        
    else:
        root.after(10, serialRead)


def serialCallback():
    throwaway = ser.readline()
    serialRead()

def serialInput(which):
    pprint(which)
    if which == "0":
        last = hallokinder()
        root.after(last, serialCallback)
    else:
        root.after(10, serialRead)

root.after(10, serialRead)

# run
root.mainloop()
