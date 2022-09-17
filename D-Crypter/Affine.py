#Taking the input of encrypted text and then making it all upper text to avoid any unnecessary errors.
EncStr = str(input("Enter the encrypted text: "))
EncStr = EncStr.upper()

#Making a list of alphabets which will act as the decryption as well as encryption grid
StrLi = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Appending the index values from String List by checking at which index each character of encrypted string lies in String List
EncLi = []
for i in EncStr:
    EncLi.append(StrLi.index(i))

#Taking input of 2 keys 'a' and 'b'. 'a' and 'm' should be coprime(m=26[no. of alphabets])
a = eval(input("Enter the key 'a': "))
b = eval(input("Enter the key 'b': "))

#Applying the formula: a^-1(x-b)mod m. To get the numbers with which encryption will be performed.
DecLi = []
for i in EncLi:
    DecLi.append(pow(a,-1,26)*(i-b)%26)

#Adding letters to the Decrypted string by finding them in the StrLi according to the Decrypted List by looking up the indexes.
DecStr = ""
for i in DecLi:
    DecStr+=StrLi[i]

print(f"Decrypted Text is: {DecStr}")