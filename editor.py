#NOTEPAD
from tkinter import*
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo
from tkinter import simpledialog
import os
from deep_translator import GoogleTranslator

root = Tk()
root.title("Untitled - Scribble")
root.geometry("800x700")
file = None

def newfile():
    global file
    root.title("Untitled - Scribble")
    #first line and 0th character
    textarea.delete(1.0,END)
    file = None
    
def openfile():
    global file
    file=askopenfilename(defaulttexttension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
       file = None
    else:
        root.title(os.path.basename(file)+" -Scribble")
        textarea.delete(1.0,END)
        f = open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
        
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitle.txt",defaulttextension=".txt",filetypes=[("All Files","*.*"),
                                                                                              ("Text Documents","*.txt")])
        if file ==" ":
            file = None
        else:
            f = open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"- Scribble")
    else:
        f = open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
        
def quitApp():
    root.destroy()
    
def cut():
    textarea.event_generate(("<<Cut>>"))
    
def copy():
    textarea.event_generate(("<<Copy>>"))
    
def paste():
    textarea.event_generate(("<<Paste>>"))
    
def helpmenu():
    showinfo("Notepad","Notepad By Gautami")

def translate():
    answer = simpledialog.askstring("Input", "Which word do you want scribble to translate?",
                                parent=root)
    ch = simpledialog.askstring("Input","marathi->mr,french->fr,korean->ko,japnese->ja",
                                parent=root)
    translated = GoogleTranslator(source='auto', target=ch).translate(answer)
    print(translated)
    showinfo("The translation comes as:",translated)
        
#Add Textarea
textarea = Text(root,font="lucida 13")
textarea.pack(expand=True,fill=BOTH)

#Add Scrollbar
scroll = Scrollbar(textarea)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)

#menus
MenuBar = Menu(root)

FileMenu = Menu(MenuBar,tearoff=0)
FileMenu.add_command(label="New",command=newfile)
FileMenu.add_command(label="Open",command=openfile)
FileMenu.add_command(label="Save",command=savefile)
FileMenu.add_command(label="Exit",command=quitApp)
MenuBar.add_cascade(label="File",menu=FileMenu)

EditMenu = Menu(MenuBar,tearoff=0)
EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="Paste",command=paste)
MenuBar.add_cascade(label="Edit",menu=EditMenu)

HelpMenu = Menu(MenuBar,tearoff=0)
HelpMenu.add_command(label="About Notepad",command=helpmenu)
MenuBar.add_cascade(label="Help",menu=HelpMenu)

translatemenu = Menu(MenuBar,tearoff=0)
translatemenu.add_command(label="translator",command=translate)
MenuBar.add_cascade(label="Translate",menu=translatemenu)

root.config(menu=MenuBar)

root.mainloop()
