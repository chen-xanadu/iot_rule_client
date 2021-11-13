from pathlib import Path

SERVER_DOMAIN = 'wiscshr.com'
SERVER_BASE_URL = 'https://' + SERVER_DOMAIN

INSPECTOR_URL = 'http://localhost:46241'

USER_FILE = Path.home() / 'user.json'
DEVICE_DIR = Path.home() / 'devices'

# path to tcpdump json files
TCPDUMP_DIR = Path.home()  / '$HOME/iot_rule_client/tcpdumpoutJSON'

# path to tcpdump pcaps
# TCPDUMP_DIR = Path.home()  / '$HOME/iot_rule_client/tcpdumpout'

SFTP_UPLOAD_INTERVAL_IN_MINUTES = 1
