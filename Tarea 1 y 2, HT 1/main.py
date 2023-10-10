from Profesor import Profesor
from Estudiante import Estudiante
from load import *
import re
import os
import struct
from datetime import datetime
from Disco import Disco

if __name__ == "__main__":
    idProfesor = 1
    idEstudiante = 1
    desplazamiento = 0
    desplazamiento2 = 0
    auxProfesor = []
    auxEstudiante = []
    

    try:
        with open('profesores.sdk', 'rb+') as file: 
            auxProfesor = Alectura_desplazado(file,desplazamiento,auxProfesor)
            if len(auxProfesor)>0:
                idProfesor = auxProfesor[-1].id+1
    except FileNotFoundError:
        abrirArvhivo = open('profesores.sdk',"wb") # escritura binaria
        abrirArvhivo.close()

    try:
        with open('estudiantes.sdk', 'rb+') as file: 
            auxEstudiante = Alectura_desplazado(file,desplazamiento2,auxEstudiante)
            if len(auxEstudiante)>0:
                idEstudiante = auxEstudiante[-1].id+1
            
    except FileNotFoundError:
        abrirArvhivo = open('estudiantes.sdk',"wb") # escritura binaria
        abrirArvhivo.close()
    

    while (True):
        print("#********* MENU *********#")
        print("# 1. Registro profesor   #")
        print("# 2. Registro estudiante #")
        print("# 3. Ver registro        #")
        print("# 4. Crear disco         #")
        print("# 5. Salir               #")
        print("#************************#")
        
        eleccion = int(input('Elija la opcion: '))
        if eleccion == 1:
            print("Llene los campos de profesor: ")
            cui = int(input('CUI: '))
            nombre = input('Nombre: ')
            curso = input('Curso: ')
            profesor = Profesor()
            profesor.set_tipo('P')
            profesor.set_id(idProfesor)
            profesor.set_cui(cui)
            profesor.set_nombre(nombre)
            profesor.set_curso(curso)
            auxProfesor.append(profesor)
            archivo = open('profesores.sdk',"rb+")
            Aescritura_desplazado(archivo,desplazamiento,auxProfesor)
            archivo.close()
        elif eleccion == 2:
            print("Llene los campos del estudiante: ")
            cui = int(input('CUI: '))
            nombre = input('Nombre: ')
            carnet = int(input('Carnet: '))
            estudiante = Estudiante()
            estudiante.set_tipo('E')
            estudiante.set_id(idEstudiante)
            estudiante.set_cui(cui)
            estudiante.set_nombre(nombre)
            estudiante.set_carnet(carnet)
            auxEstudiante.append(estudiante)
            archivo = open('estudiantes.sdk',"wb")
            Aescritura_desplazado(archivo,desplazamiento,auxEstudiante)
            archivo.close()
        elif eleccion == 3:
            print("Registro de la data: ")
            print("#********* PROFESOR *********#")
            if len(auxProfesor)>0:
                for profesor in auxProfesor:
                    profesor.imprimir_info()
            
            print("#******** ESTUDIANTE ********#")
            if len(auxEstudiante)>0:
                for estudiante in auxEstudiante:
                    estudiante.imprimir_info()
        elif eleccion == 4:
            print("Escribe el comando: ")
            comando = input()
            validando = re.search(r'^execute\s*-path="([^"]+)"$', comando)
            if validando :
                rutaArchivo = validando.group(1)
                print("Ruta: "+ rutaArchivo)
                ruta = os.path.dirname(rutaArchivo)
                if os.path.exists(ruta):
                    disco = Disco()
                    disco.set_infomation(5242880,datetime.now().strftime('%d/%m/%Y, %H:%M:%S'),0)
                    fileOpen = open(rutaArchivo, "wb") 
                    print("********* MKDISK *********")
                    Winit_size(fileOpen,5)
                    Aescritura_desplazado(fileOpen,desplazamiento,disco)
                    print("*********** REP **********")
                    print("MBR: ")
                    disco.display_info()
                    fileOpen.close()  
            else:
                print("El comando no se puede ejecutar.")
        else:
            exit()
        
    
   