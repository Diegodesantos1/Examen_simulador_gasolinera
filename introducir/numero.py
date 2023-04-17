"""
Módulo que agrupa todas las funcionalidades
que permiten solicitar introducir un dato numérico
"""


import sys


MIN = 0
MAX = 100


def solicitar_introducir_numero_binario(invite):
    """
    Esta función verifica que tenemos un número
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end="")
        datoIntroducido = input()

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            print(
                "Solo están autorizados los caracteres [0-1].", file=sys.stderr)
        else:
            "comprueba que solo son 1s y 0s"
            for num in str(datoIntroducido):
                if num not in "01":
                    print(
                        "Solo están autorizados los caracteres [0-1].", file=sys.stderr)
                    break
            else:
                # Tenemos lo que queremos, salimos del bucle saliendo de la función
                return datoIntroducido


def solicitar_introducir_numero(invite):
    """
    Esta función verifica que tenemos un número
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end="")
        datoIntroducido = input()

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            print("Solo están autorizados los caracteres numéricos.", file=sys.stderr)
        else:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido


def solicitar_introducir_numero_extremo(invite, minimum=MIN, maximum=MAX):
    """
    Esta función utiliza el anterior y añade una post-condición
    sobre los extremos del número a introducir
    """
    invite = "{}".format(invite)
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        datoIntroducido = solicitar_introducir_numero(invite)

        if minimum <= datoIntroducido <= maximum:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido
