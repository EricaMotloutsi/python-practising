#Dictionary operations and methods:Accessing, Updating, .GET(), .KEYS(), and .VALUES

#Assignment and copying

model_params = {'layers':24, 'units':512, 'activation':'relu'}
shared_params = model_params

model_params['activation'] = 'gelu'
print(shared_params)

safe_params = model_params.copy()
model_params['layers']= 48
print(safe_params)

#The update() method for merging dictionaries
base_config = {'batch_size':32, 'epochs':10}
version_config = {'learning_rate':0.001, 'units':128}
base_config.update(version_config)
print(base_config)

#Clearing dictionary with clear()
model_params.clear()
print(model_params)

#Dictionary Views with keys(), values(), and items()
print(base_config.keys())

print(base_config.values())

for key, value in base_config.items():
    print(f'{key}=>{value}')

#Testing Memebership with in
print('batch_size' in base_config)
print

#iterate over values
for value in base_config.values():
    print(f'Value:{value}')

#iterate over keys and values
for key, value in base_config.items():
    print(f'{key} => {value}')

#Setting Operations with Dictionary Keys and Items
config_a = {'batch_size':32, 'optimizer':'adam'}
config_b= {'batch_size':64, 'optimizer':'adam', 'momentum':0.9}

#dict.pop(key)
data = {'name':'Alice', 'age':30, 'city':'New York'}
age = data.pop('age')
print(age,data)

country = data.pop('country', 'Not found')
print(country)

#dict.popitem()
data = {'name':'Alice', 'age':30, 'city':'New York'}

last_item = data.popitem()
print(last_item,data)

#del dict[key]
data = {'name':'Alice', 'age':30, 'city':'New York'}
del data['city']
print(data)
