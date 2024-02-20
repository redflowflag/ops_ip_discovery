# -*- coding: utf-8 -*-
import sys
from scapy.all import *
from random import randint
import subprocess
import os

def main(filename):
    with open(filename, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            if ping_subprocess(line):
                print(line + "\t reachable")
            else:
                print(line + "\t unreachable")

def ping_subprocess(host) -> bool:
    try:
        # 构建ping命令
        command = ['ping', '-n', '1', host]
        
        # 运行ping命令并获取输出结果
        result = subprocess.run(command, capture_output=True)
        
        if result.returncode == 0:
            return True
        else:
            return False
    except FileNotFoundError:
        print("未找到ping命令。请确保已安装了相应的工具。")

def ping_scrapy(host) -> bool:
    # 随机产生IP包Id
    ip_id = randint(1, 65535)
    # 随机产生ICMP包Id
    icmp_id = randint(1, 65535)
    # 随机产生ICMP包Seq
    icmp_seq = randint(1, 65535)
    ans = sr1(IP(id=ip_id, dst=host, ttl=64) /
                ICMP(id=icmp_id, seq=icmp_seq) / b'',
                timeout=5,
                verbose=False)
    # ans.show()
    if ans:
        return True
    else:
        return False

if __name__ == "__main__":
    filename = "ips.txt"
    if  len(sys.argv) > 1:
        filename = sys.argv[1]
    main(filename)