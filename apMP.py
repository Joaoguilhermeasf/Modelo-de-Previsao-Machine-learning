import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def PrecoM2(valor):
    
    DataSet = pd.read_csv(
        'BaseDados.csv',
        encoding='latin-1',
        parse_dates=['data'],
        header=0,
        names=['data', 'status', 'endereco', 'area', 'quartos', 'banheiros', 'vagas', 'col8', 'col9', 'tipo'],
    )

    DataSet['status'] = (
        DataSet['status']
        .str.replace('R$', '', regex=False)
        .str.replace('.', '', regex=False)
        .str.strip()
        .replace("Sob consulta", float('nan'))
        .astype(float)
    )

    DataSet = DataSet.dropna()
    DataSet = DataSet.sort_values('status', ascending=True)

    Apartamentos = DataSet[DataSet['tipo'] == 'apartamentos'].copy()


    Apartamentos['area'] = (
        Apartamentos['area']
        .str.replace(r'm[^\d]*$', '', regex=True)
        .str.strip()
        .astype(float)
    )

    Eixo_y = Apartamentos['status']  
    Eixo_x = Apartamentos['area']   

    xTreino, xTeste, yTreino, yTeste = train_test_split(
        Eixo_x,
        Eixo_y,
        test_size=0.25,
    )

    fRegressao = LinearRegression()
    fRegressao.fit(xTreino.values.reshape(-1, 1), yTreino.values.ravel())

    preco_previsto = fRegressao.predict([[float(valor)]])
    return f'Um apartamento de {float(valor):.2f}m² deverá custar aproximadamente: R$ {preco_previsto[0]:,.2f}'