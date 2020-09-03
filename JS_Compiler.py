import tkinter as tk
from os import name, system
from os.path import isfile, dirname, realpath
from subprocess import Popen


class JsCompiler(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.envProp()


    def envProp(self):
        self.run = tk.Button(self, text='     Run     ', fg='green', font=('helvetica', 11, 'bold'), command=self.startNode)
        self.run.pack(pady=2)
        self.quit = tk.Button(self, text='     Quit     ', fg='red', font=('helvetica', 10, 'bold'), command=self.master.destroy)
        self.quit.pack(pady=2)
        self.info = tk.Label(self, text='made by felpshn\nNode JS environment', fg='grey')
        self.info.pack(pady=2)


    def startNode(self):
        if name == 'nt':
            getNode = 'C:\\Program Files\\nodejs\\node.exe'
            Popen([r'{}'.format(getNode), '{}'.format(jsFile)])
            system('cls')
        else:
            try:
                getNode = '/usr/bin/node'
                Popen([r'{}'.format(getNode), '{}'.format(jsFile)])
            except:
                getNode = '/usr/bin/nodejs'
                Popen([r'{}'.format(getNode), '{}'.format(jsFile)])
            system('clear')


if name == 'nt':
    system('cls')
    getFile = str(input('File name?\n> '))
    jsFile = f'{dirname(realpath(__file__))}\\{getFile}'
    checkFile = isfile(jsFile)
else:
    system('clear')
    getFile = str(input('File name?\n> '))
    jsFile = f'{dirname(realpath(__file__))}/{getFile}'
    checkFile = isfile(jsFile)
if checkFile == True:
    print('-'*22, '\nDone! Process started.')
    root = tk.Tk()
    root.title('JS Compiler')
    root.geometry('235x105')
    root.resizable(0, 0)
    app = JsCompiler(master=root)
    app.mainloop()
else:
    print('-'*44, "\n!>> Error: Couldn't find the specified file!\n")
    print('Check if the js file is in the same directory as the compiler.\n')
    input('Press any key to continue ...')
