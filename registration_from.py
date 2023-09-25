from tkinter import *

root=Tk()
root.geometry("450x500")
root.maxsize(450,500)
root.config(background="skyblue")
root.title("GUI APP")

l0=Label(root,text="--- Registeration Form ---",font=('arial',20),width=20,bg="skyblue")
l0.place(x=60,y=45)

l1=Label(root,text="Enter your First Name : ",width=25)
l1.place(x=30,y=120)
e1=Entry(root,width=30)
e1.place(x=220,y=120)

l2=Label(root,text="Enter your Last Name : ",width=25)
l2.place(x=30,y=160)
e2=Entry(root,width=30)
e2.place(x=220,y=160)

l3=Label(root,text="Enter Email : ",width=25)
l3.place(x=30,y=200)
e3=Entry(root,width=30)
e3.place(x=220,y=200)

l4=Label(root,text="Contact Number : ",width=25)
l4.place(x=30,y=240)
e4=Entry(root,width=30)
e4.place(x=220,y=240)

l5=Label(root,text="Gender : ",width=25)
l5.place(x=30,y=280)
vars = IntVar()
Radiobutton(root,text="Male",padx=5,variable=vars,value=1,bg="skyblue").place(x=220,y=280)
Radiobutton(root,text="Female",padx=10,variable=vars,value=2,bg="skyblue").place(x=290,y=280)

l6=Label(root,text="Select Country : ",width=25)
l6.place(x=30,y=320)
def show():
    Label.config( text = clicked.get()  ,width=10)
options = [
    "India",
    "USA",
    "England",
    "Canada",
    "France",
    "Italy",
    "UK"
]
clicked = StringVar()
clicked.set( "India" )
drop = OptionMenu( root , clicked , *options).place(x=220,y=320)

l7=Label(root,text="Enter Password : ",width=25)
l7.place(x=30,y=360)
e5=Entry(root,width=30,show="*")
e5.place(x=220,y=360)

l8=Label(root,text="Re-Enter Password : ",width=25)
l8.place(x=30,y=400)
e6=Entry(root,width=30,show="x")
e6.place(x=220,y=400)

b1=Button(root,text="Submit",bg="black",fg="white",font=('arial',10))
b1.place(x=200,y=450)

root.mainloop()