


class Estudiante:

    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def mostrarInfo(self):
        print(f" Estudiante: {self.nombre} | Edad: {self.edad} | Promedio: {self.promedio}")

    def setpromedio(self, nuevo_promedio):
        self.promedio = nuevo_promedio

Estudiantes = [
    Estudiante("jorge Pantoja", 21, 4.0),
    Estudiante("carlos Molano", 23, 5.0),
    Estudiante("andres Bravo", 30, 3.0)
]

print("informacion del estudiante en python")

for est in Estudiantes:
    est.mostrarInfo()

Estudiantes[1].setpromedio(8.0)
print("\n --- despues actualizar promedio de luis--")
Estudiantes[1].mostrarInfo()
