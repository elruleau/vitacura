from funs.dimensiones import top_dims
from funs.porcent import per_str

from data.texto.conclusiones import *
from data.texto.dimensiones import *


def conclusiones(data, dims_glob):
    """
    Llena en el diccionario de 'data' los textos correspondientes para las concusiones.

    <dim> = Nombre completo de la dimensión.
    <per> = Valor en porcentaje de apreciación positiva/neutr/negativa de la dimensión.
    <txt> = Puntos sobre lo que se necesita mejorar.
    """
    # Conclusiones Positivas
    dim_pos_cod1 = list(top_dims(dims_glob, data[f'<area_list_pos>']))[0]
    dim_pos_per1 = per_str(list(top_dims(dims_glob, data[f'<area_list_pos>']).values())[0])
    dim_pos_cod2 = list(top_dims(dims_glob, data[f'<area_list_pos>']))[1]
    dim_pos_per2 = per_str(list(top_dims(dims_glob, data[f'<area_list_pos>']).values())[1])

    data['<dim_pos1>'], data['<per_pos1>'], data['<txt_pos1>'] = dict_dims[dim_pos_cod1], dim_pos_per1, dict_c_pos[dim_pos_cod1]
    data['<dim_pos2>'], data['<per_pos2>'], data['<txt_pos2>'] = dict_dims[dim_pos_cod2], dim_pos_per2, dict_c_pos[dim_pos_cod2]


    # Conclusiones Negativas
    dim_neg_cod1 = list(top_dims(dims_glob, data[f'<area_list_neg>']))[0]
    dim_neg_per1 = per_str(list(top_dims(dims_glob, data[f'<area_list_neg>']).values())[0])
    dim_neg_cod2 = list(top_dims(dims_glob, data[f'<area_list_neg>']))[1]
    dim_neg_per2 = per_str(list(top_dims(dims_glob, data[f'<area_list_neg>']).values())[1])

    data['<dim_neg1>'], data['<per_neg1>'], data['<txt_neg1>'] = dict_dims[dim_neg_cod1], dim_neg_per1, dict_c_neg[dim_neg_cod1]
    data['<dim_neg2>'], data['<per_neg2>'], data['<txt_neg2>'] = dict_dims[dim_neg_cod2], dim_neg_per2, dict_c_neg[dim_neg_cod2]