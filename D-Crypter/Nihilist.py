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
    i = int(i)
    CipherLi.append(i)

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
    elif i in Row2:
        R += '1'
        C = Row2.index(i)
        C = C+1
    elif i in Row3:
        R += '1'
        C = Row3.index(i)
        C = C+1
    elif i in Row4:
        R += '1'
        C = Row4.index(i)
        C = C+1
    elif i in Row5:
        R += '1'
        C = Row5.index(i)
        C = C+1
    R = int(R)
    C = int(C)
    Key.append(R)
    Key.append(C)

