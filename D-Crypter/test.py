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
print(len(KeyLi))