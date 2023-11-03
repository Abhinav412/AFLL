import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = ('IF', 'ELIF', 'ELSE', 'COLON', 'INDENT', 'DEDENT', 'NAME', 'EQUALS', 'NUMBER', 'LPAREN', 'RPAREN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LT', 'GT', 'EQ', 'NEQ', 'LE', 'GE', 'AND', 'OR', 'NOT', 'NEWLINE')

# Regular expression rules for simple tokens
t_IF = r'if'
t_ELIF = r'elif'
t_ELSE = r'else'
t_COLON = r':'
t_INDENT = r'\t'
t_DEDENT = r'\n'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQUALS = r'='
t_NUMBER = r'\d+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_GT = r'>'
t_EQ = r'=='
t_NEQ = r'!='
t_LE = r'<='
t_GE = r'>='
t_AND = r'and'
t_OR = r'or'
t_NOT = r'not'
t_NEWLINE = r'\n'

# Parsing rules
def p_statement_if(p):
    'statement : IF expression COLON NEWLINE INDENT statements DEDENT'

def p_statement_elif(p):
    'statement : ELIF expression COLON NEWLINE INDENT statements DEDENT'

def p_statement_else(p):
    'statement : ELSE COLON NEWLINE INDENT statements DEDENT'

# Parsing rules
# Parsing rules
def p_statements(p):
    '''statements : statement
                  | statement statements
                  | empty'''

def p_empty(p):
    'empty :'
    pass

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression AND expression
                  | expression OR expression
                  | NOT expression
                  | expression EQ expression
                  | expression NEQ expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | NAME
                  | NUMBER
                  | LPAREN expression RPAREN'''

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

while True:
    try:
        s = input('Enter a Python if statement > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)