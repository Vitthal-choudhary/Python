x = input("Enter a string")
vowel=0
vowels="AEIOUaeiou"
consonant=0
for i in range(len(x)):
    if x[i] in vowels:
        vowel+=1
    else:
        consonant+=1
print("No. of vowels are:\n",vowel)
print("No. of Consonants are:\n",consonant)