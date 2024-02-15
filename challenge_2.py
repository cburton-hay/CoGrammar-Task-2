string_fav = input("What's your favourite restaurant?")
int_fav = input("What's your favourite number?")
int_fav = int(int_fav)
print(string_fav)
print(int_fav) # Printed successfully with 'Well Kneaded' and '13'
string_fav = int(string_fav) # Error because the string uses the alphabet instead of numerals, therefore has no numerical value.