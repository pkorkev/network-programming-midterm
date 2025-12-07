import socket

def start_client():
    host = "127.0.0.1"  # Connect to your local server
    port = 5000         # Same port as server

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print("[CLIENT] Attempting connection...")

        # Attempt to connect to the server
        client_socket.connect((host, port))
        print(f"[CLIENT] Connected to server at {host}:{port}")

        while True:
            # Get input from user
            msg = input("Enter message (or 'quit'): ")

            # Allow user to disconnect
            if msg.lower() == "quit":
                print("[CLIENT] Disconnecting...")
                break

            # Send message to server
            client_socket.send(msg.encode())

            # Receive a response from the server
            data = client_socket.recv(1024).decode()
            print(f"[CLIENT] Server response: {data}")

    except ConnectionRefusedError:
        # Happens when server is not running
        print("[CLIENT ERROR] Server is not running or refused the connection.")

    except Exception as e:
        # Handles all other errors
        print(f"[CLIENT ERROR] {e}")

    finally:
        # Cleanly close the socket
        client_socket.close()
        print("[CLIENT] Connection closed.")

if __name__ == "__main__":
    start_client()
