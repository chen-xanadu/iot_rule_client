#!/bin/bash

source $HOME/iot-inspector-local/iot/bin/activate
cd $HOME/iot-inspector-local/src
sleep 20 #TODO: wait until Internet is up
sudo python3  $HOME/iot-inspector-local/src/start_inspector.py  #>/dev/null 2>&1