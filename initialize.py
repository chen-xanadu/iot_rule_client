import json
import subprocess
import time
from datetime import datetime
from pathlib import Path

import requests

import utils
from config import *


user = json.loads(USER_FILE.read_text())

nickname = user['nickname']
token = user['token']

# wait for user to be set to active
while not utils.is_active(token):
    print('The user \"{}\" is not active'.format(nickname))
    time.sleep(10)

user['is_active'] = True
USER_FILE.write_text(json.dumps(user))


# upload pi's local IP
p = subprocess.run('hostname -I', shell=True, stdout=subprocess.PIPE)
local_ip = p.stdout.encode().strip()

utils.update_local_ip(token, local_ip)


# wait for IoTInspector
while not utils.is_inspector_ready():
    print('IoT inspector is not ready')
    time.sleep(2)


# Continue to monitor old devices and scan for new devices
interval = 10
max_interval = 600

while True:

    if utils.is_inspector_ready():
        utils.ping_server(token)
    else:
        continue

    devices = utils.get_devices_from_inspector()

    for device_id, device in devices.items():
        device_file = DEVICE_DIR / (device_id + '.json')
        if device_file.is_file():

            device_attr_old = json.loads(device_file.read_text())

            # if device_attr_old['name'] == device['dhcp_name'] and \
            #         device_attr_old['internal_ip'] == device['device_ip'] and \
            #         device_attr_old['is_monitored'] == device['is_inspected']:
            #     continue

            if device_attr_old['is_monitored'] != device['is_inspected']:
                if device_attr_old['is_monitored']:
                    requests.get(INSPECTOR_URL + '/enable_inspection/' + device['device_id'])
                    device['is_inspected'] = True
                else:
                    requests.get(INSPECTOR_URL + '/disable_inspection/' + device['device_id'])
                    device['is_inspected'] = False


        device_attr = {
            'id': device['device_id'],
            'internal_ip': device['device_ip'],
            'mac': device['device_mac'],
            'name': device['dhcp_name'],
            'is_monitored': device['is_inspected'],
            'last_monitor_timestamp': str(datetime.utcnow())
        }

        resp = requests.post(SERVER_BASE_URL + '/device.add', params={'token': token}, json=device_attr)

        device_file.write_text(json.dumps(resp.json()))


    time.sleep(interval)
    interval = interval + 10
    if interval > max_interval:
        interval = max_interval

