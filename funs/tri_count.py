def tri_count(df, dims, items, print=False):
    """
    Crea columnas con el contero de la frecuencia de valores positivos, neutros y negativos en los items, según su dimensión corrspondiente.
    
    dims = Sigla de las dimensiones (en mayúscula y sín número)
    items = Sigla de los ítems (en minúscula y con número)
    print = Ver los items que se consideraron en la creación de las columnas según dimensión

    *En esta parte es muy importante que las dimensiones y los items ingresados sean los mismos que se usaron en el estudio
    """

    for d in dims:
        x = []
        for i in items:
            if i in df.columns:
                if i[:3].upper() == d:
                    x.append(i)
            else:
                raise Exception(f'El ítem {i} no se encuentra en la base de datos')
        if print == True:
            print(x)
        df[f"{d}_pos"] = (df[x] >= 4).sum(axis=1)
        df[f"{d}_neu"] = (df[x] == 3).sum(axis=1)
        df[f"{d}_neg"] = (df[x] <= 2).sum(axis=1)
    
    return df