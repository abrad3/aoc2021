import pandas as pd
filename="./input-day3.csv"
df=pd.read_csv(filename, header=None, dtype=str)
df.columns=['data']
ls=df['data'].to_list()

# initialising binary gamma, which I represent with a str
bgamma=""

# two for loops, one to go over each bit
# and an inner one to go through each piece of data
for i in range(0, len(ls[0])):
    counter=0
    for j in range(0, len(ls)):
            counter+=int(ls[j][i])
    # if our counter has a value of over half the number of rows
    # then "1" must be the most common bit value
    if counter >= len(ls)//2: bgamma+="1"
    else: bgamma+="0"

# find the binary value of epsilon by inverting the binary gamma value
bepsilon = "".join(["1" if b == "0" else "0" for b in bgamma])

# convert binary values to base 10
gamma=int(bgamma,2)
epsilon=int(bepsilon,2)

print("the power consumption is: "+str(gamma*epsilon))    
