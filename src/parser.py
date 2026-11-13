from ply import yacc
from lexer import lexer, tokens

# Regras gramaticais agrupadas
def p_gramatica(p):
    """
    Programa : PROGRAM VAR Linhas END

    Linhas  : Linhas Conteudo
            | Linhas INT Conteudo
            | Conteudo

    Conteudo : PRINT '*' ',' Valores
    Conteudo : Declaracao Variaveis
    Conteudo : CONTINUE
    Conteudo : DO INT VAR '=' VarInt ',' VarInt 
    Conteudo : READ '*' ',' VAR
    Conteudo : VAR '=' expression

    Valores : Valores ',' Valor
            | Valor
    
    Valor : VAR
          | STRING
          | TRUE
          | FALSE
          | INT

    Declaracao : INTEGER
               | REAL
               | LOGICAL
               | CHARACTER '*' INT

    Variaveis : Variaveis ',' VAR
              | VAR

    VarInt : INT
           | VAR
           
    expression : expression '+' term
               | expression '-' term
               | term   
    term : term '*' factor
         | term '/' factor
         | factor
    factor : Valor
           | '(' expression ')'
    """
    pass

def p_error(p):
    if p:
        print(f"Erro sintático no token '{p.value}' (tipo {p.type}) na linha {p.lineno}")
    else:
        print("Erro sintático: fim inesperado do ficheiro (EOF)")
    parser.success = False

# Construção do parser (gera o autómato LALR(1))
parser = yacc.yacc(debug=False, write_tables=False)

exemplo = """
      PROGRAM FATORIAL
      INTEGER N, I, FAT
      PRINT *, 'Introduza um numero inteiro positivo:'
      READ *, N
      FAT = 1
      DO 10 I = 1, N
         FAT = FAT * I
   10 CONTINUE
      PRINT *, 'Fatorial de ', N, ': ', FAT
      END
"""

# for frase in exemplos:
parser.success = True  # Reinicialização essencial!
parser.parse(exemplo, lexer=lexer)
if parser.success:
    print(f"✓ VÁLIDA:   {exemplo}")
else:
    print(f"✗ INVÁLIDA: {exemplo}")