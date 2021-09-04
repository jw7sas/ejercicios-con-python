# -*- coding: utf-8 -*-

# imports
import os
import zipfile

def verify_path_exists(path_w):
    return os.path.exists(path_w)


def compress_files(folder_w, filename_w, ext):
    """ Método para comprimir archivos. """
    try:
        ext_w = "*"
        if ext != "":
            ext_w = tuple(ext.split(","))

        newFileZip = zipfile.ZipFile(f"{folder_w}\{filename_w}.zip", "w")

        for folder, subfolders, files in os.walk(folder_w):
            for file_w in files:
                if ext_w != "*" and file_w.endswith(ext_w):
                    newFileZip.write(
                        os.path.join(folder, file_w), 
                        os.path.relpath(os.path.join(folder, file_w), folder_w), 
                        compress_type=zipfile.ZIP_DEFLATED
                    )
                else:
                    if file_w != f"{filename_w}.zip" and ext_w == "*":
                        newFileZip.write(
                            os.path.join(folder, file_w), 
                            os.path.relpath(os.path.join(folder, file_w), folder_w), 
                            compress_type=zipfile.ZIP_DEFLATED
                        )

        newFileZip.close()

    except FileNotFoundError:
        print("ERROR ARCHIVO O DIRECTORIO NO ENCONTRADO")
    except ValueError:
        print("ERROR AL COMPRIMIR EL ARCHIVO")


def unzip_files(filename_w, folder_w):
    """ Método para descomprimir archivos. """
    try:
        currentFileZip = zipfile.ZipFile(filename_w)
        currentFileZip.extractall(folder_w)

        currentFileZip.close()

    except FileNotFoundError:
        print("ERROR ARCHIVO O DIRECTORIO NO ENCONTRADO")
    except ValueError:
        print("ERROR AL DESCOMPRIMIR EL ARCHIVO")


def run():
    print("<------ Bienvenidos al sistema de compresión PYTHON ------>")
    menu = """ 
            Ingrese una de las opciones:

            [A] Comprimir archivos
            [B] Descomprimir archivos
            [C] Salir
            \n
            """
    while True:
        option = str(input(menu)).upper()

        if  option == "A":
            folder = str(input("Ingrese la ubicación del directorio a comprimir: "))
            filename = str(input("Ingrese el nombre del archivo: "))
            ext = str(input("Si desea ingrese extensión de archivos a comprimir: "))
            if verify_path_exists(folder):
                compress_files(folder, filename, ext)
            else:
                print("Error: La ruta especificada NO existe")

        elif option == "B":
            filename = str(input("Ingrese la ubicación del archivo a descomprimir: "))
            folder = str(input("Ingrese la ubicación del directorio donde va a descomprimir los archivos: "))
            if verify_path_exists(filename):
                unzip_files(filename, folder)
            else:
                print("Error: La ruta especificada NO existe")

        elif option == "C":
            break

        else:
            print(f"<------- [{option}] OPCION NO VALIDA, INTENTE NUEVAMENTE!! ------> \n")

if __name__ == '__main__':
    run()
