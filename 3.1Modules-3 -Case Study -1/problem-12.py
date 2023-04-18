
given_string = input("Enter strings separated by whitespaces :-") 

words = [word for word in given_string.split(" ")] 

unique_words = set(words)

print(" ".join(sorted(list(unique_words))))