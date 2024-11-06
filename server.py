import socketio
from flask import Flask

# Create a Socket.IO server with CORS allowed for all origins (for testing)
sio = socketio.Server(cors_allowed_origins='*')
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

# Serve the main page
@app.route('/')
def index():
    return "Chat server is running!"

# Handle new connections
@sio.event
def connect(sid, environ):
    print(f"User {sid} connected")
    sio.emit('message', {'msg': f"User {sid} has joined the chat!"}, to=sid)

# Handle disconnections
@sio.event
def disconnect(sid):
    print(f"User {sid} disconnected")

# Handle incoming chat messages
@sio.event
def message(sid, data):
    print(f"Message from {sid}: {str(data)}")
    # Broadcast message to all clients except the sender
    sio.emit('message', data, skip_sid=sid)

# Run the server
if __name__ == '__main__':
    app.run(port=12345)
