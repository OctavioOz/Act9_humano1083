print("Act 9 clase humano")
print("Octavio Ozaeta Mat: 22308051281083")

# Zona de clases
class Humano1083:
    # Zona de atributos
    edad=0
    peso=0
    estatura=0
    fecha_nacimiento=""
    ojos=""
    color_cabello=""

    # Zona de funciones dentro de la clase
    def correr1083(self,n):
        print(f"{n} esta corriendo uff...")

    def caminar1083(self,n):
        print(f"{n} esta caminando")

    def hablar1083(self,n):
        print(f"{n} esta hablando")

    def comer1083(self,n):
        print(f"{n} esta comiendo")

    def dormir1083(self,n):
        print(f"{n} esta durmiendo")

    def bailar1083(self,n):
        print(f"{n} esta bailando")

# Zona de creacion de objetos
octavio=Humano1083()
maria=Humano1083()

# Zona de usando objetos

print("Resultados para Octavio") 
octavio.edad=17
print(f"Edad: {octavio.edad}")
octavio.estatura="1.71"
print(f"Estatura: {octavio.estatura}m")
octavio.fecha_nacimiento="29 Junio de 2007"
print(f"Fecha de nacimiento: {octavio.fecha_nacimiento}")
octavio.peso="72"
print(f"Peso: {octavio.peso}kg")
octavio.ojos="Cafes"
print(f"Color de ojos: {octavio.ojos}")
octavio.color_cabello="Negro"
print(f"Color de cabello: {octavio.color_cabello}")

print("")

octavio.correr1083("Octavio")
octavio.bailar1083("Octavio")
octavio.caminar1083("Octavio")
octavio.hablar1083("Octavio")
octavio.comer1083("Octavio")

print("-----------------------------------------")

print("Resultados para Maria")
maria.edad=19
print(f"Edad: {maria.edad}")
maria.estatura="1.65"
print(f"Estatura: {maria.estatura}m")
maria.fecha_nacimiento="14 Agosto de 2005"
print(f"Fecha de nacimiento: {maria.fecha_nacimiento}")
maria.peso="60"
print(f"Peso: {maria.peso}kg")
maria.ojos="Cafes"
print(f"Color de ojos: {maria.ojos}")

print("")

maria.correr1083("Maria")
maria.bailar1083("Maria")
maria.caminar1083("Maria")
maria.hablar1083("Maria") 