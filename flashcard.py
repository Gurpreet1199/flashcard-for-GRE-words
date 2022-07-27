import numpy as np
import random
myfile = open("Word list gre.txt", 'r')
data_dict = {}
delim= "->"
for line in myfile:
    data= line.strip().split("->")
    data_dict[data[0]]=np.array(data[1:])       
 
myfile.close()
print("       n for next and m for meaning\n\n\n")
while(True):
    word,meaning =random.choice(list(data_dict.items()))
    print(word)
    option=input("s-> search word by yourself, n->generate next word , m-> meaning , q-> quit\n")
    if(option=='n'):
        continue
    elif(option == 'm'):
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



 
