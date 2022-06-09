import socket


def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = False
    try:
        sock.connect((ip, port))
        result = True
        sock.close()
    except:
        pass
    return result


def receive_open_ports(ip, begin_port, end_port):
    open_ports = {}
    for i in range(begin_port, end_port + 1):
        # print(open_ports)
        if scan_port(ip, i):
            open_ports[i] = "open"
            continue
        open_ports[i] = "close"
    return open_ports
