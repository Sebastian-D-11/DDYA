def evaluar_signo(num):
    # Punto 1: Positivo, negativo o cero
    if num == 0:
        print("El número es cero")
    elif num < 0:
        print("El número es negativo")
    else:
        print("El número es positivo")

def evaluar_paridad(num):
    # Punto 2: Par o impar
    if num % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

def es_fibonacci(num):
    # Punto 3: Serie de Fibonacci 
    a = 0
    b = 1
    while a < num:
        c = a + b
        a = b
        b = c
    
    if a == num and num >= 0:
        print("El número si es de la serie Fibonacci")
    else:
        print("El número no es de la serie Fibonacci")

def es_primo(num):
    # Punto 4: Determinar si es primo
    num_entero = int(num)
    if num_entero <= 1:
        print("El número no es primo")
        return

    divisores = 0
    for i in range(1, num_entero + 1):
        if num_entero % i == 0:
            divisores = divisores + 1
            
    if divisores == 2:
        print("El número si es primo")
    else:
        print("El número no es primo")

def sumar_intermedios(n1, n2):
    # Punto 5: Suma de números intermedios
    n1 = int(n1)
    n2 = int(n2)
    
    if n1 < n2:
        menor = n1
        mayor = n2
    else:
        menor = n2
        mayor = n1
        
    suma = 0
    for i in range(menor + 1, mayor):
        suma = suma + i
        
    print("La suma de los números intermedios es:", suma)

def elevar_segun_paridad(num):
    # Punto 6: Impar o par
    if num % 2 == 0:
        resultado = num * num * num
        print("Como es par, elevado al cubo es:", resultado)
    else:
        resultado = num * num
        print("Como es impar, elevado al cuadrado es:", resultado)

def fecha_codigo_estudiante(cadena):
    # Punto 8: fecha de nacimiento y codigo de estudiante
    mes = ""
    numero_str = ""
    
    for caracter in cadena:
        if caracter >= 'a' and caracter <= 'z' or caracter >= 'A' and caracter <= 'Z':
            mes = mes + caracter
        elif caracter >= '0' and caracter <= '9':
            numero_str = numero_str + caracter
            
    print("\nMes extraído:", mes)
    
    if numero_str != "":
        num_resultante = float(numero_str)
    else:
        num_resultante = 0.0
        
    print("Número resultante extraído:", num_resultante)
    return mes, num_resultante

def analizar_vocales_consonantes(texto):
    # Punto 9: Separar vocales y consonantes
    vocales = ""
    consonantes = ""
    
    for letra in texto.lower():
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vocales = vocales + letra + " "
        else:
            consonantes = consonantes + letra + " "
            
    print("Vocales encontradas:", vocales)
    print("Consonantes encontradas:", consonantes)

def posicion_abecedario(texto):
    # Punto 10: Posición en el abecedario
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    print("Posición de las letras en el abecedario:")
    
    for letra in texto.lower():
        posicion = 1
        for letra_abc in abecedario:
            if letra == letra_abc:
                print("Letra '" + letra + "' está en la posición:", posicion)
                break
            posicion = posicion + 1


def main():
    print("Buen dia, se realizara la prueba diagnostica\n")
    
    entrada = input("Ingrese su fecha de nacimiento y código del carnet estudiantil (ejemplo: 1enero2000100032300) o un número: ")
    
    # Comprobar si la entrada tiene letras buscando manualmente
    tiene_letras = False
    for caracter in entrada:
        if caracter >= 'a' and caracter <= 'z' or caracter >= 'A' and caracter <= 'Z':
            tiene_letras = True
            break
            
    if tiene_letras:
        mes, num = separar_mes_y_numero(entrada)
        analizar_vocales_consonantes(mes)
        posicion_abecedario(mes)
    else:
        num = float(entrada)
        
    print("\n--- Resultados del número ---")
    evaluar_signo(num)
    evaluar_paridad(num)
    es_fibonacci(num)
    es_primo(num)
    elevar_segun_paridad(num)
    
    print("\n--- Suma de intermedios ---")
    num2 = float(input("Ingrese un segundo número: "))
    sumar_intermedios(num, num2)

main()
