import yaml
import os

from net_scanning.net_scanning import NetScanning 

# Reading YAML File
def get_yaml_data(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    # print(result, type(result))
    return result




def run():
    # get configuration 
    current_path = os.path.abspath(".")
    yaml_path = os.path.join(current_path, "config.yaml")
    subnets = get_yaml_data(yaml_path)

    netScanning = NetScanning()
    # host discovery by subnet scan
    alive_hosts = {}
    for subnet in  subnets["subnets"]:
        rlt = netScanning.scan(subnet)
        alive_hosts[subnet] = rlt
    print(alive_hosts)





if __name__ == "__main__":
    run()