import tkinter
import tkinter.colorchooser
import tkinter.filedialog

def btn_Click():
   #
   path=tkinter.filedialog.askopenfilenames()
    myColor=tkinter.colorchooser.askcolor()
    btn["bg"]=myColor[1]
    print(myColor[1])
root=tkinter.Tk()
root.minsize(300,300)
btn=tkinter.Button(root,text="choose color",command=btn_Click)
#btn.bind("<Button-1>",btn_Click)
btn.grid(row=0,column=0)
root.mainloop()