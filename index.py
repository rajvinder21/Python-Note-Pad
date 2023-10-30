import webbrowser as web
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, showwarning


##############   Function for handling Buttons ################### 


def myFunc():
    print('avoid me')

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All file', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)



    print(filename)
    if filename == "":
        return False
    
    else:
        # showinfo(
        #     title='Selected File',
        #     message= f"Opening File {filename}"
        # )
        root.title(f"Note Pad ~{filename}")
        text_edit.delete(1.0,END)

        f1 = open(filename,'r')
        text = f1.read()
        text_edit.insert(END,text) 

#################### SAVe AS File #########################


def saveasFile():
    filetype = [
        ("Text File","*.txt"),
        ("All File","*.*")
    ]
    
    files = fd.asksaveasfile(filetypes=filetype, defaultextension=".txt")
    

    

    if not files:
        showwarning(
        "Note Pad",
        "Your File Is Note Save"
        )
        
    else:    
        root.title(f"Note Pad ~{files.name}")
        f2 = open(files.name,"w")

        text = text_edit.get(1.0,END)
        f2.write(text)

################# saving a file

def save_file():
    if root.title() == "Note Pad":
        saveasFile()

    else:
        fileAddress = root.title()
        f2 = open(fileAddress[10:],"w")

        text = text_edit.get(1.0,END)
        f2.write(text)
        f2.close()


############## TExct Edit function   #############

class edit:
    def __init__(self):
        self.copy_text = ""

    def clearFile(self):
        text_edit.delete("1.0",END)


    def getSelective(self):
        try:
            self.copy_text = text_edit.selection_get()
        except:
            self.copy_text = ""

        

    def paste(self):
        position = text_edit.index(INSERT)
        text_edit.insert(position,self.copy_text)




################ VIew MEnu Function ##############

class zoomer:

    def __init__(self):
        self.size = 14

    def zoom_in(self): 
        self.size = self.size +  2
        # print(self.size)
        text_edit.config(font=("Helvatical",self.size))

    def zoom_out(self):
        self.size = self.size -  2
        # print(self.size)
        text_edit.config(font=("Helvatical",self.size))



######################## Code For help menyu function

def link_dev():
    web.open("https://github.com/rajvinder21/")



def link_code():
    web.open("https://github.com/rajvinder21/Python-Note-Pad")

####################### Tkiner Widget Start from here ###################### 


root = Tk()
root.title("Note Pad")
img = PhotoImage(file='notes.png')
root.iconphoto(False, img)
root.geometry("1000x600")



###########     Adding Menu From  Here #################

filemenu = Menu(root)
 
m1 = Menu(filemenu,tearoff=0)
m1.add_command(label="Open File", command=select_file)
m1.add_command(label="Save As", command=saveasFile)
m1.add_command(label="Save", command=save_file)
m1.add_separator()
m1.add_command(label="Exit", command=exit)

root.config(menu=filemenu)
filemenu.add_cascade(label="File",menu=m1)

m2 = Menu(filemenu, tearoff=0)
edit_obj = edit()

m2.add_command(label="Copy", command=edit_obj.getSelective)
m2.add_command(label="Paste",command=edit_obj.paste)
m2.add_command(label="Clear All",command=edit_obj.clearFile)
root.config(menu=filemenu)
filemenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(filemenu,tearoff=0)
zoom_obj = zoomer()
m3.add_command(label="Zoom In", command=zoom_obj.zoom_in)
m3.add_command(label="Zoom Out", command=zoom_obj.zoom_out)

root.config(menu=filemenu)
filemenu.add_cascade(label="View",menu=m3)


m4 = Menu(filemenu,tearoff=0)

m4.add_command(label="Show Me Code", command=link_code)
m4.add_command(label="About Developer", command=link_dev)

root.config(menu=filemenu)
filemenu.add_cascade(label="Help", menu=m4)

text_edit = Text(root,width=200, height=50,background="#232D3F",fg="white", font=('Helvatical',14),insertbackground="white")
AddNoteText = "Add Your Text Here......"
text_edit.insert(END,AddNoteText)
text_edit.focus_set()
text_edit.pack(fill="both")




root.mainloop()


