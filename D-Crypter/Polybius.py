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
NumLi = []
for i in Input:
    i = int(i)
    NumLi.append(i)

'''Decryption:
Polybius cipher uses a Grid which can be Randomised to Encrypt LETTERS as NUMBERS. This grid contains 25 cells(I & J are
usually grouped together to save space) which can also be increased depending on the number of letters the language used
has.
We can think of the Grid as a Graphical Plane and the Rows as X-axis & Columns as Y-axis and finally the Letters Inside
the Grid as the point that are on the graph. Then we split the ciphertext into parts of 2 out of which first one is RowNum
and second one is ColumnNum which will then Point/Lead to the deciphered letter.
Ex: Ciphertext: 351332542114
    Deciphered text: POLYBE'''
Result = ''
for i in range(0,len(Input),2):
    R,C = NumLi[i],NumLi[i+1]
    Result += DecryptionGrid[R-1][C-1]
print("Deciphered text:",Result)