import socket

SERVER_IP = "127.0.0.1"
PORT = 5002

msg = input("Enter your message: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_IP, PORT))
    client_socket.sendall(msg.encode())
    response = client_socket.recv(1024).decode()
    print("Server says:", response)
