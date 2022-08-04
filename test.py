import pandas as pd
import numpy as np
list1 = ["Yatharth",0,25,1,1]
inp = np.array(list1[1:]).reshape(1,-1)
print(inp)
# name,gender,age,class,married
list1 = list(map(str,list1))
datafile = "data.txt" 
with open(datafile,"a") as file:
    file.writelines(",".join(list1) + "\n")