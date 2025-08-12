import socket

SERVER_IP = "127.0.0.1"
PORT = 5003

hours_worked = int(input("Enter hours worked: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_IP, PORT))
    client_socket.sendall(str(hours_worked).encode())
    salary = client_socket.recv(1024).decode()
    print(f"Calculated Salary: Tk {salary}")
    