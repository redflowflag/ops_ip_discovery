# -*- coding: utf-8 -*-
import sys
import subprocess
import os
import concurrent.futures
 
import platform
 


def main(filename):
    # 创建一个ThreadPoolExecutor对象，指定最大工作线程数为5
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    with open(filename, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            # task_get_hostname(line)
            executor.submit(task_get_keys, line, 10050, ["agent.hostname", "agent.version", "system.hostname"] )
            # task_get_keys(line,10050, ["agent.hostname", "agent.version"] )
    executor.shutdown()

def task_get_keys(host, port=10050, keys=["agent.hostname", "agent.version"]):
    lstRlt = zbx_get_keys(host, port, keys)
    for rlt in lstRlt:
        if len(rlt) > 1:
            x = rlt[0].strip() + "\t" + rlt[1].strip() + "\t" + str(rlt[2]) + "\t" + rlt[3].decode('utf-8').strip() + "\t" + rlt[4].decode('utf-8').strip()
            print(x)
# def task_get_hostname(host):
#     rlt = zbx_get_hostname(host)
#     if len(rlt) > 1:
#         x = host + "\t " + rlt[0].decode('utf-8') + "\t" + rlt[1].decode('utf-8')
#         print(x)

# def zbx_get_hostname(host) -> tuple:
#     try:
#         os_type = platform.system()
#         zbx_cmd = "zabbix_get" if os_type == "Windows" else "C:\\zabbix_agent5.0.2\\bin\\zabbix_get.exe"
#         # command = ["zabbix_get",  "-s",  host, "-p", "10050",  "-k", "agent.hostname"]
#         # command = ["C:\\zabbix_agent5.0.2\\bin\\zabbix_get.exe",  "-s",  host, "-p", "10050",  "-k", "agent.hostname"]
#         command = [zbx_cmd, "-s", host, "-p", "10050", "-k", "agent.hostname"]
        
#         # 运行ping命令并获取输出结果
#         result = subprocess.run(command, capture_output=True)
        
#         if result.returncode == 0:
#             return (result.stdout, result.stderr)
#         else:
#             return (result.stdout, result.stderr)
#     except FileNotFoundError:
#         print("err: cannot file zabbix_get command")
#         return ()

def zbx_get_keys(host, port=10050, keys=["agent.hostname", "agent.version"]) -> tuple:

    os_type = platform.system()
    zbx_cmd = "zabbix_get" if os_type != "Windows" else "C:\\zabbix_agent5.0.2\\bin\\zabbix_get.exe"
    # command = ["zabbix_get",  "-s",  host, "-p", "10050",  "-k", "agent.hostname"]
    # command = ["C:\\zabbix_agent5.0.2\\bin\\zabbix_get.exe",  "-s",  host, "-p", "10050",  "-k", "agent.hostname"]
    # Return value: [key, success:true/false, output, errmsg]
    returnValue = []
    for key in keys:
        # try:
        command = [zbx_cmd, "-s", host, "-p", str(port), "-k", key]
        result = subprocess.run(command, capture_output=True)
    
        if result.returncode == 0:
            returnValue.append((host, key, True,  result.stdout, result.stderr))
        else:
            returnValue.append((host, key, False,  result.stdout, result.stderr))
        # except FileNotFoundError:
        #     print("err: cannot locate zabbix_get command")
    return returnValue

if __name__ == "__main__":
    filename = "ips_10050.txt"
    if  len(sys.argv) > 1:
        filename = sys.argv[1]
    main(filename)