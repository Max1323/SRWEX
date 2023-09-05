# SRWEX
Datos de Super Robot Wars EX (Super Nintendo)

## Carpetas
* Tabla (Son las tablas en Español)
   * `SRWEX ESP.tbl`: Es la tabla para los textos principales del juego.
   * `SRWEX Titulo ESCENA.tbl`: Es la tabla solo para el título de ESCENA que aparece al iniciar el capítulo.
   * `SRWEX Titulo.tbl`: Es la tabla para los títulos del capítulo.

* Titulos SRWEX
  Contiene el archivo en python y un archivo de texto.
   * `Titulos_SRWEX.py`: Archivo en Python. Más detalles abajo.
   * `titulos.txt`: Contiene el tamaño de los caracteres, solo es información para poner en el archivo de python.

## Titulos SRWEX
El archivo `Titulos_SRWEX.py` surge a raíz de que para cada título del juego tiene:
* Una cantidad de caracteres que vamos a usar para el título.
* El caracter
* De que fuente es el caracter
* La posición de la altura para dicho caracter.
* La posición del ancho.

A principio, lo tenia que hacer manualmente, calculando solo el ancho de dicho caracter con una calculadora de Programador. Para ello cree este programa para no hacerlo todo a mano.

### Como se usa
* `PRIMERO`: Lo único que hace este programa es darte los valores del ancho de los caracteres para acomodarlos uno al lado del otro. O sea, que tendrás que usar un editor hex para cambiar los valores de las posiciones de ancho.

