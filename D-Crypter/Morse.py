#Importing json so as to convert the contents of the file to a dictionary
import json

#Opening and storing the data of the file Morse.txt
with open('E:\XxX\D-Crypter\Morse.txt') as f:
    data = f.read()
#Making a JSON object(Dictionary) from the data
MorseDict = json.loads(data)

Input = input("Enter morse code separated with space:")
Input = Input.split()
Result = ''

#Deciphering morse by matching it with dictionary
for i in Input:
    Result = Result+MorseDict[i]
print(Result)