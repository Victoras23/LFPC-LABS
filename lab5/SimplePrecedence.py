from texttable import Texttable

class SimplePrecedence :
    def __init__(self, terminal, nonterminal , dict, index ,first,last):
        self.terminal=terminal
        self.nonterminal=nonterminal
        self.symbols=nonterminal+terminal
        self.dict=dict
        self.index=index
        self.first=first
        self.last=last
        self.allSymbols=self.createDictionary()
        self.matrix=self.createMatrix()
        self.computeMatrix()
    
    def createDictionary(self):
        dict={}
        index=1
        for i in self.nonterminal:
            dict[i]=index
            index+=1
        for i in self.terminal:
            dict[i]=index
            index+=1
        return dict

    def createMatrix(self):
        matrix= [[" " for x in range(len(self.symbols) + 2)] for y in range(len(self.symbols) + 2)]
        for i in range (len(self.symbols)):
            matrix[0][i+1]=self.symbols[i]
            matrix[i+1][0]=self.symbols[i]
        matrix[len(self.symbols)+1][0]="$"
        matrix[0][len(self.symbols)+1]="$"
        for i in range (len(self.symbols)):
            matrix[len(self.symbols)+1][i+1]="<"
            matrix[i+1][len(self.symbols)+1]=">"
        return matrix

    def computeMatrix(self):
        for key in self.dict:
            for prod in self.dict[key]:
                if len(prod)>1:
                    for idx in range(len(prod) - 1):
                        first_symbol = prod[idx]
                        second_symbol = prod[idx + 1]
                        if first_symbol in self.nonterminal and second_symbol in self.terminal:
                            first_index = self.index.index(first_symbol)
                            for s in self.last[first_index]:
                                if self.matrix[self.allSymbols[s]][self.allSymbols[second_symbol]]:
                                    self.matrix[self.allSymbols[s]][self.allSymbols[second_symbol]]=('>')
                        
                        if second_symbol in self.nonterminal:
                            second_index = self.index.index(second_symbol)
                            for s in self.first[second_index]:
                                if self.matrix[self.allSymbols[first_symbol]][self.allSymbols[s]]:
                                    self.matrix[self.allSymbols[first_symbol]][self.allSymbols[s]]=('<')

                        if self.matrix[self.allSymbols[first_symbol]][self.allSymbols[second_symbol]]:
                            self.matrix[self.allSymbols[first_symbol]][self.allSymbols[second_symbol]]=('=')
                    
    
    def printMatrix(self):
        print()
        print("Simple precedence Matrix")
        print()
        t=Texttable()
        t.add_rows(self.matrix)
        print(t.draw())
        return self.matrix,self.allSymbols

        