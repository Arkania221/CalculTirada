"""

1. ¿Que se necesita? Se precisa saber la probabilidad de que toque cierto resultado
   mas los posibles resultados menores.

2. Los posibles resultados vienen dados de la suma de dos dados de seis caras 
   (2 - 12)

3. El resultado a operar sera ofrecido por el usuario, se debe invalidad cualquier
   dato dado por el usuario que ses salga fuera del rango.

    3.1. Para evitar la entrada de numeros que no puedan ser manejados por los dados,
         "int", se utiliza el metodo isdigit() que itera sobre toos los caracteres
         de la varible dada confirmando que estos sean "int", lo que termina evitando
         la entrada de floats o str's.

4. Para calcular su porcentaje de probabilidad se debe realizar la siguiente 
   operacion: [Suma de la cantidad de posibles resultados que den X o inferior]
   * 100 / 36 
   
    4.1. Para lograr hacer la suma de posibilidad se debera iterar sobre los
         dados, pasando por todas las posibilidades que den como resultado X

5. Se debe mostrar por pantalla el porcentaje de probabilidad del numero.

"""

dado1 = [1, 2, 3, 4, 5, 6]
dado2 = [1, 2, 3, 4, 5, 6]

def Calculo100(numero):
    casos = 0
    for i in dado1:
        for j in dado2:
            resultado = (i + j)
            
            if resultado <= numero:
                casos += 1
            else:
                break
    resultado = (casos * 100 / 36)
    porcent = round(resultado, 1)
    return(porcent)




def Programa():
    while True:
        enter = input("Por favor introduce el numero (2 - 12): ")
        
        if not enter.isdigit():
            print("Por favor introduzca un número válido.")
            continue 
        num = int(enter)
        if num < 2 or num > 12:
            print("Por favor introduzca un número válido.")
        else:
            porcent = Calculo100(num)
            print("La probabilidad es de: ", porcent, "%")


Programa()