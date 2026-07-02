import psutil
import platform

def get_cpu_info():
    return {
        "CPU Name": platform.processor(),
        "Physical Cores": psutil.cpu_count(logical=False),
        "Logical Cores": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(interval=1)
    }
    