import socket
import threading
from flask import Flask

app = Flask(__name__)

UDP_IP = "0.0.0.0"
UDP_PORT = 11111

def udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"UDP Server listening on {UDP_PORT}")

    while True:
        data, addr = sock.recvfrom(4096)
        message = data.decode()

        print(f"Received from {addr}: {message}")

        if message == "ping":
            sock.sendto(b"pong", addr)

@app.route("/")
def index():
    return "Flask server running"

if __name__ == "__main__":
    thread = threading.Thread(target=udp_server, daemon=True)
    thread.start()

    app.run(host="0.0.0.0", port=5000)