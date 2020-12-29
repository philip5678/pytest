import yaml


file = open('../yaml_data/data2.yaml', 'r+', encoding='utf-8')
data = yaml.load(file,Loader=yaml.FullLoader)

print(" yaml_data type: \n---------------------------------------------------")
print(type(data))

print(" whole yaml_data: \n---------------------------------------------------")
print(data)

print("\n---------------------------------------------------")

stream = open('../yaml_data/document.yaml', 'w')
data[0] = 77
yaml.dump(data, stream)  # Write a YAML representation of data to 'document.yaml'.
print(yaml.dump(data))  # Output the document to the screen.
