key = str(input("Enter the key: "))
key = key.upper()

AlphaLi = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

KeyLi = []
for i in key:
    if i not in KeyLi:
        KeyLi.append(i.upper())
for i in range(0,25):
    if AlphaLi[i] not in KeyLi:
        KeyLi.append(AlphaLi[i])

DecGrid = []
st = 0
end = 5
while len(DecGrid)<5:
    Row = []
    for i in range(st,end):
        Row.append(KeyLi[i])
    st+=5
    end+=5
    DecGrid.append(Row)


CipherText = str(input("Enter the ciphertext: "))
OgLen = len(CipherText)
if len(CipherText)/2!=0:
    CipherText+='z'
CipherText = CipherText.upper()
CipherLi = []
st = 0
end = 2
for i in range(0,int(len(CipherText)/2)):
    Row = []
    for i in range(st,end):
        Row.append(CipherText[i])
    st+=2
    end+=2
    CipherLi.append(Row)

CoordLi = []
for i in CipherLi:
    Coord = []
    for j in i:
        for k in DecGrid:
            if j in k:
                Coord.append([DecGrid.index(k),k.index(j)])
    if len(Coord)!=0:
        CoordLi.append(Coord)

DecText = ""
for i in CoordLi:
    if i[0][1]==i[1][1]:
        DecText += f"{DecGrid[i[0][0]-1][i[0][1]]}{DecGrid[i[1][0]-1][i[1][1]]}"
    elif i[0][0]==i[1][0]:
        DecText += f"{DecGrid[i[0][0]][i[0][1]-1]}{DecGrid[i[1][0]][i[1][1]-1]}"
    else:
        DecText += f"{DecGrid[i[0][0]][i[1][1]]}{DecGrid[i[1][0]][i[0][1]]}"

for i in DecText:
    if i=='X' and DecText[DecText.index(i)-1]==DecText[DecText.index(i)+1]:
        DecText = DecText.replace('X','',1)


if OgLen/2!=0:
    print(DecText[0:OgLen-1])
else:
    print(DecText)