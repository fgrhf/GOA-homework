phrase = "Python Programming"
#მხოლოდ Python
print(phrase[:6])
#მხოლოდ Programming
print(phrase[7:])
#ყოველი მესამე სიმბოლო
print(phrase[::3])

# დავალება 4
text = "PythonSlicing"
#პირველი 6 სიმბოლო
print(text[:6])
#სტრინგი უკუღმა
print(text[::-1])
#ყოველი მეორე სიმბოლო
print(text[::2])

#დავალება 5
letters = ['a','b','c','d','e','f','g','h','i']
#ლუწი
print(letters[::2])
#2 დან 7 მდე
print(letters[2:7:2])
#უკუღმა
print(letters[:5:-1])

#დავალება 6 
sentence = "Slicing makes Python powerful"
#სიტყვა Python
print(sentence[14:20])
#სიტყვა Powersul უკუღმა

# ყოველი მესამე სიმბოლო
print(sentence[::3])