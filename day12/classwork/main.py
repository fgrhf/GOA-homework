#დავალება1
number = int(input("შემოიტანეთ ნებისმიერი რიცხვი: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
    #დავალება2
correct_password = "python123"
while True:
    user_password = input("შემოიტანეთ პაროლი: ")

    if user_password == correct_password:
        print("Access granted")
        break  
    else:
        print("Wrong password, try again")
#დავალება 3
fruits = ["banana", "apple", "orange", "mango", "cherry"]
print("მეორე წევრი:", fruits[1])  # apple
print("მესამე წევრი:", fruits[2])  # orange
print("მეხუთე წევრი:", fruits[4])  # cherry