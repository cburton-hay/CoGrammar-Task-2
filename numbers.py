number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")
number_3 = input("Enter the third number: ")
number_1 = int(number_1) # Making sure that the numbers are contained as integers.
number_2 = int(number_2)
number_3 = int(number_3)

number_list = [number_1, number_2, number_3] # Creating a list for all three numbers.
#print(number_list) Can use to chec that the list is being created correctly.
total = sum(number_list)

print(total)
print(number_1 - number_2)
print(number_3 * number_1)
print(total/number_3)