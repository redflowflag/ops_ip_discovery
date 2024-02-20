# -*- coding: utf-8 -*-

import socket
import sys

def is_port_open(ip, port = 10050):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        return True
    except:
        return False
    finally:
        s.close()
    


def main(filename, port = 10050):
    with open(filename, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            if is_port_open(line, port):
                print(line + "\t open")
            else:
                print(line + "\t closed")


if __name__ == "__main__":
    filename = "ips.txt"
    if  len(sys.argv) > 1:
        filename = sys.argv[1]
    main(filename)