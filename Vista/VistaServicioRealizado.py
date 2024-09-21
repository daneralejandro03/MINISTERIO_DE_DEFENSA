from datetime import datetime

from Controlador import ControladorServicioRealizado
from Modelo.ServicioRealizado import ServicioRealizado

class VistaServicioRealizado:

    def __init__(self, controladorServicioRealizaodo: ControladorServicioRealizado):
        self.controladorServicioRealizaodo = controladorServicioRealizaodo
        self.archivo = "serviciosRealizados.json"
        self.cargarServicioRealizaodo()

    def menu(self):
        while True:
            try:
                print("\nServicio Realizado")
                print("1. Crear Servicio Realizado")
                print("2. Listar Servicios Realizados")
                print("3. Buscar Servicio Realizado")
                print("4. Actualizar Servicio Realizado")
                print("5. Eliminar Servicio Realizado")
                print("6. Salir")
                opcion = int(input("Elija una opción: "))

                if opcion == 1:
                    self.crearServicioRealizado()
                elif opcion == 2:
                    self.listarServiciosRealizados()
                elif opcion == 3:
                    self.buscarServicioRealizado()
                elif opcion == 4:
                    self.actualizarServicioRealizaodo()
                elif opcion == 5:
                    self.eliminarServicioRealizado()
                elif opcion == 6:
                    print("Saliendo del menú...")
                    break
                else:
                    print("Opción no válida, por favor elija una opción del 1 al 6.")
            except ValueError:
                print("Error: Ingrese un número válido.")

    def crearServicioRealizado(self):
        idServicioRealizado = input("Ingrese el ID del Sservicio Realizado: ")
        actividad = input("Ingrese la actividad del Servicio Realizado: ")

        # Pedimos la fecha y la convertimos al formato datetime
        fecha_str = input("Ingrese la fecha del Servicio Realizado (formato YYYY-MM-DD): ")
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return  # Se detiene si la fecha es incorrecta

        despliegue = ServicioRealizado(idServicioRealizado, actividad, fecha)
        self.controladorServicioRealizaodo.create(despliegue)
        print("Servicio Realizado creado exitosamente.")
        self.guardarServicioRealizado()


    def listarServiciosRealizados(self):
        serviciosRealizados = self.controladorServicioRealizaodo.index()
        if serviciosRealizados:
            for servicioRealizado in serviciosRealizados:
                print(servicioRealizado.toStr())
        else:
            print("No hay Servicios Realizados.")

    def buscarServicioRealizado(self):
        idDespliegue = input("Ingrese el ID del Servicio Realizado: ")
        despliegue = self.controladorServicioRealizaodo.get(idDespliegue)
        if despliegue is not None:
            print(despliegue.toStr())
        else:
            print("Servicio Realizado no encontrado.")

    def actualizarServicioRealizaodo(self):
        idServicioRealizado = input("Ingrese el ID del Sservicio Realizado: ")
        actividad = input("Ingrese la actividad del Servicio Realizado: ")

        # Pedimos la fecha y la convertimos al formato datetime
        fecha_str = input("Ingrese la fecha del Servicio Realizado (formato YYYY-MM-DD): ")
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return  # Se detiene si la fecha es incorrecta

        servicioRealizado = ServicioRealizado(idServicioRealizado, actividad, fecha)
        actualizado = self.controladorServicioRealizaodo.update(servicioRealizado)
        if actualizado:
            print("Servicio Realizado actualizado exitosamente.")
            self.guardarServicioRealizado()
        else:
            print("Servicio Realizaodo no encontrado.")

    def eliminarServicioRealizado(self):
        idServicioRealizado = input("Ingrese el ID del Servicio Realizado: ")
        eliminado = self.controladorServicioRealizaodo.delete(idServicioRealizado)
        if eliminado:
            print("Servicio Realizado eliminado exitosamente.")
            self.guardarServicioRealizado()
        else:
            print("Servicio Realizado no encontrado.")


    # Métodos para guardar y cargar automáticamente
    def guardarServicioRealizado(self):
        """Guarda automáticamente las compañías al salir de la aplicación."""
        self.controladorServicioRealizaodo.guardar(self.archivo)

    def cargarServicioRealizaodo(self):
        """Carga automáticamente las compañías al iniciar la aplicación."""
        self.controladorServicioRealizaodo.cargar(self.archivo)


