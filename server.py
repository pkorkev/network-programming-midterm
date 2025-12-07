import socket

def start_server():
    # Server will run on localhost (my own machine)
    host = "127.0.0.1"
    port = 5000

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to an IP and port
        server_socket.bind((host, port))

        # Start listening for incoming connections (max 1 client)
        server_socket.listen(1)
        print(f"[SERVER] Listening on {host}:{port}...")

        # Accept a connection when a client connects
        conn, addr = server_socket.accept()
        print(f"[SERVER] Connection established with {addr}")

        # Communication loop
        while True:
            # Receive data from the client
            data = conn.recv(1024).decode()

            # If client sends nothing, it likely disconnected
            if not data:
                print("[SERVER] Client disconnected gracefully.")
                break

            print(f"[SERVER] Received from client: {data}")

            # Create a response and send back to client
            response = f"Server received: {data}"
            conn.send(response.encode())

    except Exception as e:
        # Handles any unexpected errors
        print(f"[SERVER ERROR] {e}")

    finally:
        # Ensure server shuts down properly
        server_socket.close()
        print("[SERVER] Shutdown successfully.")

if __name__ == "__main__":
    start_server()
