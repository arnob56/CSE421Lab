import socket

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            data = conn.recv(1024).decode()
            print(f"Client connected from IP: {addr[0]}")
            print(f"Device Name: {data}")
            response = "Device name received"
            conn.sendall(response.encode())

            print("Response sent to client")
            conn.close()
            print("Connection closed")
            print("Waiting for next connection...")
 