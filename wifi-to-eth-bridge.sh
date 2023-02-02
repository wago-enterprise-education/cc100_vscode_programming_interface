#Folgender Programmcode verbindet den W-Lan-Adapter des Raspberry Pi 4 mit dem Ethernetanschluss.
#Dadurch lässt sich ein Endgerät (WAGO -Controller) mit dem öffentlichen W-Lan verbinden.
#"sudo apt-get install dnsmasq" muss im Vorfeld auf dem Raspberry Pi installiert worden sein.

#!/bin/bash

#Konfigurieren der Internet-Verbindung:
ip_address="192.168.2.1"
netmask="255.255.255.0"
dhcp_range_start="192.168.2.2"
dhcp_range_end="192.168.2.200"
dhcp_time="12h"
dns_server="1.1.1.1"
eth="eth0"
wlan="wlan0"

#Starten des Netzwerkdienst:
sudo systemctl start network-online.target &> /dev/null

#Konfigurieren der NAT-Einstellungen zur Weiterleitung der Ethernet-Anfragen über die W-Lan-Verbindung
sudo iptables -F
sudo iptables -t nat -F
sudo iptables -t nat -A POSTROUTING -o $wlan -j MASQUERADE
sudo iptables -A FORWARD -i $wlan -o $eth -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i $eth -o $wlan -j ACCEPT

#IP-Weiterleitung aktivieren:
sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"

#IP-Routing einrichten:
sudo ifconfig $eth down
sudo ifconfig $eth up
sudo ifconfig $eth $ip_address netmask $netmask

sudo ip route del 0/0 dev $eth &> /dev/null

sudo systemctl stop dnsmasq

sudo rm -rf /etc/dnsmasq.d/* &> /dev/null

#Konfigurieren der DNS-Einstellungen:
echo -e "interface=$eth
bind-interfaces
server=$dns_server
domain-needed
bogus-priv
dhcp-range=$dhcp_range_start,$dhcp_range_end,$dhcp_time" > /tmp/custom-dnsmasq.conf

#Starten der DNS-Dienste:
sudo cp /tmp/custom-dnsmasq.conf /etc/dnsmasq.conf
sudo systemctl start dnsmasq
