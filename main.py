import pandas as pd




def capturar_cadena(cadena):
    consonantes = {}
    operadores = {}

    for caracter in cadena:
        if caracter.isalpha() and caracter.lower() in 'bcdfghjklmnpqrstvwxyz':
            consonantes[caracter] = 0
        elif caracter in '!&|>=':
            operadores[caracter] = 0

    n = len(consonantes)
    df = pd.DataFrame(generate_truth_combinations(n), columns=consonantes.keys())

    return df

def generate_truth_combinations(n):
    if n == 0:
        return [[]]
    else:
        smaller_combinations = generate_truth_combinations(n - 1)
        return [[True] + rest for rest in smaller_combinations] + [[False] + rest for rest in smaller_combinations]


def disyuncion(operando1, operando2):
    return operando1 or operando2

def conjuncion(operando1, operando2):
    return operando1 and operando2

def implicacion(operando1, operando2):
    return (not operando1) or operando2

def doble_implicacion(operando1, operando2):
    return operando1 == operando2

def calcular_operacion(df, operacion):
    for idx, row in df.iterrows():
        resultado = row[operacion[0]]
        for i in range(1, len(operacion), 2):
            operador = operacion[i]
            operando = row[operacion[i+1]]
            if operador == '|':
                resultado = disyuncion(resultado, operando)
            elif operador == '&':
                resultado = conjuncion(resultado, operando)
            elif operador == '>':
                resultado = implicacion(resultado, operando)
            elif operador == '=':
                resultado = doble_implicacion(resultado, operando)
        df.loc[idx, operacion] = resultado

cadena = input("Cadena a procesar: ")
cadena_sin_espacios = cadena.replace(" ", "")
df = capturar_cadena(cadena_sin_espacios)
calcular_operacion(df, cadena_sin_espacios)
print(df)

