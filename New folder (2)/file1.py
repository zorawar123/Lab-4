file = open("file.txt",'r')
for i in file:
    i = i.strip("_")
    print(i)
