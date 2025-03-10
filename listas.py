from functools import reduce

def mapear(f, lista):
  ''' Obtener la lista resultante de aplicar la función f a cada elemento de la lista dada.
  @pre la función f se puede aplicar con cada elemento de la lista dada.
  @param f : A -> B
  @param lista : [A]
  @tipo [B]
  '''
  return list(map(f, lista))

def filtrar(f, lista):
  ''' Obtener la lista resultante de quitar de la lista dada aquellos elementos que no cumplen el filtro f.
  @pre la función f se puede aplicar con cada elemento de la lista dada.
  @param f : A -> booleano
  @param lista : [A]
  @tipo [A]
  '''
  return list(filter(f, lista))

def fold(f, z, lista):
  ''' Obtener el resultado de la recursión sobre la lista dada usando f para el caso recursivo y z para el caso base.
  @param f : B -> A -> B
  @param z : B
  @param lista : [A]
  @tipo B
  '''
  return reduce(f, lista, z)

def fold1(f, lista):
  ''' Obtener el resultado de la recursión sobre la lista dada usando f para el caso recursivo y el primer elemento de la lista dada para el caso base.
  @pre la lista dada no está vacía.
  @param f : A -> A -> A
  @param lista : [A]
  @tipo A
  '''
  return reduce(f, lista)

def elementosDespuesDe_(lista, elemento):
  ''' Obtener los elementos de la lista dada que están después de la primera aparición del elemento dado.
  @pre el elemento aparece al menos una vez en la lista.
  @param lista : [A]
  @param elemento : A
  @tipo [A]
  '''
  i = 0
  while lista[i] != elemento:
    i += 1
  return lista[i+1:]

def elementosDesde_(lista, elemento):
  ''' Obtener los elementos de la lista dada desde de la primera aparición del elemento dado.
  @pre el elemento aparece al menos una vez en la lista.
  @param lista : [A]
  @param elemento : A
  @tipo [A]
  '''
  i = 0
  while lista[i] != elemento:
    i += 1
  return lista[i:]

def elementosAntesDe_(lista, elemento):
  ''' Obtener los elementos de la lista dada que están antes de la primera aparición del elemento dado.
  @pre el elemento aparece al menos una vez en la lista.
  @param lista : [A]
  @param elemento : A
  @tipo [A]
  '''
  i = 0
  while lista[i] != elemento:
    i += 1
  return lista[0:i]

def elementosHasta_(lista, elemento):
  ''' Obtener los elementos de la lista dada hasta la primera aparición del elemento dado.
  @pre el elemento aparece al menos una vez en la lista.
  @param lista : [A]
  @param elemento : A
  @tipo [A]
  '''
  i = 0
  while lista[i] != elemento:
    i += 1
  return lista[0:i+1]