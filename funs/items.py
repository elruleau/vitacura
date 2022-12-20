from numpy import unique

def items (dict = {}, dim= ''):
    """
    Invoca en enuncuado de los ítems que compone una dimensión específica
    Crea una lista con los respectivos enunciados.

    dict = Diccionario donde se encuentran todos los ítems con sus respectivas siglas
    dim  = Dimensión que se desa analizar 
    """
    items = []
    for i in dict.keys():
        if i[:3] == dim:
            items.append(dict[i])
    return items

def sum_lists(*args):
    """
    Suma el contenido de las listas
    """
    return list(map(sum, zip(*args)))

def get_pts_items(df, dim='', signo = ''):

    dim_pos = []
    dim_neu = []
    dim_neg = []

    items = [i for i in df.columns if i[:3] == dim.lower()]

    for i in items:
        tmp_pos = df[df[i] >= 4][i].count()
        tmp_neu = df[df[i] == 3][i].count()
        tmp_neg = df[df[i] <= 2][i].count()

        dim_pos.append(tmp_pos)
        dim_neu.append(tmp_neu)
        dim_neg.append(tmp_neg)

    tot = sum_lists(dim_pos, dim_neu, dim_neg)

    dim_per_pos = [dim_pos[j]/tot[j] for j in range(len(items))]
    dim_per_neu = [dim_neu[j]/tot[j] for j in range(len(items))]
    dim_per_neg = [dim_neg[j]/tot[j] for j in range(len(items))]

    if signo == 'pos':
        return dim_per_pos
    elif signo == 'neu':
        return dim_per_neu
    elif signo == 'neg':
        return dim_per_neg
    else:
        return False


def top_items(df, dict_items, dims=list, signo=str, drop=['PBD', 'CFZ'], top=3):
    """
    Entrega un diccionario de los ítems y sus puntajes proporcionales según su signo.
    Se calcula al sacar la proporción de la 'positividad', 'neutralidad' o 'negatividad' de cada ítem
    Es decir, cuál obtuvo una mayor porción de respuesta según el signo.
    
    El diccionario está ordenado de mayor a menor según su valor
    En caso de que los porcentajes sean iguales, se considerará un orden alfabético inverso

    df = Base de datos
    dims = Dimensiones elegidas 'organizacionales' o 'locales'
    signo = pos, neu o neg
    top = Cantidad de elementos que tendrá el diccionario
    """

    itms = [i for i in dict_items.keys() if i[:3].upper() not in drop]

    if type(dims) == list:
        itms = [i for i in itms if i[:3].upper() in dims]
    else:
        raise TypeError("Se debe elegir el tipo de dimensiones ('loc', 'org')")

    dict_items = {}

    for i in itms:
        series_val = df[i].value_counts('%').reindex([1,2,3,4,5], fill_value = 0)
        if signo == 'pos':
            dict_items[i] = series_val[4] + series_val[5]
        elif signo == 'neu':
            dict_items[i] = series_val[3]
        elif signo == 'neg':
            dict_items[i] = series_val[2] + series_val[1]

    dict_items_sorted = dict(sorted(dict_items.items(), key=lambda item: item[1], reverse=True))

    if top == False:
        return dict_items_sorted
    else:
        dict_filt = {}
        for i in range(top):
            dict_filt[list(dict_items_sorted.keys())[i]] = list(dict_items_sorted.values())[i]
        return dict_filt