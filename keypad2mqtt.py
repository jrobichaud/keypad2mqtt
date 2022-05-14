import paho.mqtt.client as mqtt
import argparse
import traceback
import sys
import evdev
import glob

parser = argparse.ArgumentParser(description='keypad2mqtt')
parser.add_argument("hostname", help="broker hostname")
parser.add_argument('--device', '-d', dest='device', help='input device name')
parser.add_argument('--port', dest="port", type=int, default=1883, help='broker port (default: %(default)s)')
parser.add_argument('--username', '-u', dest='username', help='broker username')
parser.add_argument('--password', '-p', dest='password', help='broker password')
args = parser.parse_args()


mqtt_client = mqtt.Client(client_id="keypad")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected (Code 0)")
        return
    elif rc == 1:
        raise Exception("Connection refused (Code 1) – incorrect protocol version")
    elif rc == 2:
        raise Exception("Connection refused (Code 2) – invalid client identifier")
    elif rc == 3:
        raise Exception("Connection refused (Code 3) – server unavailable")
    elif rc == 4:
        raise Exception("Connection refused (Code 4) – bad username or password")
    elif rc == 5:
        raise Exception("Connection refused (Code 5) – not authorised")
    raise Exception(f"Connection refused (Code {rc}) – unknown error code")

mqtt_client.on_connect = on_connect

if args.username or args.password:
    mqtt_client.username_pw_set(username=args.username, password=args.password)

mqtt_client.connect(args.hostname, port=args.port, keepalive=60, bind_address="")

mqtt_client.loop_start()

def send_key(key):
    print(key)
    mqtt_client.publish(f"keypad/{key}")

try:
    keys = {
        evdev.ecodes.KEY_F1: "F1",
        evdev.ecodes.KEY_F2: "F2",
        evdev.ecodes.KEY_F3: "F3",
        evdev.ecodes.KEY_F4: "F4",
        evdev.ecodes.KEY_F5: "F5",
        evdev.ecodes.KEY_F6: "F6",
        evdev.ecodes.KEY_F7: "F7",
        evdev.ecodes.KEY_F8: "F8",
        evdev.ecodes.KEY_F9: "F9",
        evdev.ecodes.KEY_F10: "F10",
        evdev.ecodes.KEY_F11: "F11",
        evdev.ecodes.KEY_F12: "F12",
        evdev.ecodes.KEY_F13: "F13",
        evdev.ecodes.KEY_F14: "F14",
        evdev.ecodes.KEY_F15: "F15",
        evdev.ecodes.KEY_F16: "F16",
    }
    from evdev import InputDevice, categorize, ecodes
    dev = None
    for file in glob.glob("/dev/input/event*"):
        dev = InputDevice(file)
        if dev.name == args.device:
            print(f"keypad found {args.device} {file}")
            break
        else:
            dev = None
    if dev is None:
        raise Exception(f"keypad not found {args.device}")

    KEY_DOWN = 1

    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY and event.value == KEY_DOWN:
            # print(event, event.code, event.type, event.value)
            if event.code in keys:
                send_key(keys[event.code])
except KeyboardInterrupt:
    pass
finally:
    mqtt_client.loop_stop()
