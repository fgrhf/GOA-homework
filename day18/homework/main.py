#დავალება2
def get_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
#დავალება3
def count_evens(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count
#დავალება4
def count_odds(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count
#დავალება5
def double_values(numbers):
    new_list = []
    for num in numbers:
        new_list.append(num * 2)
    return new_list
#დავალება6
def square_values(numbers):
    new_list = []
    for num in numbers:
        new_list.append(num ** 2)
    return new_list
#დავალრბა7
def sum_three(a,b,c):
    return a + b + c
#დავალება8
def substract(a, b):
    return a - b
#დავალება9
def multiply(a, b):
    return a * b
#დავალება10
def check_age(age):
    if age >= 18:
        print('access granted')
    else:
        print('access denied')
#დავალება11
def print_names(names):
    for name in names:
        print(name)
#დავალება12
def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
#დავალება13
def student_grade(score):
    if 90 <= score <= 100:
        print('a')
    elif 70 <= score <= 89:
        print('b')
    elif 50 <= score <= 69:
        print('c')
    elif 0 <= score <= 49:
        print('f')
#დავალება14
def user_info(name, last_name, age):
    return f"მომხმარებელი: {name} {last_name}, ასაკი: {age} წლის."
print(user_info('ანა მარია', 'გვიანიშვილი', 16))
#დავალება15
def arithmetic_mean(numbers):
    if not numbers:
        return 0 
    return sum(numbers) / len(numbers)
print(arithmetic_mean([10, 20, 30, 40]))
#დავალება16
def filter_vowels(text):
    vowels = 'aeiou'
    result = ""
    for char in text:
        if char in vowels:
            result += char
    return result
print(filter_vowels('გამარჯობა როგორ ხარ? hello'))
#დავალება17
def remove_duplicates(my_list):
    return list(set(my_list))
print(remove_duplicates([1,2,3,4,5]))
#დავალება18
def manual_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(manual_sum([5,10,15,20]))