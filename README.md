# Onboard CC100 programming

## Teilnehmer

- Bjarne Zaremba <bjarne.zaremba@wago.com>
- Nele Stocksmeyer <nele.stocksmeyer@wago.com>
- Bekim Imrihor <bekim.imrihor@wago.com>
- Tobias Pape <tobias.pape@wago.com>
- Tobias Schäkel <tobias.schaekel@wago.com>
- Mattis Schrade <mattis.schrade@wago.com>
- Konrad Holsmölle <konrad.holsmoelle@wago.com>
- Danny Meihoefer <danny.meihoefer@wago.com>
- Sascha Hahn <sascha.hahn@wago.com>

## Installation des Code-Servers auf dem CC100
### Einrichtung im WBM
1. WBM mit ``` 192.168.1.17 ``` aufrufen (Anmeldung mit: Benutzer: **admin**; Passwort: **wago**)
2. IP-Adresse auf ``` 192.168.2.xxx ``` ändern (*Configuration->Networking->TCP/IP-Configuration->Static-IP umstellen*)
3. WBM mit neuer IP-Adresse aufrufen (vorher Netzwerk-Einstellungen der Schnittstelle am PC passend einstellen)
4. SD-Karte hinzufügen (*Configuration -> Mass Storage -> Create new Filesystem on Memory Card (**Ext4**; Label: **sd***)

### Für Internet über den RaspberryPi
1. Image für den Raspberry vom Github runterladen (**!!Link folgt noch!!**)
2. Mit [*Windows Disk-Imager*](https://sourceforge.net/projects/win32diskimager/) das Image auf leere SD-Karte spielen
3. Raspberry starten
4. Treiber für das Display installieren ``` sudo bash ./LCD5-show ```
#### Einstellungen im WBM
6. Subnetzmaske **255.255.255.0** und Default Gateway **192.168.2.1** eintragen (*Configuration->Networking->TCP/IP-Configuration*)
7. Neuen DNS-Server mit IP **192.168.2.1** hinzufügen (*Configuration->Networking->TCP/IP-Configuration*)
8. IP-Forwarding through multiple interfaces aktivieren (*Configuration->Networking->Routing*) 
9. HTTP aktivieren (*Configuration->Ports and Services->Network Services*)
10. DNS-Server hinzufügen IP-Address: **192.168.2.1** ; Hostname: **Raspberry** (*Configuation->Ports and Services->DNS*)

### Installation des Code-Servers
1. Per SSH auf den CC100 schalten (Git Bash öffnen ``` ssh root@192.168.2.xxx ``` Passwort: **wago**)
2. startup.sh-Datei auf den CC100 laden (``` wget -P /root/startup https://raw.githubusercontent.com/wago-enterprise-education/cc100_vscode/main/startup.sh?token=GHSAT0AAAAAAB7X46MHPJJM34RNYN66ABVSZAO7HIA ``` )
3. Startup.sh ausführen ``` sh /root/startup/startup.sh ```

## Weiteres Hilfsreiches
### Raspberry Pi

#### Downloads

- [*Windows Disk-Imager*](https://sourceforge.net/projects/win32diskimager/)

- [*Image-Download*](https://www.raspberrypi.com/software/operating-systems/)

- [*Treiber für das 5" Touchdisplay*](https://joyiteurope-my.sharepoint.com/personal/onedrive_joyiteurope_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fonedrive%5Fjoyiteurope%5Fonmicrosoft%5Fcom%2FDocuments%2F5display%2FLCD%2Dshow%2Dmaster%2Ezip&parent=%2Fpersonal%2Fonedrive%5Fjoyiteurope%5Fonmicrosoft%5Fcom%2FDocuments%2F5display&ga=1)

#### Anleitungen

Treiber-Installation:
``` bash
cd Downloads
unzip LCD-show-master.zip
cd LCD-show-master/
sudo bash ./LCD5-show
```


