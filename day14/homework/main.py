#დავალება 3
phrase = "Python Programming"
word1 = phrase[0:6]
print(word1)

word2 = phrase[7:]
print(word2)

every_third = phrase[::3]
print(every_third)


#დავალება4
text = "PythonSlicing"
first_six = text[:6]
print(first_six)

reversed_text = text[::-1]
print(reversed_text)

every_second = text[::2]
print(every_second)


#დავალება5
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
even_indices = letters[::2]
print(even_indices)

slice_step = letters[2:7:2]
print(slice_step)

first_five_reversed = letters[:5][::-1]
print(first_five_reversed)


#დავალება6
sentence = "Slicing makes Python powerful"
python_word = sentence[14:20]
print(python_word)

powerful_reversed = sentence[21:][::-1]
print(powerful_reversed)

every_third_char = sentence[::3]
print(every_third_char)