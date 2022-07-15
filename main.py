def bomb(b,r,c):
    field = [['O' for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            if b[i][j] == 'O':
                field[i][j] = '.'
                if j+1<c:
                    field[i][j+1] = '.'
                if i+1<r:
                    field[i+1][j] = '.'
                if j>0:
                    field[i][j-1] = '.'    
                if i>0:
                    field[i-1][j] = '.'

    return field
    
r,c,n = input().split()
r,c,n = int(r),int(c),int(n)
b = []

for i in range(r):
        row = list(input())
        b.append(row)
        
if n%2==0:
    f = [['O' for i in range(c)] for j in range(r)] 
    for i in range(r):
        print(''.join(map(str,f[i])))
else:
    bombed = bomb(b,r,c)               
    bombedd = bomb(bombed,r,c)  
    
    if n==1:
        for i in range(r):
            print(''.join(map(str,b[i])))
    elif (n+1)%4==0:
        for i in range(r):
            print(''.join(map(str,bombed[i])))
    elif (n+2)%4==0:
        for i in range(r):
            print(''.join(map(str,b[i])))
    else:
        for i in range(r):
            print(''.join(map(str,bombedd[i])))