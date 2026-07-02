import socket

def get_network_info():
    return {
        "Hostname": socket.gethostname(),
        "Local IP Address": socket.gethostbyname(socket.gethostname())
    }