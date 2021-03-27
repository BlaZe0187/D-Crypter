'''Taking the input of CIPHERTEXT from the user and removing UNWANTED CHARACTERS and/or WHITESPACES'''
Input = input("Enter ciphertext:")
Input = Input.upper()
NotRecog = '''`~1234567890!@#$%^&*()-_=+[{]}\|'";:.>/?,< '''
for i in Input:
    if i in NotRecog:
        Input = Input.replace(i,'')

'''Taking the input of KEY from the user and removing UNWANTED CHARACTERS and/or WHITESPACES'''
Key = input("Enter key:")
Key = Key.upper()
NotRecog = '''`~1234567890!@#$%^&*()-_=+[{]}\|'";:.>/?,< '''
for i in Key:
    if i in NotRecog:
        Key = Key.replace(i,'')

'''Making the KEYWORD which will be used to decipher the ciphertext
Keyword is made on the basis of two things:
1) LENGTH of the Ciphertext = Keyword
2) The KEY is REPEATED again and again till the length is statisfied
Ex: Ciphertext: Aeeealuyel
    Key: Hippo
    Keyword:HippoHippo'''
Keyword = ''
for i in range(0,len(Input)):
    if len(Keyword)<=len(Input):
        if len(Input)==len(Key):
            n = len(Input)
            Keyword += Key[0:n]
        elif len(Input)-len(Key)<=len(Input)-len(Keyword):
            n = len(Input)-len(Key)
            Keyword += Key[0:n]
        else:
            n = len(Input)-len(Keyword)
            Keyword += Key[0:n]
    if len(Keyword)==len(Input):
        break

'''Deciphering the Ciphertext using the Keyword and TempLists
The AlphaList and TempLists are reversed,i.e.,A will be Z, B will be Y and so on, This is the main difference between 
Vigenere and Beaufort Cipher'''
AlphaList = ['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A']
Result = ''

'''Creation of TempLists:
TempLists(Required row of letters from vigenere grid) is made on the basis of Caesar shift.
A Beaufort Square has 26 Rows & Columns each labeled as a LETTER of the ALPHABET in ORDER.
Each row is shifted(Caesar Shift) according to the formula: Index/Number of Label Letter-1
Ex: Let the row be Z
    Number of Label Letter: 26
    Shift: 26-1=25
After Shifting the List is reversed on the basis explained above.

Deciphering:
Deciphering is done in 3 steps:
1) A letter of the Keyword is taken
2) Corresponding(Same index/number) Letter of Ciphertext is searched in the row of TempLists
3) After finding the Ciphertext Letter the Column Letter/Index(Check the letter at same index in original AlphaList) is
the Deciphered Letter
Ex: Ciphertext: Aeeealuyel
    Key: Hippo
    Keyword: Hippohippo
    Let letter be H
    Corresponding Letter in Ciphertext: A
    TempList: ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I']
    Location of A in TempList: Index 7
    In AlphaList at Index 7 is H
    ColumnName/Index: H
    Deciphered Letter: H'''
for i in range(0,len(Keyword)):
    TempLi = ['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A']
    if Keyword[i]=='A':
        Result += Input[i]
    else:
        for j in range(0,AlphaList.index(Keyword[i])):
            TempLi+=[TempLi.pop(0)]
        L = Input[i]
        n = TempLi.index(L)
        Result += AlphaList[25-n]

print("Deciphered text:",Result)