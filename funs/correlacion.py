import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from data.texto.dimensiones import dict_dims



def cor_mtx(df_dims_mean, dims=False):
    """
    Da una matrix de correlación con su respectiva significancia estadística representada con (*).
    df_dims_mean = Es solo un "row_means" con los diferentes ítems de las dimensiones específicas.

    Significancia:
    0.05 = (*)
    0.01 = (**)
    0.001 = (***)
    """

    rho = df_dims_mean.corr()
    pval = df_dims_mean.corr(method=lambda x, y: pearsonr(x, y)[1]) - np.eye(*rho.shape)
    p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01, .001] if x<=t]))
    matrix = rho.round(2).astype(str) + p

    if dims == False:
        return matrix
    
    else:
        matrix_dims = matrix[dims].copy()
        matrix_dims_drop = matrix_dims.drop(dims, axis=0)
        return matrix_dims_drop


def dict_cor(matrix, dim, menor_a_mayor=False, top=4):
    """
    Entrega un diccionario con las correlaciones más importantes con sus respectivas dimensiones
    Se puede ordenar de mayor a menor, o viceversa.
    Filtra por significacia estadística (>0.05) para fuera
    
    matrix=matriz de correlaciones
    dim = dimensión que se desea analizar (solo 1)
    top = Largo del ranking
    
    """

    dim_serie = matrix[dim].copy()
    idx_drop = dim_serie[dim_serie.str[-1] != '*'].index
    filt = dim_serie.drop(index=idx_drop, axis=0)
    clean = filt.str.replace("*", "")
    nro = pd.to_numeric(clean)
    nro_sort = nro.sort_values(ascending=menor_a_mayor)
    tmp_dict = nro_sort[:top].to_dict()

    x = {}
    x[dim] = tmp_dict

    return x


def dict_cor_ppt(matrix, dims):

    x = {}
    for i in dims:
        cor_dict = dict_cor(matrix, dim=i)
        for j in range(0, 4):
            x[f"<{i.lower()}_id{j+1}>"] = dict_dims[list(cor_dict[i].keys())[j]]
            x[f"<{i.lower()}_c{j+1}>"] = list(cor_dict[i].values())[j]

    return x