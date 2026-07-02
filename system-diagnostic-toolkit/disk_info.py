import psutil

def get_disk_info():
    disk = psutil.disk_usage('/')

    return {
        "Total Storage (GB)": round(disk.total / (1024 ** 3), 2),
        "Used Storage (GB)": round(disk.used / (1024 ** 3), 2),
        "Free Storage (GB)": round(disk.free / (1024 ** 3), 2),
        "Disk Usage (%)": disk.percent
    }