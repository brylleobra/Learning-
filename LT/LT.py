import csv

def prediction(ds):
    derivative = 0
    while True:
        nt=aRnSum(ds)
        if sum(map(abs,nt)) > sum(map(abs,ds)):
            break
        ds=nt
        derivative+=1
    ds.append(ds[-1])
    for x in range(derivative):
        ds=rnSum(ds)
    return ds

def rnSum(ds):
    rs=[ds[0]]
    for emt in ds[1:]:
        rs.append(rs[-1]+ emt)
    return rs

def aRnSum(ds):
    rs=[ds[0]]
    for x in range(1,len(ds)):
        rs.append(ds[x] - ds[x-1])
    return rs



with open('LT.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='-')

    row=[]
    for i in readCSV:
        row.append(i)
       
    for x in range(0,89):
        print(row[x])

#    print(prediction([24,10,18,40,33,1]))
