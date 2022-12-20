import pandas as pd
from funs.dimensiones import get_per_dims

def dict_car(df, nro_car, dims, list_sort=False):
    """
    Crea un diccionario con las listas de los valores pos, neu y neg de las diversas características invocadas
    La cantidad de listas dentro de cada "key" dependera de la variedad de las características.
    """

    dic = {}

    pos = []
    neu = []
    neg = []

    if list_sort == False:
        cars = [i for i in pd.unique(df[f"car_{nro_car}"]) if type(i) == str]
    else:
        cars = list_sort

    for k in cars:

        pos.append(get_per_dims(df[df[f"car_{nro_car}"] == k], dims=dims, signo='pos', promedio=True))
        neu.append(get_per_dims(df[df[f"car_{nro_car}"] == k], dims=dims, signo='neu', promedio=True))
        neg.append(get_per_dims(df[df[f"car_{nro_car}"] == k], dims=dims, signo='neg', promedio=True))

    dic["pos"] = pos
    dic["neu"] = neu
    dic["neg"] = neg
        
    return dic