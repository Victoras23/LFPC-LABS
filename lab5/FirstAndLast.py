class FirstAndLast : 
    
    def __init__(self , grammar , terminal , nonTerminal):
        self.grammar=grammar
        self.terminal=terminal
        self.nonTerminal=nonTerminal
        self.dict=self.parseGrammar()
        self.first,self.last,self.index=self.compute()


    def parseGrammar(self):
        fa = {}
        for rulepart in self.grammar:
            x = rulepart.split('->')
            if not x[0] in fa:
                fa[x[0]] = []

            symbols = []
            for symbol in x[1]:
                symbols.append(symbol)
            fa[x[0]].append(symbols)

        return fa
    
    def compute(self):
        index = []
        first = []
        last = []
        for symbol in self.dict:
            index.append(symbol)
            to_find = []
            to_find.append(symbol)
            found = []
            first_symbol = []

            i = 0
            while i < len(to_find):
                if to_find[i] in self.dict:
                    found.append(to_find[i])
                    for rule in self.dict[to_find[i]]:
                        if rule[0] not in first_symbol:
                            first_symbol.append(rule[0])
                        if rule[0] in self.nonTerminal and rule[0] not in found:
                            to_find.append(rule[0])
                i += 1

            first.append(first_symbol)
            to_find = []
            to_find.append(symbol)
            found = []
            last_symbol = []

            i = 0
            while i < len(to_find):
                if to_find[i] in self.dict:
                    found.append(to_find[i])
                    for rule in self.dict[to_find[i]]:
                        if rule[-1] not in last_symbol:
                            last_symbol.append(rule[-1])
                        if rule[-1] in self.nonTerminal and rule[-1] not in found:
                            to_find.append(rule[-1])
                i += 1
            last.append(last_symbol)

        return first , last , index

    def pFirstAndLast(self):
        print("{:>9} {:>19}".format("First","Last"))
        for i in range(5):
            print ("{:<1} : {:<20} {:20}".format(str(self.index[i]),str(self.first[i]),str(self.last[i])))
        return self.dict,self.index,self.first,self.last