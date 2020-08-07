import tkinter as tk
from os import name, path, system, startfile
from time import sleep

class gppCompiler(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.envProp()
    

    def envProp(self):
        self.run = tk.Button(self, text='     Run     ', fg='green', font=('helvetica', 11, 'bold'), command=self.startGpp)
        self.run.pack(pady=2)
        self.quit = tk.Button(self, text='     Quit     ', fg='red', font=('helvetica', 10, 'bold'), command=self.master.destroy)
        self.quit.pack(pady=2)
        self.info = tk.Label(self, text='made by felphn\nminGW environment', fg='grey')
        self.info.pack(pady=2)
    

    def startGpp(self):
        system(f'g++ "{cFile}"')
        checkCompFile = path.isfile(f'{path.dirname(path.realpath(__file__))}\\a.exe')
        if checkCompFile == True:
            startfile(f'{path.dirname(path.realpath(__file__))}\\a.exe')
        else:
            pass


if name == 'nt':
    system('cls')
    getFile = str(input('File name?\n> '))
    checkFile = path.isfile(f'{path.dirname(path.realpath(__file__))}\\{getFile}')
    if checkFile == True:
        print('-'*22, '\nDone! Process started.')
        sleep(.5)
        system('cls')
        cFile = f'{path.dirname(path.realpath(__file__))}\\{getFile}'
        root = tk.Tk()
        root.title('C/C++ Compiler')
        root.geometry('260x105')
        root.resizable(0, 0)
        app = gppCompiler(master=root)
        app.mainloop()
    else:
        print('-'*44, "\n!>> Error: Couldn't find the specified file!\n")
        print('Check if the c/cpp file is in the same directory as the compiler.\n')
        system('pause')
else:
    print('!>> Not an Windows OS!')
