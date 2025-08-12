import socket
import platform

SERVER_IP = "127.0.0.1"  # Change to server IP if remote
PORT = 5000

device_name = platform.node()  # Get computer/device name

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_IP, PORT))
    client_socket.sendall(device_name.encode())
    print(f"Device name '{device_name}' sent to server")
    response = client_socket.recv(1024).decode()   