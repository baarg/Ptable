from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import filedialog as fd

manu = []
list1= []
list2= []
filename = ""
char ="ABCDEFGHIJKLMNOPQRSTUVQXYZ"
row,column =20,9
offset = column
def openf():# open button function
    global filename
    f = filedialog.askopenfile(mode='r')
    if f is None:
        return
    print(filename)
    list2=[]
    j=0
    string =""
    for k in range(row):
        text = f.readline()
        j=0
        string = ""
        print(text)
        for i in text:
            if i ==",":
               #list2.append(string)
               manu[k][j].delete(0,END)
               manu[k][j].insert(0,string)
               #print (list2[j])
               j+=1
               string = ""
            else: 
                string += i
    f.close()
    
def saveas():# Save as button function
    global filename
    f = filedialog.asksaveasfile(mode='w', defaultextension = '.d')
    print(filename)
    if f is None:
        return
    Rows = 0
    for i in range(row):
        for j in range(column):
            if manu[i][j].get() != "":
                f.write(manu[i][j].get()+",")
            else:
                f.write(",")
        f.write(" ;")
        f.write("\n")
    f.close()
    


root = Tk()
root.title("Ptable")

root.geometry("1120x500")
#menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="open", command = openf)
filemenu.add_command(label="save as", command = saveas)

helpmenu = Menu(menu)
menu.add_cascade(label="help", menu = helpmenu)

#

#
for i in range(column):
    if i % 2 ==0:
        l = Label(root,text = char[i], bg = "#dfe6e9",pady = 10, padx = 55).grid(row = 0, column =i ,pady=4)
    else:
        l = Label(root,text = char[i], bg = "#b2bec3",pady = 10, padx = 55).grid(row = 0, column =i ,pady=4)
    
for i in range(row):
    list1 = []
    for j in range(column):
        list1.append(Entry(root,))
    manu.append(list1)
    
for i in range(row):
    for j in range(column):
        manu[i][j].grid(row = i+1, column = j, ipady=3)



root.mainloop()
