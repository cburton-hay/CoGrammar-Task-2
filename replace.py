sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
space_sentence = sentence.replace("!", " ") #sentence has spaces instead of !
print(space_sentence)
upper_sentence = space_sentence.upper() #sentence in all capitals
print(upper_sentence)
reverse_sentence = space_sentence[::-1] #sentence with spaces backwards
print(reverse_sentence)