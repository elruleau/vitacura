def dict_ir(df_sub, df_imp, dims=list, top=4):
    """
    Crea un diccionario ordenado de mayor a menor con los puntajes en importancia relativa
    donde la key es la sigla de la dimensión y el valor el el puntaje obtenido por la fórmula
    """
    
    # Filtrar la base de datos según índice
    df_imp_filt = df_imp[df_imp.index.isin(df_sub.index)][dims]

    tmp_min = df_imp_filt.min().min()
    tmp_max = df_imp_filt.max().max()
    rango = tmp_min + tmp_max
    
    df_imp_filt_in = rango - df_imp_filt

    tmp_count = df_imp_filt_in.count().sum()
    tmp_sum = df_imp_filt_in.sum()
    tmp_dict = (tmp_sum/tmp_count).to_dict()

    tmp_dict_sorted = dict(sorted(tmp_dict.items(), key=lambda item: item[1], reverse=True))
    
    tmp_dict_sorted_filt= {}

    for i in range(top):
        tmp_dict_sorted_filt[list(tmp_dict_sorted.keys())[i]] = list(tmp_dict_sorted.values())[i]
    
    return tmp_dict_sorted_filt