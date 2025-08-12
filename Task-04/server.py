import socket

def calculate_salary(hours):
    if hours <= 40:
        return hours * 200
    else:
        return 8000 + (hours - 40) * 300

HOST = "0.0.0.0"
PORT = 5003

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Salary Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            data = conn.recv(1024).decode()
            hours = int(data)
            salary = calculate_salary(hours)
            conn.sendall(str(salary).encode())
            print(f"Client connected from IP: {addr[0]}")
            print(f"Calculated Salary: Tk {salary}")    