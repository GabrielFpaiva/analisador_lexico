from enum import Enum

# Define os tipos de tokens que o analisador léxico reconhecerá.
class TipoToken(Enum):
    NUM = 1             # Número (inteiro ou fracionário)
    STRING = 2          # String (delimitada por aspas duplas)
    TRUE = 3            # Palavra-chave "true"
    FALSE = 4           # Palavra-chave "false"
    NULL = 5            # Palavra-chave "null"
    ABRE_CHAVES = 6     # Símbolo de abertura de chaves '{'
    FECHA_CHAVES = 7    # Símbolo de fechamento de chaves '}'
    ABRE_COLCHETES = 8  # Símbolo de abertura de colchetes '['
    FECHA_COLCHETES = 9 # Símbolo de fechamento de colchetes ']'
    DOIS_PONTOS = 10    # Símbolo de dois pontos ':'
    VIRGULA = 11        # Símbolo de vírgula ','
    ERRO = 12           # Tipo de token para erros léxicos
    EOF = 13            # Fim da entrada

# Função auxiliar para criar tokens
# tipo: tipo do token (TipoToken)
# lex: lexema que originou o token (string)
# valor: valor associado ao token (opcional, pode ser None)
class Token:
    def __init__(self, tipo, lex, valor=None):
        self.tipo = tipo
        self.lex = lex
        self.valor = valor

    def __repr__(self):
        return f"Token(tipo={self.tipo}, lexema='{self.lex}', valor={self.valor})"

    def __str__(self):
        return self.__repr__()

# ajustei a função `token` para retornar uma instância dessa classe `Token`:
def token(tipo, lex, valor=None):
    return Token(tipo, lex, valor)

