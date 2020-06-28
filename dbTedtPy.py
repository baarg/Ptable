from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import filedialog as fd

manu = []
list1= []
list2= []
l = []
filename = ""
darkOn= True
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
    
def ser():
    on = False
    r = 0
    c = 0
    string =""
    for i in range(row):
        for j in range(column):
            if manu[i][j].get() == en1.get() and manu[i][j].get() != None:
                on = True
                r = i
                c = j
                break
        if(on == True):
            break
    if on:
        for i in range(row):
            for j in range(column):
                if i == r and manu[i][j].get() != "":
                    string+=char[j]+""+str(i)+":"+manu[i][j].get()+","

    #la.config(text = string)
    s = ""
    List.delete(0,END)
    for i in string:
        if(i == ','):
            List.insert(END,s)
            s = ""
        else:
            s+=i
    scrollbar.config( command = List.yview )
    
            
            
def max():
    max = 0
    j = int(en1.get())
    for i in range(row):
        try:
            n = float(manu[i][j].get())
            if n > max:
                max = n
        except:
            print(i,"is not number")
       
    print(max)
    la.config(text = max)
def sum():
    sum = 0
    j = int(en1.get())
    for i in range(row):
        try:
            n = float(manu[i][j].get())
            sum+=n
        except:
            print("it is text ")
    print(sum)
    la.config(text = sum)
def min():
    j = int(en1.get())
    min = int(manu[0][j].get())
    for i in range(row):
        try:
            n = float(manu[i][j].get())
            if n < mix:
                mix = n
        except:
            print(i,"is not number")
       
    print(max)
    la.config(text = min)
def darkmode():
    global darkOn
    if darkOn == True:
        for i in range(row):
            for j in range(column):
                manu[i][j].config(fg = "#0984e3",bg="#485460")
        for i in range(column):
            l[i].config(bg="#636e72")
        root.config(bg="#d2dae2")
        bu.config(bg="#d2dae2")
        summ.config(bg="#d2dae2")
        min.config(bg="#d2dae2")
        bser.config(bg="#d2dae2")
        dark.config(bg="#d2dae2")
        count.config(bg="#d2dae2")
        store.config(bg="#d2dae2")
        autonum.config(bg="#d2dae2")
        
        darkOn = False
    else:
        darkOn = True
        for i in range(row):
            for j in range(column):
                manu[i][j].config(fg = "black",bg="white")
        for i in range(column):
            if i % 2 ==0:
                l[i].config(bg ="#dfe6e9")
            else:
                l[i].config(bg ="#b2bec3")
        root.config(bg="#81ecec")
        bu.config(bg="white")
        summ.config(bg="white")
        min.config(bg="white")
        bser.config(bg="white")
        dark.config(bg="white")
        count.config(bg = "white")
        store.config(bg = "white")
        autonum.config(bg = "white")
        darkOn = True
def count():
    count = 0
    j = int(en1.get())
    for i in range(row):
        if manu[i][j].get() !="":
            count+=1
    la.config(text=count)

def store():
    m = 0
    string = en1.get()
    ind = []
    if string[0] in char:
        ind.append(char.index(string[0]))
    else:
        ind.append(int(string[0]))
    try:
        x = int(string[1]+""+string[2])
    except:
        x = int(string[1])
    ind.append(x)
    manu[ind[1]][ind[0]].insert(0,la.cget('text'))
def autonumber():

    j = int(en1.get())
    for i in range(row):
        manu[i][j].insert(0,i+100) 
root = Tk()
root.config(bg = "#81ecec")
root.title("Ptable")
root.geometry("1280x600")
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
        l.append(Label(root,text = char[i], bg = "#dfe6e9",pady = 10, padx = 55))
        l[i].grid(row = 0, column =i ,pady=4)
    else:
        l.append( Label(root,text = char[i], bg = "#b2bec3",pady = 10, padx = 55))
        l[i].grid(row = 0, column =i ,pady=4)
    
for i in range(row):
    list1 = []
    for j in range(column):
        list1.append(Entry(root,bg="white"))
    manu.append(list1)
    
for i in range(row):
    for j in range(column):
        manu[i][j].grid(row = i+1, column = j, ipady=4)

bu = Button(root,text="find max",command = max)
bu.grid(row = 1, column = column, ipadx = 30)
min = Button(root,text="find min",command = min)
min.grid(row = 2, column = column, ipadx = 31)
bser = Button(root, text = "serach",command = ser)
bser.grid(row = 3, column = column, ipadx = 37)
summ = Button(root, text = "find sum", command = sum)
summ.grid(row = 4, column = column,ipadx = 30)
count= Button(root,text="find count",command = count)
count.grid(row = 5, column = column, ipadx = 25)
store = Button(root,text = "store in", command = store)
store.grid(row = 6, column = column, ipadx = 32)
autonum = Button(root,text="AutoNumbring",command = autonumber)
autonum.grid(row = 7, column = column, ipadx = 10)
dark = Button(root, text = "DarkMode",command = darkmode)
dark.grid(row =8, column= column)

en1 = Entry(root)
en1.grid(row = 9, column = column, padx = 10)
la = Label(root,text="")
la.grid(row = 0 ,column = column, padx = 10, ipadx = 10)

scrollbar = Scrollbar(root)
scrollbar.grid(row = 10, column =column, rowspan = 10)

List = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(row):
    for j in range(column):
        List.insert(END,"Label")
List.grid(row = 10, column =column, rowspan = 10)
scrollbar.config( command = List.yview )

root.mainloop()
