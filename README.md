# Setup Guide for Raspberry Pi OS

## Before shipping to the participant

*What we need to do?*

### 1. Install required packages

```shell
#!/bin/bash

sudo apt update
sudo apt install -y python3-pip, python3-venv, git, autossh, lftp
pip3 install httpx
```

### 2. Install IoT Inspector local
```shell
cd $HOME
git clone https://github.com/nyu-mlab/iot-inspector-local.git
cd iot-inspector-local
python3 -m venv iot
source ./iot/bin/activate
pip3 install -r ./src/requirements.txt
deactivate
```

### 3. Register with server

Set the server API key to the environment variable `SERVER_API_KEY`
```shell
export SERVER_API_KEY=????
```

Download this repo under the home directory and run `register.py`.
```shell
cd $HOME
git clone https://github.com/chen-xanadu/iot_rule_client
python3 ./iot_rule_client/register.py
```
If `register.py` runs successfully, it will output a nickname:
```
The nickname for this device is: buckeye
```
Tape the nickname onto the Raspberry Pi box, as it will be used as the id for the device.


### 4. Shutdown/reboot the Pi
```shell
sudo reboot
```



## After the participant gets the device

Once the Raspberry Pi is powered on (by the participant), the IoTInspector (and a few helper script) should be running automatically.

**Please ensure the router is connected to the Internet AND the Raspberry Pi is connected to the router before powering on the Raspberry Pi!**  Sometimes the IoTInspector hangs up (failing to detect any local devices) if no Internet is detected. Reboot the Pi if such issue is encountered.

### Choose which devices to monitor



#### For actual participant

During our meeting with the participant, we will visit `http://ec2-18-119-20-148.us-east-2.compute.amazonaws.com:5000/devices/[nickname]` and select which devices to monitor. Then, we can ssh into the Pi to run `monitor.py` to start monitoring.

#### For internal testing

Visit `http://ec2-18-119-20-148.us-east-2.compute.amazonaws.com:5000/[nickname]`, which will redirect to a page hosted locally by the Pi to select which devices to monitor.

*Note:* if most device names are empty, restarting the router usually helps. 