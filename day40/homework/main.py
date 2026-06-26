#დავალება 1
students = {
    "ანა": 45,
    "გიორგი": 72,
    "ნიკა": 50,
    "ლუკა": 85
}
students["მარიამი"] = 90
students["ანა"] = 55
good_students = [name for name, grade in students.items() if grade > 50]

print("სტუდენტები 50-ზე მეტი ნიშნით:", good_students)

#დავალება 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [num ** 2 for num in numbers]
print("კვადრატები:", squares)
even_squares = [sq for sq in squares if sq % 2 == 0]
print("ლუწი კვადრატები:", even_squares)
#დავალება 3
words = ["Python", "AI", "Development", "Code", "Learning", "Data"]
long_words = [word for word in words if len(word) > 4]

print("სიტყვები, რომელთა სიგრძე > 4:", long_words)
#დავალება 4
products = {
    "პური": 1.2,
    "ყველი": 4.5,
    "რძე": 3.2,
    "წყალი": 0.8,
    "შოკოლადი": 3.5
}
expensive_products = [name for name, price in products.items() if price > 3]

print("პროდუქტები, რომელთა ფასი > 3$:", expensive_products)