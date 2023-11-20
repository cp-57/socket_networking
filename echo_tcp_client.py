import socket
import sys

def send_message_to_server(host, port, message):
    """ Sends a single message to the server and prints the response """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))
            print("Sent: ", message)
            client_socket.sendall(message.encode())

            response = client_socket.recv(1024)
            print("Received: ", response.decode())

        except ConnectionRefusedError:
            print("Connection failed. Is the server running?")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Server's hostname or IP address
    PORT = 65432        # Port used by the server

    if len(sys.argv) < 2:
        print("Usage: python3 client.py 'message'")
        sys.exit(1)

    MESSAGE = sys.argv[1]
    send_message_to_server(HOST, PORT, MESSAGE)
