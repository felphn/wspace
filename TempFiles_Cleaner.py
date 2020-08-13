from os import name, system, getenv, listdir, remove
from os.path import isfile, isdir
from shutil import rmtree
from time import sleep


def deleteErr(elmnt1, elmnt2):
    print(f'!>> Couldnt delete "{elmnt1}" in "{elmnt2}"')


def clearDir(pathscr):
    dirFiles = listdir(pathscr)
    for i in range(0, len(dirFiles)):
        try:
            remove(f"{pathscr}\\{dirFiles[i]}")
            if isfile(f"{pathscr}\\{dirFiles[i]}") == True:
                deleteErr(dirFiles[i], pathscr)
        except:
            if isdir(f"{pathscr}\\{dirFiles[i]}") == True:
                try:
                    rmtree(f"{pathscr}\\{dirFiles[i]}")
                except:
                    deleteErr(dirFiles[i], pathscr)


if name == 'nt':
    system('cls')
    localAppData = getenv('LOCALAPPDATA')
#Temp folder: "C:\Users\{UserName}\AppData\Local\Temp"
    clearDir(f'{localAppData}\\Temp')
    print('// "%temp%" folder cleaned.')
    sleep(1.5)
#%temp% folder: "C:\Windows\Temp"
    clearDir('C:\\Windows\\Temp')
    print('// "Temp" folder cleaned.')
    sleep(1.5)
#Prefetch folder: "C:\Windows\Prefetch"
    clearDir('C:\\Windows\\Prefetch')
    print('// "Prefetch" folder cleaned.')
    sleep(1.5)
#WinUpdate folder: "C:\Windows\SoftwareDistribution\Download"
    clearDir('C:\\Windows\\SoftwareDistribution\\Download')
    print('// Windows Update folder cleaned.\n')
    sleep(1.5)
else:
    print('!>> Not an Windows OS!\n')
    system('pause')
