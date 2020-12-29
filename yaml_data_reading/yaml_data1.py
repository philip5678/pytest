import yaml

file = open('../yaml_data/data1.yaml', 'r+', encoding='utf-8')
data = yaml.load(file, Loader=yaml.FullLoader)

print(" yaml_data type: ---------------------------------------------------")
print(type(data))

print(" whole yaml_data: ---------------------------------------------------")
print(data)

print("\n---------------------------------------------------")
stream = open('../yaml_data/document.yaml', 'w')
data[1]['cherry'] = 77
yaml.dump(data, stream, Dumper=yaml.Dumper)  # Write a YAML representation of data to 'document.yaml'.
print(yaml.dump(data))  # Output the document to the screen.


def up_yml(ip_server):
    with open('../yaml_data/document.yaml', encoding="utf-8") as f:
        content = yaml.load(f, Loader=yaml.Loader)
        # 修改yml文件中的参数
        content[1]['cherry'] = 'mysql_host={}'.format(ip_server)
    with open('./tmp/docker-compose.yml', 'w', encoding="utf-8") as nf:
        yaml.dump(content, nf, Dumper=yaml.Dumper)
        print(yaml.dump(content))  # Output the document to the screen.


up_yml("https://www.ip_server/api")
