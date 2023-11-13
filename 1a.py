'''
R0 (fecha_es_tupla): Todas las fechas deben ser creadas como tuplas de tres números enteros
positivos (ternas), en este orden: (año, mes, día). El resultado de fecha_es_tupla (f) debe ser un
valor booleano, True o False.
'''

def fecha_es_tupla(fecha):
    return (
        type(fecha) == tuple and len(fecha) == 3 and 
        type(fecha[0]) == int and type(fecha[1]) == int and type(fecha[2]) == int 
        and fecha[0] > 0 and fecha[1] > 0 and fecha[2] > 0)

    
fecha_tupla = (2019, 10, 10)
print("R0: ", fecha_es_tupla(fecha_tupla))

'''
R1 (bisiesto): Dado un año perteneciente al rango permitido, determinar si este es bisiesto. El
resultado debe ser un valor booleano, True o False.
'''

def bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False


'''
R2 (fecha_es_valida): Dada una fecha, determinar si ésta es válida según el calendario
gregoriano. El resultado debe ser un valor booleano, True o False.
'''

def fecha_es_valida(fecha):

    # Verificar que el formato de la fecha sea una tupla
    if fecha_es_tupla(fecha):
        
        # Verificar que la fecha sea mayor al 4 de octubre de 1582
        if fecha >= (1582, 10, 4):

            # Verificar que el mes este entre 1 y 12
            if fecha[1] >= 1 and fecha[1] <= 12:

                meses_con_31_dias = [1, 3, 5, 7, 8, 10, 12]
                meses_con_30_dias = [4, 6, 9, 11]

                # Si es un mes con 31 dias, verificar que el dia este entre 1 y 31
                if fecha[1] in meses_con_31_dias: 
                    return fecha[2] >= 1 and fecha[2] <= 31
                
                # Si es un mes con 30 dias, verificar que el dia este entre 1 y 30
                elif fecha[1] in meses_con_30_dias:
                    return fecha[2] >= 1 and fecha[2] <= 30
                
                # Si el mes es febrero
                elif fecha[1] == 2:
                    if bisiesto(fecha[0]):
                        # Si el año es bisiesto verificar que el dia este entre 1 y 29
                        return fecha[2] >= 1 and fecha[2] <= 29
                    else:
                        # Si el año no es bisiesto verificar que el dia este entre 1 y 28
                        return fecha[2] >= 1 and fecha[2] <= 28
                    
    # Si no cumple con las condiciones anteriores, la fecha no es valida
    return False

fecha_valida = (2023, 2, 28);
otra_fecha_valida = (2024, 2, 29);

fecha_no_valida = (2023, 2, 29);
otra_fecha_no_valida = (2024, 4, 31);

print("R2: ", fecha_es_valida(otra_fecha_valida))

'''
R3 (dia_siguiente): Dada una fecha válida, determinar la fecha del día siguiente. El resultado
debe ser una fecha válida (tupla de tres números enteros positivos, que corresponde a una fecha
en el calendario gregoriano, conforme a nuestra convención).
'''

def dia_siguiente(fecha):     #fecha = (año, mes, dia)

    if (not fecha_es_tupla(fecha)):   #Se verifica que sea una tupla
        return "Debe ingresar una tupla con la fecha: (año, mes, dia)"

    if (not fecha_es_valida(fecha)):  #Se verifica que la fecha sea valida
        return "Debe ingresar una fecha válida"

    año = fecha[0]
    mes = fecha[1]
    dia = fecha[2]

    meses_30 = [4, 6, 9, 11]
    meses_31 = [1, 3, 5, 7, 8, 10]

    if (mes == 2):              #aqui se verifica si es febrero y se el año es bisiesto para cambiar de mes o no
        if (bisiesto(año)):
            if (dia == 29):
                return (año, mes+1, 1)
            else:
                return (año, mes, dia+1)
        else:
            if (dia == 28):
                return (año, mes+1, 1)
            else:
                return (año, mes, dia+1)

    if (mes == 12):        #aqui se compara si es el ultimo dia del año para hacer el cambio de año
        if (dia == 31):
            return (año+1, 1, 1)
        else:
            return (año, mes, dia+1)

    if (mes in meses_30):        #aqui se compara si es el ultimo dia de un mes de 30 dias
        if (dia == 30):
            return (año, mes+1, 1)
        else:
            return (año, mes, dia+1)

    if (mes in meses_31):        #aqui se compara si es el ultimo dia de un mes de 31 dias
        if (dia == 31):
            return (año, mes+1, 1)
        else:
            return (año, mes, dia+1)  

