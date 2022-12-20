import pandas as pd
from funs.dimensiones import *
from funs.criterios import criterios
from funs.porcent import per_str

def get_areas(df, segs):
    """
    Da una lista con todas las agrupaciones y subagrupaciones
    """
    areas = []
    for i in segs:
        for j in df[i].unique():
            if type(j) == str:
                areas.append(j)
    
    return areas

def get_areas_not(df_as, areas, disclaimer=False):
    """
    Entrega una lista de las áreas que no cumplen con los criterios.
    df_as = Base de datos donde está la asistencia
    areas = Todas las áreas
    """
    x = []
    for i in areas:
        cantidad, tasa_respuesta = criterios(df_as, i)
        if (cantidad <= 6) or (tasa_respuesta <= 0.4):
            x.append(i)
            if disclaimer == True:
                print(f"Cantidad: {cantidad}\t\tTasa de respuesta: {per_str(tasa_respuesta)}\t\t{i}")
    return x

def nxt(df, seg):
    """
    Crea 2 listas
    nxt_seg = El segmento sucesor
    tmp_areas_clear = las áreas que existen en dicho segmento siguiente

    segm = Segmento correspondiente del grupo que está iterando
    """

    tmp_segs = [i for i in df.columns if i[:3] == 'seg']
    tmp_len = len(tmp_segs)

    tmp_index = tmp_segs.index(seg)
    tmp_index +=1
    
    if tmp_index == tmp_len:
        return [], []
    else:
        nxt_seg = tmp_segs[tmp_index]
        tmp_areas = list(pd.unique(df[nxt_seg]))
        tmp_areas_clear = [j for j in tmp_areas if type(j) == str]
        return nxt_seg, tmp_areas_clear

def ant(df, seg):
    """
    Entrega el nombre del area madre que elgloba el segmento elegido
    seg = Segmento del que se quiere obrtener el grupo de su segmento madre
    """
    if seg != 'seg_1':
        nro = int(seg[-1]) - 1
        pre_seg = 'seg_' + str(nro)
        ant_seg = np.unique(df[pre_seg])
        if len(ant_seg) == 1:
            return pre_seg, ant_seg[0]
        else:
            raise Exception('Existe más de un segmento madre')
    else:
        return seg, np.unique(df[seg])[0]

def dict_areas(df, segmento, areas, dims):
    """
    Crea un diccionario cuyos valores son las listas de los valores según la cantidad de áreas del segmento

    df = Base de Datos
    segmento = el nombre del segmento sucesor del de la base de datos que está iterando
    areas = Lista de las áreas que existen en el segmento sucesor.
    dims = Dimensiones que se quieren considerar para el análisis.
    """
    dic = {}

    pos = []
    neu = []
    neg = []

    for k in areas:
        # Antes estaba así
        # pos.append(get_per_dims(df[df[segmento] == k], dims, signo='pos')[0])
        pos.append(get_per_dims(df[df[segmento] == k], dims, signo='pos', promedio=True))
        neu.append(get_per_dims(df[df[segmento] == k], dims, signo='neu', promedio=True))
        neg.append(get_per_dims(df[df[segmento] == k], dims, signo='neg', promedio=True))

    dic["pos"] = pos
    dic["neu"] = neu
    dic["neg"] = neg
        
    return dic