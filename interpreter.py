file = open("file.sp", "r")
line = file.readline()

if line > "usando spl":
	for x in file:
		if "imprimir" in x:
			o = x
			o = o.replace("imprimir", "")
			o = o.replace("\n", "")
			print(o)
		if "bucle" in x:
			while True:
				pass

file.close