def criterios(df, area):
    """
    Entrega la cantidad de personas que respondieron la encuesta según su área
    y la tasa de respuesta de cada áreas
    df = Base de datos
    area = Área (perdón la falta de creatividad)
    """
    return df.loc[area][1] , df.loc[area][1]/df.loc[area][0]