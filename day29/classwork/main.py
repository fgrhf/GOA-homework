#sets ->{} არ ინახავს დუბლიკატ ელემენტებს.დაულაგებელი მონაცემის ტიპია,ინდექსები არა აქვს.

#myset= {1,2,3,4,4,5,6,7,7,7,8,'ana'}
#print(myset)

#myset2 = {'apple', 'melon', 'cherry'}
#.remove() set-ში შლის ელემენტს მისის დასახელების მიხედვით.ინდექსებს არ აქვს მნიშვნელობა.
#.add() set -ში ამატებს ელემენტს.ინდექსებს არ არქვს მნიშვნელობა.
#.clear() set-ს მთლიანად ასუპთავებს.
#.union() აერთიანებს ორ სეტის ელემენტებს.
#.difference() გამოიტანს იმ ელემენტებს რაც ერთ set-ს განსხვავებული მეორესგან.

#myset2.add("watermelon")
#print(myset2)

#myset3 = {'carrot', 'cucumber', 'basil'}
#myset3.remove('cucumber')
#print(myset3)


myset4 = {1,3,5,7}
myset5 = {2,4,6,8}
print(myset4.union(myset5))
print(myset4.difference(myset5))
print(myset5.difference(myset4))

set1 = {'apple', 'melon', 'strawberry'}
set2 = {'banana', 'apple','strawberry'}
print(set2.difference(set1))




languages = {'html', 'css', 'javascript'}
languages.remove('javascript')
languages.add('react')
print(languages)


countries = {'georgia', 'germany', 'usa'}
countries.clear()
countries.add('tbilisi')
countries.add('berlin')
countries.add('new york')
print(countries)


set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}
combo = set1.union(set2)
print(combo)

#{'apple','banana','cherry','orenge'}
#union აერთიანებს ორ სეტს და აშორებს დუბლიკატებს. რადგან 'banana' რივე სვეტშია,საბოლოო შედეგში ის მხოლოდ ერთხელ ჩაიწერება.