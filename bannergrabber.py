import socket

def banner(ip , port):
    s = socket.socket()
    
    s.connect((ip, port))

    print(str(s.recv(1024)).strip('b'))

if __name__ == "__main__":
    ip = input("Please enter the IP: ")
    port = int(input("Please enter the port: "))
    banner(ip, port)
