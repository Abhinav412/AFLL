import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'def' : 'DEF',
    'if'  : 'IF',
    'else': 'ELSE'
}
# List of token names
tokens = (
    'DEF',
    'ID',
    'LPAREN',
    'RPAREN',
    'COLON',
    'COMMA'
)

# Regular expression rules for simple tokens
t_DEF = r'def'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','
t_ignore = ' \t'

# A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_function_definition(p):
    'function : DEF ID LPAREN parameter_list RPAREN COLON'
    print("Function definition is syntactically correct.")

def p_parameter_list(p):
    '''
    parameter_list : parameter_list COMMA ID
                   | ID
                   | empty
    '''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test it out
data = input()

# Give the data to the lexer
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break

# Parse the data
result = parser.parse(data)