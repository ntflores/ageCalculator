#tkinter
from tkinter import *
from datetime import date
root = Tk()
root.title("Otters Club")
root.geometry('750x500') #it give us width and size
root.resizable(0, 0)

#create an image background for your gui
img = PhotoImage(file="csumbtransparent.PNG")
label =Label(root, image=img, width=750, height=500)
label.place(x=0, y=-120)


datebox = Entry(root)
datebox.place(x=420, y=320)

namebox = Entry(root)
namebox.place(x=420, y=350)

def submit():
   today = date.today()
   age = today.year - int(datebox.get())
   label3.configure(text= "Your age is " + str(age) + " " + namebox.get())


#create a button and link it with out DEF function
#command function allows button to be connected or to recall the DEF function
button1= Button(root, text ="Submit your answer", fg='Green', command=submit)
button1.place(x=320,y=270)


#we created a label that asks question
label = Label(root, text = "Year of birth: ")
label.place(x=240, y=320)

label2 = Label(root, text = "What is your name: ")
label2.place(x=240, y=350)

label3 = Label(root, text = "   ")
label3.place(x=315, y=380)

root.mainloop()


