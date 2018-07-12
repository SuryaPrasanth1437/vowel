vowel=['a','e','i','o','u']
char=input()
if type(char)!=str:
    print("invalid")
else:
    if char in vowel:
        print("Vowel")
    else:
        print("Consonant")