'''
R4 (ordinal_dia): Dada una fecha válida, (año, mes, día), determinar cuál es la posición de esa
fecha dentro del año. Por ejemplo: ordinal_dia ((2021,1,1)) = 1, ordinal_dia ((2020,3,1)) = 61,
ordinal_dia ((2020,2,29)) = 60. Note que corresponde a 1 + el número de días transcurridos
desde el primero de enero de su año. El resultado debe ser un número entero. Pueden excluir
las fechas del año en que entró en vigencia el calendario gregoriano en Roma.
'''
def ordinal_dia(fecha):

    if (not fecha_es_tupla(fecha)):   #Se verifica que sea una tupla
        return "Debe ingresar una tupla con la fecha: (año, mes, dia)"

    if (not fecha_es_valida(fecha)):  #Se verifica que la fecha sea valida
        return "Debe ingresar una fecha válida"

    meses_30 = [4, 6, 9, 11]

    año = fecha[0]
    mes = fecha[1]
    dia = fecha[2]

    dias_del_año = 0

    if (mes > 2 and bisiesto(año)):      #Si el mes es mayor a 2 y el año es bisiesto, se le suma un dia extra
        dias_del_año += 1
        
    for mes_ant in range(1, mes):      #aqui se suman los dias de los meses anteriores
        if (mes_ant == 2):
            dias_del_año += 28
        elif (mes_ant in meses_30):
            dias_del_año += 30
        else:
            dias_del_año += 31

    return dias_del_año + dia             #Se le suma el dia del mes en el que esta            

'''
R5 (imprimir_3x4): Dado un año perteneciente al rango permitido, desplegar en consola el
calendario de ese año en formato de 3 secuencias (‘filas’) de 4 meses cada una. El resultado
debe lucir semejante al que se muestra al final de este enunciado. Pueden excluir la impresión
del año en que entró en vigencia el calendario gregoriano en Roma.
'''

def imprimir_3x4(año):

    # Verificar que el año sea mayor al año en que entró en vigencia el calendario gregoriano en Roma
    if año > 1582:
        
        print("    --------------------------------- Calendario del año", año, "D.C. ------------------------------------")

        print()

        # Definir los nombres de los meses
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre"]
        
        # Definir la cantidad de dias de cada mes
        dias_por_mes = [31, 28 if not bisiesto(año) else 29, 31, 30, 31, 30, 
                        31, 31, 30, 31, 30, 31]
        
        # Almacena los datos de las semanas
        semanas = []

        # Recorre los meses
        for i in range(0, len(meses)):
            
            # Obtiene la ubicacion del primer dia del mes
            primer_dia = primer_dia_del_mes(año, i + 1)

            semana = [] # Almacena los datos de las semanas
            dias = [] # Almancena los dias de esa semana
            dia = 1 # Contador de los dias

            # tamaño del calendario es 6 x 7
            for j in range(0, 6 * 7):

                # Empieza a contar desde el primer dia del mes
                # Y hasta el ultimo dia del mes, sustrayendo la posicion del primer dia del mes
                if j == primer_dia or j > primer_dia and j - primer_dia < dias_por_mes[i]:
                    dias.append(str(dia).rjust(2, ' '))
                    dia = dia + 1
                else:
                    # Si todavía no es el primer dia o ya pasó el ultimo dia, se llena con espacios en blancos
                    dias.append(str.rjust('', 2, ' '))
                    
            # Recorre la lista de dias y los une en una sola cadena de texto
            for i in range(0, len(dias), 7):
                semana.append(' '.join(str(e) for e in dias[i:i + 7]))

            # Guarda la cadena de texto de la semana en el array
            semanas.append(semana)

        # Imprime el calendario por secciones
        size = 4
        for i in range(0, len(meses), size):
            print_mes([
                meses[i:i + size],
                semanas[i:i + size]
            ])
            print()
    else:
        print("El año debe ser mayor al año en que entró en vigencia el calendario gregoriano en Roma (1582)")

def print_mes(data):

    # Recibe un array 7x7 con los datos del mes
    width = 25
    fill = ' '

    # Imprime los encabezados
    monthHeader = ''
    weekDaysHeader = ''
    week0 = ''
    week1 = ''
    week2 = ''
    week3 = ''
    week4 = ''
    week5 = ''

    for value in data[0]:
        monthHeader += str.center(value, width, fill) + '|'
        weekDaysHeader += str.center(' D  L  K  M  J  V  S', width, fill) + '|'

    for week in data[1]:
        week0 += str.center(week[0], width, fill) + '|'
        week1 += str.center(week[1], width, fill) + '|'
        week2 += str.center(week[2], width, fill) + '|'
        week3 += str.center(week[3], width, fill) + '|'
        week4 += str.center(week[4], width, fill) + '|'
        week5 += str.center(week[5], width, fill) + '|'

    print(monthHeader)
    print(weekDaysHeader)
    print(week0)
    print(week1)
    print(week2)
    print(week3)
    print(week4)
    print(week5)


def primer_dia_del_mes(año, mes):
        
    dia = 1

    # Congruencia de Zeller
    # https://es.wikipedia.org/wiki/Congruencia_de_Zeller

    a = int((14 - mes) / 12)
    y = año - a
    m = int(mes + (12 * a) - 2)
    d = int(dia + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7

    # Si la fecha es valida, retornar el dia de la semana
    return d
    

print("R5: ")
imprimir_3x4(1583)


