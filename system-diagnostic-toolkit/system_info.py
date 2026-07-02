import socket
import getpass
import platform
def get_system_info():
    return {
        "Computer Name": socket.gethostname(),
        "Current User": getpass.getuser(),
        "Operating System": platform.system(),
        "Architecture": platform.architecture()[0],
        "Python Version": platform.python_version(),
        "Machine Type": platform.machine()
    }