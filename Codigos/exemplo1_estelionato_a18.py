# EXEMPLO 1 - Exercício anterior modificado
import pandas as pd
import numpy as np
import os

# Obter dados
try:
    os.system("cls")
    print("Obtendo dados...")
    ENDERECO_DADOS="https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
    
    #encodings: utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=";", encoding="iso-8859-1")
    # Delimitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_estelionato_mes = df_ocorrencias[["mes_ano","estelionato"]]

    df_estelionato_mes = df_estelionato_mes.groupby(["mes_ano"]).sum(["estelionato"]).reset_index()

    print("Dados obtidos com sucesso!")

except Exception as e:
    print(f"Erro ao obter dados: {e}")
    exit()


# Gerando informações
try:
    print("\nCalculando informações sobre padrão de roubo de veículos...")
    # Array Numpy
    array_estelionato = np.array(df_estelionato_mes["estelionato"])

    media_estelionato = np.mean(array_estelionato)
    mediana_estelionato = np.median(array_estelionato)

    # Calculando a distancia entre média e mediana
    dist_estelionato = abs((media_estelionato-mediana_estelionato)/mediana_estelionato)
    # Se a distancia passou de 25% ocorre maior chance dos dados serem heterogeneos

    # Quartis (Há métodos diferentes, weibull (para dados heterogeneos), linear (padrao), lower, higher, nearest, midpoint)
    q1 = np.quantile(array_estelionato, 0.25, method="weibull")
    q2 = np.quantile(array_estelionato, 0.50, method="weibull")
    q3 = np.quantile(array_estelionato, 0.75, method="weibull")

    # Pegando os meses de maiores ocorrencias de estelionatos
    df_mes_ano_acima_q3 = df_estelionato_mes[df_estelionato_mes["estelionato"] > q3]

    # Pegando os meses de menores ocorrencias de estelionatos
    df_mes_ano_abaixo_q1 = df_estelionato_mes[df_estelionato_mes["estelionato"] < q1]

    print("\n","="*30)
    print("\nMEDIDAS DE TENDÊNCIA CENTRAL")
    print(f"Total de casos de estelionato por mês:\n{df_estelionato_mes.head(12)}\n")
    print(f"Totais de casos gerais de estelionato: {np.sum(array_estelionato)}")
    print(f"\nMédia de casos de estelionato: {media_estelionato:.2f}")
    print(f"Mediana de casos de estelionato: {mediana_estelionato:.2f}")
    print(f"Distância entre média e mediana: {dist_estelionato:.2f}%")
    print(f"Não há uma distância aceitável para calcularmos um valor médio de casos por mês, nesse caso a média será {mediana_estelionato}.")
    print(f"\nMAIORES MESES E ANOS:\n{df_mes_ano_acima_q3.sort_values(by='estelionato', ascending=False)}")
    print(f"\nMENORES MESES E ANOS:\n{df_mes_ano_abaixo_q1.sort_values(by='estelionato')}")
except Exception as e:
    print(f"Erro ao obter informações sobre padrão de roubo de veículos: {e}")
    exit()
