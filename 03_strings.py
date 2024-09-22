### Strings ###

my_string = 'Mi string';
my_other_string = 'Mi otro string';

print(len(my_string));
print(len(my_other_string));

print(my_string + ' ' + my_other_string);

my_new_line_string = 'Este es un string \ncon salto de línea';
print(my_new_line_string);

my_tab_string = '\tEste es un string con tabulación';
print(my_tab_string);

my_scape_string = '\tEste es un string con \nescapado';
print(my_scape_string);

# Cómo evitar caracteres especiales
my_scape_string = '\\tEste es un string con \nescapado'; # con la doble barra
print(my_scape_string);

# Formateo

name, surname, age = 'John', 'Doe', 26;
print('Mi nombre es %s %s, y mi edad es %d' %(name, surname, age)); # trabajando directamente con los datos formateados. El mejor caso, usar esto
print('Mi nombre es {} {}, y mi edad es {}'.format(name, surname, age)); # imprimir tal cual el objeto
print('Mi nombre es ' + name + ' ' + surname + ', y mi edad es ' + str(age));

# se imprime todo en formato de string:
print('Mi nombre es {name} {surname}, y mi edad es {age}'); 
# y este pilla bien el formato
print(f'Mi nombre es {name} {surname}, y mi edad es {age}'); # Esta es de las mejores formas si no se formatean los datos.la 'f' es para formatear

# Desempaqueado de caracteres
language = 'Python';
a, b, c, d, e, f = language;
print(a);
print(e); 

# División

language_slice = language[1:3];
print(language_slice);

language_slice = language[1:];
print(language_slice);

language_slice = language[-2];
print(language_slice);

language_slice = language[1:2:4];
print(language_slice);

language_slice = language[0:6:2];
print(language_slice);

# Reverse

reversed_language = language[::-1];
print(reversed_language);

# Funciones

print(language.capitalize());
print(language.upper());
print(language.count('t'));
print(language.isnumeric());
print('1'.isnumeric());
print(language.lower());
print(language.upper().isupper());
print(language.startswith('Py'));
print('Py' == 'py');