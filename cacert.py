
#!C:\Python36\python.exe

import os, sys, configparser, cert, keyboard, browser, clipboard, shutil

from colorama import Fore, Style, init

init(autoreset=False) # for the color reset to default



def ReadiniFile():
    config = configparser.ConfigParser()

    config.read('config.ini')


    config.sections()

    cert = config['PATHS']['cert']
    copyCert = config['PATHS']['source']

    return cert, copyCert
	
def changeDir(xpath):
    if os.path.isdir(xpath):
        os.chdir(xpath)
        #print(Fore.BLUE, os.listdir() )
        
    else:
        print(Fore.RED + "ERROR: Sorry The dir:", xpath, "doesnt exist")
        exit()

def createDir(cDir):
    os.mkdir(cDir)  # create new dir
    os.chdir(cDir)  # enter to new dir
    print(Fore.CYAN + f'dir {cDir} was created')
    print(Fore.CYAN, os.getcwd())
    return True


def isExistsDir(cDir):
    if os.path.isdir(cDir):
        print( Fore.RED + "ERROR: Dir [[%s]] is exists" % cDir )
        choise = input('y  - delete, n - exit: ')
        if choise.lower() == 'y':
            for root, dir, files in os.walk(cDir):
                os.chdir(root)
                for i in files:
                    os.remove(i)
            os.chdir('../')
            os.rmdir(cDir)
            return True
        if choise.lower() == 'n':
            exit()
        else:
            exit()
    else:
        createDir(cDir)


def CopyCert(cDir):
    print(os.getcwd())
    cert, copyCert = ReadiniFile()

    source = f'{copyCert}\{cDir}\certnew.cer'
    target = f'{os.getcwd()}\{cDir}'

    print(source)
    print(target)
    exit()
    shutil.move(source, target)
    print(f'Certifikate was move from {source} to {target}')

def doCert(cDir):
     #createDir(cDir) #create dir
     if isExistsDir(cDir): #create dir
        createDir(cDir)
     cert.createCNF(cDir) #create cnf file
     cert.cKey(cDir) #cree key
     cert.cCsr(cDir) #create csf file
     cert.setClipboard(cDir)
     s = clipboard.paste()
     browser.generateCert(s)
     CopyCert(cDir)
     




def main():

    #because first arg is path of the program

    ################# testing ##################
    #key.cKey()
    ############################################

    if (len(sys.argv)) > 1:
        name = sys.argv[1]

        cert = ReadiniFile()[0]
        changeDir(cert)

        name = str(name)

        #doCert(name)
        #cert.cPfx(name)
        CopyCert(name)
    else:
        print(Fore.MAGENTA + 'warning: i\'m sorry, but argument is missing, please add argument - usually the name of certificate')




if __name__ == '__main__':
    main()


    
