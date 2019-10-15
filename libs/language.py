####### PYPWD MANAGER BY GARANET.NET Version 1.0.8 ####
import sys
sys.path.append("./libs/")
from configfile import *
#######################################################

### Define Language List
optlang = ['English','Italian']

### Define Encoding List
optenco = ['utf-8','iso-8859-1','UTF-16','UTF-32']

### Check language config
if language == 'English':
    ### LOGIN PAGE
    LWTE = "PyPWD {} - Login".format(ver)
    LUSR = "Username"
    LPWD = "Password"
    LBOK = "OK"
    LMSG = "Welcome in PYPWD Manager {}".format(ver)
    LFUP = "Please fill the Username and password to LOGIN"
    LUCE = "The Username cannot be empty"
    LPCE = "The Passwords cannot be empty"
    LOMM = "Opening the Menu"
    LMPW = "Wrong Username or Password!"
    LMUW = "The MASTER Username is wrong"    
    ### DELETE DIALOG BOX
    DWTE = "PyPWD {} - Delete Password".format(ver)
    DQDR = "Are you sure to delete the record ?"
    DMDS = "After deleting, You cannot recover the record !"
    DBCC = "Cancel"
    DADM = "You cannot delete this record. Error !"
    DEBT = "Exit"
    DRDL = "Record deleted !"
    ### CREATE MASTER DIALOG
    CCMP = "Create the Master Pasword"
    CWTE = "PyPWD {} -  Create Master".format(ver)
    CMRB = "Repeat"
    CMSP = "Save"
    CRPE = "The repeat password cannot be empty!"
    CPNS = "The passwords are note the same!"
    ### CREATE PASSWORD DIALOG
    CPPE = "The project name cannot be empty"
    CPWT = "PyPWD {} - Create new".format(ver)
    CPNP = "Create a new Record Pasword"
    CPPN = "Project"
    CPNO = "Notes"
    CPSP = "Save"
    CPCA = "Clear All"
    CPCD = "Close"
    CPPS = "Password saved !"
    CPCS = "I cannot save this record !"
    ### OPTIONS DIALOG BOX
    OWTE = "PyPWD {} - Configuration".format(ver)
    OSTO = "Set Timeout"
    OSEN = "Set Encoding"
    OSSL = "Set Language"
    OSEB = "Export for Backup"
    OSCB = "Export Cleaned in Excel"
    ORRD = "Reset/Remove Database"
    OSID = "Import Database"
    OOOP = "Old Password"
    OONP = "New Password"
    ORMP = "Reset the Master password"
    OROF = "Reset"
    OFEE = "Excel Exported"
    OBED = "BACKUP Exported"
    OBEP = "I Cannot export the backup"
    OOFD = "PyPWD {} - Files Box".format(ver)
    OPED = "Export Excel"
    OPEB = "Export Backup"
    OPIB = "Import Backup"
    ORAP = "Reset admin password done, RESTART!"
    OIDB = "Imported, RESTART!"
    OAPR = "All saved password removed!"
    ODMD = "Are you sure to remove all Password ?"
    OAPN = "You cancel the Reset"
    ODMT = "Confirm delete"
    OIDF = "Failed to import the backup"
    OAPP = "I Cannot save the settings"
    OWEA = "Warning"
    ### MAINMANU OPT
    MWTE = "PyPWD {} - Main Menu".format(ver)
    MMCR = "Create"
    MMSP = "Search"
    MMDP = "Delete"
    MMSA = "Show All"
    MMCM = "Config"
    MMSO = "Select your Option:"
    MMRD = "Record Deleted"
    MMPC = "Record Copied in the Clipboard"
    MMRR = "Reading all saved Records"
    MMPN = "Searching in Projects and Notes..."
    MMMM = "Please select the row to delete"
    MMSE = "The Search box is empty, type something..."
    MMNF = "Not record found, try again..."
    MMFR = "Records Found: "
    MMTP = "There is a system problem..." 
    TMOT = "The Session is expired, closing the app!"
    
