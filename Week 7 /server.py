import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8000

print(f"server starting on {host}:{port}")
server_socket.bind((host, port))

server_socket.listen(1)
print("Server is listening for the connection...")

client_connection, client_address = server_socket.accept()
print(f"client connected {client_address}")

data = client_connection.recv(1024)
print(f"Received from client: {data.decode()}")

response = "Hello from server! I received your message."
client_connection.send(response.encode())
print("Response sent to client")

client_connection.close()
server_socket.close()
print("Connection closed")