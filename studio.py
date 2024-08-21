from dados import carregar_dados
from analise_dados import analisar_dados
from graficos import gerar_graficos
from atividades import filtrar_atividade

def main():
    # Carregar os dados
    data = carregar_dados('dados_clientes.csv')
    
    # Analisar os dados
    analisar_dados(data)
    
    # Gerar gráficos
    gerar_graficos(data)
    
    # Filtrar e salvar dados específicos (exemplo com 'Yoga')
    filtrar_atividade(data, 'Yoga')

if __name__ == "__main__":
    main()
