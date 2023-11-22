import socket
import asyncio
from main import Blockchain

# Configurações do servidor
#HOST = '127.0.0.1'  # Endereço IP local
#PORT = 5555  # Porta para a conexão

# Inicialização da Blockchain
blockchain = Blockchain()

# Inicialização do socket do servidor
#server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.bind((HOST, PORT))
#server_socket.listen()  # Aceita até 2 conexões de clientes

# Lista para armazenar as conexões dos usuários
#users_connections = []

def blockchain_server_init(port):
    asyncio.run(blockchain_server(port))

async def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        print(f"Received data from client: {data}")

        # Processar dados recebidos
        response = "Hello, client!"
        client_socket.send(response.encode())

    except ConnectionResetError:
        print("Connection reset by the remote host.")

    finally:
        client_socket.close()

async def blockchain_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server_socket.bind((host, port))
    #server_socket.listen()

    server = await asyncio.start_server(
        handle_client, host, port
    )

    async with server:
        print(f"Server is listening on {host}:{port}")
        await server.serve_forever()

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

        print(f"Clients connected: {clients.items}") #Clientes se descobrindo

        client_socket.close()
        pass


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    asyncio.run(blockchain_server(host, port))