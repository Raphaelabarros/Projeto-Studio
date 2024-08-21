import pandas as pd
import matplotlib.pyplot as plt
from dados import carregar_dados

def gerar_graficos(data):
    """Gerar e salvar gráficos baseados nos dados fornecidos."""
    # Gráfico de barras para atividades preferidas
    atividade_preferida = data['Atividade Preferida'].value_counts()
    plt.figure(figsize=(10, 6))
    atividade_preferida.plot(kind='bar', color='skyblue')
    plt.title('Número de Clientes por Atividade Preferida')
    plt.xlabel('Atividade')
    plt.ylabel('Número de Clientes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('atividade_preferida.png')
    plt.show()

    # Gráfico de barras para frequência de participação
    frequencia_participacao = data['Frequência de Participação'].value_counts()
    plt.figure(figsize=(10, 6))
    frequencia_participacao.plot(kind='bar', color='lightgreen')
    plt.title('Frequência de Participação')
    plt.xlabel('Frequência')
    plt.ylabel('Número de Clientes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('frequencia_participacao.png')
    plt.show()

if __name__ == "__main__":
    df = carregar_dados('dados_clientes.csv')
    gerar_graficos(df)
