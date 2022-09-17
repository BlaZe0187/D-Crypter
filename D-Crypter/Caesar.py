'''Caesar Cipher:Decrypts the given input by using shift of letters(even if the shift isn't known)
Keyed Caesar Cipher:First decrypts the given input on the basis of the key provided then shifts to decrypt and get the result'''

Input = input("Enter:")

#Removes unwanted characters like punctuations and whitespaces
NotRecog = '''`~1234567890!@#$%^&*()-_=+[{]}\|'";:.>/?,< '''
for i in Input:
    if i in NotRecog:
        Input = Input.replace(i,'')

Result = ''
AlphaList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
AskKey = input("Key??(Y/N):")

#Decryption if no key is there
if AskKey.lower()=='n':
    #Shifting to get the deciphered result
    Shift = int(input("Enter shift if known else '0':"))
    if Shift==0:
        #Trying all shifts(not knowing the shift)
        for i in range(1,27):
            Result = ''
            for j in Input:
                n = AlphaList.index(j.upper())
                Result = Result+AlphaList[n-i]
            print(f"Shift={i}:{Result}\n")
    else:
        #Knowing the shift
        for i in Input:
            n = AlphaList.index(i.upper())
            Result = Result+AlphaList[n-Shift]
        print(Result)

#Decryption if a key is used to encode the text
else:
    Key = input("Enter key:")

    #Removing unwanted characters from key like punctuations and whitespaces
    for i in Key:
        if i in NotRecog:
            Key = Key.replace(i,'')
    
    #Creating the wordlist used to encode with the help of key
    KeyedList = ''
    KeyedList = KeyedList+Key.upper()
    for i in AlphaList:
        if i in KeyedList:
            continue
        else:
            KeyedList = KeyedList+i
    
    #Transforming keyed caesar to normal caesar by using KeyedList and getting the text before applying the key
    UnKeyed = ''
    for i in Input:
        n = KeyedList.index(i.upper())
        UnKeyed = UnKeyed+AlphaList[n]
    
    #Shifting to get the deciphered result
    Shift = int(input("Enter shift if known else '0':"))
    if Shift==0:
        #Not knowing the shift
        for i in range(1,27):
            Result = ''
            for j in UnKeyed:
                n = AlphaList.index(j.upper())
                Result = Result+AlphaList[n-i]
            print(f"Shift={i}:{Result}\n")
    else:
        #Knowing the shift
        for i in UnKeyed:
            n = AlphaList.index(i.upper())
            Result = Result+AlphaList[n-Shift]
        print(Result)