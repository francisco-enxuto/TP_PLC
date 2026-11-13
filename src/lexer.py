from ply import lex

# Pode ter mais, acrescentar depois
tokens = (
    'PROGRAM', # Palavras chave
    'INTEGER',
    'REAL',
    'LOGICAL',
    'CHARACTER',
    'IF',
    'THEN',
    'ELSE',
    'ENDIF',
    'DO',
    'CONTINUE',
    'GOTO',
    'READ',
    'PRINT',
    'END', # adicionar FORMAT, EXTERNAL?
    'TRUE', # Identificadores, literais numéricos e lógicos
    'FALSE',
    'EQ', # Operadores aritméticos, relacionais
    'NE',
    'LT',
    'LE',
    'GT',
    'GE',
    'AND',
    'OR',
    'NOT',
    'VAR', # Variáveis
    'INT',
    'STRING',
    'FLOAT',
    'COMMENT'
)

literals = {'+', '(', ')', '-', '*', '/', '=', ',', ';'}

def t_STRING(t):
    r'\'.*\''
    return t

def t_PROGRAM(t):
    r'[pP][rR][oO][gG][rR][aA][mM]'
    return t

def t_INTEGER(t):
    r'[iI][nN][tT][eE][gG][eE][rR]'
    return t

def t_REAL(t):
    r'[rR][eE][aA][lL]'
    return t

def t_LOGICAL(t):
    r'[lL][oO][gG][iI][cC][aA][lL]'
    return t

def t_CHARACTER(t):
    r'[cC][hH][aA][rR][aA][cC][tT][eE][rR]'
    return t

def t_IF(t):
    r'[iI][fF]'
    return t

def t_THEN(t):
    r'[tT][hH][eE][nN]'
    return t

def t_ELSE(t):
    r'[eE][lL][sS][eE]'
    return t

def t_ENDIF(t):
    r'[eE][nN][dD][iI][fF]'
    return t

def t_DO(t):
    r'[dD][oO]'
    return t

def t_CONTINUE(t):
    r'[cC][oO][nN][tT][iI][nN][uU][eE]'
    return t

def t_GOTO(t):
    r'[gG][oO][tT][oO]'
    return t

def t_READ(t):
    r'[rR][eE][aA][dD]'
    return t

def t_PRINT(t):
    r'[pP][rR][iI][nN][tT]'
    return t

def t_END(t):
    r'[eE][nN][dD]'
    return t

def t_COMMENT(t):
    r'C     .*'
    pass  # Ignora comentários

t_TRUE = r'\.[tT][rR][uU][eE]\.'
t_FALSE = r'\.[fF][aA][lL][sS][eE]\.'

t_EQ = r'\.EQ\.'
t_NE = r'\.NE\.'
t_LT = r'\.LT\.'
t_LE = r'\.LE\.'
t_GT = r'\.GT\.'
t_GE = r'\.GE\.'

t_AND = r'\.AND\.'
t_OR = r'\.OR\.'
t_NOT = r'\.NOT\.'

t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INT = r'\d+'
t_FLOAT = r'\d+\.\d+'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
  print(f"Caractere inválido '{t.value[0]}' na linha {t.lexer.lineno}")
  t.lexer.skip(1)

lexer = lex.lex()

# ---
import sys

for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        print(tok)
