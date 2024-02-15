str_manip = input("Enter a short sentence.") #e.g. hello and goodbye
print(len(str_manip)) #length of the sentence
last_letter = str_manip[-1] #what's the last letter in the sentence
rep_word = str_manip.replace(last_letter, "@") #replace all occurances of the last letter with @
print(rep_word)
last_three = str_manip[:-4:-1] #the last 3 letters of the string
print(last_three)
frist_three_letters = str_manip[0:3] #the first 3 letters of the string
last_two_letters = str_manip[-2:]# the last 2 letters of the string
print(frist_three_letters + last_two_letters)