from Sender import Sender
from os.path import exists

def read_phone():
    print("Ingrese número de teléfono en formato 569xxxxxxxx:")
    return int(input())

def send_message(sender: Sender):
    print("Ingrese mensaje:")
    message = input()

    print("Ingrese repeticiones:")
    amount = int(input())

    sender.send_message(message, amount)

def send_image(sender: Sender):
    print("Ingrese nombre del archivo:")
    file = input()
    path = f"images/{file}"

    if not exists(path):
        print("Error: el archivo no existe")
        return
    
    print("Ingrese repeticiones:")
    amount = int(input())
    
    sender.send_image(path, amount)

########################################

phone = read_phone()
sender = Sender(phone)

while True:
    print("Opciones")
    print("1. Enviar mensaje de texto")
    print("2. Enviar imagen")
    print("3. Salir")

    print("Ingrese opción:")
    option = int(input())

    if option == 1:
        send_message(sender)
    elif option == 2:
        send_image(sender)
    elif option == 3:
        sender.destroy()
        break
    else:
        print("Opción no válida\n")
    
