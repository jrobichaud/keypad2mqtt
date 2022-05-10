# keypad2mqtt
 send F1-F16 keys through mqtt

# Usage

```bash
usage: keypad2mqtt.py [-h] [--port PORT] [--username USERNAME] [--password PASSWORD] [--device DEVICE] hostname

keypad2mqtt

positional arguments:
  hostname              broker hostname

optional arguments:
  -h, --help            show this help message and exit
  --port PORT           broker port (default: 1883)
  --username USERNAME, -u USERNAME
                        broker username
  --password PASSWORD, -p PASSWORD
                        broker password
  --device DEVICE, -i DEVICE
                        input device path (default: /dev/input/event0)
```

# Example

```bash
 python -m "keypad2mqtt" "homeassistant.local" -u "homeassistant" -p "changeme"
```

# Receive data

Topic: `keypad/F{1-16}`
