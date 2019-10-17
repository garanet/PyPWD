####### PYPWD MANAGER BY GARANET.NET Version 1.0.8 ####
import os, sys, time, base64, pyAesCrypt
import pandas as pd

from zipfile import ZipFile 

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

sys.path.append("./libs/")
from configfile import *
from language import *
#######################################################
class core:
    
    ### Write the Timeout Session
    def session():
        token = base64.urlsafe_b64encode(os.urandom(60)) 
        timestart = time.time()
        f=open(sessiontmp,"w+")        
        f.write(str(token))
        f.write('\n')
        f.write(str(timestart))
        f.close()
        return(token,timestart)

    ### POPUP Timeout
    def dialog_exit():
        app = QtWidgets.QApplication([])
        infoBox = QtWidgets.QMessageBox()
        infoBox.setIcon(QtWidgets.QMessageBox.Warning)
        infoBox.setWindowTitle(OWEA)
        infoBox.setText(TMOT)
        infoBox.exec_()
        return False
    
    ### Check the Session
    def sessioncheck():
        try:
            f = open(sessiontmp,"r")        
            session = f.read()
            result = [x.strip() for x in session.split('\n')]
            otoken = result[0]
            timestart =  result[1]
            core.timeout(timestart)
            f.close()
            return True
        except:            
            core.exit_now('','')
            return False
        return None

    ### Calculate the Session Timeout
    def timeout(timestart):
        timedone = time.time()
        elapsed = float(timedone) - float(timestart)
        if elapsed >= secout:
            core.dialog_exit()
            self.close()            
            core.exit_now('','')
        else:
            return None
        return None

    ### Close all system    
    def exit_now(token,timestart):
        try:
            df.drop(df.index, inplace=True)
        except:
            timestart=''
        try:
            os.remove(filetemp)
        except:
            token=''
        try:
            os.remove(sessiontmp)
        except:
            pass
        try:
            os.system('exit')
        except:
            pass
        return(sys.exit(1))

    ### Simple DATE/TIME function
    def now():
        now = time.localtime()
        year = now[0]
        month = now[1]
        day = now[2]
        return (now,year,month,day)

    ### Restart the APP for the first login
    def restart():
        eapp = os.getcwd()
        os.execv('{}/pypwd.py'.format(eapp), sys.argv)        
        sys.exit()
        return None    
    
    ### Find and check the Master Password
    def detemppwd(password):        
        datapwd = password.split("b'")[1]        
        password = datapwd.split("'")[1]
        password = datapwd.encode(encoding) 
        keysalt = base64.urlsafe_b64encode(key+key)
        cipher_suite = Fernet(keysalt)
        password = cipher_suite.decrypt(password)     
        password = password.decode('utf-8')
        return password
    
    ### Decrypt password for keyfile
    def decrypt(password):
        bpass = bytes(password, encoding)
        kdf = PBKDF2HMAC(
             algorithm=hashes.SHA256(),
             length=23,
             salt=key,
             iterations=100000,
             backend=default_backend()
        )
        keyencrypt = base64.urlsafe_b64encode(kdf.derive(bpass))
        keyfile = keyencrypt.decode(encoding)
        return keyfile
    
    ### Encrypt / Decrypt Master File
    def encryptMaster(password):
        bpass = bytes(password, encoding)
        keysalt = os.urandom(16)
        kdf = PBKDF2HMAC(
             algorithm=hashes.SHA256(),
             length=23,
             salt=keysalt,
             iterations=100000,
             backend=default_backend()
         )
        keyfile = base64.urlsafe_b64encode(kdf.derive(bpass))        
        keyfile = keyfile.decode(encoding)
        ### READ CONFIG
        f = open("./libs/configfile.py","rt")        
        options = f.read()
        result = [x.strip() for x in options.split('\n')]
        key = result[3]; key = [x.strip() for x in key.split(' = ')];
        f.close()        
        ### SAVE SALT
        options = options.replace(str(key[1]),str(keysalt))
        f = open("./libs/configfile.py","wt")         
        f.write(options)        
        f.close()        
        ### SALT PASSWORD
        keysalt = base64.urlsafe_b64encode(keysalt+keysalt)
        bpass = bytes(password, encoding)
        cipher_suite = Fernet(keysalt)      
        encoded_text = cipher_suite.encrypt(bpass)
        return keyfile,encoded_text      
        
    ### Hashing Password
    def hash_password(password):
        keysalt = base64.urlsafe_b64encode(key+key)
        bpass = bytes(password, encoding)
        cipher_suite = Fernet(keysalt)      
        encoded_text = cipher_suite.encrypt(bpass)
        return encoded_text      

    ### Password Verification
    def verify_password(datapass,password):        
        keysalt = base64.urlsafe_b64encode(key+key)
        bpass = bytes(password, encoding)      
        cipher_suite = Fernet(keysalt) 
        datapwd = datapass.split("b'")[1]        
        datapass = datapwd.split("'")[1]
        datapass = datapwd.encode(encoding)        
        dtext = cipher_suite.decrypt(datapass)      
        dtext = dtext.decode(encoding)
        return password == dtext
############################################################################################################