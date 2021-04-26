import re
import os

#Abrir el json a cambiar
with open ("cosas2.json") as f:
    things = f.read()

#Array de los nombres (keys) que quieres que estén, para verificar cuales no estan.
new_keys = ["src", "window", "name"]

#Todos los nombres que estan en el json. 
# (No me acuerdo si tienen o no espacios los nombres(keys) que tienes, ahi deje un regex que hace match sin espacios o con 1 o 2 espacios)
array_keys = re.findall(r"([\"]\w+[\s]?\w+[\s]?\w+\"[:])", things)
def cut(n):
    return n[1:-2]
old_keys = list(map(cut,array_keys))
print(old_keys)

#Los nombres que debes cambiar (los que no estan en new_keys).
def select(x):
    if (x in new_keys):
        return False
    else:
        return True
difference = list(filter(select, old_keys))
print(difference)

#El json del principio pero en con los nombres en minusculas.
def lower(string):
    string= string.lower()
    return string
minus_replace = re.sub(r"([\"]\w+[\s]?\w+[\s]?\w+\"[:])",lambda m: m.group(0).lower(), things)
print(minus_replace)
# minus_string = list(map(lower,array_keys))


#Guardar el nuevo json en minuscula en el disco.
save_path = './'
file_name = "data.json"

completeName = os.path.join(save_path, file_name)

file1 = open(completeName, "w")
file1.write(minus_replace)
file1.close()








