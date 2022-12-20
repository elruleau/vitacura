import pandas as pd
import numpy as np
from funs.porcent import per_str

def get_per_dims(df, dims=list, signo=str, promedio=False, string=False):

    """
    Entrega los valores porcentuales de las dimensiones elgidas

    dims = Lista de dimensiones (columnas) que se quiere analizar. Elige todas las dimensiones por defecto. Tiene que estar en formato de lista!
    signo = Elegir qué signo se quiere dentro de las opciones tricotomizadas.
    promedio = Si se desea obtener el promedio de los valores
    string = Si se desea en formato de string con el signo '%'
    """

    columns = [i for i in df.columns if i[:3] in dims]

    pos = np.array([sum(df[i]) for i in columns if i[-3:] == 'pos'])
    neu = np.array([sum(df[i]) for i in columns if i[-3:] == 'neu'])
    neg = np.array([sum(df[i]) for i in columns if i[-3:] == 'neg'])

    tot = pos + neu + neg
  
    pos_per = pos/tot
    neu_per = neu/tot
    neg_per = neg/tot

    # Signo
    if signo == 'pos':
        if promedio == True:
            x = sum(pos)/sum(tot)
        else:
            x = list(pos_per)
    elif signo == 'neu':
        if promedio == True:
            x = sum(neu)/sum(tot)
        else:
            x = list(neu_per)
    elif signo == 'neg':
        if promedio == True:
            x = sum(neg)/sum(tot)
        else:
            x = list(neg_per)
    
    if string == True:
        return per_str(x)
    else:
        return x


def top_dims(dims=list, values=list, sort=True):
    """
    Crea un diccionario con las siglas de las dimensiones y sus respectivos valores
    Por defecto, el diccionarios se ordenará de mayor a menor según lo valores del diccionario
    
    * En caso de que más de una key tengo el mismo valor, las llaves  del diccionario se ordenarán alfabéticamente (de manera inversa)
    """
    tmp_dict = dict(zip(dims, values))
    
    if sort == True:
        return dict(sorted(tmp_dict.items(), key=lambda item: item[1], reverse=True))
    else:
        return tmp_dict


def count_pts_dims(df, col_lim=None):
    """
    Crea un df con el conteo de los puntajes de los diferentes ítems según su dimensión
    Esto sirve para generar una matriz de las correlaciones

    df = Base de datos con los valores NUMÉRICOS de los candidatos en escala liket
    col_lim = Límite de las columnas donde se encuentras todos los items en la base de datos de lime
    """
    tmp_cols = df.columns[1:col_lim]
    df_dims = pd.DataFrame()
    x = []

    for i in range(len(tmp_cols)):

        s_now = tmp_cols[i][:3] 
        if i == len(tmp_cols)-1:
            s_sus = None
        else:
            s_sus = tmp_cols[i+1][:3]
        
        if s_now == s_sus:
            x.append(tmp_cols[i])
        elif s_now != s_sus:
            x.append(tmp_cols[i])
            df_dims[x[0][:3].upper()] = df[x].sum(axis=1)
            x = []

    return df_dims