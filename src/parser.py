from ply import yacc
from lexer import lexer, tokens

# Regras gramaticais agrupadas
def p_gramatica(p):
    """
    Linha1 : PROGRAM VAR Linha

    Linha  : Conteudo END

    Conteudo : PRINT '*' ',' STRING
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
      PROGRAM HELLO
      PRINT *, 'Ola, Mundo!'
      END
"""

# for frase in exemplos:
parser.success = True  # Reinicialização essencial!
parser.parse(exemplo, lexer=lexer)
if parser.success:
    print(f"✓ VÁLIDA:   {exemplo}")
else:
    print(f"✗ INVÁLIDA: {exemplo}")