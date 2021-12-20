# https://rosalind.info/problems/ba3f/
'''
Input: An integer k followed by a list of k-mers Patterns.
Output: A string Text with k-mer composition equal to Patterns. 

'''
#steps: 
'''
1. form a deBruijn Graph from given reads
2. find eularian path from the graph (traverses all edges once)
3. path to genome!
'''
with open('dataset_203_7.txt', 'r') as file:
    kmers=list(line.strip() for line in file)

graph_={}

#graph_ is dictionary with kmers
graph_[kmers[0][:-1]]=[kmers[0][1:]]
for j in range(1,len(kmers)):
    if kmers[j][:-1] not in graph_.keys():
        graph_[kmers[j][:-1]]=[kmers[j][1:]]
    else:
        graph_[kmers[j][:-1]].append(kmers[j][1:])

#Snodes= list of all possible unique string nodes of graph_ ("CTT"->"TTA" and so)
Snodes=list(graph_.values())
Snodes = [item for sublist in Snodes for item in sublist]
for i in list(graph_.keys()):
	if i not in Snodes:
		Snodes.append(i)


#map_ gives a value to every element of Snode
#"CCT":"0", "TTA":"1".. 
map_={}
for i in range(len(Snodes)):
    map_[Snodes[i]]=str(i)



#graph is same dictionary as graph_ but with numberic nodes
graph={}

for i in range(len(list(graph_.keys()))):
    graph[map_[list(graph_.keys())[i]]]= [ (map_[(graph_[list(graph_.keys())[i]])[j]]) for j in range(len(graph_[list(graph_.keys())[i]]))]


nodes=list(graph.values())
nodes = [item for sublist in nodes for item in sublist]
for i in list(graph.keys()):
	if i not in nodes:
		nodes.append(i)
       
adj_mx=[[0 for i in range(len(nodes))] for j in range(len(nodes))]

for i in nodes:
    for j in nodes:
        try:
            if j in graph[i]:
               adj_mx[int(i)][int(j)]=1
        except:
            continue

def unvisited_edge(adj_mx):
    for i in range(len(adj_mx)):
        for j in range(len(adj_mx)):
            if adj_mx[i][j]==1:
                return True
            else:
                continue
    return False
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


eularian_pathS=[ "" for i in range(len(eularian_path))]

def getKeyFromValue(val):
    for key, value in map_.items():
        if val == value:
            return key
 
    return "key doesn't exist"
for i in range(len(eularian_path)):
    eularian_pathS[i]=getKeyFromValue(str(eularian_path[i]))

genome=eularian_pathS[0]
for i in range(1,len(eularian_pathS)):
    genome=genome+eularian_pathS[i][-1]

f=open("finalOutput.txt","w")
f.write(genome)
f.close()
import atexit

atexit.register(print,"Program exited successfully!") 
