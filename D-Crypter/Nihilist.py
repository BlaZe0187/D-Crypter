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

'''Entering the Ciphertext(Numbers), Converting them to integer type and making a NumList out of them.'''
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

'''Entering the Key'''
Key = input("Enter key:")
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

print(DoubledKeyLi)

Keyword = []
while len(Keyword)<len(DoubledCipherLi):
    if len(DoubledCipherLi)-len(Keyword)<len(DoubledKeyLi):
        n = len(DoubledCipherLi)-len(Keyword)
        Keyword += DoubledKeyLi[0:n]
    else:
        n = len(DoubledCipherLi)-len(DoubledKeyLi)
        Keyword += DoubledKeyLi[0:n+2]

print(Keyword)

CipherLi = []

for i in range(0,len(DoubledCipherLi)):
    n = DoubledCipherLi[i]-Keyword[i]
    CipherLi.append(n)

CiLi = []

for i in CipherLi:
    R = i//10
    C = i%10
    CiLi.append(R)
    CiLi.append(C)

print(CiLi)

Result = ''
for i in range(0,len(CiLi),2):
    R,C = CiLi[i],CiLi[i+1]
    print(R,C)
    Result += DecryptionGrid[R-1][C-1]
print("Deciphered text:",Result)