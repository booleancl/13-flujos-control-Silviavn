your_preference = int(input("Dime cuantos años estudiarás antes de trabajar: \n"))

# el computador preguntará por cada "if" que encuentre escrito en el programa
if (your_preference == 1):
  print("puedes optar a sueldos entre 500.000 y 600.000. pero debes tener asistencia o ponerse al día en el 100 por ciento de las actividades del curso. NO puede quedar nada en el tintero.")

if (your_preference > 2):
  print("es una buena decisión estudiar al menos 2 años antes de comenzar. mientras busca proyectos reales ya sea de tus propias ideas, amigos o familiares que necesiten tecnología para emprender. la práctica hace al maestro.")

if (your_preference > 1 and your_preference <= 3):
  print("estudiar entre 1 y 3 años te aseguro que te hará programar a un nivel que encontrarás trabajo casi asegurado. siempre y cuando en ese período hayas hecho proyectos reales de práctica o que generen ingresos reales. y si haz interactuado con bases de datos y servicios en la nube es mucho más seguro encontrar trabajo con buenos sueldos")

if (your_preference >= 4):
  print("increible decisión! desde 4 años en adelante la experiencia es más que suficiente para triunfar en la industria. procura conocer varias áreas del desarollo y te darás cuenta como es que varias comparten cosas en comun y como es que se centran en las decisiones y/o necesidades de los usuarios y las empresas que ofrecen productos")
