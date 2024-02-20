# -*- coding: utf-8 -*-
import sys
import subprocess
import os
import concurrent.futures
 

def main(filename):
    # 创建一个ThreadPoolExecutor对象，指定最大工作线程数为5
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    with open(filename, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            # task_get_hostname(line)
            executor.submit(task_get_hostname, line)
    executor.shutdown()
def task_get_hostname(host):
    rlt = zbx_get_hostname(host)
    if len(rlt) > 1:
        x = host + "\t " + rlt[0].decode('utf-8') + "\t" + rlt[1].decode('utf-8')
        print(x)

def zbx_get_hostname(host) -> tuple:
    try:
        # 构建ping命令
        command = ["C:\\zabbix_agent5.0.2\\bin\\zabbix_get.exe",  "-s",  host, "-p", "10050",  "-k", "agent.hostname"]
        # command = ["zabbix_get",  "-s",  host, "-p", "10050",  "-k", "agent.hostname"]
        
        # 运行ping命令并获取输出结果
        result = subprocess.run(command, capture_output=True)
        
        if result.returncode == 0:
            return (result.stdout, result.stderr)
        else:
            return (result.stdout, result.stderr)
    except FileNotFoundError:
        print("err: cannot file zabbix_get command")
        return ()


if __name__ == "__main__":
    filename = "ips_10050.txt"
    if  len(sys.argv) > 1:
        filename = sys.argv[1]
    main(filename)