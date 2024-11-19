from mi_paquete import Cliente, Producto, Carrito, GestorDeClientes
import os

def main():
    gestor = GestorDeClientes()
    base_datos = {}

    while True:
        # Registro al nuevo usuario
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        contrasena = input("Ingrese la contraseña (Solo numeros): ")
        if nombre_usuario in base_datos:
            print("El usuario ya está registrado.\n")
        else:
            base_datos[nombre_usuario] = contrasena
            print("Usuario registrado exitosamente.\n")

        print("Ingrese sus datos:")
        
        # Ingresa los datos del clientes y registra la compra
        while True:
            email = input("Email del cliente (o 'salir' para terminar): ")
            if email.lower() == 'salir':
                break

            # Verifica si el cliente ya está registrado
            if gestor.cliente_registrado(email):
                print("El cliente ya está registrado.")
                continue

            nombre = input("Nombre del cliente: ")
            apellido = input("Apellido del cliente: ")
            direccion = input("Dirección del cliente: ")
            gestor.agregar_cliente(nombre=f"{nombre} {apellido}", email=email, direccion=direccion)

            # Crea el producto y calcula el total de la venta
            print("\nRealice la compra:")
            productos = []
            total_venta = 0
            num_productos = int(input("¿Cuántos productos deseas ingresar? "))
            for _ in range(num_productos):
                nombre_producto = input("Nombre del producto: ")
                precio_producto = float(input("Precio del producto: "))
                producto = Producto(id=len(productos) + 1, nombre=nombre_producto, precio=precio_producto)
                productos.append(producto)
                total_venta += precio_producto

            # Asigna productos al carrito del cliente recién registrado
            cliente = gestor.clientes[gestor.proximo_id_cliente - 1]
            for producto in productos:
                cliente.agregar_producto_al_carrito(producto)
            cliente.mostrar_carrito()

            # Muestrar el total de la venta
            print(f"Total de la venta: ${total_venta}")

            # Solicita el medio de pago
            medio_pago = input("Medio de pago (tarjeta, efectivo, etc.): ")

            # Login usuario antes de pagar
            while True:
                nombre_usuario = input("Ingrese el nombre de usuario para login: ")
                contrasena = input("Ingrese la contraseña: ")
                if nombre_usuario in base_datos and base_datos[nombre_usuario] == contrasena:
                    print("Login exitoso.\n")
                    break
                else:
                    print("Usuario o contraseña incorrectos. Intente de nuevo.\n")

            # Muestra el resumen de la compra
            print("\n--- Resumen de la Compra ---")
            print(f"Cliente: {cliente.nombre}, Email: {cliente.email}, Dirección: {cliente.direccion}")
            for producto in productos:
                print(f"Producto: {producto.nombre}, Precio: ${producto.precio}")
            print(f"Total de la venta: ${total_venta}")
            print(f"Medio de pago: {medio_pago}")
            print("Pago realizado con éxito.\n")

            # Guarda los datos de la compra en un archivo de texto
            guardar_compra(cliente, productos, total_venta, medio_pago)

            # Salir del bucle interno para registrar un nuevo usuario
            break

def guardar_compra(cliente, productos, total_venta, medio_pago):
    directorio = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(directorio, "compras.txt"), "a") as file:
        file.write(f"Cliente: {cliente.nombre}, Email: {cliente.email}, Dirección: {cliente.direccion}\n")
        for producto in productos:
            file.write(f"Producto: {producto.nombre}, Precio: ${producto.precio}\n")
        file.write(f"Total de la venta: ${total_venta}\n")
        file.write(f"Medio de pago: {medio_pago}\n")
        file.write("-----\n")

if __name__ == "__main__":
    main()
#fin del programa