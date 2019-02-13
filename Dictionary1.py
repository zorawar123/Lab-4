word = open("file.txt.txt","r") 
def create_word_dict(f):
    d = dict()
    D = {}
    for line in f:
        line = line.strip(' *')
        lines = line.split()
        for k  in line:
            d[k]  = d.get(k,1) + 2
        for i in d:
            print(i, d[i])    

       
       
print(create_word_dict(word))