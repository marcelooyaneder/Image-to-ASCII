################################
####GRUPO2: TRANSFORMACION DE###
########IMAGEN A ASCII##########
################################

################################
######BLOQUE DE DEFINICION######
################################

#IMPORTAR FUNCIONES

from PIL import Image

from numpy import array

import numpy as np

import easygui as eg


#CONSTANTES

formato='.ppm'

CaracteresAscii= ['@','#','%','&','$','+','*',';',':','.',' ']

#DEFINICION  DE FUNCIONES

#interfaz grafica 
def GUI():
	archivo = eg.fileopenbox(msg="",title="Seleccione foto a transformar.",default='',filetypes='')
	return archivo

#su funcion es abrir una imagen cualquiera y transformarla a formato PPM
#ENTRADA: imagen en cualquier formato
#SALIDA: imagen en formato PPM
def ingresoimagen(ruta):
	ImagenIngresada= Image.open(ruta)
	if ImagenIngresada.format=='PPM':
		return ImagenIngresada
	else: 
		name = raw_input('se creara una imagen en formato PPM, ingrese el nombre de esta: ')
		NuevaImagen=ImagenIngresada.save(name+formato)
		ImagenPPM= Image.open(name+formato)
		print 'se creo exitosamente la imagen en PPM'
		return ImagenPPM

#caja de mensajes 
def CajaDeMensaje(ruta):
	imagen= Image.open(ruta)
	if imagen.format=='PPM':
		eg.msgbox('El archivo de texto de salida sera guardado en el directorio en que se encuentra el archivo python', "LEER", ok_button="Continuar")
	else:
		eg.msgbox('La imagen en formato PPM, al igual que el archivo de texto de salida seran guardados en el directorio en que se encuentra el archivo python', "LEER", ok_button="Continuar")

#funcion para redimensionar la imagen, conservando su proporcion
#ENTRADA: imagen 
#SALIDA: imagen redimensionada conservando la proporcion 
def EscalarImagen(Imagen):
	EscaladaX=100
	(X,Y)=imagen.size
	Radio=Y/float(X)
	EscaladaY=int(Radio*EscaladaX)
	ImagenEscalada= Imagen.resize((EscaladaX,EscaladaY))
	return ImagenEscalada

#funcion para transformar una imagen a color a escala de grises
#ENTRADA: imagen en color 
#SALIDA: imagen en escala de grises
def GrayScale(imagen):
	imagenNueva= imagen.convert('L')
	ImagenNueva= imagenNueva.convert('RGB')
	return array(ImagenNueva)

#funcion para crear un a matriz identica a otra
#ENTRADA: matriz
#SALIDA: matriz 
def CreacionMatriz(matriz):
	numero_filas=len(matriz)
	numero_columnas=len(matriz[0])
	MatrizFinal = [None] * numero_filas
	for i in range(numero_filas):
		MatrizFinal[i] = [None] * numero_columnas	
	return MatrizFinal

#funcion para transformar el valor de un pixel a un caracter ascii
#ENTRADA: array con pixeles
#SALIDA: matriz en ascii
def CambioAASCII(Arreglo,MatrizCreada):
	i=0
	while i<len(Arreglo):
		j=0
		while j<len(Arreglo[i]):
			Pixel=Arreglo[i][j][0]
			Posicion=Pixel/25
			Caracter=CaracteresAscii[Posicion]
			MatrizCreada[i][j]=Caracter
			j+=1
		i+=1
	return MatrizCreada

#funcion para escribir el archivo de salida
#ENTRADA: array
#SALIDA: archivo de texto 
def EscribirArchivo(matriz):
	nombre= raw_input('ingrese nombre del archivo de texto de salida: ')
	Archivo= open(nombre+'.txt','w')
	for linea in matriz:
		for pixel in linea:
			Archivo.write(str(pixel))
		Archivo.write('\n')
	Archivo.close()
	print 'se a creado el archivo de texto con exito...'


################################
########BLOQUE PRINCIPAL########
################################

#ENTRADAS
ruta= GUI()

#PROCESO
imagen=ingresoimagen(ruta)

CajaDeMensaje(ruta)

imagenescalada= EscalarImagen(imagen)

ArregloGrises=GrayScale(imagenescalada)

MatrizFormada= CreacionMatriz(ArregloGrises)

MatrizAscii= CambioAASCII(ArregloGrises,MatrizFormada)

Final= EscribirArchivo(MatrizAscii)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
