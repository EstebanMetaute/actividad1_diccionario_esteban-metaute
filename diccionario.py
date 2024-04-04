mi_diccionario = []
list_pendiente = []
import os
sw = True
def fnt_añadir_estudiante(diccionario, codigo, nombre, apellidos, contacto, correo, edad, estracto, sexo, direccion):
    if codigo == '' or nombre == '' or apellidos == '' or contacto == '' or correo == '' or edad == '' or estracto == '' or sexo == '' or direccion == '':
        enter = input('Diligenciar toda la informacion solicitada <ENTER>')
    else:
        diccionario[codigo] = {'nombre': nombre, 'apellidos': apellidos, 'contacto': contacto, 'edad': edad, 'estracto': estracto, 'sexo': sexo, 'direccion': direccion}