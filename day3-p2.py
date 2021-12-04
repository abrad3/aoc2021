import pandas as pd
filename="./input-day3.csv"
df=pd.read_csv(filename, header=None, dtype=str)
df.columns=['data']
ls=df['data'].to_list()

def commonBit(index, l, most):
    counter = 0
    for i in range(0, len(l)):
        counter+=int(l[i][index])
    if counter >= len(l)/2 and most=="True": return "1"
    if counter < len(l)/2 and most=="False": return "1"
    else: return "0"

def bitFilter(l, most):
    result=l
    for i in range(0, len(l[0])):
        result = [ x for x in result if x[i] == commonBit(i, result, most) ]
        if len(result) == 1:
            break
    return result

oxyGen=bitFilter(ls, "True")
co2Scrub=bitFilter(ls, "False")

power=int(oxyGen[0],2)*int(co2Scrub[0],2)
print("The power rating is: "+str(power))
