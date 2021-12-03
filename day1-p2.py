# turn input into list
import pandas as pd
filename = './input.csv'
df = pd.read_csv(filename, header=None)
df.columns=['data']
ls = df['data'].tolist()

# county time
counter=0
for i in range(0, len(ls)):
    chunkA=ls[i:i+3]
    chunkB=ls[i+1:i+4]
    if sum(chunkA) < sum(chunkB): counter+=1
print(counter)
