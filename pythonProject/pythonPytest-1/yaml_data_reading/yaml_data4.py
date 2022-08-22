import yaml

file = open('../yaml_data/data4.yaml', 'r+', encoding='utf-8')
data = yaml.load(file, Loader=yaml.FullLoader)

print(" yaml_data type: \n---------------------------------------------------")
print(type(data))

print(" whole yaml_data: \n---------------------------------------------------")
print(data)

print("key - value: ---------------------------------------------------")
for n, d in data.items():
    print(n, d)

print("keys: ---------------------------------------------------")
for d in data:
    print(d)

print("keys: ---------------------------------------------------")
for n in data.keys():
    print(n)

print("values: ---------------------------------------------------")
for n in data.values():
    print(n)
print("\n---------------------------------------------------")

stream = open('../yaml_data/document.yaml', 'w')
data['languages_str'] = 77
yaml.dump(data, stream)  # Write a YAML representation of data to 'document.yaml'.
print(yaml.dump(data))  # Output the document to the screen.
