# Replace the "ANSWER HERE" for your answer

def enumerate_list(lst):
    """
    Dada una lista de strings, retorna una nueva lista donde cada elemento
    tiene el formato "indice. valor". Los strings vacios se deben saltear
    y no deben aparecer en la lista resultante.
    El indice debe ser consecutivo (no el indice original).

    Ejemplo: enumerate_list(["Red", "Green", "", "White"]) -> ["0. Red", "1. Green", "2. White"]
    """
    palabra = []
    indice = -1
    for valor_0, valor in enumerate(lst):
        if valor != "":
            indice = indice + 1
            palabra.append(f"{indice}. {valor}")
    return palabra


def enumerate_backwards(lst):
    """
    Igual que enumerate_list, pero cada palabra debe estar escrita al reves.
    Los strings vacios se deben saltear.

    Ejemplo: enumerate_backwards(["Red", "Green", ""]) -> ["0. deR", "1. neerG"]
    """
    palabra = []
    indice = -1
    for valor_0, valor in enumerate(lst):
        if valor != "":
            indice = indice + 1
            palabra.append(f"{indice}. {valor[::-1]}")
    return palabra
