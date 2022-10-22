from tkinter import *  # type: ignore
from tkinter import messagebox, simpledialog
print('Your data is SAFE! This version is designed to be more secure than previous versions.')
vere = 'PTOSOS_SAFEVERSION_1.5.2'
ver = vere.encode()
CTitle1e = 'Calculator'
CTitle1 = CTitle1e.encode()
LTitlee = 'Please Enter Your Username [Password Might Be Required]\n Not a user of PTOSOS Project? Please use the "guest" Username'
LTitle = LTitlee.encode()
class ostool:
    class apps:
        def quitOS(): # type: ignore
            quit()
        def Addition(): # type: ignore
            Num1=simpledialog.askinteger(CTitle1.decode(),'Number 1:')
            Num2=simpledialog.askinteger(CTitle1.decode(),'Number 2:')
            messagebox.showinfo('Calculator Output',str(Num1+Num2))  # type: ignore
        def Subtraction(): # type: ignore
            Num1 = simpledialog.askinteger(CTitle1.decode(),'Number 1:')
            Num2 = simpledialog.askinteger(CTitle1.decode(),'Number 2:')
            messagebox.showinfo('Calculator Output',str(Num1-Num2)) # type: ignore 
        def Divide(): # type: ignore
            Num1 = simpledialog.askinteger(CTitle1.decode(),'Number 1:')
            Num2 = simpledialog.askinteger(CTitle1.decode(),'Number 2:')
            messagebox.showinfo('Calculator Output',str(Num1/Num2)) # type: ignore
        def Multiply(): # type: ignore
            Num1 = simpledialog.askinteger(CTitle1.decode(),'Number 1:')
            Num2 = simpledialog.askinteger(CTitle1.decode(),'Number 2:')
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
            VerMessage= Label(root,text='Version: '+ver.decode())
            VerMessage.grid(row=450,column=450,sticky=W)
username=simpledialog.askstring('Login',LTitle.decode())
NonUserUsername = 'guest'
DefaultUser = NonUserUsername.encode()
if username==DefaultUser.decode():
    messagebox.showinfo('Message','Logged In')
    root=Tk()
    root.geometry('750x750')
    root.title('Python Tkinter Open Source OS [PTOSOS] Developed by cooldudeseven7. Version:'+ver.decode())
    ostool.appSetup.mainSetup()
    root.mainloop()
elif not username==DefaultUser.decode():
    messagebox.showerror('Error','no username was found to login to')