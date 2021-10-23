import json
import subprocess
import time
import os
from pathlib import Path

import httpx
from crontab import CronTab

import utils
from config import *

user = json.loads(USER_FILE.read_text())

nickname = user['nickname']
token = user['token']




