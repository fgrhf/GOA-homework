#დავალება1
#dictionary (ლექსიკონი) არის მონაცემთა სტრუქტურა, რომელიც ინახავს ინფორმაციას "key: value" (გასაღები: მნიშვნელობა) წყვილებად.
#ის არის შეცვლადი (mutable) და მასში ელემენტები არ არის დალაგებული ინდექსების მიხედვით, არამედ მათზე წვდომა ხდება უნიკალური გასაღებების (key) საშუალებით.
#დავალება2
footballer = {
    'name': 'Lionel Messi',
    'country': 'Argentina',
    'goals_count': 850
}
print(footballer)
#დავალება3
supra = {
    'foods': ['ხინკალი', 'მწვადი', 'ქაბაბი']
}
print(supra['foods'][2])
#დავალება4
movie = {
    'title': 'Inception',
    'year': 2010
}
movie['year'] = 2024
print(movie)
#დავალება5
student = {
    'name': 'გიორგი',
    'age': 18
}
del student['age']

print(student)
