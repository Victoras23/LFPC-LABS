import Grammar
from FirstAndLast import FirstAndLast 
from SimplePrecedence import SimplePrecedence
from ParsingWord import ParsingWord

g = Grammar

grammar=[]
terminalSimbols=[]
nonTerminalSimbols=[]
grammar, terminalSimbols, nonTerminalSimbols=g.gramm()

fl=FirstAndLast(grammar,terminalSimbols,nonTerminalSimbols)
dict,index,first,last=fl.pFirstAndLast()

sp=SimplePrecedence(terminalSimbols,nonTerminalSimbols,dict,index,first,last)
matrix,allSymbols=sp.printMatrix()

word="cabacadd"

po=ParsingWord(matrix,allSymbols,word,grammar)
