import ply.lex as lex
import ply.yacc as yacc

tokens = ('IF', 'ELIF', 'ELSE', 'FUNC', 'DEF', 'FOR', 'WHILE', 'ID', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA', 'INT', 'FLOAT', 'STRING')

t_IF = r'if'
t_ELIF = r'elif'
t_ELSE = r'else'
t_FUNC = r'def'
t_DEF = r':'
t_FOR = r'for'
t_WHILE = r'while'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COMMA = r','
t_INT = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_STRING = r'\".*?\"'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Parsing rules
def p_start(p):
    '''start : func_def
             | while_stmt
             | for_stmt
             | if_stmt
             | FUNC ID LPAREN params RPAREN COLON block'''

def p_func_def(p):
    '''func_def : FUNC ID LPAREN params RPAREN COLON block'''

def p_while_stmt'''
(p
def):
 p_    '''whilewhile_stmt_stmt( : WHp):
    '''while_stmt :I WHLE conditionI COLONLE condition block''' COLON

 blockdef''' p_

for_def pstmt(_pfor_):
stmt    '''(pfor_):
stmt : FOR ID    IN ''' iterfor_stmt : FOR ID INable iter COLable COLON blockON'''
 block'''
def

 p_defif p_stmt_if(_p):stmt
(p    '''):
if   _ '''ifstmt :_ IF conditionstmt : COL IF conditionON block COL
ON               | block
 IF condition               | COLON IF condition block E COLLIFON condition block E COLONLI blockF condition
               | COLON IF condition block
 COLON               block E | IFLIF condition COL condition COLON block EON block ELSELIF COLON block condition COL'''
ON block
 ELSEdef p COLON block'''_block(

pdef p):
_    '''block(blockp): : L
BRACE    statements ''' Rblock :BRACE''' statement SE
MI

def p             |_params LBR(pACE statements):
 RBR    '''ACE'''params : ID


              | ID COMdef pMA params'''_statements

(pdef p):
_iterable    '''(pstatements):
 :    statement SE '''MI
iter                able : ID
                |  ID COM| statementsMA iter statement SEable'''MI

def'''

 p_def pcondition_statement((p):p):

    '''    '''statement :condition : assign_ expression'''stmt


                 |def p function__call_statementsstmt(p
                ):
 | pass    '''_stmtstatements'''
 : statement
def
                 p_ |assign_ statement statements'''stmt(p

):
    '''def passign__statementstmt :(p ID):
    ASS '''statementIGN value''' : assignment

_stmtdef p
                 |_function while_call_stmt_stmt(p):
                
 | for_stmt
                    ''' | iffunction__stmt
call_stmt                 | func_ : ID Ldef
PAREN                 | block args RPAR
                 | returnEN'''
_stmt
def
                 p_ | pass_pass_stmt
stmt(p                 | continue):
_stmt
    '''pass                 |_stmt : break_stmt PASS
                '''

 | empty'''def p_

params(def p_p):assignment_
    '''stmt(params : IDp):

              |    '''ass params COMMAignment_stmt ID'''
 : ID ASS
def pIGN expression SE_args(MI'''p):


def    '''args : p_return value_stmt(p
            |):
    args COMMA '''return_ value'''
stmt :
def p RETURN expression SE_condition(p):
MI    '''condition'''

 : valuedef p_
                 | valuepass_stmt(p COMPARE):
    '''pass value_stmt : PA'''

defSS SEMI'''
 p_iterable(
def p_continuep):
   _stmt(p): '''iterable : value'''
    '''continue

def p_stmt_value(p : CONT):
   INUE SEMI '''value : ID'''


             |def p_ INT
             |break_stmt FLOAT(p):
             | STR
    '''ING'''

break_stmt :def p_ BREAKerror(p): SEMI'''
    if

def p p:
        print("_empty(p):
    '''empty : '''Syntax error at '%

def p_s'" % perror(p.value)
    else:
       ):
    print("Syntax if p:
 error at EOF        print("Syntax")

 error at '%parser = yaccs'" % p..yacc()