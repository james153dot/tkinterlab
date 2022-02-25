from tkinter import *

app = Tk()
app.title("GUI Example 2")
app.geometry('200x100')

def changeLabelText():
    if  l1['text'] == "Text A":
        l1['text'] = "Text B"
    else:
        l1['text'] = "Text A"
        
b1 = Button(app, text="Change Text", command=changeLabelText)

l1 = Label(app, text="Text A")

l1.pack(side='bottom')
b1.pack(side='bottom')


app.mainloop()
