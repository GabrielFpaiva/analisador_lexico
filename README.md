# LFA - Projeto 1 e 2 - Analisador Léxico e Sintático JSON

## Explicação

Este projeto implementa um **analisador léxico** e um **analisador sintático** para uma versão simplificada do formato JSON. O **analisador léxico** transforma a string de entrada em uma sequência de **tokens**, que são as unidades mínimas da linguagem, como números, strings, booleanos, `null`, objetos (`{}`), e arrays (`[]`). Já o **analisador sintático** utiliza esses tokens para construir uma estrutura hierárquica (ou árvore) que representa a organização dos dados JSON, garantindo que eles estejam bem formados conforme a especificação da linguagem.

## Estrutura do Projeto

1. **`tokens.py`**:
   - Define os **tipos de tokens** que o analisador léxico reconhecerá, como números, strings, palavras-chave (ex.: `true`, `false`, `null`), e os símbolos estruturais do JSON (`{}`, `[]`, `:`, `,`).
   - Inclui a função auxiliar `token`, que cria tokens com base no tipo e valor lido da entrada.

2. **`analisador_lexico.py`**:
   - Contém as funções que realizam a análise léxica da string de entrada. Essas funções eliminam espaços, reconhecem números, strings, palavras-chave e símbolos do JSON, transformando a string em uma sequência de tokens.
   - A função principal `analise_lexica` percorre toda a string, retornando uma lista de tokens que será usada pelo analisador sintático.

3. **`analisador_sintatico.py`**:
   - Este arquivo contém o **analisador sintático**, que utiliza a técnica de **análise descendente recursiva**. Ele recebe os tokens gerados pelo analisador léxico e constrói uma representação estruturada dos dados JSON.
   - O analisador sintático segue a gramática JSON e reconhece objetos, arrays e valores atômicos como números, strings e palavras-chave (`true`, `false`, `null`).
   - Caso encontre um erro durante a análise sintática (como um símbolo fora do lugar ou estrutura inválida), o analisador relata o erro com detalhes, facilitando a depuração.

4. **`test.py`**:
   - Contém uma lista de exemplos de JSON que são utilizados para testar tanto o analisador léxico quanto o sintático.
   - Ele sorteia um dos exemplos, executa o analisador léxico e o sintático sobre o teste escolhido, e exibe os tokens gerados junto com a estrutura JSON resultante.

## Funcionalidades Principais

### Analisador Léxico

1. **Eliminação de Espaços (`elimina_espacos(s)`)**:
   - Remove espaços em branco no início da string, garantindo que não interfiram na análise léxica.

2. **Reconhecimento de Números (`rec_numero(s)`)**:
   - Reconhece números inteiros e fracionários, inclusive números negativos. Ele percorre a string, formando o número completo e gerando o token correspondente.

3. **Reconhecimento de Strings (`rec_string(s)`)**:
   - Processa strings delimitadas por aspas duplas, retornando o conteúdo sem as aspas.

4. **Palavras-chave JSON (`rec_palavra_chave(s)`)**:
   - Reconhece palavras reservadas do JSON, como `true`, `false` e `null`, gerando tokens específicos para essas palavras.

5. **Identificação de Tokens (`proximo_token(s)`)**:
   - Função principal que navega pela string, identifica o próximo token, e chama as funções apropriadas para números, strings ou palavras-chave.

6. **Análise Léxica Completa (`analise_lexica(s)`)**:
   - Percorre toda a string de entrada, chamando `proximo_token` repetidamente até que o fim da entrada seja alcançado (indicado pelo token **EOF**). Retorna uma lista de tokens para o analisador sintático.

### Analisador Sintático

1. **Análise de Valores (`valor()`)**:
   - Função principal que processa valores JSON. Ela determina se o valor é um número, string, booleano, `null`, objeto ou array, e chama a função correspondente para realizar a análise.

2. **Análise de Arrays (`array()`)**:
   - Reconhece arrays JSON que começam com `[`. Ele verifica cada valor dentro do array, e caso haja múltiplos valores, os separa por vírgulas. Arrays vazios também são tratados corretamente.

3. **Análise de Objetos (`objeto()`)**:
   - Processa objetos JSON que começam com `{`. Ele analisa os pares chave-valor dentro do objeto e lida com múltiplos pares, separados por vírgulas. Objetos vazios são suportados.

4. **Análise de Listas de Valores (`lista_valores()`)**:
   - Função recursiva que trata múltiplos valores dentro de arrays, observando a vírgula como separador.

5. **Análise de Pares Chave-Valor (`pares()`)**:
   - Lida com pares chave-valor dentro de objetos JSON, verificando se a chave é uma string e se é seguida pelo símbolo `:`.

6. **Erros Sintáticos**:
   - Caso o analisador encontre algo inesperado (por exemplo, um símbolo ou estrutura incorreta), ele gera um erro sintático e relata o problema, facilitando a identificação de entradas JSON malformadas.

7. **Construção de Estrutura JSON**:
   - O analisador sintático constrói uma representação completa dos dados JSON em forma de estruturas do Python, como **dicionários** para objetos e **listas** para arrays, mantendo a fidelidade da estrutura original.

## Novas Funcionalidades

Com a adição do analisador sintático, o sistema agora é capaz de:

1. **Processar Estruturas Complexas de JSON**:
   - Agora o sistema processa não apenas valores atômicos (números, strings, booleanos), mas também estruturas complexas como objetos aninhados e arrays dentro de objetos.

2. **Detecção de Erros Sintáticos**:
   - Se o JSON estiver malformado (com chaves ou colchetes não correspondentes, por exemplo), o analisador sintático interrompe a execução e exibe uma mensagem detalhada, permitindo que você corrija rapidamente.

3. **Integração Completa Léxico + Sintático**:
   - O analisador léxico e o sintático agora trabalham juntos. Primeiro, o léxico transforma a string em tokens, e o sintático processa esses tokens para garantir que estejam organizados de acordo com a estrutura esperada de um JSON.

4. **Exibição Formatada do JSON**:
   - Ao final da análise sintática, o JSON é exibido de forma formatada e indentada, facilitando a leitura e compreensão da estrutura.

## Testes e Validação

O arquivo `test.py` continua sendo usado para validar o analisador, mas agora com um passo adicional. Após a geração dos tokens, o analisador sintático processa esses tokens para verificar a conformidade com a estrutura JSON. Se tudo estiver correto, ele exibe a estrutura JSON de maneira organizada. Caso haja erros, eles são relatados com detalhes.

## Conclusão

Este projeto evoluiu de um analisador léxico simples para um sistema completo de análise de JSON, incluindo tanto a parte léxica quanto a sintática. Agora, além de reconhecer e gerar tokens, o sistema é capaz de validar a estrutura completa de arquivos JSON, detectando erros e fornecendo uma representação clara dos dados.
