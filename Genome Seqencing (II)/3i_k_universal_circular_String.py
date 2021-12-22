k=int(input())

def produce_kmers(k):
    a = "0b"+"0"*k
    l=[a]
    b="0b"+("0"*(k-1))+"1"
    while a!="0b"+"1"*k:
        a = bin(int(a,2)+int(b,2))
        l.append(a)

    l = [ i[2:] for i in l]
    l = [ "0"*(k-len(i))+i for i in l ]
    return l

kmers = produce_kmers(k)
# building deBruijn Graph

overlaps = produce_kmers(k-1)  # nodes

adj_mx = [ [0 for i in range(len(overlaps))] for j in range(len(overlaps))]
for i in kmers:
    # if i[1:] and i[:-1] in overlaps:
    adj_mx[overlaps.index(i[:-1])][overlaps.index(i[1:])]+=1

#finding eularian cycle

def check(adj_mx):
    c=[0 for i in range(len(adj_mx))]

    for i in range(len(adj_mx)):
        for j in range(len(adj_mx)):
            c[i]=c[i]+adj_mx[i][j]

    for j in range(len(adj_mx)):
        for i in range(len(adj_mx)):
            c[j]=c[j]-adj_mx[i][j]

    return c


c=check(adj_mx)
s=0
e=0
for i in range(len(c)): 
    if c[i]==-1:
        e=i
    if c[i]==1:
        s=i

def eularianPath(adj_mx):
    
    stack=[]
    path=[]
    stack.append(s)

    while(len(stack)!=0):

        v=stack[-1]
        
        for j in range(len(adj_mx)):
            d=0
            if adj_mx[v][j]==1:
                d=d+1
                stack.append(j)
                adj_mx[v][j]=0
                v=j
                break
            
        if d==0:
            # degree(v)=0
            path.append(v)
            del stack[-1]

        
                
    return path[::-1]

    #s- starting node, e= ending node

eularian_path=eularianPath(adj_mx)




eularian_path  = [ overlaps[i]  for i in eularian_path]



for i in range(len(eularian_path)):
    if i==0:
        continue
    else:
        eularian_path[i] = eularian_path[i][-1]

s= ""
for i in eularian_path:
    s=s+i
print(s[:-2])
