import socket

def send_file_to_server(host, port, filename):
    """ Sends a file to the server """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))

            client_socket.sendall(filename.encode())

            with open(filename, 'rb') as file:
                while True:
                    bytes_read = file.read(4096)
                    if not bytes_read:
                        # File transmission is done
                        break
                    client_socket.sendall(bytes_read)
            
            print(f"File {filename} has been sent.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    HOST = '10.10.10.2'  
    PORT = 5000
    # read from an example file in current directory
    FILENAME = 'example.txt'

    send_file_to_server(HOST, PORT, FILENAME)
