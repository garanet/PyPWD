####### PYPWD MANAGER BY GARANET.NET Version 1.0.8 ####
import sys
sys.path.append("./libs/")
from core import *
from mainmenu import *
######################################################
class Ui_createpwd(object):
    def setupUi(self, createpwd):
        createpwd.setObjectName("createpwd")
        createpwd.resize(354, 313)
        createpwd.setWindowModality(QtCore.Qt.ApplicationModal)        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(createpwd.sizePolicy().hasHeightForWidth())
        createpwd.setSizePolicy(sizePolicy)
        createpwd.setMaximumSize(QtCore.QSize(354, 313))
        self.label = QtWidgets.QLabel(createpwd)
        self.label.setGeometry(QtCore.QRect(50, 0, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(createpwd)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(createpwd)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(createpwd)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(createpwd)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")        
        self.lineProject = QtWidgets.QLineEdit(createpwd)
        self.lineProject.setGeometry(QtCore.QRect(110, 50, 201, 30))
        self.lineProject.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineProject.setObjectName("lineProject")
        self.lineUsername = QtWidgets.QLineEdit(createpwd)
        self.lineUsername.setGeometry(QtCore.QRect(110, 90, 201, 30))
        self.lineUsername.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineUsername.setObjectName("lineUsername")
        self.linePassword = QtWidgets.QLineEdit(createpwd)
        self.linePassword.setGeometry(QtCore.QRect(110, 130, 201, 30))
        self.linePassword.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.linePassword.setObjectName("linePassword")
        self.lineNotes = QtWidgets.QLineEdit(createpwd)
        self.lineNotes.setGeometry(QtCore.QRect(110, 170, 201, 30))
        self.lineNotes.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineNotes.setObjectName("lineNotes")
        self.pushSave = QtWidgets.QPushButton(createpwd)
        self.pushSave.setGeometry(QtCore.QRect(10, 260, 110, 41))
        self.pushSave.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushSave.setObjectName("pushSave")
        self.pushClear = QtWidgets.QPushButton(createpwd)
        self.pushClear.setGeometry(QtCore.QRect(120, 260, 110, 41))
        self.pushClear.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushClear.setObjectName("pushClear")
        self.pushClose = QtWidgets.QPushButton(createpwd)
        self.pushClose.setGeometry(QtCore.QRect(230, 260, 110, 41))
        self.pushClose.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushClose.setObjectName("pushClose")
        self.label_Msg = QtWidgets.QLabel(createpwd)
        self.label_Msg.setGeometry(QtCore.QRect(0, 210, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Msg.setFont(font)
        self.label_Msg.setText("")
        self.label_Msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Msg.setObjectName("label_Msg")
        
        self.toolButtonGenerate = QtWidgets.QToolButton(createpwd)
        self.toolButtonGenerate.setGeometry(QtCore.QRect(310, 130, 30, 30))
        self.toolButtonGenerate.setObjectName("toolButtonGenerate")

        self.retranslateUi(createpwd)
        QtCore.QMetaObject.connectSlotsByName(createpwd)
        ### Action Buttons
        self.pushSave.clicked.connect(self.newpassword)
        self.pushClear.clicked.connect(self.clearall)
        self.pushClose.clicked.connect(self.reject) 
        self.toolButtonGenerate.clicked.connect(self.generate) 
        
    def retranslateUi(self, createpwd):
        _translate = QtCore.QCoreApplication.translate
        createpwd.setWindowTitle(_translate("createpwd", CPWT))
        self.label.setText(_translate("createpwd", CPNP))
        self.label_2.setText(_translate("createpwd", CPPN))
        self.label_3.setText(_translate("createpwd", LUSR))
        self.label_4.setText(_translate("createpwd", LPWD))
        self.label_5.setText(_translate("createpwd", CPNO))
        self.pushSave.setText(_translate("createpwd", CPSP))
        self.pushClear.setText(_translate("createpwd", CPCA))
        self.pushClose.setText(_translate("createpwd", CPCD))
        self.toolButtonGenerate.setText(_translate("createpwd", "..."))
    
    ### CLOSE DIALOG
    def reject(self):
        core.sessioncheck()
        self.close()
        return False
    
    ### CLEAR FIELDS
    def clearall(self):
        self.lineProject.setText("")
        self.lineUsername.setText("")
        self.linePassword.setText("")
        self.lineNotes.setText("")
        core.sessioncheck()
        self.repaint()
        return None
    
    ### GENERATE RANDOM PASSWORD
    def generate(self):
        t = time.time()
        data = '{}{}'.format(t,rand)
        encodedBytes = base64.b64encode(data.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        encodedStr = encodedStr[13:23]
        self.linePassword.setText(encodedStr)
        self.repaint()
        return True
        
    ### CREATE NEW PASSWOD
    def newpassword(self):
        core.sessioncheck()        
        project = self.lineProject.text()        
        username = self.lineUsername.text()
        password = self.linePassword.text()
        notes = self.lineNotes.text()
        if project == '':
            self.label_Msg.setText(CPPE)
            self.repaint()
            return None
        if username == '':
            self.label_Msg.setText(LUCE)
            self.repaint()
            return None
        if password == '':
            self.label_Msg.setText(LPCE)
            self.repaint()
            return None

        ### Hash password
        p = core.hash_password(password)
        
        ### Check duplicates IDs
        date = core.now()
        df = pd.read_csv(filetemp, header=0)
        did = df['id']
        nid = len(df)              
        for idd in did:
            if idd == nid:
                nid = 1+nid
            else:
                nid = nid

        ### Create date
        ndate = "{}-{}-{}".format(date[3],date[2], date[1])
        df.loc[nid] = [nid, project, username, p, notes, ndate]
        ### Save the changes
        try:
            with open(filetemp, 'w') as f:
                df.to_csv(f,sep=',', encoding=encoding,index=False, mode='a')
                f.close()
                ### CREATE ENC KEY for FILE AND HASH                               
                admpwd = df['password'][0]
                password = core.detemppwd(admpwd)
                keyfile = core.decrypt(password)        
                pyAesCrypt.encryptFile(filetemp, filename, keyfile, bufferSize) 
                
                self.label_Msg.setText(CPPS)
                self.lineProject.setText("")
                self.lineUsername.setText("")
                self.linePassword.setText("")
                self.lineNotes.setText("")
                core.sessioncheck()
                self.repaint()
        except:            
            self.label_Msg.setText(CPCS)
            self.repaint()
            core.sessioncheck()
        return None
