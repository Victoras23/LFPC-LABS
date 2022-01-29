import networkx as nx
import matplotlib.pyplot as plt

Vn=input("enter the Vn : ")
Vt=input("enter the Vt : ")
print("enter the value of P : ")
P=[]
i=-1
while input:
    i=i+1
    P.append(input())
    if P[i].find('}')!=-1:break

points=int(0)
a=Vn.index('{')
b=Vn.index('}')
mx=[]
for i in range(a,b):
    if Vn[i].isalpha(): 
        points+=1
        mx.append(Vn[i])

matrix = [[0 for x in range(points+1)] for y in range(points+1)] 

for i in range(1,points+1):
    matrix[i][0]=mx[i-1]
    matrix[0][i]=mx[i-1]

x=len(P)
edge1=[]
edge2=[]
lg=[]
ind=1
for i in range(1,(x)):
    bool=True
    empty=True
    for j in range (0,len(P[i])):
        if P[i][j].islower() :
            lg.append(P[i][j])
        elif P[i][j].isupper() :
            if bool:
                edge1.append(P[i][j])
                bool=False
            elif P[i][j].isupper():
                edge2.append(P[i][j])
                empty=False
                break
    if empty :
       edge2.append(str(ind))
       ind+=1

for i in range(0 , len(edge2)):
    el1=0
    el2=0
    if edge2[i].isdigit()==False: 
        for j in range(0,len(mx)):
            if edge2[i]==mx[j]:
                el1=j
            if edge1[i]==mx[j]:
                el2=j
        matrix[el1+1][el2+1]=lg[i]

print("\n the matrix \n")
for i in range (points+1):
    print(matrix[i])
print("\n the edges \n")
print(edge1)
print(edge2)
print(lg)
gr=nx.Graph()
gr.add_nodes_from(mx)
for i in range (0, len(edge1)):
    gr.add_edge(edge1[i],edge2[i],length=lg[i])
pos = nx.spring_layout(gr)
nx.draw_networkx(gr,pos)
nx.draw_networkx_edge_labels(gr, pos)
plt.show()