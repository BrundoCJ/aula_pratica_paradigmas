print("Hello, World!")

continuar = "s"

while continuar == "s":
    numero = input("Digite um número: ")

    for i in range(1, 11):
        resultado = int(numero) * i
        print(f"{numero} x {i} = {resultado}")

    continuar = input("Deseja digitar outro número? (s/n): ")

print("Programa encerrado.")
