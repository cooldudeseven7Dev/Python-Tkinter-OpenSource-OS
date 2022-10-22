from tkinter import *  # type: ignore
from tkinter import messagebox, simpledialog

ver = '1.1'
class ostool:
    class apps:
        def quitOS(): # type: ignore
            quit()
        def Addition(): # type: ignore
            Num1=simpledialog.askinteger('Calculator','Number 1:')
            Num2=simpledialog.askinteger('Calculator','Number 2:')
            messagebox.showinfo('Calculator Output',str(Num1+Num2))  # type: ignore
        def Subtraction(): # type: ignore
            Num1 = simpledialog.askinteger('Calculator','Number 1:')
            Num2 = simpledialog.askinteger('Calculator','Number 2:')
            messagebox.showinfo('Calculator Output',str(Num1-Num2)) # type: ignore 
        def Divide(): # type: ignore
            Num1 = simpledialog.askinteger('Calculator','Number 1:')
            Num2 = simpledialog.askinteger('Calculator','Number 2:')
            messagebox.showinfo('Calculator Output',str(Num2/Num1)) # type: ignore
        def Multiply(): # type: ignore
            Num1 = simpledialog.askinteger('Calculator','Number 1:')
            Num2 = simpledialog.askinteger('Calculator','Number 2:')
            messagebox.showinfo('Calculator Output',str(Num1*Num2)) # type: ignore
    class appSetup:
        def mainSetup(): # type: ignore
            quitOS= Button(root,text='Quit',command=ostool.apps.quitOS)
            quitOS.grid()
            Addition= Button(root,text='Addition',command=ostool.apps.Addition)
            Addition.grid()
            Subtraction= Button(root, text='Substraction',command=ostool.apps.Subtraction)
            Subtraction.grid()
            Divide= Button(root,text='Divide',command=ostool.apps.Divide)
            Divide.grid()
            Multiply= Button(root,text='Multiply',command=ostool.apps.Multiply)
            Multiply.grid()
            #Write Above
            VerMessage= Label(root,text='Version: '+ver)
            VerMessage.grid(row=450,column=450,sticky=W)
            
            

username=simpledialog.askstring('Login','Please enter your username')
NonUserUsername = 'guest'
DefaultUser = NonUserUsername.encode()
if username==DefaultUser.decode():
    messagebox.showinfo('Message','Logged In')
    root=Tk()
    root.geometry('750x750')
    ostool.appSetup.mainSetup()
    root.mainloop()
elif not username==DefaultUser.decode():
    messagebox.showerror('Error','no username was found to login to')
