from tkinter import *

def insertData() :
    pass

def SelectData() :
    pass

root = Tk()
root.title("컴퓨터과 3학년 1반 3번 권오연")
edtFrame = Frame(root)
edtFrame.pack()
lstFrame = Frame(root)
lstFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

##
edt1 = Entry(edtFrame, width=10)
edt2 = Entry(edtFrame, width=10)
edt3 = Entry(edtFrame, width=10)
edt4 = Entry(edtFrame, width=10)

edt1.pack(side=LEFT, padx=10, pady=10)
edt2.pack(side=LEFT, padx=10, pady=10)
edt3.pack(side=LEFT, padx=10, pady=10)
edt4.pack(side=LEFT, padx=10, pady=10)
##

btnInsert = Button(edtFrame, text="입력", command = insertData)
btnInsert.pack(side = LEFT, padx=10, pady=10)

btnSelect = Button(edtFrame, text="조회", command = SelectData)
btnSelect.pack(side = LEFT, padx=10, pady=10)

##

lstData1 = Listbox(lstFrame, bg = 'lightcyan')
lstData1.pack(side=LEFT, fill=BOTH, expand=1)

lstData2 = Listbox(lstFrame, bg = 'lightcyan')
lstData2.pack(side=LEFT, fill=BOTH, expand=1)

lstData3 = Listbox(lstFrame, bg = 'lightcyan')
lstData3.pack(side=LEFT, fill=BOTH, expand=1)

lstData4 = Listbox(lstFrame, bg = 'lightcyan')
lstData4.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()
