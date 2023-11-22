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
        data = await loop.sock_recv(client_socket, 1024)
        print(f"Received data from client: {data.decode()}")

        # Processar dados recebidos
        response = "Hello, client!"
        await loop.sock_sendall(client_socket, response.encode())

    except ConnectionResetError:
        print("Connection reset by the remote host.")

    finally:
        client_socket.close()

async def blockchain_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    try:
        while True:
            client_socket, client_address = await loop.sock_accept(server_socket)
            print(f"Accepted connection from {client_address}")

            loop.create_task(handle_client(client_socket))

    except Exception as e:
        print(f"Error in server: {e}")

    finally:
        server_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    loop = asyncio.get_event_loop()
    loop.run_until_complete(blockchain_server(host, port))