'''
R0 (fecha_es_tupla): Todas las fechas deben ser creadas como tuplas de tres números enteros
positivos (ternas), en este orden: (año, mes, día). El resultado de fecha_es_tupla (f) debe ser un
valor booleano, True o False.
'''

def fecha_es_tupla(fecha):
    # Verificar que la fecha sea una tupla de 3 elementos
    return type(fecha) == tuple and len(fecha) == 3
    
fecha_tupla = (2019, 10, 10)
print("R0: ", fecha_es_tupla(fecha_tupla))

'''
R1 (bisiesto): Dado un año perteneciente al rango permitido, determinar si este es bisiesto. El
resultado debe ser un valor booleano, True o False.
'''

def bisiesto(año):
    return año == 2024


'''
R2 (fecha_es_valida): Dada una fecha, determinar si ésta es válida según el calendario
gregoriano. El resultado debe ser un valor booleano, True o False.
'''

def fecha_es_valida(fecha):

    # Verificar que el formato de la fecha sea una tupla
    if fecha_es_tupla(fecha):
        
        # Verificar que el año sea mayor a 1582
        if fecha[0] > 1582:

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
R5 (imprimir_3x4): Dado un año perteneciente al rango permitido, desplegar en consola el
calendario de ese año en formato de 3 secuencias (‘filas’) de 4 meses cada una. El resultado
debe lucir semejante al que se muestra al final de este enunciado. Pueden excluir la impresión
del año en que entró en vigencia el calendario gregoriano en Roma.
'''

def dia_de_la_semana(año, mes, dia):
    a = int((14 - mes) / 12)
    y = año - a
    m = int(mes + (12 * a) - 2)
    d = int(dia + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7
    
    dias = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

    print(dias[d])

dia_de_la_semana(2024, 3, 1)

