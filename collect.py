import json
import subprocess
from pathlib import Path

import requests



# def get_mac_vendor(mac: str):
#     mac = mac.replace(':', '')
#     mac_prefix = mac[:6]

#     p = subprocess.run(f"grep -i '{mac_prefix}' /usr/share/nmap/nmap-mac-prefixes", shell=True, capture_output=True, text=True)

#     if p.stdout == '':
#         return 'Unknown'
#     else:
#         return p.stdout.strip()[7:]
