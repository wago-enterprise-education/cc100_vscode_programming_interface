python /home/code-server/config/workspace/RoboArm.py
chmod -R 777 //sys/kernel/dout_drv/DOUT_DATA
chmod -R 777 /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0
chmod -R 777 /sys/devices/platform/soc/40017000.dac
chmod -R 777 /etc/calib
chmod -R 777 /sys/devices/platform/soc/48003000.adc
sleep 5
chmod +x /root/docker.sh
docker run -d --name=code-server -e PUID=1000 -e PGID=1000 -e TZ=Europe/Berlin -p 8443:8443 -v /home/code-server/config:/config --restart unless-stopped --privileged \
-v /sys/kernel/dout_drv:/home/ea/dout \
-v /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0:/home/ea/din \
-v /sys/devices/platform/soc/40017000.dac:/home/ea/anout \
-v /etc/calib:/home/ea/cal/calib \
-v /sys/devices/platform/soc/48003000.adc:/home/ea/anin \
--privileged konradholsmoelle/vscpy:cc100.1