

given_string = input("Enter strings separated by commas :-") 

words = [word for word in given_string.split(",")] 

words.sort()

print(",".join(words))
