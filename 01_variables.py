# la forma de nombrar variables suele ser la lowercamelcase o snake_case
# la forma más correcta es la segunda

first_variable = 'Mi primera variable';
print(first_variable);

number_variable = 7;
print(number_variable);

variable_bool = False;
print(variable_bool);

# Concatenación
print('Se concatenan', 'los textos', 'con comas', 'entre los elementos', 'y se autoañaden los espacios entre los elementos');
print(first_variable, number_variable, variable_bool);

my_int_to_str_variable = str(number_variable);
print(my_int_to_str_variable, type(my_int_to_str_variable));
print(type(print(my_int_to_str_variable, type(my_int_to_str_variable)))); # <class 'NoneType'>

print('Este es el valor de:', variable_bool);

# Algunas funciones del sistema
print(len(my_int_to_str_variable)); # lenght

# Variables en una sola línea. ¡Cuidad con abusar de esta sintaxis!
name, surname, alias, age = 'John', 'Doe', 'johndoe', 35;
print(name, surname, '. Mi edad es de' , age, '. Y mi alias es:', alias);

# Inputs
first_name = input('¿Cuál es tu nombre?');
age = input('¿Cuál es tu edad?');

print(first_name, age);

# Python es un lenguaje débilmente tipado, cosa que hay que tener en cuenta a la hora de creación de variables
# Cambiamos su tipo

first_name = 35;
age = 'John Doe';

print(first_name, age);

# ¿Forzamos el tipo?
address: str = 'Mi dirección'; # con esto gripamos la variable, asignándole un tipo concreto, es para ayudarnos mayormente
address = 32;
address = True;
address = 32.4;
# Se queda siempre con el último
print(type(address));
