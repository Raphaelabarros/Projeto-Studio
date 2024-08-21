import pandas as pd
from dados import carregar_dados

def analisar_dados(data):
    """Analisar os dados e imprimir estatísticas básicas."""
    atividade_preferida = data['Atividade Preferida'].value_counts()
    frequencia_participacao = data['Frequência de Participação'].value_counts()
    
    print("Análise das Atividades Preferidas:")
    print(atividade_preferida)
    
    print("\nAnálise da Frequência de Participação:")
    print(frequencia_participacao)

if __name__ == "__main__":
    df = carregar_dados('dados_clientes.csv')
    analisar_dados(df)
