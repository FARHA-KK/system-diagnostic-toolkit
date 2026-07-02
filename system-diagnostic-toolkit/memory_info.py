import psutil
def get_memory_info():
    memory=psutil.virtual_memory()
    return{
        "Total RAM (GB)":round(memory.total/(1024**3),2),
        "Used RAM (GB)":round(memory.used/(1024**3),2),
        "Free RAM (GB)":round(memory.available/(1024**3),2),
        "RAM Used (%)":memory.percent
    }