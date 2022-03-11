import Lexer

file=open("input.lex",'r')
text = file.readline()
while text!='':
    print("\n",text)
    result, error = Lexer.run('<stdin>', text)
    if error: print(error.as_string())
    else: print(result)
    text = file.readline()