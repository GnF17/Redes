import socket
import asyncio

async def client_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = "Hello, server!"
    client_socket.send(message.encode())

    data = client_socket.recv(1024).decode()
    print(f"Received data from server: {data}")

    client_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    client_server(host, port)
