# https://rosalind.info/problems/ba3d/

fobj=open("qr.txt","r")

#collecting data
kmers=fobj.readlines()
for i in range(len(kmers)):
    kmers[i]=kmers[i][:-1]

#creating nodes as the k-1 mers but only unique
#uniqueness ensure gluing of nodes
nodes=set()
for i in range(len(kmers)):
    nodes.add(kmers[i][1:])
    nodes.add(kmers[i][:-1])
nodes=list(nodes)

f2=open("o.txt","a")
#print(nodes)
for i in range(len(nodes)):
    c=0
    f2.write(nodes[i]+" -> ")
    for j in range(len(nodes)):
        if nodes[i][1:]==nodes[j][:-1] and nodes[i]+nodes[j][-1] in kmers:
            
            c+=1
            if c==1:
                f2.write(nodes[j])
            
            if c>1:
                f2.write(","+nodes[j])

    f2.write('\n')

f2.close()
fobj.close()
