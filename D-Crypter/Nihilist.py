print('''Steps to enter the Decryption Grid:
Type the rows one-by-one as a list which will then act as the grid used for DecryptionGrid.
Note: Keep I & J in the same cell as "I,J"''')
Row1 = eval(input("Row1:"))
Row2 = eval(input("Row2:"))
Row3 = eval(input("Row3:"))
Row4 = eval(input("Row4:"))
Row5 = eval(input("Row5:"))

'''Making DecryptionGrid(Nested List) by utilising the lists entered before'''
DecryptionGrid = [Row1,Row2,Row3,Row4,Row5]

'''Entering the Ciphertext(Numbers), Converting them to integer type and making a List out of them.'''
Input = input("Enter ciphertext:")
CipherLi = []
for i in Input:
    CipherLi.append(i)

for i in range(0,len(CipherLi)):
    CipherLi[i:i+2] = [''.join(CipherLi[i:i+2])]

for i in range(0,len(CipherLi)//2):
    CipherLi.pop()

DoubledCipherLi = []
for i in CipherLi:
    i = int(i)
    DoubledCipherLi.append(i)

'''Entering the Key and making a List out of it'''
Key = input("Enter key:")
Key = Key.upper()
KeyLi = []
for i in Key:
    R = ''
    C = ''
    if i in Row1:
        R += '1'
        C = Row1.index(i)
        C = C+1
        C = str(C)
    elif i in Row2:
        R += '2'
        C = Row2.index(i)
        C = C+1
        C = str(C)
    elif i in Row3:
        R += '3'
        C = Row3.index(i)
        C = C+1
        C = str(C)
    elif i in Row4:
        R += '4'
        C = Row4.index(i)
        C = C+1
        C = str(C)
    elif i in Row5:
        R += '5'
        C = Row5.index(i)
        C = C+1
        C = str(C)
    KeyLi.append(R)
    KeyLi.append(C)

for i in range(0,len(KeyLi)):
    KeyLi[i:i+2] = [''.join(KeyLi[i:i+2])]

for i in range(0,len(KeyLi)//2):
    KeyLi.pop()

DoubledKeyLi = []
for i in KeyLi:
    i = int(i)
    DoubledKeyLi.append(i)
'''The DoubledLists are created such that Decryption could take place as Each Element of Input taken Two at a time must be
Subtracted by the Key to get the CIPHERTEXT'''

'''Decryption:
Nihilist cipher works Similar to Polybius cipher the only major difference being here is that Nihilist cipher is Double
Encrypted so as to make the decryption a bit tricky than the normal Polybius.
To Decrypt it we follow the following steps:
1) First we break the input Ciphertext in parts of two(Set of Coordinates in the Grid).
2) We convert the given Key to Numbers by using the given Grid and also break it in parts of Two.
3) We make a KeywordList from the Key ,such that, we repeat the Key until the length of KeywordList Becomes Equal to that
of the CipherList.
4) After this, Corresponding Elements of CipherList are Subtracted from the Elements of Keyword, so as to get the Final
Ciphertext.
5) Final Ciphertext is completely splitted ,i.e., no Two numbers are Grouped for ease of decryption.
6) Now the Ciphertext is deciphered using the Grid provided just like PolybiusCipher.
Ex: Ciphertext: 577066392880
    Key: CODE
    Key after coding on the basis of Grid: 13351415
    Keyword: 133514151335
    Final Ciphertext: [57 70 66 39 28 80]-[13 35 14 15 13 35]=443552241545
    Decrypted text: SOVIET'''

'''Making the Keyword by Repeating the Key so as to Satisfy/Equal to the length of the Ciphertext/Input'''
Keyword = []
while len(Keyword)<len(DoubledCipherLi):
    if len(DoubledCipherLi)-len(Keyword)<len(DoubledKeyLi):
        n = len(DoubledCipherLi)-len(Keyword)
        Keyword += DoubledKeyLi[0:n]
    else:
        n = len(DoubledCipherLi)-len(DoubledKeyLi)
        Keyword += DoubledKeyLi[0:n+2]

'''Refreshing the cipher list to get the final Ciphertext by Subtracting each Corresponding Element of DoubledCipherList
to KeywordList'''
CipherLi = []

for i in range(0,len(DoubledCipherLi)):
    n = DoubledCipherLi[i]-Keyword[i]
    CipherLi.append(n)

'''Making final list to get the Ciphertext Separated so we could Decrypt it by using the provided Grid'''
CiLi = []

for i in CipherLi:
    R = i//10
    C = i%10
    CiLi.append(R)
    CiLi.append(C)

'''Decrypting the CipherList(Same as PolybiusCipher'''
Result = ''
for i in range(0,len(CiLi),2):
    R,C = CiLi[i],CiLi[i+1]
    print(R,C)
    Result += DecryptionGrid[R-1][C-1]
print("Deciphered text:",Result)