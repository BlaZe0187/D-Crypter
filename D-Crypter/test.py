PolybiusList = [['A','B','C','D','E'],['F','G','H','I,J','K'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']]
C = '23331223112432112422113314452345'
Li = []
for i in C:
    i = int(i)
    Li.append(i)
print(Li)
Result = ''
for i in range(0,len(C),2):
    print(i)
    R,C = Li[i],Li[i+1]
    Result += PolybiusList[R-1][C-1]

L1 = [1,2]
L2 = [2,3]
NL = [L1,L2]
print(NL)