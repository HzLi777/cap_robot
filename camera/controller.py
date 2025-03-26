import evdev
import subprocess

def find_controller():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if "Pro Controller" in device.name:
            print(f"Connected to {device.name} at {device.path}")
            return device
    return None

def run_camera():
    print(" Running real_time_recognize.py...")
    subprocess.run(["python3", "/home/Haozhe/robot/camera/real_time_recognize.py"])

controller = find_controller()
if not controller:
    print(" Pro Controller not found. Make sure it's paired via Bluetooth.")
    exit(1)


BUTTON_Y = 308  

print(" Listening for Pro Controller inputs...")
for event in controller.read_loop():
    if event.type == evdev.ecodes.EV_KEY and event.value == 1:  # Button Pressed
        if event.code == BUTTON_Y:
            run_camera()