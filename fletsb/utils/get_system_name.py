import platform



def get_system_name ():
    """Output: mac, windows, linux or unknown"""
    system = platform.system()

    if system == "Windows":
        return "windows"
    elif system == "Darwin":
        return "mac"
    elif system == "Linux":
        return "linux"
    else:
        return "unknown"