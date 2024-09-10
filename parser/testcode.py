def process_data(data):
    config ={'version': 1.0,'options':{'verbose': True,'log_level': 'debug'},'filters': [lambda x: x * 2,lambda x: x + 5],'data':{'items': [{'name': 'item1', 'value': 10},{'name': 'item2', 'value': 20},{'name': 'item3', 'value': 30}            ],'settings': {'threshold': 15,'enabled': True}}}
    if (threshold := config['data']['settings']['threshold']) and any(item['value'] > threshold for item in config['data']['items']):
        print(f"Threshold ({threshold}) exceeded!")
    filtered_data = [filter_func(x) for x in data for filter_func in config['filters']]
    return filtered_data

simple_dict ={'key1':'value1','key2': 100}
nested_dict ={'level1':{'level2': {'level3': {'key': 'value'}}}}
list_comp_dict ={'squares': [x ** 2 for x in range(5)],'even_numbers': [x for x in range(10) if x % 2 == 0]}
data = [5, 10, 15, 20]
processed_data = process_data(data)
print(processed_data)
print("Simple Dictionary:", simple_dict)
print("Nested Dictionary:", nested_dict)
print("List Comprehension Dictionary:", list_comp_dict)
