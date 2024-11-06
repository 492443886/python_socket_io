import socketio

sio = socketio.Client()


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
    else:
        print("'info' key does not exist in data")


if __name__ == '__main__':
    # Connect to the server
    sio.connect("http://localhost:12345")   
    while True:
        pass

