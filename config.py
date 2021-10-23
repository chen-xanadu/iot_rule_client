from pathlib import Path

SERVER_DOMAIN = 'ec2-18-119-20-148.us-east-2.compute.amazonaws.com'
SERVER_BASE_URL = 'http://' + SERVER_DOMAIN + ':5000'

INSPECTOR_URL = 'http://localhost:46241'

USER_FILE = Path.home() / 'user.json'
DEVICE_DIR = Path.home() / 'devices'

# TODO: set to actual tcpdump dir
TCPDUMP_DIR = Path.home() / 'dummy'

SFTP_UPLOAD_INTERVAL_IN_MINUTES = 1