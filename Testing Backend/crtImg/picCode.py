from tkinter import *
from PIL import Image, ImageTk

colors = ["red", "green", "blue", "yellow"]
points = [[2, 79, 72, 179], [72, 79, 142, 179], [142, 79, 212, 179], [212, 79, 282, 179],
          [2, 179, 72, 279], [72, 179, 142, 279], [142, 179, 212, 279], [212, 179, 282, 279],
          [2, 279, 72, 379], [72, 279, 142, 379], [142, 279, 212, 379], [212, 279, 282, 379],
          [2, 379, 72, 479], [72, 379, 142, 479], [142, 379, 212, 479], [212, 379, 282, 479]]
codes = []
images = []

def toFour(code):
    code4Str = ""
    codeFour = 0
    while (code != 0):
        code4Str += str(code % 4)
        # codeFour *= 10
        # codeFour += code % 4
        code = int(code / 4)
    # code4Str = str(codeFour)
    for i in range(len(code4Str), 16):
        code4Str += "0"
    code4Str = code4Str[::-1]
    print(code4Str)
    toTen(code4Str)
    return code4Str

def toTen(a):
    a = a[::-1]
    uin = 0
    for i in range(16):
        dig = int(a[i])
        uin += dig * (4 ** i)
    print(uin)

def genImg(y):
    y = list(y)
    im = Image.new("RGB", (284, 558), "#FF05EE")
    codes.append(y.copy())
    for x in range(16):
        im.paste((colors[int(y[x])]), (points[x][0], points[x][1], points[x][2], points[x][3]))


    im.paste("turquoise", (2, 481, 282, 556))
    # black lines
    im.paste("black", (0, 0, 284, 4))
    im.paste("black", (0, 76, 284, 80))
    im.paste("black", (0, 478, 284, 482))
    im.paste("black", (0, 555, 284, 559))
    im.paste("black", (0, 0, 4, 558))
    im.paste("black", (281, 0, 285, 558))
    im.paste("black", (70, 79, 74, 479))
    im.paste("black", (140, 79, 144, 479))
    im.paste("black", (210, 79, 214, 479))
    im.paste("black", (2, 177, 282, 181))
    im.paste("black", (2, 277, 282, 281))
    im.paste("black", (2, 377, 282, 381))
    # im.show()
    images.append(im)
    return im

def show():
    print('Enter your UIN:')
    numImg = int(input())
    if len(str(numImg)) == 9:
        im = genImg(toFour((numImg)))
        # im.show()
        root = Tk()
        canvas = Canvas(root, width=300, height=560)
        canvas.pack()
        img = ImageTk.PhotoImage(im)
        canvas.create_image(2, 2, image=img, anchor="nw")
        root.mainloop()
    else:
        print("UINs are exactly nine digits!")

show()
