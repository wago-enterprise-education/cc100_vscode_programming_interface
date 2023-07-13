#
# Download und Installation von Docker und Python
#
mkdir /root/ipk_packages

wget -P ~/ipk_packages https://github.com/WAGO/docker-ipk/releases/download/v1.0.4-beta/docker_20.10.5_armhf.ipk?raw=true
opkg install ~/ipk_packages/docker_20.10.5_armhf.ipk?raw=true

wget -P ~/ipk_packages https://github.com/WAGO/cc100-howtos/blob/main/HowTo_AddPython3/packages/python3_3.7.6_armhf.ipk?raw=true
opkg install ~/ipk_packages/python3_3.7.6_armhf.ipk?raw=true

rm -rf ~/ipk_packages

#
#Speicherort der Docker-Container auf die SD-Karte verschieben 
#
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


#
# Modification of folders
#
chmod -R 777 /sys/kernel/dout_drv/DOUT_DATA
chmod -R 777 /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0
chmod -R 777 /sys/devices/platform/soc/40017000.dac
chmod -R 777 /etc/calib
chmod -R 777 /sys/devices/platform/soc/48003000.adc
chmod -R 777 /sys/bus/iio/devices

#
#Start des Code-Server-Containers
#
docker pull wagoeducation/cc100vscode
docker run -d --name=code-server -e PUID=1000 -e PGID=1000 -e TZ=Europe/Berlin -p 8443:8443 -p 3000:3000 -v /home/code-server/config:/config --restart unless-stopped \
-v /sys/kernel/dout_drv:/home/ea/dout \
-v /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0:/home/ea/din \
-v /sys/devices/platform/soc/40017000.dac:/home/ea/anout \
-v /etc/calib:/etc/calib \
-v /sys/devices/platform/soc/48003000.adc:/home/ea/anin \
--privileged wagoeducation/cc100vscode

#
#Automatisches Erstellen und Ausfüllen der start.sh-Datei
#
echo 'python3 /home/code-server/config/init/Autostart.py 
chmod -R 777 /sys/kernel/dout_drv/DOUT_DATA
chmod -R 777 /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0
chmod -R 777 /sys/devices/platform/soc/40017000.dac
chmod -R 777 /etc/calib
chmod -R 777 /sys/devices/platform/soc/48003000.adc
chmod -R 777 /sys/bus/iio/devices
docker run -d --name=code-server -e PUID=1000 -e PGID=1000 -e TZ=Europe/Berlin -p 8443:8443 -p 3000:3000 -v /home/code-server/config:/config --restart unless-stopped \
-v /sys/kernel/dout_drv:/home/ea/dout \
-v /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0:/home/ea/din \
-v /sys/devices/platform/soc/40017000.dac:/home/ea/anout \
-v /etc/calib:/etc/calib \
-v /sys/devices/platform/soc/48003000.adc:/home/ea/anin \
--privileged wagoeducation/cc100vscode
docker exec --workdir /home/cc100_programming_interface/server code-server npm start
' > /etc/init.d/start.sh
chmod -R 777 /etc/init.d/start.sh
ln -s /etc/init.d/start.sh /etc/rc.d/

#
#Start des Programming Interface im Container
#
docker exec --workdir /home/cc100_programming_interface/server code-server npm start
