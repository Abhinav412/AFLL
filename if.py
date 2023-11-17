import ply.lex as lex

reserved = {
    'if' : 'IF'
}
tokens = ('IF', 'ID', 'EQ', 'INT', 'COLON', 'GT', 'LT','ASSIGN')

t_IF = r'if'
t_EQ = r'=='
t_COLON = r':'
t_ASSIGN = r'='
t_GT = r'>'
t_LT = r'<'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_INT(t):
    r'\d+'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def lex_analyse(text):
    lexer.input(text)

    while True:
        token = lexer.token()
        if not token:
            break
        print(token)

text=input()
lex_analyse(text)

import ply.yacc as yacc

def p_statement_if(p):
    'statement : IF ID EQ INT COLON ID ASSIGN INT'
    p[0] = ('if', p[2], p[4], p[6], p[8])
def p_statement_if_gt(p):
    'statement : IF ID GT INT COLON ID ASSIGN INT'
    p[0] = ('if-gt', p[2], p[4], p[6], p[8])

def p_statement_if_lt(p):
    'statement : IF ID LT INT COLON ID ASSIGN INT'
    p[0] = ('if-lt', p[2], p[4], p[6], p[8])
    
def p_error(p):
    global syntax_error
    syntax_error = True
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

def parse(input):
    global syntax_error
    syntax_error = False
    result = parser.parse(input, lexer=lexer)
    if syntax_error:
        print("Incorrect Syntax")
    else:
        print("Correct Syntax")
    print(result)

parse(text)