### Tuples ###

my_tuple = tuple();
my_other_tuple = tuple();

# Una tupla es un conjunto de valores

my_tuple = (26, 1.72, 'Caindra', 'SilverHeart');
print(my_tuple);
print(type(my_tuple));

# Acceso a elementos y búsqueda

print(my_tuple[0]);
print(my_tuple[-1]);
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Caindra"))
print(my_tuple.index("SilverHeart"))
print(my_tuple.index("Caindra"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "miralin"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
