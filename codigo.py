# Lista com os valores das despesas realizadas em diferentes categorias do mês
despesas_mensais = [150.75, 45.00, 320.50, 750.20, 10.00]

# Função que recebe uma lista de valores e retorna a soma total
def calcular_total_despesas(valores_despesas):
    return sum(valores_despesas) # Soma todos os valores da lista e retorna o total

# Função que gera um relatório simples com o total de despesas
def gerar_relatorio_despesas():
    total = calcular_total_despesas(despesas_mensais) # Chama a função para calcular o total
    print("--- Relatório de Despesas - Maio ---") # Exibe o título do relatório
    print(f"Total de Despesas: R$ {total:.2f}") # Exibe o valor total calculado com 2 casas decimais

# Chamada da função principal para executar o relatório
gerar_relatorio_despesas()
