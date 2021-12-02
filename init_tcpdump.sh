#!/bin/bash


if [ ! -e "$HOME/iot_rule_client/tcpdumpout" ]; then
`mkdir -p "$HOME/iot_rule_client/tcpdumpout"`
fi


UNCOMMENT LINES TO CONVERT TO JSON
#if [ ! -e "$HOME/iot_rule_client/tcpdumpoutJSON" ]; then
#`mkdir -p "$HOME/iot_rule_client/tcpdumpoutJSON"`
#fi

if [ ! -e "$HOME/iot_rule_client/tcpdumpoutCSV" ]; then
`mkdir -p "$HOME/iot_rule_client/tcpdumpoutCSV"`
fi


sleep 30

while true
do 
        curr_date=$(date "+%Y_%m_%d_%T")
        sudo timeout 15m tcpdump -i eth0 -s96 -w $HOME/iot_rule_client/tcpdumpout/tcpdumpout.${curr_date}.pcap 2>&1
        
        # UNCOMMENT LINE TO COLLECT ENTIRE PACKETS
        #sudo timeout 15m tcpdump -i eth0 -w $HOME/iot_rule_client/tcpdumpout/tcpdumpout.${curr_date}.pcap 2>&1
        
        # UNCOMMENT LINES TO CONVERT TO JSON
        #ls -t $HOME/iot_rule_client/tcpdumpout/tcpdumpout.* | head -n 1 | xargs -I XX tshark -r XX -T json > $HOME/iot_rule_client/tcpdumpoutJSON/tcpdumpoutJSON.${curr_date}.json
        #rm $HOME/iot_rule_client/tcpdumpout/tcpdumpout.${curr_date}.pcap
        
        # LINES TO CONVERT TO CSV
        ls -t  $HOME/iot_rule_client/tcpdumpout/tcpdumpout.* | head -n 1 | xargs -I XX tshark -r XX fields -e frame.number -e frame.time_relative -e _ws.col.Protocol -e frame.len -e frame.time_delta -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.src_host -e ip.dst_host -e ip.proto -e udp.srcport -e udp.dstport -e ip.len -e udp.length -e tcp.srcport -e tcp.dstport -e tcp.len  -E header=y -E separator=, > $HOME/iot_rule_client/tcpdumpoutCSV/tcpdumpoutCSV.${curr_date}.csv
        rm $HOME/iot_rule_client/tcpdumpout/tcpdumpout.${curr_date}.pcap
        
done

