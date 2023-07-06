# Visual Studio Code and WAGO Programming Interface for WAGO CC100

This Image contains Visual Studion Code as a webservice for the WAGO CC100 Compact Controller. It uses the wago_cc100_python module to easily access the inputs and outputs of the WAGO CC100. In addition, it provides the CC100 Programming Interface to control the inputs and outputs directly via a web interface.

**This repository is a development repository that was created as part of a student project and is not regularly maintained. It is neither a stable version nor an official repository of WAGO GmbH & Co. KG.** 

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

## Installation of code server and WAGO Programming Interface on the CC100
### Prerequisite
- CC100 Firmware >= 23(04.01.10)
- CC100 is connected to Internet

### Setup in WBM
1. Enter WBM with IP address of CC100 (login with: user: **admin**; password: **wago**)
2. insert SD card
3. add SD card as storage medium (*Configuration -> Mass Storage -> Create new Filesystem on Memory Card (**Ext4**; Label: **sd***)
4. add new DNS server with IP **8.8.8.8** (*Configuration->Networking->TCP/IP-Configuration*)
5. enable IP forwarding through multiple interfaces (*Configuration->Networking->Routing*) 
6. enable HTTP (*Configuration->Ports and Services->Network Services*)


### Installation and start of the code server
1. connect to the CC100 via SSH (open Git Bash ``` ssh root@<IP address> ``` password: **wago**)
2. download setup.sh file on the CC100 (``` wget -P /root/startup https://raw.githubusercontent.com/wago-enterprise-education/cc100_vscode_programming_interface/main/setup.sh ``` )
3. execute setup.sh ``` sh /root/startup/startup.sh ``` )

### Access to the code server and the WAGO Programming Interface
To access VS Code or CC100 Programming Interface type the IP address of the WAGO CC100 in your Webbrowser and add the according port
```
http:<IP address>:8443 for VS Code
```
or
```
http:<IP address>:3000 for CC100 Programming Interface
```
