import networkx as nx
import matplotlib.pyplot as plt

print('the input should be like :')
print('enter the Vn : VN={S, A, B, C}, \nenter the Vt : VT={a, b}, \nenter the value of P :P={ \n1. S  bA \n2. A  b \n3. A aB \n4. B  bC \n5. C  cA \n6. A  bA \n7. B  aB }')
print('\nYou can get the inputs from the txt file in this repository \n')

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


x=len(P)
edge1=[]
edge2=[]
type=True
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
print("\n the edges \n")
print(edge1)
print(edge2)
print(lg)


string=''
start=edge1[0]
nr=1
nodes=0
way=edge1[0]
labeldict = {}
gr=nx.Graph()
for i in range (0, len(mx)+7):
    for j in range (0,len(edge1)):
        if edge1[j]==start and edge2[j].isdigit()==False :
            string+=lg[j]
            start=edge2[j]
            way+=' => '
            way+=lg[j]
            way+=edge2[j]
            gr.add_edge(nodes,nodes+1)
            gr.add_edge(nodes,nodes+20)
            labeldict[nodes] = edge1[j]
            labeldict[nodes+1] = edge2[j]
            labeldict[nodes+20] = lg[j]
            nodes+=1
            break
    if len(string)>(len(mx)+2):
        print("string ",nr+0," : " , string)
        print("derivation table",way)
        nr+=1
        #nx.draw(gr, labels=labeldict, with_labels = True)
        #plt.show()

grx=nx.Graph()
grx.add_nodes_from(mx)
l1={}
l1[edge1[0]]='q0'
sq='q'
di=1
isfinal=0
for i in range (0, len(edge1)):
    grx.add_edge(edge1[i],edge2[i],length=lg[i])
    if edge2[i].isdigit():
        l1[edge2[i]]=sq+str(di)
        di+=1
        isfinal+=1
    elif (edge2[i] in l1.keys())==False:
        l1[edge2[i]]=sq+str(di)
        di+=1
pos = nx.spring_layout(grx)
nx.draw_networkx(grx,pos, labels=l1, with_labels = True )
nx.draw_networkx_edge_labels(grx, pos)
plt.show()

a=Vt.index('{')
b=Vt.index('}')
mt=[]
points1=0

for i in range(a,b):
    if Vt[i].isalpha(): 
        points1+=1
        mt.append(Vt[i])

matrix = [[0 for x in range(points1+1)] for y in range(points+1)] 

for i in range(1,points+1):
    matrix[i][0]=mx[i-1]

for i in range(1,points1+1):
    matrix[0][i]=mt[i-1]

for i in range(0 , len(edge2)):
    el1=0
    el2=0
    for j in range(1,points+1):
        if edge1[i]==matrix[j][0]:
            el1=j
    for j in range (1,points1+1):
        if lg[i]==matrix[0][j]:
            el2=j
    matrix[el1][el2]=edge2[i]

print("\n the matrix \n")
for i in range (points+1):
    for j in range (points1+1):
        if matrix[i][j] in l1.keys():
            matrix[i][j]=l1[matrix[i][j]]
        else : matrix[i][j]=str(matrix[i][j])
for i in range (points+1):
    print(matrix[i])

if isfinal==0 :
    print("\n Type 2 \n")
else : 
    print("\n Type 3 \n")
