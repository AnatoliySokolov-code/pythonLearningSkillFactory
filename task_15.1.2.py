myFile = open('filename.txt', 'rt', encoding="utf8")
print(myFile.read())
myFile = open('filename.txt', 'rt', encoding="utf8")
print(myFile.read(20))
myFile = open('filename.txt', 'rt', encoding="utf8")
print(myFile.readline())
myFile = open('filename.txt', 'rt', encoding="utf8")
print(myFile.readlines())
myFile = open('filename.txt', 'rt', encoding="utf8")
for line in myFile:
    print(line)

