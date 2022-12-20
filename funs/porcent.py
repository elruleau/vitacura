from funs.otros import round_int

def porcent(x, y):
    """
    Entrega el valor de x, proporcional al total (x + y)
    x = Valor a porcentualizar
    y = El valor complemento
    """

    x = float(x)
    y = float(y)
    tot = x + y

    x_per = x/tot

    return x_per

def per_str(n=float, d=0):
    """
    Devuelve un str del valor en porcentaje con su respectivo signo para ingregrarlo en el pptx
    n = Número en decimal con valores entre 0 y 1
    d = Cantidad de decimales que aparecerán en el str
    """
    if d == 0:
        return str(round_int(n*100))+'%'
    elif d > 0:
        return str(round_int((n*100), d)).replace('.', ',')+'%'
    else:
        return 'Error!'