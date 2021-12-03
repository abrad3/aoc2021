import pandas as pd
filename="./input-day2.csv"
df=pd.read_csv(filename, header=None)
df.columns=['dir']
ls=df['dir'].to_list()
pos=0
depth=0

for i in range(0, len(ls)):
    direction = ls[i][0]
    # down
    if direction == 'd':
        dist = int(ls[i][5:])
        depth+=1
    # up
    elif direction == 'u':
        dist = int(ls[i][3:])
        depth-=1
    # forward
    elif direction == 'f':
        dist = int(ls[i][8:])
        pos+=1
    else: 
        print(direction)
        print(direction=='d')
        print("oh no! What kind of direction are you going?!")
print("depth is: "+str(depth))
print("horizontal position is: "+str(pos))
print("so puzzle answer is..."+str(depth*pos))
