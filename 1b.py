from datetime import date
from datetime import datetime, timedelta
'''
R0 (fecha_es_tupla): Todas las fechas deben ser creadas como tuplas de tres números enteros
positivos (ternas), en este orden: (año, mes, día). El resultado de fecha_es_tupla (f) debe ser un
valor booleano, True o False.
'''
def fecha_es_tupla(fecha):
    try:
        if not isinstance(fecha, tuple) or len(fecha) != 3:
            return False
    
    # Todas las entradas son numeros enteros 
        if not all(isinstance(elem, int) for elem in fecha):
            return False
    
        # todas las entradas son positivas
        if not all(elem > 0 for elem in fecha):
            return False
    
    # verificacion de rangos estandar de mes y dia. 
        if not (1 <= fecha[1] <= 12) or not (1 <= fecha[2] <= 31):
            return False
    
        return True

    except (TypeError, IndexError):
        return False

'''
R1 (bisiesto): Dado un año perteneciente al rango permitido, determinar si este es bisiesto. El
resultado debe ser un valor booleano, True o False.
'''

def bisiesto(año):
    try:
        if año>= 1582:
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                return True
            else:
                return False
        else:
            return False
    except (TypeError, IndexError):
        return False


'''
R2 (fecha_es_valida): Dada una fecha, determinar si ésta es válida según el calendario
gregoriano. El resultado debe ser un valor booleano, True o False.
'''

def fecha_es_valida(fecha):
    try:
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
    except (TypeError, IndexError):
        return False



'''
R3 (dia_siguiente): Dada una fecha válida, determinar la fecha del día siguiente. El resultado
debe ser una fecha válida (tupla de tres números enteros positivos, que corresponde a una fecha
en el calendario gregoriano, conforme a nuestra convención).
'''

def dia_siguiente(fecha):     #fecha = (año, mes, dia)
    try:
        if (not fecha_es_tupla(fecha)):   #Se verifica que sea una tupla
            return "Debe ingresar una tupla con la fecha: (año, mes, dia)"

        if (not fecha_es_valida(fecha)):  #Se verifica que la fecha sea valida
            return "Debe ingresar una fecha válida"

        año = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        meses_30 = [4, 6, 9, 11]
        meses_31 = [1, 3, 5, 7, 8, 10]

        if (mes == 2):              #Se verifica si es febrero y se el año es bisiesto para cambiar de mes o no
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

        if (mes == 12):        #Se compara si es el ultimo dia del año para hacer el cambio de año
            if (dia == 31):
                return (año+1, 1, 1)
            else:
                return (año, mes, dia+1)

        if (mes in meses_30):        #Se compara si es el ultimo dia de un mes de 30 dias
            if (dia == 30):
                return (año, mes+1, 1)
            else:
                return (año, mes, dia+1)

        if (mes in meses_31):        #Se compara si es el ultimo dia de un mes de 31 dias
            if (dia == 31):
                return (año, mes+1, 1)
            else:
                return (año, mes, dia+1)  
    except (TypeError, IndexError):
        return False


#----------------------------------------------------------------------------------------------------------------------------------------------
'''
R4 (ordinal_dia): Dada una fecha válida, (año, mes, día), determinar cuál es la posición de esa
fecha dentro del año. Por ejemplo: ordinal_dia ((2021,1,1)) = 1, ordinal_dia ((2020,3,1)) = 61,
ordinal_dia ((2020,2,29)) = 60. Note que corresponde a 1 + el número de días transcurridos
desde el primero de enero de su año. El resultado debe ser un número entero. Pueden excluir
las fechas del año en que entró en vigencia el calendario gregoriano en Roma.
'''
def ordinal_dia(fecha):
    try:
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
                  
    except (TypeError, IndexError):
        return False

'''
R5 (imprimir_3x4): Dado un año perteneciente al rango permitido, desplegar en consola el
calendario de ese año en formato de 3 secuencias (‘filas’) de 4 meses cada una. El resultado
debe lucir semejante al que se muestra al final de este enunciado. Pueden excluir la impresión
del año en que entró en vigencia el calendario gregoriano en Roma.
'''

def imprimir_3x4(año):
    try:
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
    except (TypeError, IndexError):
        return False

#funcion auxiliar para imprimir el mes
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
    




#-------------------------------------------------------------------------------------------------------------------------------------------

'''
R6 (dia_semana): Dada una fecha válida, determinar el día de la semana que le
corresponde, con la siguiente codificación: 0 = domingo, 1 = lunes, 2 = martes, 3 =
miércoles, 4 = jueves, 5 = viernes, 6 = sábado. El resultado debe ser un número entero,
conforme a la codificación indicada.
'''

