import socket
import asyncio

def blockchain_server_init(port):
    asyncio.run(blockchain_server(port))

async def blockchain_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}")

    clients = {}

    while True:
        (client_socket, client_address) = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        for client in clients.values():
            print("BLOCKCHAIN SERVER - Listening to client requests: ", client[1])
            data = client_socket.recv(1024).decode()
            print(f"Received data from client: {data}")
            response = "Hello, client!"
            client_socket.send(response.encode())
    client_socket.close()
    pass


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    blockchain_server(host, port)
