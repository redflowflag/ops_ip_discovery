# -*- coding: utf-8 -*-

import os
import sys
import fire
import json
import copy

# from scapy import data
from lib.CheckLib import CheckLib

def dict_to_flat(origin_dict, target_dict):
    keys = origin_dict.keys()
    for key in keys:
        if type(origin_dict[key]) == dict:
            x = dict_to_flat(origin_dict[key], target_dict)
            target_dict.update(x)
        else:
            target_dict[key] = origin_dict[key]
    return target_dict


def output_result(resultData, output_format="dict", output_file = ""):
    out_file = None
    if output_file != "":
        out_file = open(output_file, 'w')
    if output_format == "dict":
        if out_file is None:
            print(resultData)
        else:
            out_file.write(resultData)
            out_file.close()
        return
    elif output_format == "table":
        result = []
        str_result = ""
        for rlt in resultData:
            x = dict_to_flat(rlt,{})
            result.append(x)
        if len(result) <= 0:
            print("no data found")
            return

        for i in range(len(result)):
            headers = result[i].keys()
            if  i == 0:  #print header
                str_header = ""
                for h in headers:
                    str_header +=  h + '\t'
                str_result += str_header + "\n"
                # print(str_header)
            str_content = ""
            for h in headers:
                str_content += str(result[i][h]) + '\t'
            str_result +=  str_content + "\n"
            # print(str_content)
        if out_file is None:
            print(str_result)
        else:
            out_file.write(str_result)
            out_file.close()
        return
            
    elif output_format == "json":
        if out_file is None:
            print(json.dumps(resultData))
        else:
            out_file.write(json.dumps(resultData))
            out_file.close()
        return
    


def main(filename, ports=[], zbxkeys =[] , output_format="table", output_file = ""):
    if filename == '':
        return None
    if type(ports) != list or type(zbxkeys) != list:
        print("type of ports/keys is not list")
        return None
    try:
        checkResults = []
        checkLib = CheckLib()
        with open(filename) as file:
            while True:
                ip_addr = file.readline().strip()
                if not ip_addr:
                    break
                if ip_addr == "":
                    continue
                rlt = checkLib.check_all(ip_addr, ports=ports, zbxkeys=zbxkeys)
                checkResults.append(rlt)
                print(rlt)
        output_result(checkResults, output_format, output_file)
    except FileNotFoundError:
        print("File not found.")
        return None 

if __name__ == "__main__":
    fire.Fire(main)
