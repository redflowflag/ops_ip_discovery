### usage: 
```shell
python .\BatchCheck.py  <ip_list.txt>  --ports  "[22,3389, 10050, 161, 5985]"  --zbxkeys  "['agent.hostname', 'agent.version']"
```

*return sample:* 
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