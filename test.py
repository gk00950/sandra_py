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

mouths = ["m", "a", "e", "i", "o", "l", "f", "r", "s", "_"]
for m in mouths:
    file[m] = Image.open(m+".png").resize((mouthWidth, mouthHeight), Image.ANTIALIAS);
    img[m] = ImageTk.PhotoImage(file[m])


canvas = tkinter.Canvas(root, width=width, height=height, highlightthickness=0)
canvas.pack(side="bottom", fill="both", expand="yes")
canvas.configure(background="black")
canvas.create_image(0, 0, anchor=tkinter.NW, image=img["smile"])
canvas.create_image(mouthX, mouthY, anchor=tkinter.NW, tags="lips", image=img["m"])



# Set 1 : Hallo Kinder das ist der Franz...
def halloKinderDasIst():
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


# ap_1
def applaus():
    updateMouth("e")  # Ei
    # root.after(150, lambda: updateMouth("m"))  # Nen
    # root.after(400, lambda: updateMouth("r"))  # R
    root.after(500, lambda: updateMouth("i"))  # IE
    # root.after(950, lambda: updateMouth("f"))  # S
    root.after(1050, lambda: updateMouth("e"))  # En
    root.after(1250, lambda: updateMouth("a"))  # App
    # root.after(1450, lambda: updateMouth("l"))  # L
    # root.after(1600, lambda: updateMouth("a"))  # A
    root.after(1800, lambda: updateMouth("o"))  # U
    # root.after(2000, lambda: updateMouth("f"))  # S F
    # root.after(2300, lambda: updateMouth("o"))  # UEr
    root.after(2400, lambda: updateMouth("e"))  # dEn
    # root.after(2550, lambda: updateMouth("f"))  # Fr
    root.after(2700, lambda: updateMouth("a"))  # A
    # root.after(2900, lambda: updateMouth("m"))  # n
    root.after(3250, lambda: updateMouth("m"))  # --
    return 3250

# bist_du_1
def bistDuDirSicher():
    updateMouth("f")  # Fr
    root.after(150, lambda: updateMouth("a"))  # Anz
    root.after(500, lambda: updateMouth("m"))  #
    root.after(800, lambda: updateMouth("i"))  # bIst
    root.after(950, lambda: updateMouth("o"))  # dU dir
    root.after(1200, lambda: updateMouth("i"))  # sIch
    root.after(1550, lambda: updateMouth("a"))  # Er
    root.after(1800, lambda: updateMouth("m"))  # --

    root.after(3450, lambda: updateMouth("o"))  # Ok
    root.after(3700, lambda: updateMouth("e"))  # Ey (ich)
    root.after(4100, lambda: updateMouth("a"))  # vErtrAu
    root.after(4550, lambda: updateMouth("i"))  # dIr

    root.after(4900, lambda: updateMouth("o"))  # los
    root.after(5600, lambda: updateMouth("e"))  # gEhts

    root.after(6200, lambda: updateMouth("m"))  # --
    return 6200


# das kitzelt_1
def dasKitzelt():
    updateMouth("f")  # ...
    root.after(1000, lambda: updateMouth("_"))  # ...
    root.after(2000, lambda: updateMouth("f"))  # ...
    root.after(3200, lambda: updateMouth("a"))  # dAs
    root.after(3600, lambda: updateMouth("e"))  # kItz
    root.after(3900, lambda: updateMouth("l"))  # eLt
    root.after(4500, lambda: updateMouth("f"))  # ...
    root.after(5800, lambda: updateMouth("m"))  # --
    return 5800


# hallo kinder
def halloKinder():
    updateMouth("a")  # hA
    root.after(200, lambda: updateMouth("o"))  # llO
    root.after(350, lambda: updateMouth("i"))  # kI
    root.after(600, lambda: updateMouth("a"))  # ndEr
    root.after(800, lambda: updateMouth("m"))  # --
    return 800


# ja_klar_1
def jaKlar():
    updateMouth("A")  # jA
    root.after(450, lambda: updateMouth("l"))  # kL
    root.after(600, lambda: updateMouth("a"))  # Ar
    root.after(1000, lambda: updateMouth("m"))  # --
    return 1000


# ja sicher (langsame version)
def jaSicher_slow():
    updateMouth("a")  # jA
    root.after(450, lambda: updateMouth("i"))  # sIch
    root.after(750, lambda: updateMouth("a"))  # Er
    root.after(1000, lambda: updateMouth("m"))  # --
    return 1000


# soundcheck
def soundCheck():
    updateMouth("e")  # Eins
    root.after(400, lambda: updateMouth("a"))  # Zwei
    root.after(800, lambda: updateMouth("e"))  # Drei
    root.after(1100, lambda: updateMouth("i"))  # Vier
    root.after(1500, lambda: updateMouth("o"))  # sOUnd
    root.after(1850, lambda: updateMouth("e"))  # chEk
    root.after(2300, lambda: updateMouth("m"))  # mm
    return 2300


