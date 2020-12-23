import yaml

option = int(input("please input 1 or 2: "))
if option == 1:
    file = open('../yaml_data/data1.yaml', 'r', encoding='utf-8')
else:
    file = open('../yaml_data/data2.yaml', 'r', encoding='utf-8')
data = yaml.load(file, Loader=yaml.FullLoader)
print(" yaml_data type: ---------------------------------------------------")
print(type(data))
print(" whole yaml_data: ---------------------------------------------------")
print(data)
print("keys: ---------------------------------------------------")
for d in data:
    print(d)
print("key - value: ---------------------------------------------------")
for n, d in data.items():
    print(n, d)
print("keys: ---------------------------------------------------")
for n in data.keys():
    print(n)
print("values: ---------------------------------------------------")
for n in data.values():
    print(n)
print("---------------------------------------------------")