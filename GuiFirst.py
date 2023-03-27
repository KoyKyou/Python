import tkinter

win = tkinter.Tk()

win.title("GUI Program by KoyKyou")
win.geometry("1280x720+0+0")
win.resizable(1, 1)

def btnClick():
    label.config(font=("Arial", 40))
    label.config(text="#)QwQ)")
    label.config(fg="#000080")

label=tkinter.Label(win, text="(@OwO)~~~@")
label.pack()

button = tkinter.Button(win, text="확인", command=btnClick)
button.pack()

win.mainloop()


