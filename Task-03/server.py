import socket
import threading

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def handle_client(conn, addr):
    with conn:
        message = conn.recv(1024).decode()
        vowel_count = count_vowels(message)

        if vowel_count == 0:
            response = "Not enough vowels"
        elif vowel_count <= 2:
            response = "Enough vowels I guess"
        else:
            response = "Too many vowels"

        conn.sendall(response.encode())
    print(f"Connection closed with {addr}")

HOST = "0.0.0.0"
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Multi-threaded Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        print(f"New connection from {addr}")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("Waiting for next connection...")