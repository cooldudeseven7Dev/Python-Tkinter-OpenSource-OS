from tkinter import *  # type: ignore
from tkinter import messagebox, simpledialog
from idlelib.tooltip import Hovertip
fwUpdated = 0
fwupdatev = 'PTOSOS_1.7.1FW [Part One of 1.7]'
vere = 'PTOSOS_1.7.1 [Part One of 1.7]'
NonUserUsername = 'guest'
ver = vere.encode()
CTitle1e = 'Calculator'
TimeIndexedCMD = 1
CTitle1 = CTitle1e.encode()
LTitlee = 'Please Enter Your Username [Password Might Be Required]\n Not a user of PTOSOS Project? Please use the "guest" Username'
LTitle = LTitlee.encode()
class ostool:
    class apps:
        def WhatsNew():
            messagebox.showinfo('Changelog','Changelog\nHovertips on [some] buttons\nAdded "Whats New" Button\nNote from creater added [Please read it.]\nFramework update [Click Update Framework to fix version no.\nNo more right now! ¯\_(ツ)_/¯')
        def pleasenotice(): #type: ignore
            messagebox.showinfo('Please Read','I had been working on a version when my code had been erased. I did back it up, But turns out windows replaced a file withought asking me, Deleting the file because I had one named "main". I am really sorry I couldent show the version that I showed on my channel [ALOT OF HARD WORK, WASTED]. I will try to remake this version in the best way I can. Thank you for your time. \n\n ~cooldudeseven7\n  Creator')
        def quitOS(): # type: ignore
            q=messagebox.askyesno('Confirm Quit','Are you sure you want to quit?')
            if q==True:
                root.destroy()
                messagebox.showinfo('Message','Thanks for running PTSOS Beta! Click okay or close this message to full quit.')
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
            ah = Button(root,text='Please Read.',command=ostool.apps.pleasenotice)
            ah.grid()
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
            WhatsNew=Button(root,text='Whats New',command=ostool.apps.WhatsNew)
            WhatsNew.grid()
            fwUpdateb=Button(root,text='Update',command=ostool.Framework.apps_SPECIAL.fw_Update)
            fwUpdateb.grid()
            Hovertip(ah,'IMPORTANT MESSAGE about a hard worked on version. [From Creator]')
            Hovertip(quitOS,'Quit, That was simple. RIGHT?')
            Hovertip(Addition,'Add with two factors')
            Hovertip(Subtraction,'Subtract with two factors')
            Hovertip(Multiply,'Multiply with two factors')
            Hovertip(Divide,'Divide with two factors')
            Hovertip(WhatsNew,'Whats New')
            Hovertip(fwUpdateb,'Check for updates')
            #Write Above
            VerMessage= Label(root,text='Version: '+ver.decode())
            VerMessage.grid(row=450,column=450,sticky=W)
    class Framework:
        def FW_CMDMESSAGE_OUTPUT(msgType,message):
            print(msgType+' - '+message)  # type: ignore
        class apps_SPECIAL:
            def fw_Update():
                global fwUpdated
                global fwupdatev
                if fwUpdated==0:
                    fwUpdated+=1
                    global vere
                    vere=fwupdatev
                    messagebox.showinfo('Update','Updated to: '+vere+' [Framework Version availible in update button]')
                else:
                    messagebox.showerror('Update Error','Your on track!\nFramework Version: '+vere)
username=simpledialog.askstring('Login',LTitle.decode())
DefaultUser = NonUserUsername.encode()
if username==DefaultUser.decode():
    ostool.Framework.FW_CMDMESSAGE_OUTPUT('FW_OS_SECURITY','Login successful. Starting up...')  # type: ignore
    messagebox.showinfo('Message','Logged In')
    root=Tk()
    root.geometry('750x750')
    root.title('Python Tkinter Open Source OS [PTOSOS] Developed by cooldudeseven7. Version:'+ver.decode())
    ostool.appSetup.mainSetup()
    root.mainloop()
elif not username==DefaultUser.decode():
    messagebox.showerror('Error','no username was found to login to')
print('ready')  # type: ignore