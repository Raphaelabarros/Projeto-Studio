import pandas as pd
from dados import carregar_dados

def filtrar_atividade(data, atividade):
    """Filtrar dados com base na atividade preferida e salvar em CSV."""
    filtrado = data[data['Atividade Preferida'] == atividade]
    filtrado.to_csv(f'{atividade}_clientes.csv', index=False)
    print(f"Clientes que preferem {atividade} foram salvos em '{atividade}_clientes.csv'.")

if __name__ == "__main__":
    df = carregar_dados('dados_clientes.csv')
    filtrar_atividade(df, 'Yoga')  # Exemplo de filtro para 'Yoga'
