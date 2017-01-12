#!/bin/sh
echo 1  >/proc/sys/net/ipv4/ip_forward
iptables -t nat -F PREROUTING
iptables -t nat -A PREROUTING -d 10.9.0.41 -p tcp --dport 8443 -j DNAT --to 10.6.31.3:443
iptables -t nat -A PREROUTING -d 10.9.0.41 -p tcp --dport 8222 -j DNAT --to 10.6.31.3:22

iptables -t nat -F POSTROUTING
iptables -t nat -A POSTROUTING -d 10.6.31.3 -j SNAT --to 10.6.31.5

iptables -F FORWARD
