from tkinter import *

app = Tk()
app.title("GUI Example 3")
app.geometry('200x100')

def copyTextToLabel():
    t = v.get()
    if len(v.get()) == 0: # check if the text is null
        b1['bg'] = 'red'  # set button background red
    else:
        l1['text'] = v.get() # otherwise update the label text
        b1['bg'] = b1BgColor # restore button background
        b1['text'] = 'Clear Text' # ... and text
        b1['command'] = clearEntryText # ... and command

def clearEntryText():
    v.set("")
    b1['text'] = 'Copy Text'
    b1['command'] = copyTextToLabel
    
b1 = Button(app, text="Copy Text", command=copyTextToLabel)
b1BgColor = b1['bg']

l1 = Label(app, text="Text is displayed here")

v = StringVar()

e1 = Entry(app, textvariable = v)

l1.pack(side='bottom')
b1.pack(side='bottom')
e1.pack(side='bottom')

app.mainloop()
