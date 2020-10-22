<h1 align="center">bakalari-desktop</h1>

<div align="center">
  Desktop aplikace(2) pro pristup k informacim, protoze se mi nechce otevirat prohlizec  
  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Byl3x/bakalari-desktop)  
  ![GitHub last commit](https://img.shields.io/github/last-commit/Byl3x/bakalari-desktop)  
</div>  
## Features
Rozvrh
Znamky(Prumer a vsechny)  
Info o uzivateli(Rok studia, typ uctu, skola)  
Ukoly  
## Instalace
Je potreba python 3.7 nebo vyssi.  
Moduly: PyGObject, WebKit2Gtk, GTK a requests  
Vsechny soubory musi zustat ve stejne slozce(Nebo zmente misto v kodu)  
Prikazy: 
git clone https://github.com/Byl3x/bakalari-desktop.git  
cd bakalari-desktop  
./bakalari-desktop.py  
Pred tim musite ve baklari-desktop.py zmenit username, heslo a server  
Priklad formatu server url: "https://gvp.cz/info/api"  
## To Do
Windows verze
Lepsi Rozvrh
## OS
Testovane na Gentoo Linuxu, melo by fungovat cokoliv.  
Pokud output "python -V" neni 3.7 a vic, zmente shabang na zacatku na to, aby byl soubor otevren pythonem 3.7+  
Na Windows neni verze, mozna bude fungovat pres WSL nebo nejakou kompatibilni vrstvu.  
## TUI
Cela TUI byla napsana s ncurses, klavesove zkratky:  
u-show user info  
g-show average grades  
a-show all grades  
h-show homework 
t-show timetable  
q-quit
