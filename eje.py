#Sistema de uber eats

print("Hola, acaba de entrar a uber eats")
nombre = input("¿Cómo te llamas? ")

# Selección de tu comida
print(" **que tipo de comida desea?**")
print("1. comida mexicana")
print("2. comida italiana")
print("3. comida asiatica")
print("4. comida rapida")
print("5. postres")

comida = {
    1: ("comida mexicana", 120),
    2: ("comida italiana", 200),
    3: ("comida asiatica", 230),
    4: ("comida rapida", 100),
    5: ("postres", 85)}

comida_opcion = int(input("Selecciona tu tipo de comida (1-5): "))

if comida_opcion in comida:
    comida, precio_base = comida[comida_opcion]
    print(f"Has seleccionado como comida: {comida}")
else:
    print("comida no válido. El programa finalizará.")
    exit()

# Selección de envio
print(" **Selecciona una opción de envio**")
print("1. Entrega en 1 hora - Gratis")
print("2. Entrega en 30 minutos - $50 MXN")

opcion_envio = int(input("Escribe la opción que deseas usar: "))
if opcion_envio == 1:
    envio_costo = 0  # Entrega en 1 hora
    print("Tu pedido no tiene costo extra de envio.")
elif opcion_envio == 2:
    envio_costo = 50  # Entrega en 30 minutos extra de 50 MXN
    print("Tu pedido tiene un extra de $50 MXN.")
else:
    print("Opción no válida. Asignando equipaje de mano por defecto.")
    envio_costo = 0

# IVA (Impuesto al Valor Agregado)
IVA = 20  # IVA fija
print(f"El IVA (impuesto al valor agregado) es de: ${IVA} MXN")

# Aplicar descuentos
print("**Promociones disponibles**")
print("1. 10% de descuento por promoción del estilo de la comida")
print("2. 15% de descuento por cliente frecuente")
print("3. No aplicar ningún descuento")

opcion_descuento = int(input("Selecciona una promoción o descuento (1-3): "))

total = precio_base + envio_costo + IVA

if opcion_descuento == 1:
    total *= 0.90  # 10% de descuento
    print("Se ha aplicado un 10% de descuento.")
elif opcion_descuento == 2:
    total *= 0.85  # 15% de descuento
    print("Se ha aplicado un 15% de descuento.")
elif opcion_descuento == 3:
    print("No se aplicarán descuentos.")
else:
    print("Opción no válida. No se aplicarán descuentos.")

# Total a pagar
print(f"Subtotal sin descuentos: ${precio_base + envio_costo + IVA} MXN")
print(f"Total a pagar con descuentos aplicados: ${total:.2f} MXN")

print(f"Gracias por tu compra, {nombre}. El total de tu comida {comida} es: ${total:.2f} MXN.")
print("¡Buen provecho!")