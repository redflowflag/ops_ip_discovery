# -*- coding: utf-8 -*-

from host_scanning.host_discovery import HostDiscovery
# from port_scanning.port_scanning import PortScanning


class NetScanning:
    # def __init__(self, target):
    #     self.target = target

    def scan(self, subnet):
        print('start scanning...')
        alive_host = set()

        host_discovery = HostDiscovery(subnet, False).ping()
        while not host_discovery.res_que.empty():
            alive_host.add(host_discovery.res_que.get())
        # host_discovery = HostDiscovery(subnet, False).arping()
        # while not host_discovery.res_que.empty():
        #     alive_host.add(host_discovery.res_que.get())
        # host_discovery = HostDiscovery(subnet, False).erriping()
        # while not host_discovery.res_que.empty():
        #     alive_host.add(host_discovery.res_que.get())

        # print('alive host:')
        # alive_host = sorted(alive_host)
        # print(alive_host)
        # print('\n')

        # for host in alive_host:
        #     print('For ' + host + ':')
        #     PortScanning(host + ':1-1024').scan()

        print('scanning over')
        print(alive_host)
        return alive_host


if __name__ == '__main__':
    NetScanning().scan('192.168.1.0/28')
