# Bakalari Desktop
Desktop aplikace na bakalare, protoze se mi nechce porad otevirat prohlizec.  
## Features
Rozvrh(Pres WebKit, integrovany prohlizec)  
Znamky(Prumer a vsechny)  
Info o uzivateli(Rok studia, typ uctu, skola)  
Ukoly(pravdepodobne broken, alespon pro me nefungovaly)  
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
Parser na rozvrh(do toho bordelu se mi moc nechce)  
CLI Interface  
## OS
Testovane na Gentoo Linuxu, melo by fungovat cokoliv.  
Pokud output "python -V" neni 3.7 a vic, zmente shabang na zacatku na to, aby byl soubor otevren pythonem 3.7+  
Na Windows neni verze, mozna bude fungovat pres WSL nebo nejakou kompatibilni vrstvu.  
