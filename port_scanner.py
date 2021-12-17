"""
Basic Port Scanner

"""
import socket

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    host = input("Enter an IP: ")
    port = int(input("Enter a port: "))

    portScanner(port)