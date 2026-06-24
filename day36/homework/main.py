#დავალება1
my_set = {1, 2, 3, 3, 4, 5, 6, 6, 7, 7,}
print(my_set)
#დაცვალება2
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)
#დავალება3
favorite_movies = {'inception', 'interstellar','the dark knight'}
print(len(favorite_movies))
#დავალება4
week_days = {'monday', 'tuesday', 'wednesday'}
for day in week_days:
    print(f'დღე:{day}')
#დავალება5
football_players = {'დათო', 'ნიკა', 'ლუკა', 'ლიკა'}
basketball_players = {'ანი', 'ლუკა', 'მარიამი', 'ნიკა'}
all_players = football_players.union(basketball_players)
print(all_players)
print(len(all_players))
#დავალება6
wishlist = {'javaScript', 'python', 'html'}
learned = {'python', 'html'}
to_learn = 
#დავალება7
days_of_week = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
for day in days_of_week:
    print(f"დღე: {day}")
#დავალება8
football_players = {'დათო', 'ნიკა', 'ლუკა', 'ლიკა'}
basketball_players = {'ანი', 'ლუკა', 'მარიამი', 'ნიკა'}
all_unique_players = football_players.union(basketball_players)
total_students = len(all_unique_players)
print("ყველა უნიკალური მოსწავლე:", all_unique_players)
print("სულ უნიკალური მოსწავლეების რაოდენობა:", total_students)
#დავალება9
wishlist = {'Python', 'JavaScript', 'React', 'HTML', 'CSS', 'Django'}
learned = {'HTML', 'CSS', 'JavaScript'}
to_learn = wishlist.difference(learned)
print("ტექნოლოგიები, რომლებიც დაგრჩათ სასწავლი:", to_learn)
#დავალება10
cart = {101, 204, 305}
cart.clear()
print("კალათა გასუფთავების შემდეგ:", cart)