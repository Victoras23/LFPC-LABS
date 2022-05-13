def gramm():
    grammar = [
        'S->A',
        'A->cB',
        'B->Cd',
        'C->D',
        'C->CbD',
        'D->a',
        'D->acCd'
    ]
    terminalSimbols=['a','b','c','d']
    nonTerminalSimbols=['S','A','B','C','D']

    return (grammar, terminalSimbols, nonTerminalSimbols)