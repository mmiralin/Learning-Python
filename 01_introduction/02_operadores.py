# Operadores

print(3 + 4); # Sale el resultado de la suma
print(3 - 4); # Sale el resultado de la resta
print(3 * 4); # Sale el resultado de la multiplicación
print(3 / 4); # Sale el resultado de la división (cociente) con decimales
print(3 // 4); # Sale el resultado de la división (cociente) aprox. en número entero (trunca)
print(3 % 4); # Sale el resultado de la división (resto)
print(3 ** 4); # Sale el resultado del exponente

print(3 ** 4 + 3 - 7 / 1 // 4);

# Otra forma de concatenar, esta no autoañade los espacios como con las comas
print('hola' + 'mundo' + 'cruel');
print('hola ' + 'mundo ' + 'cruel');
print('hola ' + str(7)); # para poner enteros o otros datos, pasarlos por la función str()
print('hola ' * 7); # Esto hace que aparecezca el mensaje de la izquierda x número de veces
print('hola ' * (3 ** 4));

my_float = 2.5 * 2;
print('hola ' * int(my_float)); # Para que esto funcione, aunque el número sea x.0, hay que pasarlo a int

# Operadores comparativos

print(3 > 4);
print(3 < 4);
print(3 >= 4);
print(3 <= 4);
print(3 == 4);
print(3 != 4);
print(3 > 4 == 2);

print('Hola' > 'Python'); # Según el número de caracteres
print('Hola' < 'Python');
print('Hola' >= 'Python');
print('Hola' <= 'Python');
print('Hola' == 'Python');
print('Hola' != 'Python');

print('aaaa' >= 'abaa'); # Ordenación alfabética, también tiene en cuenta las mayúsculas
print(len('aaaa') >= len('abaa')); # Cuenta caractéres

# Operadores lógicos

print(3 > 4 and 'Hola' > 'Python'); # &&
print(3 > 4 or 'Hola' < 'Python'); # ||
print(3 < 4 and 'Hola' > 'Python'); # &&
print(3 < 4 or 'Hola' > 'Python'); # ||
# print(3 > 4 not 'Hola' > 'Python'); # !=,  este no lo admite python así, pero así vvv sí
print(not(3 > 4));

print(3 < 4 or ('Hola' > 'Python' and 4 == 4));