#Set and dictionary comprehenseions
#set comprehensions
names= {'alice', 'BOB', 'charlie', 'DAVE'}
formatted_names = {name.capitalize() for name in names}
print(formatted_names)

#Dictionary Comprehensions
hyperparams = {'layers':3,'units':256,'dropouts':0.2}
print(hyperparams)

updated_params = {k.upper() for k, v in hyperparams.items() if v>0.2}
print(updated_params)

#zip()
years = [2020, 2021, 2022]
dataset_sizes = [10000, 25000, 50000]
data_growth = dict(zip(years, dataset_sizes))
print(data_growth)

sales = {2022:50000, 2023:75000, 2024:100000}
profit = {year:revenue*0.15 for year, revenue in sales.items()}
print(profit)