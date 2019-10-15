# PyPWD 1.0.8
Python Password Manager ver. 1.0.8 
www.garanet.net

### Me:
In these last years, I created scripts in different languages (bash, python, Perl, Ruby) and recently I studied python as a Data engineer. So, in my spare time, after 10 years I started to program again and my Idea was to create something I really need, that I can trust and it can be flexible.
The first project has made for the terminal, but I had fun to learn how to export a python script to the GUI version.

### Why:
As Security Officer I cannot trust to save all my passwords to a KeyManager or to an external Password Manager, because I don't know if my passwords are transmitted via the internet or in the future we'll there a bulletin with some exploit then I have to re-change all my passwords.
I think is better to combine my basic python skills with what I need, then I created my own password manager, in Python3, with encryption based of random KEY and Password, and sure that it hasn't an internet connection.

### Requirements:
Tested on a MacOSX, working also in Linux
Python3
Pandas
cryptography
pyAesCrypt
PyQt5

### How Works:
First Run:
PyPWD > Creates Master Key with Password (Do not forget it or change the configfile, otherwise you'll be not able to open your password anymore).
PyPWD > Saves a DataFrame as CVS but as encrypted files with encrypted the encrypted password.
Login:
PyPWD > Dencrypts the password file, based of the username and password filled.

### Installation:
:# git clone https://github.com/garanet/PyPWD.git
:# cd PyPWD
:# pip3 install -r reqs.txt
:# python3 pypwd.py

### Compile APP for MAC
:# python3 setup.py py2app --qt-plugins


