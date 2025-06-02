# testar_despesas.py

# Importa a função de cálculo e os dados de despesas do arquivo 'despesas_gerenciamento.py'
from despesas_gerenciamento import calcular_total_despesas, despesas_mensais

# Importa a biblioteca 'sys', que permite encerrar o programa com códigos de erro
# Isso é importante para o GitHub Actions identificar falhas
import sys

# Define uma função de teste para validar o total de despesas
def testar_total_despesas():
    resultado = calcular_total_despesas(despesas_mensais) # Executa o cálculo com os dados atuais

    # Define os limites esperados para o total de despesas
    # Ajuste esses limites de acordo com o que você considera aceitável para suas despesas
    limite_minimo = 50.00  # Exemplo: um mínimo de despesas
    limite_maximo = 650.00 # Exemplo: um teto máximo de despesas aceitável

    # Se o resultado estiver dentro da faixa, o teste passa
    if limite_minimo <= resultado <= limite_maximo:
        print("✅ Teste passou! Total de despesas dentro da faixa esperada.")
    # Se o resultado estiver fora da faixa, o teste falha
    else:
        print("❌ Teste falhou! Valor fora da faixa. Resultado obtido: R$", f"{resultado:.2f}")
        # O sys.exit(1) encerra o programa com erro, o que sinaliza falha no GitHub Actions
        sys.exit(1)

# Executa a função de teste automaticamente ao rodar este arquivo
testar_total_despesas()
