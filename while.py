import ply.lex as lex
import ply.yacc as yacc

# List of reserved words
reserved = {
    'while': 'WHILE',
    'n': 'N',
}

# List of token names
tokens = ('WHILE', 'ID', 'LT','GT','EQ', 'NUMBER', 'COLON', 'N','TRUE')

# Regular expression rules for simple tokens
t_WHILE = r'while'
t_LT = r'<'
t_GT = r'>'
t_EQ = r'='
t_COLON = r':'
t_TRUE = r'TRUE'
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
def p_while_loop(p):
    '''while_loop : WHILE ID LT NUMBER COLON
                  | WHILE ID LT N COLON
                  | WHILE ID GT NUMBER COLON
                  | WHILE ID GT N COLON
                  | WHILE ID EQ NUMBER COLON
                  | WHILE ID EQ N COLON
                  | WHILE NUMBER GT ID COLON
                  | WHILE NUMBER LT ID COLON
                  | WHILE NUMBER EQ ID COLON
                  | WHILE N GT ID COLON
                  | WHILE N LT ID COLON
                  | WHILE N EQ ID COLON
                  | while_true'''
    print("While loop syntax is correct.")

def p_while_true(p):
    '''while_true : WHILE TRUE COLON'''
    print("While loop syntax is correct.")

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
    print(tok)

# Parse the data
result = parser.parse(data)