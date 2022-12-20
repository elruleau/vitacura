import pandas as pd

def round_int(number):
    """
    Redondea un valor a un número entero
    """
    x = (number - 0.5) + 1
    return int(x)

def saca_espacios(df):
    """
    Elimina todos los espacios vacíos antes y depués de un caracter
    """
    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    return df

def get_unique(df, column=str):
    """
    Devuelve los valores únicos de una columna específica, ordenados
    """
    return sorted(list(pd.unique([i for i in df[column] if type(i) == str])))


def txt_replace(prs, data, nro_slide=int, nro_shape=int, txt=str):
    """
    Reemplaza SOLO UN texto, sin alterar el formato.
    Sirve para ocaciones específicas.

    txt = Texto que se encuentra en el diccionario, sin los brakets '<>'
    """

    slides = prs.slides[nro_slide-1]
    shape = slides.shapes[nro_shape]
    text_frame = shape.text_frame
    paragraphs = text_frame.paragraphs

    for p in range(len(paragraphs)):

        paragraph = text_frame.paragraphs[p]
        p = paragraph._p

        for run in paragraph.runs:
            run.text = run.text.replace('>', '')
            run.text = run.text.replace('<', '')
            if run.text == txt[1:-1]:
                run.text = data[f'{txt}']


def count_areas(df):
    """
    Entrega un diccionario con la cantidad de regitros de personas
    en una base de datos específica. Se puede usar para obtener la tasa de respuesta
    """
    dot = {}

    for i in df.columns:
        if i[:3] == 'seg':
            for j in df[i].unique():
                if type(j) == str:
                    dot[j] = len(df[df[i] == j])

    return dot