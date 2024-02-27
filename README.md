## Introduction
This is a zabbix and network check tools for server monitoring. It can help you to check following item for machines:
- icmp ping reachable
- ports open or not
- get zabbix keys if you installed zabbix_get

## usage: 
- add your ips to  a plain text file
- run command 
```shell
python ./BatchCheck.py  <ip_list.txt>  --ports  "[22, 5985, 3389, 161, 10050]"  --zbxkeys  "['agent.hostname', 'agent.version','system.hostname','system.sw.os']" --output_format table  --output_file ./output.json
```

## output samples:
#### --output_format dict
```shell

[{
	"ip_addr": "xx.xx.xx.xx",
	"ping_reachable": true,
	"open_ports": {
		"22": true,
		"3389": false,
		"10050": true
	},
	"zbx_keys": {
		"agent.hostname": "xx.xx.xx.xx",
		"agent.version": "x.x.x",
		"system.hostname": "hostname1",
		"system.sw.os": "Ubuntu blahblah",

	}
}, {}]
```
#### --output_format json
```json

[
    {
        "ip_addr": "10.100.191.24",
        "ping_reachable": true,
        "open_ports": {
            "22": false,
            "5985": false,
            "3389": false,
            "161": false,
            "10050": true
        },
        "zbx_keys": {
            "agent.hostname": "",
            "agent.version": "",
            "system.hostname": "",
            "system.sw.os": ""
        }
    }
]
```
#### --output_format table
```
ip_addr	ping_reachable	22	5985	3389	161	10050	agent.hostname	agent.version	system.hostname	system.sw.os	
xx.xx.xx.101	True	False	False	False	False	True	host1	6.0.0	host1	CentOS Linux 7(Core)	
xx.xx.xx.102	True	False	False	False	False	True	host2	6.0.0	host2	CentOS Linux 7(Core)	

```