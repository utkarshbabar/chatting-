import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print("\n" + msg)
        except:
            print("Connection closed.")
            break

def start_client(server_ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, 5555))

    username = input("Enter your username: ")
    client.send(f"{username} joined the chat".encode())

    # Start thread for receiving messages
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        msg = input()
        client.send(f"{username}: {msg}".encode())

if _name_ == "_main_":
    server_ip = input("Enter server IP: ")
    start_client(server_ip)
