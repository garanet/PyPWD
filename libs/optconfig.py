####### PYPWD MANAGER BY GARANET.NET Version 1.0.8 ####
import sys
sys.path.append("./libs/")
from core import *
#######################################################
class Ui_Options(object):
    def setupUi(self, Options):
        Options.setObjectName("Options")
        Options.setWindowModality(QtCore.Qt.ApplicationModal)
        Options.resize(409, 513)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Options.sizePolicy().hasHeightForWidth())
        Options.setSizePolicy(sizePolicy)
        Options.setMinimumSize(QtCore.QSize(409, 513))
        Options.setMaximumSize(QtCore.QSize(409, 513))
        self.label_Timeout = QtWidgets.QLabel(Options)
        self.label_Timeout.setGeometry(QtCore.QRect(10, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Timeout.setFont(font)
        self.label_Timeout.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Timeout.setObjectName("label_Timeout")
        self.label_Encoding = QtWidgets.QLabel(Options)
        self.label_Encoding.setGeometry(QtCore.QRect(10, 130, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Encoding.setFont(font)
        self.label_Encoding.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Encoding.setObjectName("label_Encoding")
        self.label_Language = QtWidgets.QLabel(Options)
        self.label_Language.setGeometry(QtCore.QRect(0, 80, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Language.setFont(font)
        self.label_Language.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Language.setObjectName("label_Language")
        
        self.lineTimeout = QtWidgets.QLineEdit(Options)
        self.lineTimeout.setGeometry(QtCore.QRect(160, 30, 181, 21))
        self.lineTimeout.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineTimeout.setObjectName("lineTimeout")
        self.comboLanguage = QtWidgets.QComboBox(Options)
        self.comboLanguage.setGeometry(QtCore.QRect(160, 70, 201, 41))
        self.comboLanguage.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboLanguage.setObjectName("comboLanguage")
        self.comboEncoding = QtWidgets.QComboBox(Options)
        self.comboEncoding.setGeometry(QtCore.QRect(160, 120, 201, 41))
        self.comboEncoding.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboEncoding.setObjectName("comboEncoding")
        self.pushButtonExcel = QtWidgets.QPushButton(Options)
        self.pushButtonExcel.setGeometry(QtCore.QRect(20, 170, 181, 51))
        self.pushButtonExcel.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButtonExcel.setObjectName("pushButtonExcel")        
        self.pushButtonBackup = QtWidgets.QPushButton(Options)
        self.pushButtonBackup.setGeometry(QtCore.QRect(210, 170, 181, 51))
        self.pushButtonBackup.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButtonBackup.setObjectName("pushButtonBackup")       
        self.pushButtonRemoveDB = QtWidgets.QPushButton(Options)
        self.pushButtonRemoveDB.setGeometry(QtCore.QRect(20, 230, 181, 51))
        self.pushButtonRemoveDB.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButtonRemoveDB.setObjectName("pushButtonRemoveDB")
        self.pushButtonImport = QtWidgets.QPushButton(Options)
        self.pushButtonImport.setGeometry(QtCore.QRect(210, 230, 181, 51))
        self.pushButtonImport.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButtonImport.setObjectName("pushButtonImport")
        self.lineOldPass = QtWidgets.QLineEdit(Options)
        self.lineOldPass.setGeometry(QtCore.QRect(170, 320, 201, 21))
        self.lineOldPass.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineOldPass.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineOldPass.setObjectName("lineOldPass")
        self.lineNewPass = QtWidgets.QLineEdit(Options)
        self.lineNewPass.setGeometry(QtCore.QRect(170, 360, 201, 21))
        self.lineNewPass.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineNewPass.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineNewPass.setObjectName("lineNewPass")
        self.label_Oldpwd = QtWidgets.QLabel(Options)
        self.label_Oldpwd.setGeometry(QtCore.QRect(20, 320, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Oldpwd.setFont(font)
        self.label_Oldpwd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Oldpwd.setObjectName("label_Oldpwd")
        self.label_Newpwd = QtWidgets.QLabel(Options)
        self.label_Newpwd.setGeometry(QtCore.QRect(20, 360, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Newpwd.setFont(font)
        self.label_Newpwd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Newpwd.setObjectName("label_Newpwd")
        self.label_Reset = QtWidgets.QLabel(Options)
        self.label_Reset.setGeometry(QtCore.QRect(100, 280, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Reset.setFont(font)
        self.label_Reset.setObjectName("label_Reset")
        self.pushButtonResetAdmin = QtWidgets.QPushButton(Options)
        self.pushButtonResetAdmin.setGeometry(QtCore.QRect(270, 390, 101, 51))
        self.pushButtonResetAdmin.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButtonResetAdmin.setObjectName("pushButtonResetAdmin")
        self.pushSaveExit = QtWidgets.QPushButton(Options)
        self.pushSaveExit.setGeometry(QtCore.QRect(110, 450, 181, 51))
        self.pushSaveExit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushSaveExit.setObjectName("pushSaveExit")
        self.label_msg = QtWidgets.QLabel(Options)
        self.label_msg.setGeometry(QtCore.QRect(30, 400, 231, 31))
        self.label_msg.setText("")
        self.label_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_msg.setObjectName("label_msg")

        self.retranslateUi(Options)
        QtCore.QMetaObject.connectSlotsByName(Options)
        ### Action Buttons
        self.pushButtonExcel.clicked.connect(self.excel)
        self.pushButtonRemoveDB.clicked.connect(self.removedb)
        self.pushButtonImport.clicked.connect(self.importdb)
        self.pushButtonBackup.clicked.connect(self.backup)
        self.pushButtonResetAdmin.clicked.connect(self.resetadm)
        self.pushSaveExit.clicked.connect(self.reject)        
        
    def retranslateUi(self, Options):
        _translate = QtCore.QCoreApplication.translate
        Options.setWindowTitle(_translate("Options", OWTE))
        self.label_Timeout.setText(_translate("Options", OSTO))
        self.label_Encoding.setText(_translate("Options", OSEN))
        self.label_Language.setText(_translate("Options", OSSL))
        self.pushButtonBackup.setText(_translate("Options", OSEB))
        self.pushButtonExcel.setText(_translate("Options", OSCB))
        self.pushButtonRemoveDB.setText(_translate("Options", ORRD))
        self.pushButtonImport.setText(_translate("Options", OSID))
        self.label_Oldpwd.setText(_translate("Options", OOOP))
        self.label_Newpwd.setText(_translate("Options", OONP))
        self.label_Reset.setText(_translate("Options", ORMP))
        self.pushButtonResetAdmin.setText(_translate("Options",OROF))
        self.pushSaveExit.setText(_translate("Options", CPSP))
        
        ### LANGUAGE OPT
        for lang in optlang:
            self.comboLanguage.addItem(lang)
            
        ### ENCODING OPT
        for enco in optenco:
            self.comboEncoding.addItem(enco)
        
        ### START 
        self.runconfig()

    ### EXPORT CLEAN PWD IN EXCEL   
    def excel(self):
        core.sessioncheck()
        try:
            date = core.now()
            home = os.path.expanduser('~')
            exportxls = "PyPWD_{}-{}-{}.xls".format(date[3],date[2], date[1])
            saveFilePath = QFileDialog.getSaveFileName(self, OPED, '{}/Downloads/{}'.format(home,exportxls),'*.xls')
            df = pd.read_csv(filetemp,index_col='id',skiprows=[1])  
            for p in df['password']:
                decoded_text = core.detemppwd(p)
                df.loc[df['password'] == p, 'password'] = decoded_text
            export_excel = df.to_excel (r'{}'.format(saveFilePath[0]), index=None, header=True)
            self.label_msg.setText(OFEE)
            self.repaint()
        except:
            self.label_msg.setText(OBEP)
            self.repaint()
        return None
    
    ### EXPORT CLEAN PWD IN EXCEL   
    def backup(self):
        core.sessioncheck()
        try:            
            date = core.now()
            home = os.path.expanduser('~')
            backup_file = "PyPWD_{}-{}-{}.zip".format(date[3],date[2], date[1])        
            backup_paths = ['./{}'.format(filename),'./libs/configfile.py'] 
            saveFilePath = QFileDialog.getSaveFileName(self, OPEB, '{}/Downloads/{}'.format(home,backup_file),"*.zip")        
            with ZipFile(saveFilePath[0],'w') as zip:
                for file in backup_paths:
                    zip.write(file)
            self.label_msg.setText(OBED)   
            self.repaint()
        except:
            self.label_msg.setText(OBEP)
            self.repaint()
        return None
    
    ### IMPORT A BCKP DB
    def importdb(self):
        core.sessioncheck()
        home = os.path.expanduser('~')
        importFilePath = QFileDialog.getOpenFileNames(self, OPIB, '{}/Downloads/{}'.format(home,filename), "*.zip")              
        if importFilePath:
            try:
                with ZipFile(importFilePath[0][0], 'r') as zip: 
                    zip.extract(filename)                    
                    zip.extract('libs/configfile.py')
                self.label_msg.setText(OIDB)
            except:
                self.label_msg.setText(OIDF)
        else:
            self.label_msg.setText(OIDF)
        self.repaint()
        return None
    
    def resetadm(self):
        core.sessioncheck()
        ### Check fields
        old_pwd = self.lineOldPass.text()
        new_pwd = self.lineNewPass.text()
        date = core.now()
        if not old_pwd:
            self.label_msg.setText(LPCE)
            self.repaint()
            return False
        if not new_pwd:
            self.label_msg.setText(LPCE)
            self.repaint()
            return False
        ### Check old PWD
        df = pd.read_csv(filetemp, header=0, nrows=1)
        username = df['username'][0]
        check = core.verify_password(df['password'][0], old_pwd)
        ### Regenerate file for NEW PWD
        if check is True and new_pwd != '':
            ### CREATE ENC KEY for FILE AND HASH
            encMaster = core.encryptMaster(new_pwd)
            keyfile = encMaster[0]
            p = encMaster[1]
            ### Create the dataframe to save
            ndate = "{}-{}-{}".format(date[3],date[2], date[1])
            df = pd.read_csv(filetemp,index_col=None, header=0)      
            df.loc[0] = ['0', 'master', username, p, 'MASTER PASSWORD', ndate]
            try:
                with open(filetemp, 'w') as f:
                    df.to_csv(f,sep=',', encoding=encoding,index=False)
                    f.close()
            except:
                with open(filetemp, 'x') as f:
                    df.to_csv(f,sep=',', encoding=encoding,index=False)
                    f.close()
            ### Save Encrypted file
            pyAesCrypt.encryptFile(filetemp, filename, keyfile, bufferSize)
            self.repaint()
            self.label_msg.setText(ORAP) 
            return None
        else:
            self.label_msg.setText(LMPW)
            self.repaint()
            return False
    
    ### REMOVE ALL DB
    def removedb(self):
        core.sessioncheck()
        buttonReply = QMessageBox.question(self, ODMT, ODMD, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            os.remove(filename)
            self.label_msg.setText(OAPR) 
        else:
            self.label_msg.setText(OAPN) 
        self.repaint()
        return None
    
    ### CLOSE THE OPT DIALOG
    def reject(self):
        try:
            f = open("./libs/configfile.py","rt")        
            options = f.read()
            result = [x.strip() for x in options.split('\n')]
            secout = result[0]; secout = [x.strip() for x in secout.split('=')];
            language = result[2]; language = [x.strip() for x in language.split('=')]
            encoding = result[1]; encoding = [x.strip() for x in encoding.split('=')]
            secoutN = self.lineTimeout.text()
            languageN = '"' + self.comboLanguage.currentText() + '"'
            encodingN = '"' + self.comboEncoding.currentText() + '"'
            f.close()
            options = options.replace(str(secout[1]),str(secoutN))
            options = options.replace(str(language[1]),str(languageN))
            options = options.replace(str(encoding[1]),str(encodingN))
            f = open("./libs/configfile.py","wt")         
            f.write(options)
            f.close()
            self.repaint()
            self.close()
        except:
            self.label_msg.setText(OAPP) 
            self.repaint()
            self.close()           
        return None
    
    ### LOAD THE FILE AND THE CONFIG VARS
    def runconfig(self):
        core.sessioncheck()
        f = open("./libs/configfile.py","r")     
        options = f.read()
        result = [x.strip() for x in options.split('\n')]
        secout = result[0]; secout = [x.strip() for x in secout.split('=')];
        language = result[2]; language = language.replace('"', '', 2); language = [x.strip() for x in language.split('=')]
        encoding = result[1]; encoding = encoding.replace('"', '', 2); encoding = [x.strip() for x in encoding.split('=')]
        self.lineTimeout.setText(secout[1])
        self.comboLanguage.setCurrentText(language[1])
        self.comboEncoding.setCurrentText(encoding[1])
        f.close()
        return None
