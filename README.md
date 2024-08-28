

### LFA - Projeto 1 - Analisador Léxico JSON

### Explicação

Este projeto implementa um analisador léxico para uma versão simplificada do formato JSON.
O analisador léxico transforma a entrada (uma string JSON) em uma sequência de tokens,
que são unidades significativas como números, strings, booleanos (true, false), null, objetos ({}), e arrays ([]).

### Arquivos

1. `tokens.py`:
   - Contém a definição dos tipos de tokens que o analisador reconhecerá.
   - Inclui uma função auxiliar `token` para criar tokens.

2. `analisador_lexico.py`:
   - Contém as funções do analisador léxico, que reconhecem os tokens na string de entrada e retornam a sequência de tokens.
   - Inclui funções para eliminar espaços, reconhecer números, strings, palavras-chave (true, false, null), e símbolos estruturais ({}[]:,).
   - A função principal `analise_lexica` processa toda a string de entrada e retorna uma lista de tokens.

2. `test.py`:
   - Contém uma lista de exemplos de JSON que são utilizados para testar o analisador léxico.
   - Inclui a funcionalidade de sortear um desses testes de maneira aleatória e executar o analisador léxico sobre ele.
   - Exibe o JSON sorteado e a lista de tokens gerados.

### Funções Principais

1. `elimina_espacos(s)`:
   - Remove os espaços em branco no início da string para evitar que interfiram na análise léxica.

2. `rec_numero(s)`:
   - Reconhece números inteiros ou fracionários na string de entrada. Percorre a string enquanto encontra dígitos ou o caractere de ponto (para números fracionários).

3. `rec_string(s)`:
   - Reconhece strings delimitadas por aspas duplas. Ignora o primeiro caractere (`"`) e continua até encontrar a aspa dupla de fechamento.

4. `rec_palavra_chave(s)`:
   - Reconhece as palavras-chave `true`, `false`, e `null`. Essas palavras têm significado fixo em JSON e, se encontradas, geram um token correspondente.

5. `proximo_token(s)`:
   - Função principal para identificar o próximo token. Chama as funções auxiliares (`rec_numero`, `rec_string`, `rec_palavra_chave`) com base no primeiro caractere da string.

6. `analise_lexica(s)`:
   - Percorre toda a string de entrada, chamando repetidamente `proximo_token` até que o fim da entrada (`EOF`) seja encontrado. Retorna uma lista de tokens.

