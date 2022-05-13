# keypad2mqtt
 send F1-F16 keys through mqtt

# Usage

```bash
usage: keypad2mqtt.py [-h] [--device DEVICE] [--port PORT] [--username USERNAME] [--password PASSWORD] hostname

keypad2mqtt

positional arguments:
  hostname              broker hostname

optional arguments:
  -h, --help            show this help message and exit
  --device DEVICE, -d DEVICE
                        input device name
  --port PORT           broker port (default: 1883)
  --username USERNAME, -u USERNAME
                        broker username
  --password PASSWORD, -p PASSWORD
                        broker password
```

# Example

```bash
 python -m "keypad2mqtt" -d "ZiddyMakes ZMK_16_KEY" "homeassistant.local" -u "homeassistant" -p "changeme"
```

# Receive data

Topic: `keypad/F{1-16}`
