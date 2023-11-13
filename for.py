import ply.lex as lex
import ply.yacc as yacc

# List of reserved words
reserved = {
    'for': 'FOR',
    'in': 'IN',
    'range': 'RANGE',
    'n': 'N',
}

# List of token names
tokens = ('FOR','ID','IN','RANGE','COLON','LPAREN','RPAREN','COMMA','NUMBER', 'N')

# Regular expression rules for simple tokens
t_FOR = r'for'
t_IN = r'in'
#t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_COLON = r':'
t_RANGE = r'range'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ignore = ' \t\n'

# Regular expression rule for identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Regular expression rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_for_loop(p):
    '''for_loop : FOR ID IN RANGE LPAREN NUMBER COMMA NUMBER RPAREN COLON
                | FOR ID IN RANGE LPAREN NUMBER COMMA N RPAREN COLON'''
    print("For loop syntax is correct.")

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