def comparar_cadenas_lexicograficas(cadena1, cadena2):
    if cadena1<cadena2:
        print("-1")
    elif cadena2<cadena1:
        print("1")
    else:
        print("0")
    pass

#Ejemplo
print(comparar_cadenas_lexicograficas("abc", "abd"))