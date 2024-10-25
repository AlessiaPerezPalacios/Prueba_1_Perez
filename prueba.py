usuarios = {
    "pedro mendoza": "pepito23",
    "luis vargan": "abc456001"
}


menus = {
    "Desayuno Americano": 2.75,
    "Almuerzo Ejecutivo": 4.75,
    "Almuerzo Politécnico": 3.25,
    "Almuerzo Vegetariano": 4.75
}


def login():
    intentos = 3
    while intentos > 0:
        usuario = input("Ingrese su nombre de usuario: ").lower().strip()
        clave = input("Ingrese su clave (8 caracteres): ").strip()
        
        if len(clave) != 8:
            print("La clave debe tener exactamente 8 caracteres.")
            continue
        
        if usuario in usuarios and usuarios[usuario] == clave:
            print("\nAcceso concedido.\n")
            return True
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
    
    print("\nAcceso bloqueado. Inténtelo más tarde.")
    return False


def mostrar_menu():
    print("Menús disponibles:")
    for nombre, precio in menus.items():
        print(f"- {nombre}: ${precio:.2f}")
    
    seleccion = []
    while True:
        opcion = input("\nIngrese el nombre del menú que desea (o 'salir' para finalizar): ")
        if opcion.lower() == "salir":
            break
        elif opcion in menus:
            seleccion.append(opcion)
            print(f"{opcion} añadido al pedido.")
        else:
            print("Menú no disponible. Intente de nuevo.")
    
    return seleccion


def calcular_total(seleccion, metodo_pago):
    subtotal = sum(menus[menu] for menu in seleccion)
    print(f"\nSubtotal: ${subtotal:.2f}")
    
    if metodo_pago.lower() == "efectivo":
        descuento = subtotal * 0.10
        total = subtotal - descuento
        print(f"Descuento del 10% aplicado: -${descuento:.2f}")
    elif metodo_pago.lower() == "tarjeta":
        recargo = subtotal * 0.12
        total = subtotal + recargo
        print(f"Recargo del 12% aplicado: +${recargo:.2f}")
    else:
        print("Método de pago no válido.")
        return None
    
    return total


def main():
    if not login():
        return
    
    seleccion = mostrar_menu()
    
    if not seleccion:
        print("No se seleccionaron menús. Saliendo del programa.")
        return
    
    metodo_pago = input("\nIngrese el método de pago (efectivo/tarjeta): ").lower()
    total = calcular_total(seleccion, metodo_pago)
    
    if total is not None:
        print(f"\nTotal a pagar: ${total:.2f}")

main()
