## Variables 
#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
a= 2
print(a)

#2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

#3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(a))
#4) Crear una variable que contenga tu nombre
b= 'Damian'
#5) Crear una variable que contenga un número complejo
c= 3+ 3j
#6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(c))
#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
d = 3.1416
#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
e= True
f= 'True'
#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print('el tipo de dato de la variable e es ' , type(e) , ' y el tipo de dato de la variable f es' , type(f))
#10) Asignar a una variable, la suma de un número entero y otro decimal
g = 4 + 1.5
#11) Realizar una operación de suma de números complejos
h = 1 + 1j
i = 2 + 2j
print(h + i)
#12) Realizar una operación de suma de un número real y otro complejo
print(a + h)
#13) Realizar una operación de multiplicación
print( a * d)
#14) Mostrar el resultado de elevar 2 a la octava potencia
print( 2 ** 8)
#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
j= 27/4
print(j)
#16) De la división anterior solamente mostrar la parte entera
k= 27//4
print(k)
#17) De la división de 27 entre 4 mostrar solamente el resto
l= 27%4
print(l)
#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print( (4 * k) + l)
#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
nombre= 'Damian '
segundo_nombre= 'Javier '
apellido= 'Alonso'
print(nombre + segundo_nombre + apellido)
#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print('2'== 2)
#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(2 == int('2'))
#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float('3.8') , 'se debe colocar con punto no con coma'
#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
m = 3
m -= 3
print(m)
#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1<<2)
#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

print(2 + int('2'))
print(str(2) + '2')
print(2 + float('2'))
#26) Realizar una operación válida entre valores de tipo entero y string
n=5
o= 'te estas portando mal '
print(o*5)
