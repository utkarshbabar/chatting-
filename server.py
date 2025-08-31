import socket
import threading

# List of connected clients
clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)
    try:
        while True:
            msg = conn.recv(1024)
            if not msg:
                break
            print(f"[{addr}] {msg.decode()}")
            # Broadcast message to all other clients
            for client in clients:
                if client != conn:
                    client.send(msg)
    except:
        pass
    finally:
        print(f"[DISCONNECTED] {addr}")
        clients.remove(conn)
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))  # Listen on all network interfaces
    server.listen(5)
    print("[SERVER STARTED] Listening on port 5555...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
