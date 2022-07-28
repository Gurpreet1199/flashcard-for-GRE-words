import numpy as np
import random
import sys
f=sys.argv[1]
myfile = open(f, 'r')
data_dict = {}
re={}
delim= "->"
for line in myfile:
    data= line.strip().split(delim)
    s=np.array(data[1:])
    cs=""
    for x in s:
        cs=cs+x
    cs=cs.strip()
    data[0]=data[0].strip()
    data_dict[data[0]]=cs
myfile.close()
print("       n for next and m for meaning\n\n\n")
while(True):
    if len(data_dict)==0:
        break
    print("remaining words ",len(data_dict))
    word,meaning =random.choice(list(data_dict.items()))
    print(word)
    option=input("s-> search word by yourself, enter->generate next word , m-> meaning , q-> quit\n")
    if(option == 'm'):
        re[word]=meaning
        print("MEANING OF THE WORD IS -> ",meaning)
        print("\n\n")
    elif(option=='s'):
        x=input("enter word with a space in the end-> ")
        if x not in data_dict:
            print("Word Not Found,, Please enter correct word\n\n")
            continue       
        print(data_dict[x])
        print("\n")
    elif(option=='q'):
       break
    elif(option not in 's','m','q'):
        del data_dict[word]
print("\n\n\t\t\t press 'b' to build new file with words seem more tough else 'q' to quit\n\n")
op= input('enter choice : ')
if(op=='b'):
    with open("retry.txt",'w') as f:
        for k,v in re.items():
            f.write('%s -> %s\n'%(k,v))
