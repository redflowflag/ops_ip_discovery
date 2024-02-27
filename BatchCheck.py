# -*- coding: utf-8 -*-

import os
import sys
import fire
from lib.CheckLib import CheckLib

def main(filename, ports=[], zbxkeys =[] ):
    if filename == '':
        return None
    if type(ports) != list or type(zbxkeys) != list:
        print("type of ports/keys is not list")
        return None

    try:
        checkResults = []
        checkLib = CheckLib()
        checkLib.CheckAll()
        with open(filename) as file:
            while True:
                ip_addr = file.readline().strip()
                if not ip_addr:
                    break
                if ip_addr == "":
                    continue
                rlt = checkLib.check_all(ip_addr, ports=ports, zbxkeys=zbxkeys)
                checkResults.append(rlt)
    except FileNotFoundError:
        print("File not found.")
        return None 

if __name__ == "__main__":
    fire.Fire(main)
