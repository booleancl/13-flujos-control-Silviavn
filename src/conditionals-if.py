print("opciones:")
print("frontend")
print("backend")
print("science")

your_preference = input("Dime que área de la informática te gustaría aprender: \n")

# el computador preguntará por cada "if" que encuentre escrito en el programa
if (your_preference == "backend"):
  print("debes estudiar python, luego aprender el framework Flask y por ultimo entender bases de datos.")
if (your_preference == "frontend"):
  print("debes aprender html, luego aprender el framework Bootstrap y por ultimo entender las bases de javascript.")

# el computador preguntará por "if" y si la pregunta da una respuesta negativa, cambiará a la parte "else" escrita en el programa
# solo se puede escribir "else" relacionado a un "if"
if (your_preference == "science"):
  print("debes aprender python y bases de datos. luego debes reforzar los conocimiento en matemáticas y estadística.")
else:
  print("debes elegir alguna opción entre backend, frontend o science")

# puedes combinar las preguntas usando OR o AND, o la combinación de ambos
print("opciones:")
print("frontend")
print("backend")
print("science")

your_2nd_preference = input("Dime una segunda área de la informática que te gustaría aprender. sino hay una segunda escribe NO: \n")

if (your_preference == "backend" and your_2nd_preference == "frontend"):
  print("domina muy bien Flask con python. entiende a los usuarios y aprende nuevas técnica con Bootstrap")

if (your_2nd_preference == "backend" or your_2nd_preference == "science"):
  print("debes tener las báses de matemáticas bien cubiertas")

if(your_preference != "frontend" or your_preference != "backend" and (your_preference == "science" or your_2nd_preference == "science")):
  print("no olvides la estadística :)")

if(your_2nd_preference == "NO"):
  print(f"refuerza y domina los conceptos de tu primera opción ${your_preference}")
else:
  print("opción no reconocida")


# ACTIVIDAD EXTRA: fijate que el codigo de las opciones hace que varias veces se repita lo mismo. crea una función para mejorar y reducir la complejidad del programa
