# -*- coding: utf-8 -*-
import sys
import socket
# from scapy.all import *
from random import randint
import platform
import subprocess
import os


class CheckLib:
    
    def __init__(self) -> None:
        pass

    def ping_subprocess(self, host) -> bool:
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

    # def ping_scrapy(self, host) -> bool:
    #     ip_id = randint(1, 65535)
    #     icmp_id = randint(1, 65535)
    #     icmp_seq = randint(1, 65535)
    #     ans = sr1(IP(id=ip_id, dst=host, ttl=64) /
    #                 ICMP(id=icmp_id, seq=icmp_seq) / b'',
    #                 timeout=5,
    #                 verbose=False)
    #     # ans.show()
    #     if ans:
    #         return True
    #     else:
    #         return False
        

    def is_port_open(self, ip, port = 10050):
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
        
    def zbx_get_keys(self, host, port=10050, zbxkeys=["agent.hostname", "agent.version"]) -> list:

        os_type = platform.system()
        zbx_cmd = "zabbix_get" if os_type != "Windows" else "C:\\zabbix_agent5.0.2\\bin\\zabbix_get.exe"
        returnValue = []
        for key in zbxkeys:
            # try:
            command = [zbx_cmd, "-s", host, "-p", str(port), "-k", key]
            result = subprocess.run(command, capture_output=True)
        
            if result.returncode == 0:
                returnValue.append((host, key, True,  result.stdout.decode('utf-8').strip(), result.stderr.decode('utf-8').strip()))
            else:
                returnValue.append((host, key, False,  result.stdout.decode('utf-8').strip(), result.stderr.decode('utf-8').strip()))
            # except FileNotFoundError:
            #     print("err: cannot locate zabbix_get command")
        return returnValue

    def check_all(self, ip_addr, ports=[], zbxkeys=[], zbx_agent_port = 10050):
        if not zbx_agent_port in ports:
            ports.append(zbx_agent_port)
        
        checkResult = {"ip_addr": ip_addr,"ping_reachable":"", "open_ports":{}, "zbx_keys": {}}
        # check pingable
        pingResult = self.ping_subprocess(ip_addr)
        checkResult["ping_reachable"] = pingResult
        # check open ports
        for port in ports:
            isPortOpen = self.is_port_open(ip_addr, port)
            checkResult["open_ports"][str(port)] = isPortOpen
        
        # get zabbix keys
        if checkResult["open_ports"][str(zbx_agent_port)] == True:
            keysResults = self.zbx_get_keys(ip_addr, zbx_agent_port, zbxkeys)
            for rlt in keysResults:
                checkResult["zbx_keys"][rlt[1]] = rlt[3]

        return checkResult