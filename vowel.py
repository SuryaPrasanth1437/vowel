vowel=['a','e','i','o','u']
char=input()
if char.isalpha():
    if char in vowel:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
