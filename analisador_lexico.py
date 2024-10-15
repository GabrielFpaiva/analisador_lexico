from tokens import TipoToken, token

# elimina espaços em branco no início da string de entrada
def elimina_espacos(s):
    i = 0
    while i < len(s) and s[i].isspace():
        i += 1
    return s[i:]

# função que reconhece números na string de entrada
# se o primeiro caractere é um dígito, ele identifica o número até o final
def rec_numero(s):
    i = 0
    while i < len(s) and (s[i].isdigit() or s[i] == '.'):
        i += 1
    lexema = s[:i]
    return token(TipoToken.NUM, lexema, float(lexema)), s[i:]

# função que reconhece strings na string de entrada
# se o primeiro caractere é uma aspa dupla, identifica a string até a próxima aspa dupla
def rec_string(s):
    i = 1  # Ignora o primeiro caractere, que é a aspa inicial
    while i < len(s) and s[i] != '"':
        i += 1
    lexema = s[:i+1]
    return token(TipoToken.STRING, lexema, lexema[1:-1]), s[i+1:]

# função que reconhece as palavras-chave "true", "false", e "null"
# se uma dessas palavras é encontrada, retorna o token correspondente
def rec_palavra_chave(s):
    if s.startswith('true'):
        return token(TipoToken.TRUE, 'true', True), s[4:]
    elif s.startswith('false'):
        return token(TipoToken.FALSE, 'false', False), s[5:]
    elif s.startswith('null'):
        return token(TipoToken.NULL, 'null', None), s[4:]
    return token(TipoToken.ERRO, s[0], None), s[1:]

def proximo_token(s):
    s = elimina_espacos(s)
    if len(s) == 0:
        return token(TipoToken.EOF, '', None), ''
    
    # Verifica se o primeiro caractere é um número ou um sinal negativo
    elif s[0].isdigit() or s[0] == '-':
        return rec_numero(s)
    
    # Verifica strings
    elif s[0] == '"':
        return rec_string(s)
    
    # Verifica símbolos JSON como chaves, colchetes, vírgulas e dois pontos
    elif s[0] == '{':
        return token(TipoToken.ABRE_CHAVES, '{'), s[1:]
    elif s[0] == '}':
        return token(TipoToken.FECHA_CHAVES, '}'), s[1:]
    elif s[0] == '[':
        return token(TipoToken.ABRE_COLCHETES, '['), s[1:]
    elif s[0] == ']':
        return token(TipoToken.FECHA_COLCHETES, ']'), s[1:]
    elif s[0] == ':':
        return token(TipoToken.DOIS_PONTOS, ':'), s[1:]
    elif s[0] == ',':
        return token(TipoToken.VIRGULA, ','), s[1:]
    
    # Verifica palavras-chave JSON (true, false, null)
    elif s.startswith('true'):
        return token(TipoToken.TRUE, 'true', True), s[4:]
    elif s.startswith('false'):
        return token(TipoToken.FALSE, 'false', False), s[5:]
    elif s.startswith('null'):
        return token(TipoToken.NULL, 'null', None), s[4:]
    
    # Se o token não for reconhecido, retorna um token de erro
    else:
        return token(TipoToken.ERRO, s[0]), s[1:]


# função principal do analisador léxico
# processa toda a string de entrada e retorna uma lista de tokens
def analise_lexica(s):
    tokens = []
    while True:
        tok, s = proximo_token(s)
        tokens.append(tok)
        if tok.tipo == TipoToken.EOF: 
            break
    return tokens

