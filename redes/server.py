import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        data = client_socket.recv(1024).decode()
        print(f"Received data from client: {data}")

        response = "Hello, client!"
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    start_server(host, port)