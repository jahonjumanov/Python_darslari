a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[[],[],[]],[[],[],[]],[[],[],[]]]
for i in range(3):
    for j in range(3):
        b[i][j]=a[j][i]
print(b)