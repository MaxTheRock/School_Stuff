import socket

def receive_broadcast(port=12345):
    try:
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind to the broadcast address and port
        sock.bind(("", port))

        print(f"Listening for broadcast messages on port {port}...")
        while True:
            try:
                data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
                print(f"Received message: {data.decode()} from {addr}")
            except UnicodeDecodeError:
                print(f"Received non-decodable message from {addr}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()
        print("Socket closed.")

if __name__ == "__main__":
    receive_broadcast()