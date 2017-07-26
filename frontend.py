from tkinter import *
import backend

def get_selected_row(event):
    global selected_tupple
    index=list1.curselection()[0]
    selected_tupple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tupple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tupple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tupple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tupple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title.get(),author.get(),year.get(),isbn.get()):
        list1.insert(END,row)

def addentry_command():
    backend.insert(title.get(),author.get(),year.get(),isbn.get())
    list1.delete(0,END)
    list1.insert((title.get(),author.get(),year.get(),isbn.get()))

def update_command():
    backend.update(selected_tupple[0],title.get(),author.get(),year.get(),isbn.get())
    print(title.get(),author.get(),year.get(),isbn.get(),selected_tupple[0])

def delete_command():
    backend.delete(selected_tupple[0])
window=Tk()

window.wm_title("BookStore")

l1=Label(window,text='Title')
l1.grid(row=0,column=0)
l2=Label(window,text='Year')
l2.grid(row=1,column=0)
l3=Label(window,text='Author')
l3.grid(row=0,column=2)
l4=Label(window,text='ISBN')
l4.grid(row=1,column=2)

title=StringVar()
e1=Entry(window,textvariable=title)
e1.grid(row=0,column=1)
author=StringVar()
e2=Entry(window,textvariable=author)
e2.grid(row=0,column=3)
year=StringVar()
e3=Entry(window,textvariable=year)
e3.grid(row=1,column=1)
isbn=StringVar()
e4=Entry(window,textvariable=isbn)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text='View All',width=12,command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text='Search Entry',width=12,command=search_command)
b2.grid(row=3,column=3)
b3=Button(window,text='Add Entry',width=12,command=addentry_command)
b3.grid(row=4,column=3)
b4=Button(window,text='Update Selected',width=12,command=update_command)
b4.grid(row=5,column=3)
b5=Button(window,text='Delete Selected',width=12,command=delete_command)
b5.grid(row=6,column=3)
b6=Button(window,text='Close',width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
