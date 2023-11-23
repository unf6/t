import subprocess
import requests
import time
import os
import uuid
import platform

def get_windows_hwid():
    hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    return hardwareid

def get_android_hwid():
    m = str(uuid.uuid1())
    return m

# Replace 'your_server_url' with the actual URL of your server
site = requests.get('https://luxury-kleicha-549dac.netlify.app/hwid.txt')

hardwareid = None  # Initialize the variable outside the if conditions

try:
    if platform.system().lower() == 'windows':
        hardwareid = get_windows_hwid()
        print('[INFO] Windows HWID:', hardwareid)
    elif platform.system().lower() == 'android':
        m = get_android_hwid()
        print('[INFO] Android HWID:', m)

    if (hardwareid and hardwareid in site.text) or (m and m in site.text):
        print('[INFO] HWID found in database')
    else:
        print('[ERROR] HWID NOT in database')
        time.sleep(5)
        os._exit(0)  # Use 0 to indicate successful termination
except Exception as e:
    print('[ERROR] Exception:', str(e))
    print('[ERROR] FAILED to connect to database')
    time.sleep(5)
    os._exit(1)  # Use 1 to indicate an error termination
