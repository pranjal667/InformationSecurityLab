from telnetlib import theNULL


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cypherText = ['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']

#for encryption:
word = input("enter a word: ")
print(word)
b = word.lower()
print(b)
 
def split(b):
    return [char for char in b]
a = split(b)


for i in range(0,len(b)):
    for j in range(0,26):
        if a[i] == alphabet[j]:
            a[i] = cypherText[j]
        else:
            j = j + 1
    i = i + 1

print(a)    

#for decryption:
print('Do you want to decrypt it? Press y/n and enter.')
c =  input()
if c == 'y' or 'yes':
    def split(a):
        return [char for char in a]
    a = split(a)


    for i in range(0,len(a)):
        for j in range(0,26):
            if a[i] == cypherText[j]:
                a[i] = alphabet[j]
            else:
                j = j + 1
        i = i + 1

    print(a) 




    
     


