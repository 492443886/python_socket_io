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

def set_channel_pwm(pca, channel, value):
    pca._pca.channels[channel].duty_cycle = value


def set_servo_angle(pca, servo_num, angle):
    pca.servo[servo_num].angle = angle



@sio.event
def connect():
    print("Connected to the chat server")


@sio.event
def disconnect():
    print("Disconnected from the chat server")


@sio.on('message')
def on_message(data):
    # sender_id = data.get('sid', 'Server')  
    print(f"\n: {str(data)}")
    process(data)


def process(data):

    command = None
    info = None    
    if "command" in data:
        command = data["command"]
        print(type(command))
        print("command:", command)
    else:
        print("'command' key does not exist in data")
        return

    if "info" in data:
        info = data["info"]
        print(type(info))
        print("info:", info)
    else:
        print("'info' key does not exist in data")
        return
    
    if command == "PCA_PWM":
            #{"command": "PCA_PWM", "info":  {"value":  1000,  "channel": 2}}
        if "channel" not in info:
            print("miss channel in info")
            return
        if "value" not in info:
            print("miss value in info")
            return
        
        channel = info["channel"]
        value = info["value"]
        
        set_channel_pwm(kit, channel, value)

    elif command == "PCA_SERVO":

        if "channel" not in info:
            print("miss channel in info")
            return
        if "value" not in info:
            print("miss value in info")
            return

        channel = info["channel"]
        value = info["value"]
        
        set_servo_angle(kit, channel,value)
    else:
        print("Unknow command")



if __name__ == '__main__':
    # Connect to the server
    sio.connect("http://10.0.0.199:9001")   
    while True:
        pass

