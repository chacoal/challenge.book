X=[-1,-1, 0, 1, 1, 1, 0,-1]
Y=[ 0,-1,-1,-1, 0, 1, 1, 1]

def fill(rake, x, y):
    rake[y][x]="."
    for i in range(8):
        nx,ny=x+X[i],y+Y[i]
        if nx>=0 and ny>=0 and ny<len(rake) and nx<len(rake[0]) and rake[ny][nx]=="W":
            fill(rake, nx, ny)

def solve(N,M,rake):
    ans=0
    for y in range(N):
        for x in range(M):
            if rake[y][x]=='W':
                fill(rake, x, y)
                ans+=1
    return ans

rake=[list("W........WW.")
     ,list(".WWW.....WWW")
     ,list("..WW.....WW.")
     ,list(".........WW.")
     ,list(".........W..")
     ,list("..W......W..")
     ,list(".W.W.....WW.")
     ,list("W.W.W.....W.")
     ,list(".W.W......W.")
     ,list("..W.......W.")]
print solve(10,12,rake)
