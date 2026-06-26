#my_list = [1, 2, 3, 4, 5]
#for i in range(1,6):
#    my_list.append(i)




my_list = [num * 2 for num in range(1,6)]
print(my_list)

name = 'group 96'
split_name = [n for n in name]
print(split_name)



#my_dict = {
#    'name':'demetre',
#    'last_name': 'beridze',
#    'age': 16
#}
#print(my_dict['name'])




#values-დიქტიდან იღებს მხოლოდ VALUE-ებს
#print(my_dict.values())

#keys-დიქტიდან იღებს მხოლოდ KEY-ებს
#print(my_dict.keys())

#items დიქტიდან იღებს KEY & VALUE წყვილებს
#print(my_dict.items())
#print(my_dict)





#tags = ['vaction', 'summer', 'life']
#hashtags = ['#' + item for item in tags]
#for i in hashtags:
#    print(i)




#fruits = ['Pomegranate', 'Banana', 'Pineapple', 'Peach', 'Melon']
#მაგალითი1
#start_with_p = [x for x in fruits if x.startswith('P')]
#print(starts_with_p)
#მაგალითი 2
#filtered = [x for x in fruits if len(x) <= 5]
#print(filtered)



#squared = [{x: x**2 for x in range(1,6)}]
#print(squared)