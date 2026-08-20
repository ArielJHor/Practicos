def ordenar_lista():
  lista_desordenada = [45, 12, 89, 3, 23, 56, 7]
  print("Lista desordenada:", lista_desordenada)
  opcion = input("como la queres ordenar? (1: menor a mayor, 2: mayor a menor): ")
  lista_ordenada = []
  for numero in lista_desordenada:
    if not lista_ordenada:
      lista_ordenada.append(numero)
    else:
      insertado=False
      for i in range(len(lista_ordenada)):
        if opcion=="1":
          if numero < lista_ordenada[i]:
            lista_ordenada.insert(i, numero)
            insertado = True
            break
        else:
          if numero>lista_ordenada[i]:
            lista_ordenada.insert(i, numero)
            insertado=True
            break
      if not insertado:
        lista_ordenada.append(numero)
  print("--- Resultados ---")
  print("lista desordenada:", lista_desordenada)
  print("lista ordenada:", lista_ordenada)
ordenar_lista()