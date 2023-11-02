#code for lexer for syntax validation of if statement in python using ply tool
import sys
#defining the tokens
tokens = (
    'IF',
    'ELSE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE'
)
#defining the regular expressions for the tokens
t_IF = r'if'
t_ELSE = r'else'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
#ignoring the spaces
t_ignore = ' \t'
#defining the rule for NUMBER token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
#defining the rule for new line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
#defining the rule for error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
#building the lexer
import ply.lex as lex
lexer = lex.lex()
#reading the input from the file
file = open(sys.argv[0], "r")
data = file.read()
#tokenizing the input
lexer.input(data)
#closing the file
file.close()
#iterating over the tokens
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
