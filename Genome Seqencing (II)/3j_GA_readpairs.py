# https://rosalind.info/problems/ba3j/
'''
Input: Integers k and d followed by a collection of paired k-mers PairedReads (un ordered).
Output: A string Text with (k, d)-mer composition equal to PairedReads.
'''
# algo
'''
1. make path from pairedReads
2. Shorten path by making deBruijn Graph
3. Find all Eularian paths and allow only the one which leads to matching PrefixString and SuffixString 
'''

lines = open("input_read_pairs_ga.txt","r").read().splitlines()
lines = lines[1:]
paired_kmers = [ ["" for i in range(2)] for i in range(len(lines))]
k=50 #lazy :p
d=200
for i in range(len(lines)):
    paired_kmers[i][0] += lines[i][0:k]
    paired_kmers[i][1] += lines[i][k+1:]

# indx of read_pair in paired_kmers will be its index in adj_mx

adj_mx = [[0 for i in range(len(paired_kmers))] for j in range(len(paired_kmers))]

for i in range(len(paired_kmers)):
    for j in range(len(paired_kmers)):
        if i!=j:
            prefix1 = [paired_kmers[i][0][:-1], paired_kmers[i][1][:-1]] 
            suffix2 = [paired_kmers[j][0][1:], paired_kmers[j][1][1:]]
    
            if suffix2==prefix1:
                adj_mx[j][i]+=1

        else:
            continue


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

eularian_path = eularianPath(adj_mx)
for i in range(len(eularian_path)):
    eularian_path[i] = paired_kmers[eularian_path[i]]

PrefixString = ""
SuffixString = ""

for i in range(len(eularian_path)):
    if i==0:
        PrefixString+=eularian_path[i][0]
        SuffixString+=eularian_path[i][1]
    else:
        PrefixString+=eularian_path[i][0][-1]
        SuffixString+=eularian_path[i][1][-1]

finalString=""
c=0


for i in range(k+d,len(PrefixString)):
    if PrefixString[i]!=SuffixString[i-k-d]:
        
        print(PrefixString[i],">>",SuffixString[i-k-d])
        print("there is no string spelled by the gapped patterns")
        c=1
        break
    else:
        continue

if c==0:
    finalString= finalString + PrefixString
    finalString= finalString + SuffixString[len(SuffixString)-k-d:]


f2 = open('output_read_pairs_ga.txt',"w")
f2.write(finalString)
