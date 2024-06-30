"""Operadores en Python"""
"""Operadores Aritmeticos"""
a=2
b=3
a+b # esto es una suma
print("La suma de ",a," mas ",b," es:")
print(a+b)
a-b # esto es una resta
print("La resta de ",a," menos ",b," es:")
print(a-b)
a*b # esto es una multiplicacion
print("La multiplicación de ",a," por ",b," es:")
print(a*b)
a/b # esto es una division
print("La división de ",a," sobre ",b," es:")
print(a/b)
a//b # es una division entera
print("La división entera de ",a," sobre ",b," es:")
print(a//b)
a%b # es un modulo
print("El modulo de la devisión de ",a," sobre ",b," es:")
print(a%b)
a**b # es una potenciacion 
print("La potenciaión de ",a," por ",b," es:")
print(a**b)
#Operadores Relacionales
c=6
d=7
e=2
f=1
c>d # esto es mayor que 
print(b, "es mayor que" ,a)
print(b>a)
(b>a)# esto es menor que
print(b, "es menor que" ,d)
print(b<d)
(a<=e) # esto es menor igual que
print(a, "es menor igual que" ,e)
print(a<=e)
(a>=e) # esto es mayor igual que
print(a, "es mayor igual que" ,e)
print(a>=e)
(c!=d) # esto es diferente que
print(c, "es diferente que" ,d)
print(c!=d)
(a==e) # esto es igual que
print(a, "es igual que" ,e)
print(a==e)
#Operadores Lógicos
"""OPERADOS LÓGICOS"""
P=5>2
Q=2<1
# and = y, intersección
# or = o, unión
# not = negación
# not p or q = entonces
print ("p o q, es:")
print (P or Q)
print ("p y q, es:")
print (P and Q)
print ("La negacion de p, es:")
print (not P)
print ("p entoces q,  es:")
print (not P or Q)
print("P si solo si Q es:")
print(P and Q) or (not P and not Q)
"""TIPOS DE DIVISIONES"""
#entera    # decimal    #modular
import cmath
print("La división entera de 27 entre 14 es:")
print(27//14)
print("La división decimal de 27 entre 14 es:")
print(27/14)
print("La división modular de 27 entre 14 es:")
print(27%14)
"""CONVERSIÓN DE EXPRESIONES"""
# Conversión de entero a flotante (añadido por interes propio)
a = 5
print("El valor de a es:", a)
print("El tipo de a antes de la conversión es:", type(a))
a = float(a)
print("El valor de a después de la conversión a flotante es:", a)
print("El tipo de a después de la conversión es:", type(a))
# Conversión de flotante a entero
b = 7.8
print("El valor de b es:", b)
print("El tipo de b antes de la conversión es:", type(b))
b = int(b)
print("El valor de b después de la conversión a entero es:", b)
print("El tipo de b después de la conversión es:", type(b))
# Conversión de número a cadena
c = 10
print("El valor de c es:", c)
print("El tipo de c antes de la conversión es:", type(c))
c = str(c)
print("El valor de c después de la conversión a cadena es:", c)
print("El tipo de c después de la conversión es:", type(c))
# Conversión de cadena a número
d = "20"
print("El valor de d es:", d)
print("El tipo de d antes de la conversión es:", type(d))
d = int(d)
print("El valor de d después de la conversión a número es:", d)
print("El tipo de d después de la conversión es:", type(d))
