# Projekt "onboard CC100 programming" ET'23

## Teilnehmer

- Nele Stocksmeyer <nele.stocksmeyer@wago.com>
- Bekim Imrihor <bekim.imrihor@wago.com>
- Tobias Pape <tobias.pape@wago.com>
- Tobias Schäkel <tobias.schaekel@wago.com>
- Mattis Schrade <mattis.schrade@wago.com>
- Konrad Holsmölle <konrad.holsmoelle@wago.com>

## Ziele

- [x] Ethernetverbindung über Raspberry Pi
- [x] Webserver auf CC100
- [x] Container auf CC100 zum programmieren



### Raspberry Pi

##### Downloads

- [*Windows Disk-Imager*](https://sourceforge.net/projects/win32diskimager/)

- [*Image-Download*](https://www.raspberrypi.com/software/operating-systems/)

- [*Treiber für das 5" Touchdisplay*](https://joyiteurope-my.sharepoint.com/personal/onedrive_joyiteurope_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fonedrive%5Fjoyiteurope%5Fonmicrosoft%5Fcom%2FDocuments%2F5display%2FLCD%2Dshow%2Dmaster%2Ezip&parent=%2Fpersonal%2Fonedrive%5Fjoyiteurope%5Fonmicrosoft%5Fcom%2FDocuments%2F5display&ga=1)


##### Anleitungen

Treiber-Installation:
```
cd Downloads
unzip LCD-show-master.zip
cd LCD-show-master/
sudo bash ./LCD5-show
```

### CC100
[Docker installieren](https://github.com/WAGO/docker-ipk)

Docker Caontainer von DockerHub laden <br>
`docker pull konradholsmoelle/vscpy`

vscpy.sh ausführen
