from codebreaker import Codebreaker

intentos_totales = 10
codebreaker = Codebreaker()

intento = 0

print(
    "Jugar Codebreaker!\nTienes 10 intentos para adivinar el numero de 4 dígitos, "
    "cada X significa que tienes un numero correcto en la posición correcta y cada _ "
    "significa que tienes un numero correcto en la posición incorrecta. Suerte!"
)

while intento != intentos_totales:
    number = input("Numero:")
    resolve = codebreaker.adivinar(number)
    print(resolve)
    if resolve == "XXXX":
        print("You win!!")
        break
    if intento == intentos_totales - 1:
        print("You lose!!")
        break
    if resolve == "error":
        print("El numero debe tener 4 dígitos")
    if resolve == "Number is not defined":
        print("El numero no esta definido")

    intento += 1