from tkinter import *  # type: ignore
from tkinter import messagebox, simpledialog
from idlelib.tooltip import Hovertip
print('Imported Modules. Initializing.. Please Wait.') #Not encoded
vere = 'PTOSOS_1.6_PreBeta'
ver = vere.encode()
some1to0 = '1'
CTitle1e = 'Calculator'
CTitle1 = CTitle1e.encode()
LTitlee = 'Please Enter Your Username [Password Might Be Required]\nNot a user of PTOSOS Project? Please use the "guest" Username\nTip: use the "guest_RemoveSplash" To remove the splash screen displayed on start.'
LTitle = LTitlee.encode()
SplashDatae = 'Loading...\nThanks for running:\nPython Tkinter Open Source OS\nDevelopment by cooldudeseven7. Version:'+ver.decode()+'\nUse ALT+F4 to quit on windows\nUse Command+W For quitting on mac'
SplashData  =  SplashDatae.encode()
class ostool:
    class FrameworkApps:
        def WhatsNew(): # type: ignore
            messagebox.showinfo('Whats New in version'+ver.decode(),'Whats New in version'+ver.decode()+'\nAdded "Whats New" Button\nAdded calculator welcome message\nAdded Tooltips\nsome other mini updates')
    class apps:
        def quitOS(): # type: ignore
            quit()
        def Addition(): # type: ignore
            messagebox.showinfo('Welcome','Welcome to the PTOSOS Calculator. In the PTOSOS Calculator, you are able to do the following commands:\nAddition\nSubtraction\nMultiplication\nDivision\nEnjoy!\nV.1.1\nDeveloped by cooldudeseven7')
            Num1=simpledialog.askinteger(CTitle1.decode(),'Number 1:')
            Num2=simpledialog.askinteger(CTitle1.decode(),'Number 2:')
            messagebox.showinfo('Calculator Output',str(Num1+Num2))  # type: ignore
        def Subtraction(): # type: ignore
            messagebox.showinfo('Welcome','Welcome to the PTOSOS Calculator. In the PTOSOS Calculator, you are able to do the following commands:\nAddition\nSubtraction\nMultiplication\nDivision\nEnjoy!\nV.1.1\nDeveloped by cooldudeseven7')
            Num1 = simpledialog.askinteger(CTitle1.decode(),'Number 1:')
            Num2 = simpledialog.askinteger(CTitle1.decode(),'Number 2:')
            messagebox.showinfo('Calculator Output',str(Num1-Num2)) # type: ignore 
        def Divide(): # type: ignore
            messagebox.showinfo('Welcome','Welcome to the PTOSOS Calculator. In the PTOSOS Calculator, you are able to do the following commands:\nAddition\nSubtraction\nMultiplication\nDivision\nEnjoy!\nV.1.1\nDeveloped by cooldudeseven7')
            Num1 = simpledialog.askinteger(CTitle1.decode(),'Number 1:')
            Num2 = simpledialog.askinteger(CTitle1.decode(),'Number 2:')
            messagebox.showinfo('Calculator Output',str(Num1/Num2)) # type: ignore
        def Multiply(): # type: ignore
            messagebox.showinfo('Welcome','Welcome to the PTOSOS Calculator. In the PTOSOS Calculator, you are able to do the following commands:\nAddition\nSubtraction\nMultiplication\nDivision\nEnjoy!\nV.1.1\nDeveloped by cooldudeseven7')
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
            WhatsNewB = Button(root, text='Whats New',command=ostool.FrameworkApps.WhatsNew)
            WhatsNewB.grid(row=440,column=440,sticky=W)
            Hovertip(WhatsNewB,text='Click to open Whats New Menu. [FrameWork App]')
            Hovertip(Addition,text='Click to open Addition Menu.')
            Hovertip(Subtraction,text='Click to open Subtraction Menu.')
            Hovertip(Divide,text='Click to open Divide Menu.')
            Hovertip(Multiply,text='Click to open Multiply Menu.')
            Hovertip(quitOS,text='Click to quit OS.')
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
    root.title('Python Tkinter Open Source OS [PTOSOS] Developed by cooldudeseven7. ')
    root.wm_attributes('-fullscreen','True')
    def minisplash():
        bootsplash.destroy()
        root.wm_attributes('-fullscreen','False')
        ostool.appSetup.mainSetup()
    bootsplash = Label(root,text=str(SplashData.decode()))
    bootsplash.grid(row=0,column=0,sticky=W)
    bootsplash.after(3000,minisplash)
    root.mainloop()
if username=='guest_RemoveSplash':
    wss=messagebox.askyesno('WARNING!','WARNING!: You have chose to run withought splash screen. Please note that the username is NOT ENCODED! However, It still has minimal encoded. Are you sure you want to run withought splash?')
    if wss==True:
        root=Tk()
        root.geometry('750x750')
        root.title('Python Tkinter Open Source OS [PTOSOS] Developed by cooldudeseven7. ')
        ostool.appSetup.mainSetup()
        root.mainloop()
if username=='UserList':
    messagebox.showinfo('UserList [Updated every version release]','Active users [guests not included]\nSpooktober\nNo More Active Users ¯\_(ツ)_/¯\nWant to create your own? Check the link in the github repo.') # type: ignore
if username=='Spooktober':
    if some1to0=='1':
        messagebox.showinfo('Happy Halloween!','A special account was activated for now, Happy halloween! [You will boot withought a splash screen!]')
        root = Tk()
        root.title('Happy Halloween from PTSOS!')
        root.geometry('750x750')
        ostool.appSetup.mainSetup()
        root.mainloop()
    else:
        messagebox.showerror('Whoops!','Its not october. Please wait for october.')
elif not username==DefaultUser.decode() and not username=='guest_RemoveSplash' and not username=='UserList' and not username=='Spooktober':
    messagebox.showerror('Error','no username was found to login to')
    messagebox.showinfo('Message','Want to add a costoum user? Please look at the link in the github repo.')