import socket
import asyncio
import time
from main import *

Blockchain = Blockchain()

async def client_server(host, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        message = "Hello, server!"
        client_socket.send(message.encode())

        data = client_socket.recv(1024).decode()
        print(f"Received data from server: {data}")

        Blockchain.create_block(1,'0')

    except ConnectionResetError:
        print("Connection reset by the remote host.")

    finally:
        time.sleep(1)  # Tempo de espera antes de fechar a conexão
        client_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    asyncio.run(client_server(host, port))
