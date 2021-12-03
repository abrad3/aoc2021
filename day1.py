# turn input into list
import pandas as pd
filename = './input.csv'
df = pd.read_csv(filename, header=None)
df.columns=['data']
ls = df['data'].tolist()

# county time
counter=0
for i in range(1, len(ls)):
    if ls[i-1] < ls[i]: counter+=1
print(counter)
