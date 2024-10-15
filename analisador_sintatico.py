from tokens import TipoToken, token
from analisador_lexico import analise_lexica

# Classe para controlar o fluxo de tokens e realizar a análise sintática
class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicao_atual = 0

    def token_atual(self):
        if self.posicao_atual < len(self.tokens):
            return self.tokens[self.posicao_atual]
        return token(TipoToken.EOF, '', None)

    def consumir_token(self):
        self.posicao_atual += 1

    def erro(self, mensagem):
        raise Exception(f"Erro Sintático: {mensagem} no token {self.token_atual()}")

    def esperar(self, tipo_token):
        if self.token_atual().tipo == tipo_token:
            self.consumir_token()
        else:
            self.erro(f"Esperado {tipo_token}, mas encontrado {self.token_atual().tipo}")

    # Função principal que inicia a análise com base no não-terminal Valor
    def analisar(self):
        resultado = self.valor()
        if self.token_atual().tipo != TipoToken.EOF:
            self.erro("Entrada inválida após o fim do JSON")
        return resultado

    # Função que corresponde ao não-terminal 'Valor'
    def valor(self):
        tok = self.token_atual()

        if tok.tipo == TipoToken.NUM:
            valor = tok.valor
            self.consumir_token()
            return valor

        elif tok.tipo == TipoToken.STRING:
            valor = tok.valor  # A string já vem sem aspas
            self.consumir_token()
            return valor

        elif tok.tipo == TipoToken.TRUE:
            self.consumir_token()
            return True

        elif tok.tipo == TipoToken.FALSE:
            self.consumir_token()
            return False

        elif tok.tipo == TipoToken.NULL:
            self.consumir_token()
            return None

        elif tok.tipo == TipoToken.ABRE_CHAVES:
            return self.objeto()

        elif tok.tipo == TipoToken.ABRE_COLCHETES:
            return self.array()

        else:
            self.erro("Valor inválido")

    # Função para analisar arrays
    def array(self):
        array = []
        self.esperar(TipoToken.ABRE_COLCHETES)

        if self.token_atual().tipo != TipoToken.FECHA_COLCHETES:
            array.append(self.valor())
            while self.token_atual().tipo == TipoToken.VIRGULA:
                self.consumir_token()
                array.append(self.valor())

        self.esperar(TipoToken.FECHA_COLCHETES)
        return array

    # Função para analisar objetos
    def objeto(self):
        objeto = {}
        self.esperar(TipoToken.ABRE_CHAVES)

        if self.token_atual().tipo != TipoToken.FECHA_CHAVES:
            chave = self.token_atual().valor
            self.esperar(TipoToken.STRING)
            self.esperar(TipoToken.DOIS_PONTOS)
            valor = self.valor()
            objeto[chave] = valor

            while self.token_atual().tipo == TipoToken.VIRGULA:
                self.consumir_token()
                chave = self.token_atual().valor
                self.esperar(TipoToken.STRING)
                self.esperar(TipoToken.DOIS_PONTOS)
                valor = self.valor()
                objeto[chave] = valor

        self.esperar(TipoToken.FECHA_CHAVES)
        return objeto
