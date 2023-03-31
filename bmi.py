import tkinter
import tkinter.messagebox

screen=tkinter.Tk()

screen.title("BMI 계산기")
screen.geometry("640x400+300+300")
screen.resizable(0,0)

he = tkinter.StringVar ()
we = tkinter.StringVar ()

def btn() :
    h_value = float(he.get())
    w_value = float(we.get())
    h_value = h_value * 0.01
    result = w_value / (h_value * h_value)
    tkinter.messagebox.showinfo("결과", result)
    

tilabel=tkinter.Label(screen, text="체질량질수 계산기", bg="green")
tilabel.config(font=("arial", 25), fg="red")
tilabel.pack()

heightLabel = tkinter.Label(screen, text="신장")
heightLabel.config(font=("Arial", 24))
heightLabel.place(x=50, y=70)

height=tkinter.Entry(screen, textvariable=he)
height.place(x=150, y=85)


weightLabel = tkinter.Label(screen, text="체중")
weightLabel.config(font=("Arial", 24))
weightLabel.place(x=50, y=160)

weight=tkinter.Entry(screen, textvariable=we)
weight.place(x=150, y=175)

correct = tkinter.Button(screen, text="확인", command=btn)
correct.config(font=("Arial", 20))
correct.place(x=50, y=250)

total=tkinter.Entry(screen)
total.place(x=150, y=265)



screen.mainloop()
