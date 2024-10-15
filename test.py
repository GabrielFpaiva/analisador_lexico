import random
import json  # Para exibir a estrutura JSON formatada
from analisador_lexico import analise_lexica
from analisador_sintatico import AnalisadorSintatico

# Lista de testes JSON
testes = [
    '{"ativo": true, "saldo": 100.50, "cliente": "Maria"}',
    '{"usuarios": ["Alice", "Bob", null], "count": 3}',
    '{"data": {"dia": 25, "mes": "dezembro", "ano": 2023}, "feriado": false}',
    '{"nome": "José", "idade": 45, "saldo": -500.75, "ativo": false, "historico": [1000, -250.50, 300], "endereco": {"rua": "Rua das Flores", "numero": 123, "cidade": "São Paulo", "estado": "SP"}, "cpf": null}',
    '{"mensagem": "Erro inesperado: \\"Arquivo não encontrado\\" em linha 45.", "codigo": 404, "sucesso": false, "dados": null}',
    '{"items": [{"id": 1, "nome": "Item A", "preco": 9.99}, {"id": 2, "nome": "Item B", "preco": 19.99}, {"id": 3, "nome": "Item C", "preco": 29.99}], "total": 59.97, "pagamento": {"metodo": "cartao", "status": "pago"}}',
    '{"config": {"opcao1": true, "opcao2": false, "limite": 100, "path": "C:\\\\Arquivos\\\\Config\\\\", "timeout": null}, "ativo": true}'
]

# Sorteia um dos testes
teste_escolhido = random.choice(testes)

# Executa o analisador léxico no teste sorteado
resultado = analise_lexica(teste_escolhido)

# Exibe o teste sorteado e os tokens gerados
print("Teste Sorteado:")
print(teste_escolhido)
print("\nTokens Gerados:")
for tok in resultado:
    print(tok)

# Executa o analisador sintático
print("\nResultado da Análise Sintática:")
try:
    sintatico = AnalisadorSintatico(resultado)
    resultado_sintatico = sintatico.analisar()
    print("Análise sintática concluída com sucesso!")
    # Exibe o JSON formatado
    print("Estrutura JSON:")
    print(json.dumps(resultado_sintatico, indent=4, ensure_ascii=False))  # Formata a saída com indentação
except Exception as e:
    print(f"Erro durante a análise sintática: {e}")
