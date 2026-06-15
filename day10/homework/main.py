# დავალება 3
for i in range(50, 201):
    print(i)

# დავალება 4
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# დავალება 5
for i in range(100, 150):
    if i % 2 != 0:
        print(i)

# დავალება 6
i = 1
while i <= 50:
    print(i)
    i += 1

# დავალება 7
i = 20
while i <= 60:
    print(i)
    i += 5

# დავალება 8
gvari = input('შეიყვანეთ თქვენი გვარი: ')
for aso in gvari:
    print(aso)

# დავალება 9
maragi = 300
while maragi > 0:
    maragi -= 2
    print(f"tou have bought the drink.დარჩენილი მარაგი: {maragi}")
    print("Out of stock")

# დავალება 10
for i in range(50, 19, -3):
    print(i)

# დავალება 11
i = 150 
while i >= 0:
    print(i)
    i-= 1

# დავალება 12
#for loop - მუშაობს მაშინ როდესაც წინასწარ ვიცით ბრუნების ზუსტი რაოდენობა.ის ავტომატურად მიჰყვება მოცემულ დიაპაზონს ან სიას თავიდან ბოლომდე.

# დავალება 13
#while loop - მუშაობს მანამ სანამ პირობა ჭეშმარიტია.counter კი სჭირდება იმისთვის,რომ ყოველ ბრუნზე შეიცვალოს,პირობა საბოლოოდ დაირღვეს და ციკლი უსასრულოდ არ გაიჭედოს.