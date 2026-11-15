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
)

literals = {'+', '(', ')', '-', '*', '/', '=', ',', ';'}

def t_STRING(t):
    r"'[^']*'"
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


def preprocess(t):
    statements = [] 

    for lineno, line in enumerate(t.splitlines(), start=1):

        # 1 comment line: C, c, * in column 1
        if line[:1] in ('C','c','*'):
            continue

        # 2 blank line
        if line.strip() == '':
            continue

        # 3 split into the fixed form fields
        label = line[0:5] # column 1-5
        cont = line[5] # column 6
        body = line[6:72] # column 7-72

        if cont not in ('', ' ', '0'):
            if not statements:
                raise SyntaxError(f"linha {lineno}: continuação sem instrução anterior")
            if label.strip():
                raise SyntaxError(f"linha {lineno}: Coluna de continuação não pode ter label")
            statements[-1][1] += body
        # new statements
        else: 
            lab = label.strip()
            if lab and not lab.isdigit():
                raise SyntaxError(f"linha {lineno}: label inválido '{lab}'")
            statements.append([lab, body, lineno])

    lines = [f"{lab} {text}" if lab else text for lab, text, _ in statements]
    return '\n'.join(lines) + '\n'









lexer = lex.lex()

# ---

if __name__ == "__main__":
    import sys
    codigo = preprocess(sys.stdin.read())
    print(codigo)                           # see the cleaned text
    lexer.input(codigo)
    for tok in lexer:
        print(tok)


# import sys
# for linha in sys.stdin:
#     lexer.input(linha)
#     for tok in lexer:
#         print(tok)


'''
column:  1 2 3 4 5 | 6 | 7 ............................ 72 | 73+
         [ label   ][c][ statement                       ] [ignored]

source text ──► preprocess() ──► clean text ──► lexer ──► parser
               (columns, comments,
                continuations)

The algorithm:
For each physical line:
Column 1 is C, c or * → comment, skip it.
The line is blank → skip it.
Otherwise, cut the line into its parts:
label = line[0:5] → columns 1–5
cont = line[5:6] → column 6
body = line[6:72] → columns 7–72 (anything after 72 is thrown away; on old punched cards that area held sequence numbers)
Column 6 is not blank and not '0' → this is a continuation line. Append its body to the previous statement.
Otherwise it’s a new statement. Save (label, body).




'''