def dia_semana(fecha):
    try:
    # Verificar que la fecha sea valida
        if fecha_es_valida(fecha):

            año = fecha[0]
            mes = fecha[1]
            dia = fecha[2]

        # Congruencia de Zeller
        # https://es.wikipedia.org/wiki/Congruencia_de_Zeller

            a = int((14 - mes) / 12)
            y = año - a
            m = int(mes + (12 * a) - 2)
            d = int(dia + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7

        # Si la fecha es valida, retornar el dia de la semana
            return d
    
    # Si la fecha no es valida, retornar -1
        return -1
    except (TypeError, IndexError):
        return False

#dias = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
#dia = dia_semana((2023, 11, 12))
#print("dia_semana: ", dia, '=', dias[dia])

'''
R7(fecha_futura): Dados una fecha válida f y un número entero no-negativo n,
se quiere determinar la fecha que está n días naturales en el futuro. Si n es 0, entonces
fecha_futura(f, 0) = f. El resultado debe ser una fecha válida.
'''
def fecha_futura(fecha, n):
    try:
        año, mes, día = fecha

        # dias en año no bisieso
        días_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


        while n > 0:
            # ver si el año es bisiesto
            if bisiesto(año):
                días_por_mes[2] = 29
            else:
                días_por_mes[2] = 28

            días_en_mes_actual = días_por_mes[mes] - día + 1
            if n >= días_en_mes_actual:
                n -= días_en_mes_actual
                mes += 1
                día = 1

                if mes > 12:
                    mes = 1
                    año += 1
            else:
                día += n
                n = 0

        return año, mes, día
    except (TypeError, IndexError):
        return False


#print(fecha_futura((2023, 11, 14), 15))  

'''
R8 (dias_entre): Dadas dos fechas válidas, f1 y f2, sin importar si f1 ≤ f2 o f2 ≤ f1,
determinar el número de días naturales entre las dos fechas. Si f1 = f2, entonces
días_entre(f1, f2) = 0. El resultado debe ser un número entero no negativo.
'''

def dias_entre(f1, f2):
    try:
        if fecha_es_valida(f1) and fecha_es_valida(f2):

        # Si las fechas son iguales, retornar 0
            if f1 == f2:
                return 0
        
        # Si f1 es mayor que f2, intercambiarlas
            f1, f2 = min(f1, f2), max(f1, f2)

            dias = 0

            while f1 < f2:
                dias += 1
                f1 = dia_siguiente(f1)

            return dias
    except (TypeError, IndexError):
        return False

#print("dias_entre:", dias_entre((1590, 8, 17), (2100, 8, 17)))

'''
R9 (edad_al): Dadas dos fechas válidas, f1 y f2, donde f1 representa una fecha de
nacimiento y f2 es tal que f1 ≤ f2, determinar la edad de la persona en años, meses y
días cumplidos desde la fecha f1 hasta la fecha f2. El resultado debe ser una tupla (año,
mes, día); note que – en este caso – tal tupla no es necesariamente una fecha válida,
sino una tupla con los tres componentes enteros requeridos. El resultado debe ser una
tupla de tres números enteros no negativos.
'''
def edad_al(fecha_nacimiento):
    try:

        # Obtener la fecha actual del sistema
        fecha_actual = datetime.now()
        año_actual, mes_actual, día_actual = fecha_actual.year, fecha_actual.month, fecha_actual.day

        año_nacimiento, mes_nacimiento, día_nacimiento = fecha_nacimiento

        # Calcular la edad en años
        edad_años = año_actual - año_nacimiento

        # Si el cumpleaños no ha pasado aún, se ajusta la edad
        if (mes_actual, día_actual) < (mes_nacimiento, día_nacimiento):
            edad_años -= 1

        # Calcular los meses y días cumplidos
        if mes_actual < mes_nacimiento or (mes_actual == mes_nacimiento and día_actual < día_nacimiento):
            mes_actual += 12

        mes_cumplidos = mes_actual - mes_nacimiento
        día_cumplidos = día_actual - día_nacimiento

        # Ajustar los días si son negativos
        if día_cumplidos < 0:
            mes_cumplidos -= 1
            días_en_el_mes_anterior = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            # Verificar si el año de nacimiento es bisiesto
            if bisiesto(año_nacimiento):
                días_en_el_mes_anterior[2] = 29

            día_cumplidos = días_en_el_mes_anterior[mes_actual - 1] + día_cumplidos

        # Manejar meses negativos
        if mes_cumplidos < 0:
            mes_cumplidos += 12
            edad_años -= 1

        return edad_años, mes_cumplidos, día_cumplidos

    except (TypeError, IndexError):
        return False

'''
R10 (fecha_hoy): Obtener la fecha ‘del sistema’ a partir de la invocación de la función de
biblioteca de Pyhton today() , luego convertirla a una fecha válida 1 – tupla (año, mes,
día) – en el calendario gregoriano, según las convenciones usadas en esta asignación y
la anterior. El resultado debe ser una fecha válida. Ref. 
'''

def fecha_hoy():
    try:
        return (date.today().year, date.today().month, date.today().day);  #retorna de una vez la tupla con la fecha de hoy
    except (TypeError, IndexError):
        return False


'''
• R11 (edad_hoy): Dada una fecha válida f, que corresponde a la fecha de nacimiento de
alguna persona, determinar la edad de la persona en años, meses y días cumplidos
desde la fecha f hasta la fecha de hoy. Suponemos que f es menor o igual que la fecha
de hoy. El resultado debe ser una tupla (año, mes, día); note que – en este caso – eso
no es una fecha válida, sino una tupla con los tres componentes requeridos. El resultado
debe ser una tupla de tres números enteros no negativos.
'''

def edad_hoy(fecha):
    try:
        if (not fecha_es_tupla(fecha)):   #Se verifica que sea una tupla
            return "Debe ingresar una tupla con la fecha: (año, mes, dia)"

        if (not fecha_es_valida(fecha)) or (fecha[0] > date.today().year ):  #Se verifica que la fecha sea valida
            return "Debe ingresar una fecha válida"

        año = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        año_hoy = date.today().year
        mes_hoy = date.today().month
        dia_hoy = date.today().day

        meses_30 = [4, 6, 9, 11]

        if_año = año_hoy - año                 #Se saca la diferencia del año, del mes, y la del dia.
        dif_mes = mes_hoy - mes
        dif_dia = dia_hoy - dia

        if (dif_mes < 0):  #Si el mes es negativo se le resta uno al año ya que el mes de nacimiento es mayor que el actual 
            dif_año -= 1
            dif_mes += 12
    
        if (dif_dia < 0):  #Si el dia es negativo se le resta uno al mes ya que el dia de nacimiento es mayor que el actual 
            dif_mes -= 1
            x = dif_mes-1

            if (x == 2 and bisiesto(año)):   #Se le suman los dias del mes anterior a la diferencia de dias y aqui se verifica si es febrero, si es mes de 30 dias o si es de 31
                dif_dia += 29
            elif (x == 2 and not bisiesto(año)):
                dif_dia += 28
            else:
                dif_dia += 31

        return (dif_año, dif_mes, dif_dia)
    except (TypeError, IndexError):
        return False



while True:
    try:
        print("Elija una opción:")
        print("0. Salir")
        print("1. Verificar si una fecha es tupla")
        print("2. Verificar si un año es bisiesto")
        print("3. Determinar el día siguiente a una fecha")
        print("4. Determinar el ordinal del día en un año")
        print("5. Imprimir un calendario")
        print("6. Determinar el día de la semana de una fecha")
        print("7. Determinar una fecha en el futuro")
        print("8. Determinar días entre dos fechas")
        print("9. Determinar la edad desde una fecha hasta hoy")
        print("10.Obtener la fecha de hoy")
        print("11. Determinar la edad hasta el dia de hoy")
        
        opcion = input("Ingrese el número de la opción (0 para salir): ")

        if opcion == '0':
            break
        if opcion == '1':
            fecha = eval(input("Ingrese una fecha en formato de tupla (año, mes, día): "))
            print("fecha_es_tupla:", fecha_es_tupla(fecha))
        elif opcion == '2':
            año = int(input("Ingrese un año: "))
            print("Bisiesto:", bisiesto(año))
        elif opcion == '3':
            fecha = eval(input("Ingrese una fecha en formato de tupla (año, mes, día): "))
            print("fecha_es_valida:", fecha_es_valida(fecha))
        elif opcion == '4':
            fecha = eval(input("Ingrese una fecha en formato de tupla (año, mes, día): "))
            print("dia_siguiente:", dia_siguiente(fecha))
        elif opcion == '5':
            fecha = eval(input("Ingrese una fecha en formato de tupla (año, mes, día): "))
            print("ordinal_dia:", ordinal_dia(fecha))
        elif opcion == '6':
            año = int(input("Ingrese un año: "))
            print("dia_semana:")
            dia_semana(año)
        elif opcion == '7':
            fecha = eval(input("Ingrese una fecha en formato de tupla (año, mes, día): "))
            num = int(input("Ingrese un numero: "))
            print("fecha_futura:", fecha_futura(fecha,num))
        elif opcion == '8':
            fecha1 = eval(input("Ingrese una fecha en formato de tupla (año, mes, día): "))
            fecha2 = eval(input("Ingrese una fecha2 en formato de tupla (año, mes, día): "))
            print("dias_entre:", dias_entre(fecha1,fecha2))
        elif opcion == '9':
             fecha = eval(input("Ingrese una fecha  en formato de tupla (año, mes, día): "))
             print("edad_al:", edad_al(fecha))
        elif opcion == '10':
            print("fecha_hoy:", fecha_hoy())
        elif opcion == '11':
            fecha = eval(input("Ingrese una fecha DE NACIMIENTO en formato de tupla (año, mes, día): "))
            print("edad_hoy:", edad_hoy(fecha))
        else:
            print("Opción no válida. Por favor, ingrese un número de opción válido.")

    except (TypeError, IndexError):
        print("Algo salio mal") 