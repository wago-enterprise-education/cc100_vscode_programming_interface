#Author
#Bjarne Zaremba <bjarne.zaremba@wago.com>

#Erstellen eines Ordners für die .ipk-Dateien
mkdir /root/ipk_packages
cd /root/ipk_packages
#Download und Installation von Docker
wget -P ~/ipk_packages https://github.com/WAGO/docker-ipk/releases/download/v1.0.4-beta/docker_20.10.5_armhf.ipk?raw=true
opkg install docker_20.10.5_armhf.ipk?raw=true
#Download und Installation von Python3
wget -P ~/ipk_packages https://github.com/WAGO/cc100-howtos/blob/main/HowTo_AddPython3/packages/python3_3.7.6_armhf.ipk?raw=true
opkg install python3_3.7.6_armhf.ipk?raw=true
#Speicherort der Docker-Container auf die SD-Karte verschieben 
/etc/init.d/dockerd stop
cp -r /home/docker /media/sd/
echo '{
  "data-root":"/media/sd/docker",
        "log-driver": "json-file",
        "log-opts": {
                "max-size": "2m",
                "max-file": "5"
        }
}' > /etc/docker/daemon.json
/etc/init.d/dockerd start


#Download des Code-Server Images
docker pull bzporta/vscpy3
chmod -R 777 /sys/kernel/dout_drv/DOUT_DATA
chmod -R 777 /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0
chmod -R 777 /sys/devices/platform/soc/40017000.dac
chmod -R 777 /etc/calib
chmod -R 777 /sys/devices/platform/soc/48003000.adc
chmod -R 777 /sys/bus/iio/devices
#Start des Code-Server-Containers
docker run -d --name=code-server -e PUID=1000 -e PGID=1000 -e TZ=Europe/Berlin -p 8443:8443 -v /home/code-server/config:/config --restart unless-stopped --privileged \
-v /sys/kernel/dout_drv:/home/ea/dout \
-v /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0:/home/ea/din \
-v /sys/devices/platform/soc/40017000.dac:/home/ea/anout \
-v /etc/calib:/home/ea/cal/calib \
-v /sys/devices/platform/soc/48003000.adc:/home/ea/anin \
--privileged bzporta/vscpy3

#Modul installieren auf dem Docker-Container
#git clone https://github.com/wago-enterprise-education/wago_cc100_python.git

#Modul installieren auf dem CC100 direkt
mkdir /home/code-server/config/init
cp /home/code-server/config/workspace/Autostart.py /home/code-server/config/init
wget -P /home/code-server/config/init https://raw.githubusercontent.com/wago-enterprise-education/wago_cc100/main/CC100IO/CC100IO.py?token=GHSAT0AAAAAAB7X46MHUSK5574QLIUPB7ZUZAJ5KSQ
mv /home/code-server/config/init/CC100IO.py?token=GHSAT0AAAAAAB7X46MHUSK5574QLIUPB7ZUZAJ5KSQ /home/code-server/config/init/CC100IO.py

#Automatisches Erstellen und Ausfüllen der start.sh-Datei
echo 'python3 /home/code-server/config/init/Autostart.py 
chmod -R 777 /sys/kernel/dout_drv/DOUT_DATA
chmod -R 777 /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0
chmod -R 777 /sys/devices/platform/soc/40017000.dac
chmod -R 777 /etc/calib
chmod -R 777 /sys/devices/platform/soc/48003000.adc
chmod -R 777 /sys/bus/iio/devices
docker run -d --name=code-server -e PUID=1000 -e PGID=1000 -e TZ=Europe/Berlin -p 8443:8443 -v /home/code-server/config:/config --restart unless-stopped --privileged \
-v /sys/kernel/dout_drv:/home/ea/dout \
-v /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0:/home/ea/din \
-v /sys/devices/platform/soc/40017000.dac:/home/ea/anout \
-v /etc/calib:/home/ea/cal/calib \
-v /sys/devices/platform/soc/48003000.adc:/home/ea/anin \
--privileged bzporta/vscpy3
' > /etc/init.d/start.sh
chmod -R 777 /etc/init.d/start.sh
ln -s /etc/init.d/start.sh /etc/rc.d/
