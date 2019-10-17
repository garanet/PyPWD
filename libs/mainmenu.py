####### PYPWD MANAGER BY GARANET.NET Version 1.0.8 ####
import sys
sys.path.append("./libs/")
from core import *
from createpwd import *
from dialogdelete import *
from optconfig import *
#######################################################
class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainMenu.sizePolicy().hasHeightForWidth())
        MainMenu.setSizePolicy(sizePolicy)
        MainMenu.setMinimumSize(QtCore.QSize(1024, 768))
        MainMenu.setMaximumSize(QtCore.QSize(1024, 768))
        MainMenu.setFocusPolicy(QtCore.Qt.WheelFocus)
        MainMenu.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainMenu.setWindowModality(QtCore.Qt.ApplicationModal)
        self.lineSearch = QtWidgets.QLineEdit(MainMenu)
        self.lineSearch.setGeometry(QtCore.QRect(20, 40, 211, 31))
        self.pushButton_search = QtWidgets.QPushButton(MainMenu)
        self.pushButton_search.setGeometry(QtCore.QRect(230, 30, 111, 51))
        self.pushButton_search.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_showall = QtWidgets.QPushButton(MainMenu)
        self.pushButton_showall.setGeometry(QtCore.QRect(610, 30, 81, 51))
        self.pushButton_showall.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_showall.setObjectName("pushButton_showall")
        self.pushButton_create = QtWidgets.QPushButton(MainMenu)
        self.pushButton_create.setGeometry(QtCore.QRect(690, 30, 81, 51))
        self.pushButton_create.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_create.setObjectName("pushButton_create")        
        self.pushButton_delete = QtWidgets.QPushButton(MainMenu)
        self.pushButton_delete.setGeometry(QtCore.QRect(770, 30, 81, 51))
        self.pushButton_delete.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_config = QtWidgets.QPushButton(MainMenu)
        self.pushButton_config.setGeometry(QtCore.QRect(850, 30, 81, 51))
        self.pushButton_config.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_config.setObjectName("pushButton_config")
        self.pushButton_exit = QtWidgets.QPushButton(MainMenu)
        self.pushButton_exit.setGeometry(QtCore.QRect(930, 30, 81, 51))
        self.pushButton_exit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_exit.setObjectName("pushButton_exit")

        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineSearch.setFont(font)
        self.lineSearch.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineSearch.setObjectName("lineSearch")
        self.tableWidget = QtWidgets.QTableWidget(MainMenu)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 991, 671))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(611, 421))
        self.tableWidget.setMaximumSize(QtCore.QSize(1233, 842))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.VLine)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        #SingleSelection, MultiSelection, ExtendedSelection, ContiguousSelection
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setGridStyle(QtCore.Qt.DashDotLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(195)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setMinimumSectionSize(35)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)

        self.optionlabel = QtWidgets.QLabel(MainMenu)
        self.optionlabel.setGeometry(QtCore.QRect(450, 40, 161, 21))        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.optionlabel.setFont(font)
        self.optionlabel.setWordWrap(True)
        self.optionlabel.setOpenExternalLinks(True)
        self.optionlabel.setObjectName("optionlabel")
        self.msg_label = QtWidgets.QLabel(MainMenu)
        self.msg_label.setGeometry(QtCore.QRect(20, 10, 981, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.msg_label.setFont(font)
        self.msg_label.setText("")
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setWordWrap(True)
        self.msg_label.setOpenExternalLinks(True)
        self.msg_label.setObjectName("msg_label")           
        self.label_copy = QtWidgets.QLabel(MainMenu)
        self.label_copy.setGeometry(QtCore.QRect(20, 750, 991, 16))
        self.label_copy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_copy.setObjectName("label_copy")

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)
        
    ### Buttons action        
        self.pushButton_exit.clicked.connect(self.reject)
        self.pushButton_showall.clicked.connect(self.show_all)
        self.pushButton_search.clicked.connect(self.search_password)
        self.pushButton_create.clicked.connect(self.createpwd)
        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_config.clicked.connect(self.options)
        self.lineSearch.returnPressed.connect(self.search_password)

        self.tableWidget.doubleClicked.connect(self.copy)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", MWTE))
        self.pushButton_create.setText(_translate("MainMenu", MMCR))
        self.pushButton_search.setText(_translate("MainMenu", MMSP))
        self.pushButton_delete.setText(_translate("MainMenu", MMDP))
        self.pushButton_showall.setText(_translate("MainMenu", MMSA))
        self.pushButton_config.setText(_translate("MainMenu", MMCM))
        self.pushButton_exit.setText(_translate("MainMenu", DEBT))
        self.tableWidget.setSortingEnabled(True)
        self.optionlabel.setText(_translate("MainMenu", MMSO))
        self.label_copy.setText(_translate("MainMenu", "Copyright © Garanet.net 2019 - This copy is not for commercial use"))

    ### Close MainMenu without normal exit
    def closeEvent(self, event):
        core.exit_now('','')
        return None
    
    ### Exit/Close all (button)
    def reject(self):
        self.tableWidget.setRowCount(0);
        self.tableWidget.setColumnCount(0); 
        core.exit_now('','')
        return None
    
    ### Copy to clipboard
    def copy(self):
        for idx in self.tableWidget.selectionModel().selectedIndexes():
            row_number = idx.row()
            column_number = idx.column()
        cc = self.tableWidget.item(row_number,column_number)
        cc = cc.text()
        os.system("echo {}|pbcopy %".format(cc))
        self.msg_label.setText(MMPC)
        self.repaint()
        return None

    ### Create new password
    def createpwd(self):
        core.sessioncheck()
        self.tableWidget.setRowCount(0);
        self.tableWidget.setColumnCount(0); 
        self.createpwd = CreatePass()
        self.createpwd.show()
        return None
    
    ### Open the Options dialog box
    def options(self):
        core.sessioncheck()
        self.tableWidget.setRowCount(0);
        self.tableWidget.setColumnCount(0); 
        self.options = CreateOption()
        self.options.show()
        return None

    ### Delete selected password
    def delete(self):
        core.sessioncheck()
        try:            
            project = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            username = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()            
            notes = self.tableWidget.item(self.tableWidget.currentRow(),2).text()            
            row = self.tableWidget.currentRow()
            column = self.tableWidget.currentColumn()
            idx =  self.tableWidget.takeVerticalHeaderItem(row).text()
            self.options = DialogDelete()
            self.options.show()     
            self.msg_label.setText("") 
            self.repaint()
            row = ' ID: ' + idx + '\n Project: ' + project + '\n Username: '+ username + '\n Notes: ' + notes
            self.options.tablemsg.setText(row)
            self.options.label_id.setText(idx)
            self.options.label_id.hide()
            self.tableWidget.setRowCount(0);
            self.tableWidget.setColumnCount(0);            
            if ui.pushButtonCancel is True:
                ui.tablemsg.setText(MMRD)
                ui.tablemsg.repaint()
        except:
            self.msg_label.setText(MMMM)
            self.repaint()
        return None

    ### Show All password.
    def show_all(self):
        core.sessioncheck()
        self.tableWidget.setRowCount(0);
        self.tableWidget.setColumnCount(0); 
        self.msg_label.setText(MMRR)
        self.repaint()
        df = pd.read_csv(filetemp,index_col='id',skiprows=[1])  
        for p in df['password']:
            decoded_text = core.detemppwd(p)
            df.loc[df['password'] == p, 'password'] = decoded_text
        self.df = df
        nRows = len(self.df.index)
        nColumns = len(self.df.columns)
        R=int(nRows)        
        C=int(nColumns)
        Cn = list(df.columns.values)
        Rn = list(df.index.values)
        Rn = [str(i) for i in Rn] 
        self.tableWidget.setColumnCount(nColumns)
        self.tableWidget.setHorizontalHeaderLabels(Cn)
        self.tableWidget.setRowCount(nRows)
        self.tableWidget.setVerticalHeaderLabels(Rn)
        for i in range(R):
            for j in range(C):
                x = self.df.iloc[i, j]
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(x)))
        return None

    ### Search password in projects and notes.
    def search_password(self):
        core.sessioncheck()
        self.tableWidget.setRowCount(0);
        self.tableWidget.setColumnCount(0); 
        self.msg_label.setText(MMPN)
        self.repaint()
        sword = self.lineSearch.text()
        if len(sword) == 0:
            self.msg_label.setText(MMSE)
            self.repaint()
        else:
            try:
                df = pd.read_csv(filetemp,index_col='id',skiprows=[1])
                df_1 = df[df['project'].str.contains(sword, na=False, case=False)]
                df_2 = df[df['notes'].str.contains(sword, na=False, case=False)]
                if df_1.empty and df_2.empty:
                    self.msg_label.setText(MMNF)
                    self.repaint()
                    return False        
                else:
                    df_tot = pd.concat([df_1,df_2], ignore_index=False)
                    df_tot = df_tot.drop_duplicates()
                    tot_record = len(df_tot)
                    self.msg_label.setText(MMFR+'{}'.format(tot_record))
                    self.repaint()
                    for p in df_tot['password']:
                        decoded_text = core.detemppwd(p)
                        df_tot.loc[df_tot['password'] == p, 'password'] = decoded_text
                    self.df = df_tot
                    nRows = len(self.df.index)
                    nColumns = len(self.df.columns)
                    R=int(nRows)
                    C=int(nColumns)                    
                    Cn = list(self.df.columns.values)
                    Rn = list(self.df.index.values)
                    Rn = [str(i) for i in Rn]
                    self.tableWidget.setColumnCount(nColumns)
                    self.tableWidget.setHorizontalHeaderLabels(Cn)
                    self.tableWidget.setRowCount(nRows)
                    self.tableWidget.setVerticalHeaderLabels(Rn)
                    for i in range(R):
                        for j in range(C):
                            x = self.df.iloc[i, j]
                            self.tableWidget.setItem(i, j, QTableWidgetItem(str(x)))
                    return True
            except:
                self.msg_label.setText(MMTP)
                self.repaint()            
                return False
        return None
#######################################################
class CreatePass(QtWidgets.QWidget, Ui_createpwd):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        
class CreateOption(QtWidgets.QWidget, Ui_Options):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        
class DialogDelete(QtWidgets.QWidget, Ui_DialogDelete):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)        