cadena = '__servidor1'
cadena2 = '3servidor'
cadena3 = '__a3'
cadena4 = 'aaaa3+'

def afd(entrada):
    estado = 0
    for i in range(len(entrada)):
        if estado == 0:
            if entrada[i] == '_':
                estado = 1
            elif entrada[i].isalpha():
                estado = 2
            else:
                print("ERROR// Cadena incorrecta")
                return
        elif estado == 1:
            if entrada[i] == '_':
                estado = 1
            elif entrada[i].isalpha():
                estado = 3
            else:
                print("ERROR// Cadena incorrecta")
                return
        elif estado == 2:
            if entrada[i].isalpha():
                estado = 2
            elif entrada[i].isdigit():
                estado = 4
            else:
                print("ERROR// Cadena incorrecta")
                return
        elif estado == 3:
            if entrada[i].isdigit():
                estado = 4
            else:
                print("ERROR// Cadena incorrecta")
                return
        elif estado == 4:
            if entrada[i] != None:
                print("ERROR// Cadena incorrecta")
                return

    print("CADENA ACEPTADA CON EXITO!!!")

afd(cadena)
afd(cadena2)
afd(cadena3)
afd(cadena4)