'''
Operadores
'''

# Operadores aritmeticos

print(f"{10 + 3}") #suma
print(f"Suma: 10 + 3 = {10 + 3}") # Aqui le añado texto para que aparezca mejor en consola
print(f"Resta: 10 - 3 = {10 - 3}") # Aqui realizo una resta
print(f"Multiplicacion: 10 * 3 = {10 * 3}") # Aqui realizo una multiplicacion
print(f"Division: 10 / 3 = {10 / 3}") # Aqui realizo una division
print(f"Modulo: 10 % 3 = {10 % 3}") # El modulo es el residuo o lo que le sobra a la operacion
print(f"Exponente: 10 ** 3 = {10 ** 3}") # Es la elevacion o el exponente es decir 10 a la 3
print(f"Division entera: 10 // 3 = {10 // 3}") # Es la division entera sin que me de decimales solo un numero entero.

# Operadores de comparacion

print(f"Igualdad: 10 == 3 es {10 == 3}")  # Declara que son iguales
print(f"Desigualdad: 10 != 3 es {10 != 3}")  # Declara que no son iguales
print(f"Mayor que: 10 > 3 es {10 > 3}")  # Declara un mayor que
print(f"Menor que: 10 < 3 es {10 < 3}")  # Declara un menor que
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")  # Declara un mayor o igual que
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")  # Declara un menor o igual que

# Operadores logicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4} ") # Si las 2 afirmaciones son verdaderas las da por validas
print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}") # Si una de las 2 afirmaciones es verdadera la da por valida
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}") # Si la afirmacion es falsa el not la hace valida, y si es verdadera la hace falsa

# Operadores de asignacion

my_number = 11 # asignacion
print(my_number)
my_number += 1  # suma y asignacion
print(my_number)
my_number -= 1  # resta y asignacion
print(my_number)
my_number *= 2  # multiplicacion y asignacion     
print(my_number)
my_number /= 2  # division y asignacion
print(my_number)
my_number %= 2  # modulo y asignacion 
print(my_number)
my_number **= 1  # exponente y asignacion
print(my_number)
my_number //= 1  # division entera y asignacion
print(my_number)

# Operadores de identidad

my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}") # Con el is confirmamos que las variables contienen los mismo valores o son iguales 
print(f"my:number is not my_new_number es {my_number is not my_new_number}") # Con el is not confirmamos que las 2 variables no contienen lo mismo o no son iguales en este caso si contienen lo mismo asi que arrojara en consola que es false

# Operadores de pertenencia

print(f" 'o' in 'gersonoroz' = {'o' in 'gersonoroz'}") # Con el in nos confirma si la letra pertenece a el conjunto gersonoroz
print(f" 'j' not in 'gersonoroz' = {'j' not in 'gersonoroz'}") # Con el not in nos confirma si no esta en el conjunto gersonorozc

# Operadores de bit
                                                            # Sistema binario        64  32  16  8  4  2  1
a = 10 # 1010    10 en binario                           --->                                    1  0  1  0  = 10
b = 3  # 0011     3 en binario                           --->                                    0  0  1  1  = 3
print(f"AND: 10 & 3 = {10 & 3}") # 0010   Con el AND se comparan a y b, los 2 bit a bit multiplicandose
print(f"OR: 10 | 3 = {10 | 3}")  # 1011   Con el OR se comparan a y b, y si en al menos uno de los 2 hay un 1 vale uno y sino es cero
print(f"XOR: 10 & 3 = {10 ^ 3}") # 1001   Con el XOR se comparan a y b, y si son diferentes el resultado es 1 y si son iguales es cero
print(f"NOT: ~10 = {~10}")       # Investigar no comprendi, operador not bit a bit
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010 Me dice que desplace 2 bits al numero diez en el sistema binario hacia la derecha
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")# 101000 Me dice que desplace 2 bits al numero diez en el sistema binario hacia la izquierda


'''
Estructuras de control
'''

# Condicionales

my_string = "gerson"

if my_string == "gerson":
    print("mi_string es igual a gerson")
elif my_string == "alberto":
    print("my_string es igual a alberto")
else:
     print("my_string no es ni gerson ni alberto")


# Iterativas

for Ger in range(69):   # Con el for mas el rango que es el 69, se va imprimir en consola los numeros desde el cero hasta llegar al 69.
    print(Ger)

Ger = 0

while Ger <= 69:    # Con el while mientras Ger valga menos que 69, va a sumar 1 con el Ger += 1 hasta llegar al 69.
    print(Ger)      # Sino le colocaramos el Ger += 1 no se sumaria un numero mas a la variable Ger y se imprimiria por siempre el cero hasta que lo paremos
    Ger += 1

# Manejo de excepciones

try:
    print(10 / 2)                 # Con el try se intenta una operacion que creemos que puede tener una falla y si lo es con el except se avisa del error
except:                            # Y con el finally se finaliza la operacion sin romper el codigo o provocar un error, si el except no se activa quiere decir que salio bien la operacion.
    print("se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


# Solucion a la dificultad extra

for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