# sounderzeugen
def soundErzeugen():
    updateMouth("a")  # jA
    root.after(350, lambda: updateMouth("i"))  # sIch
    root.after(600, lambda: updateMouth("a"))  # Er
    root.after(800, lambda: updateMouth("m"))  # --

    root.after(1100, lambda: updateMouth("a"))  # dann
    root.after(1300, lambda: updateMouth("o"))  # kOnzentr
    root.after(1800, lambda: updateMouth("i"))  # Ier Ich mich
    root.after(2300, lambda: updateMouth("a"))  # Aufs

    root.after(2800, lambda: updateMouth("o"))  # sOund
    root.after(3100, lambda: updateMouth("e"))  # Erzeugen
    root.after(3800, lambda: updateMouth("m"))  # --
    return 3800


# Tschuess Kinder, bis zum naechsten Mal (langsam)
def tschuessKinder_slow():
    updateMouth("o")  # tschuess

    # root.after(350, lambda: updateMouth("i"))  # kI
    # root.after(450, lambda: updateMouth("m"))  # Nd
    root.after(520, lambda: updateMouth("e"))  # Er
    # root.after(800, lambda: updateMouth("m"))  # --

    root.after(950, lambda: updateMouth("i"))  # bI
    # root.after(1130, lambda: updateMouth("o"))  # Um

    root.after(1300, lambda: updateMouth("e"))  # naechstE
    # root.after(1500, lambda: updateMouth("m"))  # N _ M
    root.after(1650, lambda: updateMouth("a"))  # A
    root.after(2000, lambda: updateMouth("m"))  # -
    return 2000


# wer traut sich_1
def werTrautSich():
    updateMouth("e")  # wEr
    root.after(400, lambda: updateMouth("a"))  # trAut
    root.after(800, lambda: updateMouth("i"))  # sIch
    root.after(1300, lambda: updateMouth("m"))  # --
    return 1300


# springen_1
def springen():
    updateMouth("e")  # spring
    root.after(500, lambda: updateMouth("f"))  # eN
    root.after(1100, lambda: updateMouth("m"))  # --
    return 1100


# klatschen_1
def klatschen():
    updateMouth("a")  # klAtsch
    root.after(400, lambda: updateMouth("e"))  # E
    root.after(800, lambda: updateMouth("f"))  # N
    root.after(1100, lambda: updateMouth("m"))  # --
    return 1100


# haende_1
def haendeKopfKlatschen():
    updateMouth("e")  # haende
    root.after(350, lambda: updateMouth("o"))  # ueber
    root.after(500, lambda: updateMouth("e"))  # er den
    root.after(800, lambda: updateMouth("o"))  # kOpf Und
    root.after(1300, lambda: updateMouth("a"))  # klA
    root.after(1650, lambda: updateMouth("e"))  # tschEn
    root.after(2200, lambda: updateMouth("m"))  # --
    return 2200


# bogen_links_1
def bogenLinks():
    updateMouth("o")  # bOgen
    root.after(500, lambda: updateMouth("i"))  # lInk
    root.after(900, lambda: updateMouth("f"))  # S
    root.after(1200, lambda: updateMouth("m"))  # --
    return 1200


# bogen_rechts_1
def bogenRechts():
    updateMouth("o")  # bOgen
    root.after(500, lambda: updateMouth("e"))  # rEcht
    root.after(950, lambda: updateMouth("f"))  # S
    root.after(1300, lambda: updateMouth("m"))  # --
    return 1300


# hocke_1
def hocke():
    updateMouth("i")  # In dIe
    root.after(350, lambda: updateMouth("o"))  # hO
    root.after(700, lambda: updateMouth("e"))  # kE
    root.after(1100, lambda: updateMouth("m"))  # --
    return 1100


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

    # ----------------------------------------------------------------------------------------------------------------
    if which == "0":
        last = halloKinderDasIst()
        root.after(last, serialCallback)
    if which == "a":
        last = halloKinder()
        root.after(last, serialCallback)
    if which == "b":
        last = bistDuDirSicher()
        root.after(last, serialCallback)
    if which == "c":
        last = dasKitzelt()
        root.after(last, serialCallback)
    if which == "d":
        last = soundErzeugen()
        root.after(last, serialCallback)
    if which == "e":
        last = jaSicher_slow()
        root.after(last, serialCallback)
    if which == "f":
        last = jaKlar()
        root.after(last, serialCallback)
    if which == "g":
        last = tschuessKinder_slow()
        root.after(last, serialCallback)
    if which == "h":
        last = applaus()
        root.after(last, serialCallback)
    if which == "i":
        last = soundCheck()
        root.after(last, serialCallback)
    if which == "j":
        last = springen()
        root.after(last, serialCallback)
    if which == "k":
        last = klatschen()
        root.after(last, serialCallback)
    if which == "l":
        last = haendeKopfKlatschen()
        root.after(last, serialCallback)
    if which == "m":
        last = bogenLinks()
        root.after(last, serialCallback)
    if which == "n":
        last = bogenRechts()
        root.after(last, serialCallback)
    if which == "o":
        last = bogenRechts()
        root.after(last, serialCallback)
    # ----------------------------------------------------------------------------------------------------------------
    else:
        root.after(10, serialRead)


try:
    ser = serial.Serial("/dev/ttyACM0", 9600, timeout=0, writeTimeout=0)
    root.after(10, serialCallback)
except Exception:
    pass


# run
root.mainloop()
