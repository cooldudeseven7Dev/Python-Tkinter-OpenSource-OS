print('OS - Starting import of 3 modules')
print('OS - Import Graphics')
from ast import main
from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import turtle
guy = turtle.Turtle()
print('OS - Import Other Modules [Non Graphical Modules]')
from time import sleep as wait
from os import system as cmd
print('OS - Initializing for boot')
wait(0.1)
print('OS - Initializing For GUI start')
class define:
    def SearchForApp():
        print('OS - Output of [run] buttonClick: Now searching and opening...')
        text=searchEntry.get()
        if text=='quitOS':
            quit('Quit the Mini Operating System.\nThanks for running!')
        if text=='TerminalGame':
            print('OS - Chat bot session: Started')
            name = input('Hello! Whats your name?')
            print('Nice to meet you, '+name)
            input('What hobby(s) do you like to do?')
            print('Intresting, '+name)
            print('Bye for now!')
            print('OS - Chat bot session: Over')
        if text=='Addition':
            a1 = input('Number 1:')
            a2 = input('Number 2:')
            print('OS - Output of addition:'+str(int(a1)+int(a2)))
        if text=='Subraction':
            a1 = input('Number 1:')
            a2 = input('Number 2:')
            print('OS - Output of Subtraction:'+str(int(a1)-int(a2)))
        if text=='Multiplication':
            a1 = input('Number 1:')
            a2 = input('Number 2:')
            print('OS - Output of Multiplication:'+str(int(a1)*int(a2)))
        if text=='Division':
            a1 = input('Number 1:')
            a2 = input('Number 2:')
            print('OS - Output of addition:'+str(int(a1)/int(a2)))
        if text=='Circle':
            print('OS - Turtle - Rendering Small Circle')
            guy.circle(50)
        if text=='BigCircle':
            print('OS - Turtle - drawing big circle')
            guy.circle(100)
        if text=='PasswordManager':
            action=input('Action [Read,Write,DeleteAll]')
            if action=='Read':
                file = open('passwords.txt','r')
                print(file.read())
            if action=='Write':
                file=open('passwords.txt','a')
                write=input('Write:')
                file.write(str(write))
                print('Sucess!')
            if action=='DeleteAll':
                yn=input('Are you sure? [y/n] Must be spelled as noted')
                if yn=='y':
                    file = open('passwords.txt','w')
                    file.write(' ')
                else:
                    print('Did not clear file.')

        print('OS - Output of buttonClick: Opening Command List')
        commandList = Tk()
        commandList.title('OS App/Command List')
        commandList.geometry('500x500')
        commandListCmds = Label(commandList,text='quitOS - Quits OS\nTerminalGame - Runs a chat bot in the terminal\nmath commands - calculator with 2 digit Addition,Subtraction,Multiplication,Division\nCircle - Draws a small circle using turtle\nBigCircle - Draws a big circle using turtle\n No more commands right now.')
        commandListCmds.pack()
print('OS - Initializing Main Window')
root = Tk()
root.title('OS Window')
root.geometry('750x750')
print('OS - Booting System, Starting Main GUI of system')
MainLabel = Label(root,text='Welcome to the OS! Please type in a Command/App to run:')
MainLabel.pack()
commandListButton = Button(root,text='Commands List',command=define.CommandsList)
commandListButton.pack()
searchEntry = Entry(root)
searchEntry.pack()
searchButton = Button(root,text='Run',command=define.SearchForApp)
searchButton.pack()
print('OS - ALERT OUTPUT: Actions will continue to be printed!')
print('OS - Output - Complete. Mainloop Started. Enjoy the OS!')
root.mainloop()
