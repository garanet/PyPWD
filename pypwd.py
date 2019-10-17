#!/usr/bin/env python3
####### PYPWD MANAGER BY GARANET.NET Version 1.0.8 ####
import sys
sys.path.append("./libs/")
from core import *
from createmaster import *
from loginmenu import *
from mainmenu import *
#######################################################
class Login(QtWidgets.QWidget, Ui_loginmenu):    
    switch_window = QtCore.pyqtSignal()    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        return None

class MainWindow(QtWidgets.QWidget, Ui_MainMenu):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        return None
        
class CreateMaster(QtWidgets.QWidget, Ui_createmaster):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        return None
    
#######################################################        
class Controller:
    def __init__(self):
        pass
    
    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.login.show()
        return None
            
    def show_main(self):
        self.window = MainWindow()
        try:
            self.login.close()
        except:
            self.create.close()            
        ### Start session Token/Timeout
        session = core.session()      
        self.window.show()
        return None
        
    def show_create(self):
        self.create = CreateMaster()
        self.create.switch_window.connect(core.restart)
        self.create.show()
        return None
    
#######################################################        
def main():
    try:
        if os.path.isfile(filename) is True:
        ### Show Login Session
            app = QtWidgets.QApplication(sys.argv)
            controller = Controller()
            controller.show_login()
            sys.exit(app.exec_())
            core.exit_now('','')
            return None
        else:
        ### Show Create Master
            app = QtWidgets.QApplication(sys.argv)
            controller = Controller()
            controller.show_create()
            sys.exit(app.exec_())
            core.exit_now('','')
            return None
    except:
    ### Show Create Master as default     
        app = QtWidgets.QApplication(sys.argv)
        controller = Controller()
        controller.show_create()
        sys.exit(app.exec_())
        core.exit_now('','')
    return None
#######################################################
if __name__ == "__main__":
    main()