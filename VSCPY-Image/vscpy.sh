#!/bin/bash

docker run -d --name=code-server -e PUID=1000 -e PGID=1000 -e TZ=Europe/Berlin -p 8443:8443 -v /home/code-server/config:/config --restart unless-stopped --privileged \
-v /sys/kernel/dout_drv:/home/ea/dout \
-v /sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0:/home/ea/din \
-v /sys/devices/platform/soc/40017000.dac:/home/ea/anout \
--privileged vscpy_v3
