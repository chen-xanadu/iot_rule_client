import json
import subprocess
import os
from pathlib import Path

import httpx
from crontab import CronTab

from config import *


# Generating ssh key
pk = Path.home() / '.ssh' / 'id_ed25519.pub'

if not pk.is_file():
    subprocess.run(f'ssh-keygen -q -t ed25519 -N "" -f "{pk}"', shell=True, capture_output=True, text=True)


# Registering with server
SERVER_API_KEY = os.getenv('SERVER_API_KEY')

resp = httpx.post(SERVER_BASE_URL + '/user.add', params={'api_key': SERVER_API_KEY}, files={'pk': pk.open('rb')})

user_data = resp.json()

if 'id' not in user_data:
    print('Register error')
    exit()


# Saving user data
USER_FILE.write_text(json.dumps(user_data))
DEVICE_DIR.mkdir(parents=True, exist_ok=True)


print(f'The nickname for this device is: {user_data["nickname"]}')


# Format cron job commands
nickname = user_data['nickname']
ssh_port = user_data['ssh_port']

autossh_cmd = f'autossh -M 0 -o "StrictHostKeyChecking no" -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" -fN -R ' \
              f'{ssh_port}:localhost:22 {nickname}@{SERVER_DOMAIN}'


sftp_cmd = f'lftp sftp://{nickname}:@{SERVER_DOMAIN} -e "mirror -R --Move {TCPDUMP_DIR}/ uploads; bye"'

inspector_script = Path(__file__).resolve().parent / 'start_inspector.sh'
inspector_script.chmod(0o755)

tcpdump_script = Path(__file__).resolve().parent / 'init_tcpdump.sh'
tcpdump_script.chmod(0o755)

initialize_script = Path(__file__).resolve().parent / 'initialize.py'


# Set cron job
with CronTab(user=os.getlogin()) as cron:
    cron.remove_all()

    autossh_job = cron.new(command=autossh_cmd)
    autossh_job.every_reboot()

    inspector_job = cron.new(command=str(inspector_script))
    inspector_job.every_reboot()
    
    tcpdump_job = cron.new(command=str(tcpdump_script))
    tcpdump_job.every_reboot()

    initialize_job = cron.new(command='python3 ' + str(initialize_script))
    initialize_job.every_reboot()

    sftp_job = cron.new(command=sftp_cmd)
    sftp_job.minute.every(SFTP_UPLOAD_INTERVAL_IN_MINUTES)

