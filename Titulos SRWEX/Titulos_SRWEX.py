
LARGO_DS = "Ke"
LARGO_NUEVE = "MWm9"
LARGO_OCHO = "ABCDEFGHJKLNOPQRSTUVXYZÜ-abcdeghknopqsuvwxyzñáéóú02356789"
LARGO_SIETE = "f"
LARGO_SEIS = "rt1"
LARGO_CINCO = ",'"
LARGO_CUATRO = "Iijl!.¡í"
ESPACIO = 3

def ingresar_caracteres():
    caracteres = input("Ingrese caracteres: ")
    return caracteres

def ingresar_inicio_posicion():
    inicio_pos = input("Ingresar inicio de posición en valor hex (2 caracteres): ")
    try:
        return int(inicio_pos, 16)
    except ValueError:
        return "Valor Hex invalido."
    
def contar_y_cambiar(caracteres):
    contador = 0
    for i in range(len(caracteres)):
        if caracteres[i] != " ":
            contador += 1
    
    return contador
    
def sumar_hex(caracter, posicion):
    largo_caracter = saber_largo(caracter)
    nueva_posicion = largo_caracter + posicion

    return nueva_posicion

def saber_largo(caracter):
    if caracter in LARGO_NUEVE:
        return 9
    if caracter in LARGO_OCHO:
        return 7
    if caracter in LARGO_SIETE:
        return 6
    if caracter in LARGO_SEIS:
        return 5
    if caracter in LARGO_CINCO:
        return 4
    if caracter in LARGO_CUATRO:
        return 3
    if caracter == " ":
        return ESPACIO

    
def crear_lista(caracteres, inicio_pos):
    lista_vacia = []
    for c in range(len(caracteres)):
        if c == 0:
            lista_vacia.append([caracteres[c], hex(inicio_pos)[2:]])
            posicion = sumar_hex(caracteres[c], inicio_pos)
        else:
            """print(hex(posicion), "y ", hex(posicion)[2:])"""
            lista_vacia.append([caracteres[c], hex(posicion)[2:]])
            posicion = sumar_hex(caracteres[c], posicion)
    
    return lista_vacia

def quitar_espacio(lista):
    listado = []
    for valor, hex in lista:
        if valor != " ":
            if len(hex) == 3:
                 listado.append([valor, hex[1:].upper()])
            else:
                listado.append([valor, hex.upper()])

    return listado
        
def unir_todo(lista):
    letras = ""
    for i in lista:
        letras += (" = ".join(i) + ", ")
    return letras

def main():
    caracteres = ingresar_caracteres()
    inicio_pos = ingresar_inicio_posicion()
    largo = contar_y_cambiar(caracteres)

    lista = crear_lista(caracteres, inicio_pos)
    
    #print(lista)
    print(unir_todo(quitar_espacio(lista))[:-2])
    print("Total: ", largo, "| Hex: ", hex(int(largo))[2:])


    input("Presiona Enter para salir.")

main()


