import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8000

print(f"connecting to {host}:{port}")
client_socket.connect((host, port))
print("connected")

message = "Hello from Client!"
client_socket.send(message.encode())
print(f"Sent to server: {message}")

response = client_socket.recv(1024)
print(f"Received from server: {response.decode()}")

client_socket.close()
print("Connection closed")