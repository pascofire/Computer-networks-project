from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit, join_room, leave_room
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
socketio = SocketIO(app)

# Simple storage: demo study "subjects" with drive links
subjects = {
    "CAO": "https://drive.google.com/drive/folders/yourmathfolderid",
    "Cyber": "https://drive.google.com/drive/folders/11QfLzbeSqNc9yNUEwXMC65aJPOpbja0g",
    "FOP": "https://drive.google.com/drive/folders/1-o3jE6zMnigfoNcu2fvTw76XLKvKHd9B",
    "DS": "https://drive.google.com/drive/folders/16PHsl9SDSusheQhVVAenCZ5buFrRXYk",
    "OOPS": "https://drive.google.com/drive/folders/1lCWBwKV7PYzvFwmiYZoPlTjAlo13nQG6",
    "OS": "https://drive.google.com/drive/folders/1aZLSoX3EVBeRsvdCf5wbxXqXcsZ5eN-A",
}

@app.route('/')
def chat():
    return render_template('chat.html')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = 'study_room'
    join_room(room)
    emit('message', {'user': 'BOT', 'msg': f'{username} has joined the Study Room.'}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = 'study_room'
    leave_room(room)
    emit('message', {'user': 'BOT', 'msg': f'{username} has left the Study Room.'}, room=room)

@socketio.on('send_msg')
def handle_msg(data):
    username = data['username']
    msg = data['msg'].strip()
    room = 'study_room'
    # Command processing
    if msg.lower() in ['list', 'help']:
        reply = 'Available Subjects:\n' + '\n'.join(sorted(subjects.keys()))
        reply += '\nType the subject code (e.g., DS) for Drive link.'
        emit('message', {'user': 'BOT', 'msg': reply}, room=room)
    elif msg.upper() in subjects:
        link = subjects[msg.upper()]
        emit('message', {'user': 'BOT', 'msg': f'{msg.upper()} notes: {link}'}, room=room)
    elif msg.lower() in ['bye', 'exit', 'quit', 'goodbye']:
        emit('message', {'user': 'BOT', 'msg': 'Goodbye! Study hard and come back anytime!'}, room=room)
    else:
        # Broadcast to all
        emit('message', {'user': username, 'msg': msg}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
