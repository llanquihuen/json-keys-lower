import re
archivo = input("Cual archivo?\n")
file_in = open(archivo, "rt")
file_out = open("copia_"+archivo, "wt")

for line in file_in:
	line = re.sub(r'(\,+\s\s)|(\,+\s)',',',line)
	file_out.write(line)

file_in.close()
file_out.close()
