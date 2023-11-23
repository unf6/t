import subprocess
import requests
import time
import os
import uuid

# Get device UUID
hardwareid = str(uuid.uuid1())

# Replace 'your_android_server_url' with the actual URL of your server
site = requests.get('https://luxury-kleicha-549dac.netlify.app/hwid.txt')

try:
    if hardwareid in site.text:
        pass
    else:
        print('[ERROR] HWID NOT in database')
        print('[HWID:' + hardwareid + ']')
        time.sleep(5)
        os._exit(0)  # Use 0 to indicate successful termination
except:
    print('[ERROR] FAILED to connect to database')
    time.sleep(5)
    os._exit(1)  # Use 1 to indicate an error termination
