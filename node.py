import socket
import threading

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.peers = []

    def start_server(self):
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"Listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server.accept()
            print(f"Accepted connection from {client_address}")
            self.peers.append(client_socket)

    def start_client(self, peer_host, peer_port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((peer_host, peer_port))
        # Implement your client logic here

    def send_data(self, data):
        # Implement sending data to peers


if __name__ == "__main__":
    node = Node('127.0.0.1', 5000)
    server_thread = threading.Thread(target=node.start_server)
    server_thread.start()
