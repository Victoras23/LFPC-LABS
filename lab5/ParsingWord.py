import matplotlib.pyplot as mp
import networkx as nt

class ParsingWord:
    def __init__(self, matrix, allSymbols, word, grammar):
        self.matrix=matrix
        self.Symbols=allSymbols
        self.Symbols['$']=len(self.Symbols)+1
        self.word='$'+word+'$'
        self.grammar=grammar
        self.dict=self.NewDict()
        self.g=nt.Graph()
        self.modifyWord()

    def NewDict(self):
        dict={}
        for line in self.grammar:
            string=line.split("->")
            value=string[0]
            key=''
            for i in range(len(string[1])):
                key+=string[1][i]
                if i!=len(string[1])-1:
                    key+='='
            dict[key]=value
        return dict

    def modifyWord(self):
        print("\nParsing Word :\n")
        word=''
        for i in range (1,len(self.word)):
            word+=(self.word[i-1])
            word+=(self.matrix[self.Symbols[self.word[i-1]]][self.Symbols[self.word[i]]])
        word+=(self.word[len(self.word)-1])
        print(word)

        while word[2]!="S":
            for key in self.dict.keys():
                place=0
                l1=[]
                l2=[]
                dir=[]
                l3=[]
                while word.find(key,place+1)!=-1:
                    place=word.find(key,place+1)
                    lsign=self.matrix[self.Symbols[word[place-2]]][self.Symbols[self.dict[key][0]]]
                    rsign=self.matrix[self.Symbols[self.dict[key][len(self.dict[key])-1]]][self.Symbols[word[place+len(key)+1]]]
                    if rsign=='=' and lsign=='=':
                        l1.append(place)
                    elif rsign=='=' or lsign=='=':
                        if rsign!=' ' and lsign!=' ':
                            l2.append(place)
                            if rsign=='=':
                                dir.append("<")
                            else:
                                dir.append(">")
                    else :
                        l3.append(place)

                if len(l1)>0:
                    for i in l1:
                        findex=i+len(key)
                        rep=word[i-1]+key+word[findex]
                        newWord=word.split(rep,1)
                        word=newWord[0]+"="+self.dict[key]+"="+newWord[1]
                elif len(l2)>0:
                    for i in range (len(l2)):
                        findex=l2[i]+len(key)
                        rep=word[l2[i]-1]+key+word[findex]
                        newWord=word.split(rep,1)
                        if dir[i]=="<":
                            word=newWord[0]+"<"+self.dict[key]+"="+newWord[1]
                        else :
                            word=newWord[0]+"="+self.dict[key]+">"+newWord[1]
                elif len(l3)>0:
                    for i in l3:
                        findex=i+len(key)
                        rep=word[i-1]+key+word[findex]
                        newWord=word.split(rep,1)
                        word=newWord[0]+"<"+self.dict[key]+">"+newWord[1]
            print(word)
