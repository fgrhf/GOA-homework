#Tuple unpacking არის პროცესი, როდესაც თაიფლის (tuple) შიგნით არსებულ ელემენტებს პირდაპირ ვანიჭებთ ცალკეულ ცვლადებს.

#მაგალითი 1: სტანდარტული unpacking (Asterisk-ის გარეშე)
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)  # გამოიტანს: 10 20 30

#მაგალითი 2: Unpacking Asterisk (*) ოპერატორით (დასაწყისში და შუაში ელემენტების აღება)
numbers = (1, 2, 3, 4, 5)
a, b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4] -> მასივის სახით აგროვებს დარჩენილებს
print(c)  # 5

#მაგალითი 3: Unpacking Asterisk (
#) ოპერატორით ბოლოში
colors = ("Red", "Green", "Blue", "Yellow")
primary1, primary2, *others = colors
print(primary1)  # Red
print(primary2)  # Green
print(others)    # ['Blue', 'Yellow']


#​თაფლი არის უცვლადი (immutable), ამიტომ მას მხოლოდ ორი ჩაშენებული მეთოდი აქვს:
#count() - ითვლის კონკრეტული ელემენტის რაოდენობას
#index() - აბრუნებს პირველივე ნაპოვნი ელემენტის ინდექსს
#ასევე გამოიყენება ზოგადი ფუნქციები: len(), max(), min(), sum(), tuple()


#არ მუშაობს: append(), extend(), insert(), remove(), pop(), clear(), sort(), reverse()


info = ("გიორგი", 17, "თბილისი", "სტუდენტი", "შავი ზღვა")

name, age, city, status, uni = info

print(name)  # გიორგი
print(age)   # 17

numbers_tuple = (5, 10, 3.14, 2.71, 8, 9.9)
num1, *rest = numbers_tuple
print(num1)  
print(rest)  


fruits = ('Apple', 'Pomegranate', 'Cherry', 'Strawberry', 'Blueberry')
*fruit1, fruit2, fruit3 = fruits

#ამ კოდის გაშვებისას თაიფლის ბოლო ორი ელემენტი ('Strawberry' და 'Blueberry') მიენიჭება შესაბამისად fruit2-ს და fruit3-ს. ვარსკვლავიანი ცვლადი *fruit1 კი თავის თავში მოაქცევს ყველა დარჩენილ ელემენტს დასაწყისიდანვე სიის (List) სახით.