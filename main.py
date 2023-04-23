from Sender import Sender

def read_phone():
    print("Ingrese número de teléfono en formato 569xxxxxxxx:")
    return int(input())

def send_message(sender: Sender):
    print("Ingrese mensaje:")
    message = input()

    print("Ingrese repeticiones:")
    amount = int(input())

    sender.send_message(message, amount)

########################################

phone = read_phone()
sender = Sender(phone)

while True:
    print("Opciones")
    print("1. Enviar mensaje de texto")
    print("2. Salir")

    print("Ingrese opción:")
    option = int(input())

    if option == 1:
        send_message(sender)
    elif option == 2:
        sender.destroy()
        break
    else:
        print("Opción no válida\n")
    
