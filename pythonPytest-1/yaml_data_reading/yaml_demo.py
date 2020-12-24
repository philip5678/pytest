import yaml

option = int(input("please input 1, 2 or 3: "))
if option == 1:
    file = open('../yaml_data/data1.yaml', 'r+', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
elif option == 2:
    file = open('../yaml_data/data2.yaml', 'r+', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
else:
    file = open('../yaml_data/data3.yaml', 'r+', encoding='utf-8')
    data = yaml.dump(file)

print(" yaml_data type: \n---------------------------------------------------")
print("\n---------------------------------------------------")
print(type(data))

print(" whole yaml_data: \n---------------------------------------------------")
print("\n---------------------------------------------------")
print(data)

# print("keys: \n---------------------------------------------------")
# print("\n---------------------------------------------------")
# for d in data:
#     print(d)
# print("key - value: \n---------------------------------------------------")
# print("\n---------------------------------------------------")
#
# if option == 3:
#     for n, d in data.items():
#         print(n, d)
# print("keys: \n---------------------------------------------------")
# print("\n---------------------------------------------------")
#
# if option == 3:
#     for n in data.keys():
#         print(n)
# print("values: \n---------------------------------------------------")
# print("\n---------------------------------------------------")
#
# if option == 3:
#     for n in data.valu1es():
#         print(n)
# print("\n---------------------------------------------------")

print("\n---------------------------------------------------")
stream = open('../yaml_data/document.yaml', 'w')
data[1]['cherry'] = 77
yaml.dump(data, stream)  # Write a YAML representation of data to 'document.yaml'.
print(yaml.dump(data))  # Output the document to the screen.
