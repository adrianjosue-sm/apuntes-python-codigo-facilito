mensaje = 'Hola mundo!'
izquierda = 'ADRIAN'  #'Este es un mensaje justificado a la izquierda'
derecha = 'MEDINA'  #'Este es un mensaje justificado a la derecha'

# ljust -> Justificar a la Izquierda
# rjust -> Justificar a la Derecha
# center -> Centrar

mensaje = mensaje.center(20)
izquierda = izquierda.ljust(20)
derecha = derecha.rjust(20)

print(mensaje)
print(izquierda)
print(derecha)