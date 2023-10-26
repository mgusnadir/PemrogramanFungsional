random_list = [105, 3.1, "Hello", 737, "Phyton", 2.7, "World", 412, 5.5, "AI"]

float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

def map_int(value):
    result = {}
    if value < 10:
        result['satuan'] = value
        result['puluhan'] = 0
        result['ratusan'] = 0
    elif value < 100:
        result['satuan'] = value // 10
        result['puluhan'] = value % 10
        result['ratusan'] = 0
    else:
        result['satuan'] = value // 100
        result['puluhan'] = (value // 10) % 10
        result['ratusan'] = value % 10
    return result

int_mapped = list(map(map_int, int_values))

print("Data Float:")
print(float_values)
print("Data int:")
for item in int_mapped:
    print(item)
print("Data String:")
print(string_values)
