#Esto es un comentario 
"""esto es un comentario 
de varias lineas"""
nombre="juan esteban ardila Martínez"
edad=14
estado=true 
nota=42

#como saber el tipo de dato de cada variable 

Print (type(nombre)) #resultado:<class:"str">

Print (type(edad)) #resultado <class:'int'>
Print (type(estado))#resultado<class:'bool'
Print (type(nota))#resuktado<class:'float'

#mostrar el valor que contiene cada variable 
Print(nombre)
Print(edad)
Print(estado)
Print(nota)

#vamos a utilizar la funcion input para recojer datos por medio del teclado.
nombre=input("¿como te llamas? ")
edad=input("¿que edad tienes? ")
estado=input("¿En que estado te encuentras? ")
nota=input("¿cual es tu nota? ")

#para visualizar que guardamos en las variables anteriores
print("Hola,",nombre,"un gusto conocerte")
print("Tu edad es:",edad)
print("Tu estado es:",estado)
print("Tu nota es:",nota)
