import random
from datetime import datetime

cuentas = {}
nip_cuentas = {}
historial_transacciones = {}
historial_acceso = {}

def main():
    while True:
        print("\nBienvenido al Simulador de Banco")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            crear_cuenta()
        elif opcion == 2:
            iniciar_sesion()
        elif opcion == 3:
            print("Gracias por usar el Simulador de Banco. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def crear_cuenta():
    nombre = input("Ingrese su nombre: ")

    # Generar número de cuenta aleatorio
    numero_cuenta = "ACC" + str(1000 + random.randint(0, 9000))

    # Generar NIP aleatorio de 4 dígitos
    nip = 1000 + random.randint(0, 9000)

    cuentas[numero_cuenta] = 0.0
    nip_cuentas[numero_cuenta] = nip
    historial_transacciones[numero_cuenta] = []
    historial_acceso[numero_cuenta] = []

    print("¡Cuenta creada con éxito!")
    print("Su número de cuenta es:", numero_cuenta)
    print("Su NIP es:", nip)

def iniciar_sesion():
    numero_cuenta = input("Ingrese su número de cuenta: ")

    if numero_cuenta in cuentas:
        nip_ingresado = int(input("Ingrese su NIP: "))

        if nip_cuentas[numero_cuenta] == nip_ingresado:
            # Registrar acceso en el historial
            historial_acceso[numero_cuenta].append(f"Acceso: {datetime.now()}\n")

            mostrar_menu_principal(numero_cuenta)
        else:
            print("NIP incorrecto. Inténtelo de nuevo.")
    else:
        print("Número de cuenta no encontrado. Verifique e inténtelo de nuevo.")

def mostrar_menu_principal(numero_cuenta):
    while True:
        print("\nMenú Principal")
        print("1. Consultar saldo")
        print("2. Realizar depósito")
        print("3. Realizar retiro")
        print("4. Cambiar NIP")
        print("5. Ver historial de transacciones")
        print("6. Cerrar sesión")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            consultar_saldo(numero_cuenta)
        elif opcion == 2:
            realizar_deposito(numero_cuenta)
        elif opcion == 3:
            realizar_retiro(numero_cuenta)
        elif opcion == 4:
            cambiar_nip(numero_cuenta)
        elif opcion == 5:
            ver_historial_transacciones(numero_cuenta)
        elif opcion == 6:
            # Registrar cierre de sesión en el historial
            historial_acceso[numero_cuenta].append(f"Cierre de sesión: {datetime.now()}\n")

            print("Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def consultar_saldo(numero_cuenta):
    saldo = cuentas[numero_cuenta]
    print(f"Su saldo actual es: ${saldo:.2f}")

def realizar_deposito(numero_cuenta):
    cantidad = float(input("Ingrese la cantidad a depositar: $"))
    saldo_actual = cuentas[numero_cuenta]
    cuentas[numero_cuenta] = saldo_actual + cantidad

    historial_transacciones[numero_cuenta].append(f"Depósito de ${cantidad:.2f}\n")

    print(f"Depósito realizado con éxito. Nuevo saldo: ${cuentas[numero_cuenta]:.2f}")

def realizar_retiro(numero_cuenta):
    cantidad = float(input("Ingrese la cantidad a retirar: $"))
    saldo_actual = cuentas[numero_cuenta]

    if saldo_actual >= cantidad:
        cuentas[numero_cuenta] = saldo_actual - cantidad

        historial_transacciones[numero_cuenta].append(f"Retiro de ${cantidad:.2f}\n")

        print(f"Retiro realizado con éxito. Nuevo saldo: ${cuentas[numero_cuenta]:.2f}")
    else:
        print("Saldo insuficiente para realizar el retiro.")

def cambiar_nip(numero_cuenta):
    nuevo_nip = int(input("Ingrese su nuevo NIP (4 dígitos): "))
    nip_cuentas[numero_cuenta] = nuevo_nip

    print("NIP cambiado con éxito.")

def ver_historial_transacciones(numero_cuenta):
    print("Historial de transacciones:")
    for transaccion in historial_transacciones[numero_cuenta]:
        print(transaccion)

if __name__ == "__main__":
    main()
