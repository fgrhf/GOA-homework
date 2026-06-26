my_dict = {
    'name': 'anna maria',
    'surname': 'gvianishvili',
    'age': 16
}

for key,value in my_dict.items():
    print(key,value)


numbers = [1, 2, 3, 4, 5]
doubled_numbers = [x*2 for x in numbers]
print(doubled_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 !=0:
        print(num)