# დავალება 1
number = int(input('შემოიტანეთ რიცხვი: '))
if number % 2 == 0:
    print('ლუწია')
else:
    print('კენტია')
# დავალება 2
temp = float(input("შეიყვანეთ ტემპერატურა: "))
if temp > 30:
    print("it'hot")
elif 15 <= temp <= 30:
    print("it's warm")
else:
    print("it's cold")
# დავალება 3
num = int(input('შემოიტანე რიცხვი: '))
if num < 0:
    print("negative")
elif num % 2 == 0:
    print("positive even")
else:
    print("positive odd")
# დავლება 4
limit = int(input("შეიყვანეთ მაქსიმალური რიცხვი: "))
for i in range(limit + 1):
    if i % 2 == 0:
        print(f"{i} - even")
    else:
        print(f"{i} - odd")
# დავალება 5
positives = 0
negatives = 0
zeros = 0
print("შემოიტამეთ 10 რიცხვი: ")
for _ in range(10):
    n = float(input())
    if n > 0:
        positives += 1
    elif n < 0:
        negatives += 1
    else:
        zeros += 1
print(f"დადებითი: {positives},უარყოპიტი: {negatives},ნული: {zeros}")
# დავალება 6
fruits = ["apple", "banana", "orange", "grape"]
index = fruits.index("banana")
fruits[index] = "kiwi"
print(fruits)
# დავალება 7
nums = [4, 8, 12, 16, 20]
result = nums[0] + nums[-1]
print(result)
# დავალება 8
my_list = [10, 20, 30, 40, 50]
for item in my_list:
    print(item)
# დავალება 9
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numbers_list:
    if n % 2 == 0:
        print(n)
# დავალება 10
numbers_list = [5, 10, 15, 20, 25, 30]
even_sum = 0
for n in numbers_list:
    if n % 2 == 0:
        even_sum += n
print("ლუწების ჯამი:", even_sum)
# დავალება 11
numbers_list = [2, 5, 6, 8, 11, 3, 9]
for n in numbers_list:
    if n > 6:
        print(n)
# დავალება 12
word = "python"
for letter in word:
    print(letter)
# დავალება 13
my_list = ["ა", "ბ", "გ", "დ" , "ე"]
print(my_list[:3])
