# we have to find the sum of two list indices that gives t
num=[3,2,4]
t=6
for i in range(2) :
    for j in range (3):
        if i==j:
            continue
        q=num[i]+num[j]
        if q==t:
            print(i,j)
        
        