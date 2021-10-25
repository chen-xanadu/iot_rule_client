#!/bin/bash


if [ ! -e "$HOME/iot_rule_client/tcpdumpout" ]; then
`mkdir -p "$HOME/iot_rule_client/tcpdumpout"`
fi


sleep 30

while true
do 
        sudo timeout 30m tcpdump -i eth0 -s96 'ip or icmp or tcp or udp' -w $HOME/iot_rule_client/tcpdumpout/tcpdumpout.`date "+%Y_%m_%d_%T"`.pcap 2>&1
done

