import socketio

# Initialize the client
sio = socketio.Client()

# Connect to the server
@sio.event
def connect():
    print("Connected to the chat server")

# Handle disconnections
@sio.event
def disconnect():
    print("Disconnected from the chat server")

# Handle incoming messages
@sio.on('message')
def on_message(data):
    sender_id = data.get('sid', 'Server')  # Default to 'Server' if 'sid' is missing
    print(f"{sender_id}: {data}")

# Connect to the server
sio.connect("http://localhost:12345")

# Send messages in a loop
try:
    while True:
        msg = input("You: ")
        sio.emit('message', {'msg': msg})
except KeyboardInterrupt:
    print("Exiting chat...")
finally:
    sio.disconnect()
