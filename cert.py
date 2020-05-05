
# openssl pkcs12 -inkey secawarenesshra.key -in secawarenesshra.cer -export -out secawarenesshra.pfx

# z

import os, time, clipboard
from colorama import Fore, Style, init
init(autoreset=False) # for the color reset to default

def createCNF(cDir):
    print(Fore.GREEN + 'Creating CNF file...')
    f = cDir+'.cnf'
    with open(f, 'w') as cnfFile:
         cnfFile.write('''[req]
distinguished_name = req_distinguished_name
req_extensions = v3_req
[req_distinguished_name]
countryName = Country Name (2 letter code)
countryName_default = CZ
stateOrProvinceName = State or Province Name (full name)
stateOrProvinceName_default = Czech Republic
localityName = Locality Name (eg, city)
localityName_default = Praha
organizationName = Organization name
organizationName_default = MONETA Money Bank, a.s.
organizationalUnitName = Organizational Unit Name (eg, section)
organizationalUnitName_default = IT
commonName = Common name
commonName_default = ''' + cDir + '''
commonName_max = 64
[v3_req]# Extensions to add to a certificate request
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = ''' + cDir + '''
DNS.2 = MBCZVW6AL0IDMS1.mbid.cz
DNS.3 = MBCZVW6AL0IDMS1
DNS.4 = MBCZVW6AL0IDMT1
#DNS.4 = contractorstst.mbid.cz
#DNS.6 = ''' + cDir + '''dev.mbid.cz




         ''')
    cnfFile.close()



def cKey(cDir):
    print(Fore.GREEN + 'Creating key file...')
    cDir = cDir+'.key'
    TheCommand = r'openssl.exe genrsa -out ' + cDir +' 2048'
    os.system(TheCommand)
    time.sleep(5)


#openssl.exe req -new -out secawarenesshra.csr -key secawarenesshra.key -config secawarenesshra.cnf
def cCsr(cDir):
    print(Fore.GREEN + 'Creating CSR file...')
    csrFile = cDir+'.csr'
    keyFile = cDir+'.key'
    cnfFile = cDir+'.cnf'

    if os.path.isfile(keyFile) and os.path.isfile(cnfFile):
        TheCommand = 'openssl.exe req -new -out ' + csrFile +' -key ' + keyFile +' -config ' + cnfFile
        os.system(TheCommand)
        time.sleep(5)
    else:
        print( Fore.RED + "ERROR: The Files for create csr file dont exists" )

def setClipboard(cDir):
    print(Fore.BLUE + 'Copy csr file to clipboard')
    with open(cDir+'.csr','r') as s:
        s = s.read()
        s = clipboard.copy(s)




def cPfx(cDir):
    print(Fore.GREEN + 'Creating PFX file...')
    #os.chdir(r'c:\Users\212437054\Documents\certifikaty\' + cDir)
    os.chdir(cDir)
    print(os.listdir())
    keyFile = cDir+'.key'
    cerFile = 'certnew.cer' #cDir+'.cer'
    if os.path.isfile(cerFile) == False:
        print( Fore.RED + "ERROR: File [[%s]] is not exists, check The name of certificate" % cerFile )
        exit()
    else:
        out = cDir+'.pfx'

        TheCommand = 'openssl pkcs12 -inkey '+ keyFile +' -in '+ cerFile +' -export -out '+ out 
        os.system(TheCommand)

