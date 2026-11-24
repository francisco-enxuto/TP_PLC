import re

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
    r'program'
    return t

def t_INTEGER(t):
    r'integer'
    return t

def t_REAL(t):
    r'real'
    return t

def t_LOGICAL(t):
    r'logical'
    return t

def t_CHARACTER(t):
    r'character'
    return t

def t_IF(t):
    r'if'
    return t

def t_THEN(t):
    r'then'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ENDIF(t):
    r'endif'
    return t

def t_DO(t):
    r'do'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_READ(t):
    r'read'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_END(t):
    r'end'
    return t

def t_COMMENT(t):
    r'C     .*'
    pass  # Ignora comentários


t_TRUE = r'\.true\.'
t_FALSE = r'\.false\.'

t_EQ = r'\.eq\.'
t_NE = r'\.ne\.'
t_LT = r'\.lt\.'
t_LE = r'\.le\.'
t_GT = r'\.gt\.'
t_GE = r'\.ge\.'

t_AND = r'\.and\.'
t_OR = r'\.or\.'
t_NOT = r'\.not\.'

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

lexer = lex.lex(reflags=re.IGNORECASE) #com isto o lexer ignora maiúsculas e minúsculas, ou seja, não diferencia "program" de "PROGRAM"

# ---
import sys

for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        print(tok)
