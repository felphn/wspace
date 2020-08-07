import tkinter as tk
from os import name, path, system
from subprocess import Popen

class jsCompiler(tk.Frame):
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
        self.info = tk.Label(self, text='made by felphn\nNode JS environment', fg='grey')
        self.info.pack(pady=2)


    def startNode(self):
        getNode = 'C:\\Program Files\\nodejs\\node.exe'
        Popen([r'{}'.format(getNode), '{}'.format(jsFile)])
        system('cls')


if name == 'nt':
    system('cls')
    getFile = str(input('File name?\n> '))
    checkFile = path.isfile(f'{path.dirname(path.realpath(__file__))}\\{getFile}')
    if checkFile == True:
        print('-'*22, '\nDone! Process started.')
        jsFile = f'{path.dirname(path.realpath(__file__))}\\{getFile}'
        root = tk.Tk()
        root.title('JS Compiler')
        root.geometry('235x105')
        root.resizable(0, 0)
        app = jsCompiler(master=root)
        app.mainloop()
    else:
        print('-'*44, "\n!>> Error: Couldn't find the specified file!\n")
        print('Check if the js file is in the same directory as the compiler.\n')
        system('pause')
else:
    print('!>> Not an Windows OS!')
