# Ejemplo de listas

Misnovias= ["Aripina", "Anastasia", "Maria"]
Misnumeros = [666, 77, 10]
# Mostrando mis novias
print(Misnovias)
# Mostrando mis numeros raros
print(Misnumeros)
print("---Accediendo a los elementos de la lista---")
if "Agripina" in Misnovias:
    print("Si, 'Agripina' está en la lista de mis novias")
else:
    print("Chale, no eres mi novia")
print("Numeros de novias")
Nnovias = len(Misnovias)
print(f"Numero de novias = {Nnovias}")

print("Ciclo for en listas")
posicion = 0
for medianaranja in Misnovias:
    print(posicion," ", medianaranja)
    posicion = posicion + 1