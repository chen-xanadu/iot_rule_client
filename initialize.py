import json
import subprocess
import time
from pathlib import Path

import httpx

import utils
from config import *


user = json.loads(USER_FILE.read_text())

nickname = user['nickname']
token = user['token']

# wait for user to be set to active
while not utils.is_active(token):
    print(f'The user \"{nickname}\" is not active')
    time.sleep(10)

user['is_active'] = True
USER_FILE.write_text(json.dumps(user))


# upload pi's local IP
p = subprocess.run('hostname -I', shell=True, capture_output=True, text=True)
local_ip = p.stdout.strip()

utils.update_local_ip(token, local_ip)


# wait for IoTInspector
while not utils.is_inspector_ready():
    print(f'IoT inspector is not ready')
    time.sleep(2)


while True:
    devices = utils.get_devices_from_inspector()

    for device_id, device in devices.items():
        device_file = DEVICE_DIR / device_id
        if device_file.is_file():

            device_attr_old = json.loads(device_file.read_text())

            if device_attr_old['name'] == device['dhcp_name']:
                continue

            continue

        device_attr = {
            'id': device['device_id'],
            'internal_ip': device['device_ip'],
            'mac': device['device_mac'],
            'name': device['dhcp_name'],
        }

        resp = httpx.post(SERVER_BASE_URL + '/device.add', params={'token': token}, json=device_attr)

        device_file.write_text(resp.json())


    time.sleep(30)
