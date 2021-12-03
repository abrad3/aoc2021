import pandas as pd
filename="./input-day3.csv"
df=pd.read_csv(filename, header=None, dtype=str)
df.columns=['data']
ls=df['data'].to_list()
bgamma=""
for i in range(0, len(ls[0])):
    counter=0
    for j in range(0, len(ls)):
            counter+=int(ls[j][i])
    if counter >= len(ls)//2: bgamma+="1"
    else: bgamma+="0"

bepsilon = "".join(["1" if b == "0" else "0" for b in bgamma])
gamma=int(bgamma,2)
epsilon=int(bepsilon,2)
print("the power consumption is: "+str(gamma*epsilon))    
