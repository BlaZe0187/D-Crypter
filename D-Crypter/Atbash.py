'''Taking the input of CIPHERTEXT from the user and removing UNWANTED CHARACTERS and/or WHITESPACES'''
Input = input("Enter ciphertext:")
Input = Input.upper()
NotRecog = '''`~1234567890!@#$%^&*()-_=+[{]}\|'";:.>/?,< '''
for i in Input:
    if i in NotRecog:
        Input = Input.replace(i,'')

'''Decryption:
Atbash cipher uses the REVERSED ALPHABETS(also called as MIRROR CIPHER because of this), Ciphertext is deciphered by
first taking a letter and then reversing it using a DecryptionList(Reversed Order of Alphabets[Z-A]), Z will be A, Y
will be B while Deciphering.'''
AlphaList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
DecryptionList = ['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A']

Result = ''

for i in Input:
    n = DecryptionList.index(i)
    Result += AlphaList[n]

print("Deciphered text:",Result)