else:
    
    if language == 'Italian':
        ### LOGIN PAGE
        LWTE = "PyPWD {} - Login".format(ver)
        LUSR = "Nome"
        LPWD = "Password"
        LBOK = "OK"
        LMSG = "Benvenuto in PYPWD Manager {}".format(ver)
        LFUP = "Perfavore compila Nome e Password per accedere"
        LUCE = "Il Nome non puó essere vuoto"
        LPCE = "Le password non possono essere vuote"
        LOMM = "Aprendo il Menu"
        LMPW = "Nome o Password errate!"
        LMUW = "Il nome utente é sbagliato!"    
        ### DELETE DIALOG BOX
        DWTE = "PyPWD {} - Cancella Password".format(ver)
        DQDR = "Sei Sicuro di Cancellare questa Password ?"
        DMDS = "Dopo l'eliminazione non potrai recuperarla piú !"
        DBCC = "Cancella"
        DADM = "Non puoi cancellare questa password. Errore !"
        DEBT = "Esci"
        DRDL = "Password Cancellata !"
        ### CREATE MASTER DIALOG
        CCMP = "Crea la Password Principale"
        CWTE = "PyPWD {} -  Crea Password Principale".format(ver)
        CMRB = "Repeat"
        CMSP = "Save"
        CRPE = "The repeat password cannot be empty!"
        CPNS = "The passwords are note the same!"
        ### CREATE PASSWORD DIALOG
        CPPE = "Il progetto non puó essere vuoto"
        CPWT = "PyPWD {} - Crea Nuovo".format(ver)
        CPNP = "Crea una nuova Pasword"
        CPPN = "Progetto"
        CPNO = "Note"
        CPSP = "Salva"
        CPCA = "Cancella tutto"
        CPCD = "Chiudi"
        CPPS = "Password salvata !"
        CPCS = "Non Posso Salvare questa Password !"
        ### OPTIONS DIALOG BOX
        OWTE = "PyPWD {} - Configurazione".format(ver)
        OSTO = "Cambia Timeout"
        OSEN = "Cambia Codifica"
        OSSL = "Cambia Lingua"
        OSEB = "Esporta per Backup"
        OSCB = "Esporta in chiaro in Excel"
        ORRD = "Reset/Rimuovi Database"
        OSID = "Importa Database"
        OOOP = "Vecchia PWD"
        OONP = "Nuova PWD"
        ORMP = "Reset password principale"
        OROF = "Reset"
        OFEE = "EXCEL esportato"
        OBED = "BACKUP esportato"
        OOFD = "PyPWD {} - Files Box".format(ver)
        OPED = "Esporta Excel"
        OPEB = "Esporta Backup"
        OPIB = "Importa Backup"
        ORAP = "Admin password cambiata, riavvia"
        OIDB = "IMPORTATO, RIAVVIA"
        ODMD = "Sei Sicuro di eliminare tutto?"
        OAPR = "Tutte le password sono state rimosse!"
        OAPN = "Hai annullato l'operazione"
        ODMT = "Confirma cancellazione"
        OIDF = "Non posso importare il backup"
        OBEP = "Non posso esportare il backup"
        OAPP = "Non posso salvare le impostazioni"
        OWEA = "Attenzione"
        ### MAINMANU OPT
        MWTE = "PyPWD {} - Menu Principale".format(ver)
        MMCR = "Crea"
        MMSP = "Cerca"
        MMDP = "Cancella"
        MMSA = "Tutto"
        MMCM = "Config"
        MMSO = "Scegli un opzione:"
        MMPC = "Record copiato negli appunti"
        MMRD = "Password Cancellata"
        MMMM = "Perfavore seleziona una password da rimuovere"
        MMRR = "Leggendo tutte le password salvate..."
        MMPN = "Cercando in Progetti e Note..."
        MMSE = "Il BOX Cerca é vuoto, scrivi qualcosa..."
        MMNF = "Nessuna password trovata, riprova..."
        MMFR = "Password Trovate: "
        MMTP = "C'é stato un prolema..."
        OOFD = "PyPWD {} - Files Box".format(ver)
        TMOT = "Sessione scaduta, chiudo l'applicazione!"
        
    else:
        ### Default Language
        language == 'English'