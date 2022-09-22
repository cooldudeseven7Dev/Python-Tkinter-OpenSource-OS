print('OS - Starting import of 3 modules')
print('OS - Import Graphics')
from ast import main
from tkinter import messagebox
from tkinter import *
print('OS - Import Other Modules [Non Graphical Modules]')
from time import sleep as wait
from os import system as cmd
print('OS - Initializing for boot')
wait(0.1)
cmd('cls')
print('OS - Initializing For GUI start')
class define:
    def SearchForApp():
        pass
    def CommandsList():
        print('OS - Output of buttonClick: Opening Command List')
        commandList = Tk()
        commandList.title('OS App/Command List')
        commandList.geometry('250x250')
        commandListCmds = Label(commandList,text='quitOS - Quits OS\n No more commands right now.')
        commandListCmds.pack()
print('OS - Initializing Main Window')
root = Tk()
root.title('OS Window')
root.geometry('500x500')
print('OS - Booting System, Starting Main GUI of system')
MainLabel = Label(root,text='Welcome to the OS! Please type in a Command/App to run:')
MainLabel.pack()
commandListButton = Button(root,text='Commands List',command=define.CommandsList)
commandListButton.pack()
print('OS - Output - Complete. Mainloop Started. Enjoy the OS!')
root.mainloop()
