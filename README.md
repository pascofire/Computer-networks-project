# Study Room Group Chat Web App

A simple, real-time group chat web application for study groups, built with Flask and Flask-SocketIO. Users can join a shared chatroom, exchange messages, and instantly access Google Drive links for subject-wise study notes.

---

## Features

- **Instant group chat:** All messages are visible to every user live.
- **User presence notifications:** See who joins or leaves the study room.
- **Easy resource access:** Type `list` for available subjects or a subject code (like `DS`, `OOPS`) to get direct Google Drive links.
- **Modern responsive UI:** Works in any browser, no complicated setup.

---

## Technologies Used

- [Python 3.7+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
- HTML, CSS, JavaScript

  
---

## Getting Started

1. **Clone or download this repository.**

2. **Open a terminal in your project directory.**

3. **Install the required packages:**
    ```
    pip install flask flask-socketio
    ```

4. **Start the server:**
    ```
    python app.py
    ```

5. **Open your browser and go to:**
    ```
    http://localhost:5000
    ```

6. **Enter your name and begin chatting!**
    - Use `list` for all subjects, or type a subject code to fetch the notes link.

7. **For multiple users:**  
    Open more tabs/windows, or share your IP for friends to join on your network.

---

## Additional Tips

- To let friends join from their computers:
  - Change the last line in `app.py` to  
    `socketio.run(app, host='0.0.0.0', port=5000, debug=True)`
  - Share your IP address (`http://YOUR.IP.ADDRESS:5000`)
  - Everyone must be on the same local network

---

## Possible Extensions

- Add message history and saving.
- Enable multiple chat rooms.
- Add file sharing or other study resources.
- Implement authentication and private rooms.


## Authors

1. **Gayatri Donode** (class: A2_B2_23) (24donodeg@rbunagpur.in)<br>
2. **Sanchi Sharma** (class: A2_B4_58) (24sharmas_01@rbunagpur.in)<br>
3. **Harsh Jora**  (class: A2_B1_5)  (24jorah@rbunagpur.in)
