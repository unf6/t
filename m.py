import subprocess
import requests
import time
import os
import uuid
import platform

def get_windows_hwid():
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    return hwid

def get_android_hwid():
    hwid = str(uuid.uuid1())
    print('[INFO] Android HWID:', hwid)
    return hwid

# Replace 'your_server_url' with the actual URL of your server
site = requests.get('https://luxury-kleicha-549dac.netlify.app/hwid.txt')

try:
    if platform.system().lower() == 'windows':
        hardwareid = get_windows_hwid()
    elif platform.system().lower() == 'android':
        hardwareid = get_android_hwid()
    else:
        print('[ERROR] Unsupported platform')
        os._exit(1)

    if hardwareid and hardwareid in site.text:
        print('[INFO] HWID found in database')
    else:
        print('[ERROR] HWID NOT in database')
        print('[HWID:', str(hardwareid) + ']')
        time.sleep(5)
        os._exit(0)  # Use 0 to indicate successful termination
except Exception as e:
    print('[ERROR] Exception:', str(e))
    print('[ERROR] FAILED to connect to database')
    time.sleep(5)
    os._exit(1)  # Use 1 to indicate an error termination
