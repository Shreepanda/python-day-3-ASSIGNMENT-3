vowels = "aeiou"
statement = input("Enter a statement: ")
num_vowels = 0
num_consonants = 0
for letter in statement.lower():
    if letter.isalpha():
        if letter in vowels:
            num_vowels += 1
        else:
            num_consonants += 1

if num_vowels > num_consonants:
    print("The statement has {} vowels and {} consonants. Vowels have the maximum count.".format(num_vowels, num_consonants))
elif num_consonants > num_vowels:
    print("The statement has {} vowels and {} consonants. Consonants have the maximum count.".format(num_vowels, num_consonants))
else:
    print("The statement has {} vowels and {} consonants. Both have the same count.".format(num_vowels, num_consonants))
