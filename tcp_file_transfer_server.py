import socket

def receive_file(server_socket, output_filename):
    client_socket, addr = server_socket.accept()

    with client_socket, open(output_filename, 'wb') as file:
        while True:
            bytes_read = client_socket.recv(4096)
            if not bytes_read:    
                # when file transmission done, break
                break
            file.write(bytes_read)

def start_server(host, port, output_filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            receive_file(server_socket, output_filename)

if __name__ == "__main__":
    HOST = '10.10.10.2'  
    PORT = 5000
    OUTPUT_FILE = 'example.txt'

    start_server(HOST, PORT, OUTPUT_FILE)
