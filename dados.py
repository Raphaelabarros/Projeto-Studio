import pandas as pd

def carregar_dados(caminho_csv):
    """Carregar dados do CSV e retornar um DataFrame."""
    data = pd.read_csv(caminho_csv)
    return data

# Testar a função
if __name__ == "__main__":
    df = carregar_dados('dados_clientes.csv')
    print(df.head())
