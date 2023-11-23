import subprocess

def get_android_device_id():
    try:
        # Run the getprop command to retrieve the ro.serialno property
        result = subprocess.check_output(['getprop', 'ro.serialno']).decode().strip()
        return result
    except subprocess.CalledProcessError as e:
        print(f'Error retrieving device ID: {e}')
        return None

# Get the Android device ID
android_device_id = get_android_device_id()

if android_device_id:
    print(f'Android Device ID: {android_device_id}')
else:
    print('Failed to retrieve Android Device ID.')
