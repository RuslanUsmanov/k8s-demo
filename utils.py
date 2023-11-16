import subprocess
import re


def get_interface_ip(interface) -> str:
    command = f"ip addr show {interface}"
    output = subprocess.check_output(command, shell=True).decode()
    ip_pattern = r'inet\s+(\d+\.\d+\.\d+\.\d+)'
    match = re.search(ip_pattern, output)

    if match:
        ip_address = match.group(1)
        return ip_address
    else:
        return None


def get_interfaces() -> list[str]:
    command = "ip link list"
    output = subprocess.check_output(command, shell=True).decode()
    link_pattern = r'\d{,2}: [a-z0-9]+'
    matches = re.findall(link_pattern, output)

    return [link[1] for link in [m.split() for m in matches]]


def get_ips() -> dict[str, str]:
    ips = {}
    links = get_interfaces()
    for link in links:
        if link != 'lo':
            ips[link] = get_interface_ip(link)
    return ips
