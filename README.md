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

### Raspberry Pi

##### Downloads

- [*Windows Disk-Imager*](https://sourceforge.net/projects/win32diskimager/)

- [*Image-Download*](https://www.raspberrypi.com/software/operating-systems/)

- [*Treiber für das 5" Touchdisplay*](https://joyiteurope-my.sharepoint.com/personal/onedrive_joyiteurope_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fonedrive%5Fjoyiteurope%5Fonmicrosoft%5Fcom%2FDocuments%2F5display%2FLCD%2Dshow%2Dmaster%2Ezip&parent=%2Fpersonal%2Fonedrive%5Fjoyiteurope%5Fonmicrosoft%5Fcom%2FDocuments%2F5display&ga=1)


##### Anleitungen

Treiber-Installation:
``` bash
cd Downloads
unzip LCD-show-master.zip
cd LCD-show-master/
sudo bash ./LCD5-show
```

### CC100
- [Installation of Docker on the CC100](https://github.com/WAGO/docker-ipk)
- [Installation of Python3 on the CC100](https://github.com/WAGO/cc100-howtos/blob/main/HowTo_AddPython3/packages/python3_3.7.6_armhf.ipk) Download the .ipk-Data and install it as same as Docker in the WBM
- Pull the Docker-Container on DockerHub <br>
`docker pull bzporta/pipdocker:1.0`
- execute startup.sh
