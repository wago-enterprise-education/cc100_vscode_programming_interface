# VS Code for WAGO CC100 Web-IDE

**Dieses Repository ist ein Entwicklungs-Repository, das im Rahmen eines studentischen Projekts erstellt wurde und nicht regelmäßig gepflegt wird. Es handelt sich weder um eine stabile Version noch um ein offizielles Repository der WAGO GmbH & Co. KG.** 

## Teilnehmer
- Maik Rehburg <maik.rehburg@wago.com>
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

#### Einstellungen im WBM
6. Subnetzmaske **255.255.255.0** und Default Gateway **192.168.2.1** eintragen (*Configuration->Networking->TCP/IP-Configuration*)
7. Neuen DNS-Server mit IP **192.168.2.1** hinzufügen (*Configuration->Networking->TCP/IP-Configuration*)
8. IP-Forwarding through multiple interfaces aktivieren (*Configuration->Networking->Routing*) 
9. HTTP aktivieren (*Configuration->Ports and Services->Network Services*)
10. DNS-Server hinzufügen IP-Address: **192.168.2.1** ; Hostname: **Raspberry** (*Configuation->Ports and Services->DNS*)

### Installation des Code-Servers
1. Per SSH auf den CC100 schalten (Git Bash öffnen ``` ssh root@192.168.2.xxx ``` Passwort: **wago**)
2. startup.sh-Datei auf den CC100 laden (``` wget -P /root/startup https://raw.githubusercontent.com/wago-enterprise-education/cc100_vscode/main/startup.sh ``` )
3. Startup.sh ausführen ``` sh /root/startup/startup.sh ```
