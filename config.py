from pathlib import Path

SERVER_DOMAIN = 'wiscshr.com'
SERVER_BASE_URL = 'https://' + SERVER_DOMAIN

INSPECTOR_URL = 'http://localhost:46241'

USER_FILE = Path.home() / 'user.json'
DEVICE_DIR = Path.home() / 'devices'

# TODO: set to actual tcpdump dir
TCPDUMP_DIR = Path.home()  / 'iot_rule_client/tcpdumpout'

SFTP_UPLOAD_INTERVAL_IN_MINUTES = 1
