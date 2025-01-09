import os, io, shutil
from .listas import filtrar

def carpetaActual():
  ''' Obtener la ruta absoluta a la carpeta global
  @tipo string
  '''
  return rutaAbsolutaA_('.')

def existeArchivo_Acá(ruta):
  ''' Indicar si existe un archivo con la ruta dada desde la carpeta actual.
    @param ruta : string
      Puede ser solo el nombre del archivo o una ruta más larga compuesta de varias carpetas anidadas.
    @tipo booleano
  '''
  return existeArchivo_En_(ruta, carpetaActual())

def existeCarpeta_Acá(ruta):
  ''' Indicar si existe una carpeta con la ruta dada desde la carpeta actual.
    @param ruta : string
      Puede ser solo el nombre de la archivo o una ruta más larga compuesta de varios carpetas anidadas.
    @tipo booleano
  '''
  return existeCarpeta_En_(ruta, carpetaActual())

def CrearCarpeta_(nombre):
  ''' Crear una carpeta con el nombre dado en la carpeta actual.
    @pre no existe una carpeta con el nombre dado en la carpeta actual.
    @param nombre : string
  '''
  CrearCarpeta_En_(nombre, '.')

def BorrarCarpeta_(ruta):
  ''' Borrar la carpeta en la ruta dada.
    @pre la ruta dada es la ruta a una carpeta que existe y para la cual se tiene permiso de edición.
    @param ruta : string
  '''
  shutil.rmtree(ruta)

def listaDeArchivosEn_(ruta):
  ''' Obtener la lista de nombres de archivos en la carpeta que está en ruta dada.
    @pre a ruta dada es la ruta a una carpeta que existe y para la cual se tiene acceso.
    @param ruta : string
    @tipo [string]
  '''
  return filtrar(lambda x : existeArchivo_En_(x, ruta), listaDeArchivosYCarpetasEn_(ruta))

def listaDeCarpetasEn_(ruta):
  ''' Obtener la lista de nombres de carpetas en la carpeta que está en la ruta dada.
    @pre existe una carpeta en la ruta dada.
    @param ruta : string
    @tipo [string]
  '''
  return filtrar(lambda x : existeCarpeta_En_(x, ruta), listaDeArchivosYCarpetasEn_(ruta))

def nuevaRuta_(ruta1, ruta2):
  ''' Obtener una ruta compuesta de las 2 rutas dadas.
    @pre existe una carpeta con ruta 'ruta2 en la ruta 'ruta1'.
    @param ruta1 : string
    @param ruta2 : string
    @tipo string
  '''
  return os.path.join(ruta1, ruta2)

def existeArchivo_En_(nombre, ruta):
  ''' Indicar si existe un archivo con el nombre dado desde la carpeta de la ruta dada.
    @param nombre : string
      Puede ser solo el nombre del archivo o una ruta más larga compuesta de varias carpetas anidadas.
    @param ruta : string
      Puede ser una ruta absoluta o relativa a la carpeta actual.
    @tipo booleano
  '''
  return os.path.isfile(nuevaRuta_(ruta, nombre))

def existeCarpeta_En_(nombre, ruta):
  ''' Indicar si existe una carpeta con el nombre dado desde la carpeta de la ruta dada.
    @param nombre : string
      Puede ser solo el nombre de la archivo o una ruta más larga compuesta de varios carpetas anidadas.
    @param ruta : string
      Puede ser una ruta absoluta o relativa a la carpeta actual.
    @tipo booleano
  '''
  return os.path.isdir(nuevaRuta_(ruta, nombre))

def contenidoDe_(ruta):
  ''' Obtener el contenido del archivo en la ruta dada como texto plano.
    @pre la ruta dada es la ruta a un archivo que existe y para el cual se tiene permiso de lectura.
    @param ruta : string
    @tipo string
  '''
  f = io.open(ruta, mode='r', encoding='utf-8')
  contenido = f.read()
  f.close()
  return contenido

def rutaAbsolutaA_(ruta):
  ''' Obtener la ruta absoluta para la ruta dada.
  @pre la ruta dada es la ruta relativa a una carpeta o un archivo que existe desde la carpeta actual.
  @param ruta : string
  @tipo string
  '''
  return os.path.abspath(ruta) # Agrega como prefijo la ruta absoluta a la carpeta actual

def IrA_(ruta):
  ''' Ubicarse en la carpeta de la ruta dada.
    @pre la ruta dada es la ruta a una carpeta que existe y para la cual se tiene acceso.
    @param ruta : string
      Puede ser una ruta absoluta o relativa a la carpeta actual.
  '''
  os.chdir(ruta)

def nombreDe_(ruta):
  ''' Obtener el nombre de un archivo o una carpeta a partir de su ruta.
    @param ruta : string
    @tipo string
  '''
  nombre = os.path.basename(ruta)
  if len(nombre) == 0:
    nombre = os.path.basename(os.path.dirname(ruta))
  return nombre

def rutaRaizDe_(ruta):
  ''' Obtener la ruta a la carpeta que contiene al archivo o carpeta en la ruta dada.
    @param ruta : string
    @tipo string
  '''
  nombre = os.path.basename(ruta)
  return os.path.dirname(os.path.dirname(ruta)) if len(nombre) == 0 else os.path.dirname(ruta)

def CrearCarpeta_En_(nombre, ruta):
  ''' Crear una carpeta con el nombre dado en la carpeta de la ruta dada.
    @pre no existe una carpeta con el nombre dado en la carpeta dada.
    @param nombre : string
    @param ruta : string
  '''
  os.mkdir(nuevaRuta_(ruta, nombre))

def CrearArchivo_En_Con_(nombre, ruta, contenido):
  ''' Crear un archivo con el nombre dado en la carpeta de la ruta dada y escribir en él el contenido dado.
    @ore no existe un archivo con el nombre dado en la carpeta dada.
    @param nombre : string
    @param ruta : string
    @param contenido : string
  '''
  f = io.open(nuevaRuta_(ruta, nombre), 'w',  encoding="utf-8")
  f.write(contenido)
  f.close()

def listaDeArchivosYCarpetasEn_(ruta):
  ''' Obtener la lista de nombres de archivos y carpetas en la carpeta que está en ruta dada.
    @pre a ruta dada es la ruta a una carpeta que existe y para la cual se tiene acceso.
    @param ruta : string
    @tipo [string]
  '''
  return os.listdir(ruta)