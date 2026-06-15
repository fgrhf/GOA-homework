#დავალება2
numbers = []
for i in range(5):
    num = float(input(f"შემოიტანე {i+1}-ე როცხვი: "))
    numbers.append(num)
average = sum(numbers) / len(numbers)
print("რიცხვების საშუალო არითმეტიკული არის: ", average)
#დავალება3
sentence = input("შემოიტანე წინადადება: ")
print("წინადადების სიგრძეა: ", len(sentence))
#დავალება4
password = input("შემოიტანე პაროლი: ")
index = password.find("1")
if index != -1:
    print("პაროლი შეიცავს 1-იანს")
else:
    print('პაროლი არ შეიცავს 1-იანს')
#დავალება5
fruits = ["apple", "banana", "orange"]
fruits.append('cherry')
fruits.pop(3)
fruits.insert(3, 'blueberry')
print(fruits)
#დავალება6
word = input('შემოიტანე სიტყვა: ')
if word[0].isupper():
    print('perfect')
else:
    print('your word should be capitalized')
#დავალება7
name_surname = input('შემოიტანე სახელი და გვარი: ')
print('uppercase:', name_surname.upper())
print('lowercase:', name_surname.lower())
#დაველბა8
my_name = "ანა მარია"
user_name = input('შემოიტანეთ თქვენი სახელი: ')
if my_name.lower() == user_name.lower():
    print('our names are similar')
else:
    print('we have different names')
#დავალება9
text = "გამარჯობა მსოფლიო"
index = text.find('მ')
print('ასოს ინდექსია:', index)
#დავალება10
strings_list = ['apple', 'banana', 'cherry']
upper_list = []
for word in strings_list:
    upper_list.append(word.upper())
print(upper_list)
#დავალება11
empty_list = []
for i in range(3):
    data = input('შემოიტანე რაიმე მონაცემი: ')
    empty_list.append(data)
print('საბოლოო სია:', empty_list)
#დავალება12
fruits = ['apple', 'banana', 'cherry', 'kiwi']
new_fruit = input('შემოიტანე ახალი ხილი: ')
fruits.insert(2,new_fruit)
print('განახლებული სია:', fruits)