Input = [12,34,56,78,91]
Key = [12,34,56]
Keyword = []
while len(Keyword)<len(Input):
    if len(Input)-len(Keyword)<len(Key):
        n = len(Input)-len(Keyword)
        Keyword += Key[0:n]
    else:
        n = len(Input)-len(Key)
        Keyword += Key[0:n+2]
print(Keyword)