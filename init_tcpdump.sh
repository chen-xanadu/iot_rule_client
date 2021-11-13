#!/bin/bash


if [ ! -e "$HOME/iot_rule_client/tcpdumpout" ]; then
`mkdir -p "$HOME/iot_rule_client/tcpdumpout"`
fi

if [ ! -e "$HOME/iot_rule_client/tcpdumpoutJSON" ]; then
`mkdir -p "$HOME/iot_rule_client/tcpdumpoutJSON"`
fi


sleep 30

while true
do 
        curr_date=$(date "+%Y_%m_%d_%T")
        sudo timeout 30m tcpdump -i eth0 -s96 'ip or icmp or tcp or udp' -w $HOME/iot_rule_client/tcpdumpout/tcpdumpout.${curr_date}.pcap 2>&1
        ls -t $HOME/iot_rule_client/tcpdumpout/tcpdumpout.* | head -n 1 | xargs -I XX tshark -r XX -T json > $HOME/iot_rule_client/tcpdumpoutJSON/tcpdumpoutJSON.${curr_date}.json
done

