import socket

def count_digits(message):
    """ Count the number of digits in the message """
    return sum(char.isdigit() for char in message)

def start_server(host, port):
    """ Start the socket server """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        while True:
            client_socket, addr = server_socket.accept()
            with client_socket:

                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    message = data.decode()

                    if "SECRET" in message:
                        digits_count = count_digits(message)
                        response = f"Digits: Count: {digits_count}"
                    else:
                        response = "Secret code not found."

                    client_socket.sendall(response.encode())

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 5000

    start_server(HOST, PORT)
