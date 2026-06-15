# დავალება 2
#  ==(უდრის)
5 == 5
10 == 3
#  !=(არ უდრის)
7 != 7
4 != 4
#  >(მეტობა)
15 > 10
7 > 190
#  <(ნაკლებობა)
3 < 9
12 < 5
#  >=(მეტია ან ტოლია)
6 >= 6
4 >= 10
#  <=(ნაკლებია ან ტოლია)
5 <= 8
7 <= 2

#დავალება 3
# AND - თუ მთლიან მაგალითში ერთო true თუ ურევია ამშინ გამოიტანს false.
# OR - თუ ორივე პირობა მცდარია მაშინ დააბრუნებს false.

# დავალება 4
my_height = 170
user_height = int(input('შემოიტანეთ თქვენი სიმაღლე სანტიმეტრებში: '))
if user_height > my_height:
    print('თქვენ ემზე მაღალი ხართ! ')
else:
    print('თქვენ არ ხართ ჩემზე მაღალი')

#დავალება 5
num1 = "21"
num2 = 21
print(num1 == num2)
#num1 არის ტექსტური ტიპის და num2 არის მტელი რიცხვითი ტიპი. == ოპერატორი ადარებს როგორც მნიშვენელობას ისე ტიპს და სხვადასხვა ტიპები ერთმანეთს ვერ გაუტოლდებიან.

#დავალება 6
my_last_name == 'ana'
user_last_name == input('შემოიტანეთ თქვენი გვარი:' )


#დავალება 7
print(False or True and True and False)   # False
print(True and False or False or True)    # True
print(True or True and False or True or False and True or False)  # True


# დაავალება 8
temperature = float(input( 'შემოიტანეთ სახლის ტემპერატურა:'))
if temperature > 30 or False:
    print('გაგრილების სისტემა ავტომატურად ჩაირთო')
else:
    print('ტემპერატურა ნორმალურია.სისტემა გამორთულია.')


#დავალება 9
celsius = float(input('შემოიტანეთ ოთახის ტემპერატურა ცელსიუსში: '))
fahrenheit = (celsius*9/5) + 32
if fahrenheit > 89.6:
    print(f'ტემპერატურა:{fahrenheit} გაგრილების სისტემა ცაირტო')
else:
    print(f'ტემპერატურა:{fahrenheit} გაგრილების სისტემა გამოირთო')

