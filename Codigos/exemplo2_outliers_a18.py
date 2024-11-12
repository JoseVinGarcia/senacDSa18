# EXEMPLO 2 - OUTLIERS (EXEMPLO 2 DA AULA PASSADA)

# Numeros discrepantes
# Para descobrir os outliers precisamos descobrir o IQR (intervalo interquartil) e depois o Limite superior e o Limite inferior
# IQR = Q3 - Q1
# Limite superior = Q3 + (1.5 * IQR)
# Limite inferior = Q1 - (1.5 * IQR)
# Outliers superiores - Maiores que o limite superior
# Outliers inferiores - Menores que o limite inferior

import pandas as pd
import numpy as np

# Obter dados
try:
    print("Obtendo dados...")
    ENDERECO_DADOS="https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
    
    #encodings: utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=";", encoding="iso-8859-1")
    # Delimitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[["munic","roubo_veiculo"]]

    # totalizar roubo veiculo por munic
    # utilizando varios metodos de uma vez:
    df_roubo_veiculo = df_roubo_veiculo.groupby(["munic"]).sum(["roubo_veiculo"]).reset_index()

    # print(df_roubo_veiculo.head())

    print("\nDados obtidos com sucesso!")

except Exception as e:
    print(f"Erro ao obter dados: {e}")
    exit()


# Gerando informações
try:
    print("Calculando informações sobre padrão de roubo de veículos...")
    # Array Numpy
    array_roubo_veiculo = np.array(df_roubo_veiculo["roubo_veiculo"])


    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    dist_roubo_veiculo = abs((media_roubo_veiculo-mediana_roubo_veiculo)/mediana_roubo_veiculo)

    print("\nMedidas de tendência central:")
    print(f"Média de roubo de veículo: {media_roubo_veiculo}")
    print(f"Mediana de roubo de veículo: {mediana_roubo_veiculo}")
    print(f"Distância entre média e mediana: {dist_roubo_veiculo}%")

    # medidas de dispersao
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    # amplitude: quanto mais proxima de 0 maior homogeneidade, quanto mais proximo do maximo maior a dispersao
    amplitude = maximo - minimo

    print("\nMedidas de dispersão:")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")
    print(f"Amplitude total: {amplitude}")

except Exception as e:
    print(f"Erro ao obter informações sobre padrão de roubo de veículos: {e}")
    exit()

