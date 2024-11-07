import socketio
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

sio = socketio.Client()

def set_light_on_off(pca, channel, state):
    if state == "on":
        pca._pca.channels[channel].duty_cycle = 0xFFFF  # Full duty cycle (Light ON)
    elif state == "off":
        pca._pca.channels[channel].duty_cycle = 0x0000  # 0 duty cycle (Light OFF)
    else:
        print("Invalid state. Use 'on' or 'off'.")


@sio.event
def connect():
    print("Connected to the chat server")


@sio.event
def disconnect():
    print("Disconnected from the chat server")


@sio.on('message')
def on_message(data):
    sender_id = data.get('sid', 'Server')  
    print(f"\n{sender_id}: {str(data)}")
    process(data)


def process(data):

    if "command" in data:
        print("command:", data["command"])
    else:
        print("'command' key does not exist in data")

    if "info" in data:
        print("info:", data["info"])
        set_light_on_off(kit, 2, "on")  # Light ON
    else:
        print("'info' key does not exist in data")
        set_light_on_off(kit, 2, "off")  # Light ON


if __name__ == '__main__':
    # Connect to the server
    sio.connect("http://10.0.0.199:9001")   
    while True:
        pass

