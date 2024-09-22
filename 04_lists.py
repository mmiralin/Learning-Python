### Listas o Arrays ###

my_list = list();
my_other_list = [];

print(len(my_list));

my_list = [35, 24, 62, 52, 30, 30, 17];

print(my_list);
print(len(my_list));

my_other_list = [26, 1.72, 'Caindra', 'SilverHeart'];
print(my_other_list);
print(type(my_other_list));

'''
Un array no es lo mismo que una lista. Una lista, como estructura base, acaba teniendo por debajo un array, pero una lista
nos proporciona operaciones propias de las listas, como pueden ser ordenaciones, reverses, inyeccion de elementos, etc

Las dos formas con las que se ha definido arriba es lo mismo: una lista, no array. Es como si el array fuera directamente un arraylist
'''

print(type(my_other_list));
print(type(my_list));

print(my_other_list[1]);
print(my_other_list[0]);
print(my_other_list[-1]);
print(my_other_list[-3]);

# print(my_other_list[-5]); IndexError
# print(my_other_list[4]); IndexError

print(my_other_list.count('Caindra'));
print(my_other_list.count(30));
print(my_list.count(30));

age, height, name, surname = my_other_list;
print(name);

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3];
print(age);

# Concatenación de listas
print(my_list + my_other_list);
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("miralin")
print(my_other_list)

my_other_list.insert(1, "royal blue")
print(my_other_list)

my_other_list[1] = "royal blue"
print(my_other_list)

my_other_list.remove("royal blue")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))