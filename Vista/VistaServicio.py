from Controlador import ControladorServicio
from Controlador.ControladorServicioRealizado import ControladorServicioRealizado  # Asegúrate de importar la clase
from Modelo.Guardia import Guardia
from Modelo.Imaginaria import Imaginaria
from Modelo.Cuartelero import Cuartelero
from Vista.VistaServicioRealizado import VistaServicioRealizado


class VistaServicio:
    controladorServicioRealizado = ControladorServicioRealizado()  # Crea una instancia del controlador
    vistaServicioRealizado = VistaServicioRealizado(controladorServicioRealizado)

    def __init__(self, controladorServicio: ControladorServicio):
        self.controladorServicio = controladorServicio
        self.archivo = "servicios.json"
        self.cargarServicios()
        self.vistaServicioRealizado.cargarServicioRealizaodo()

    def menu(self):
        while True:
            self.mostrar_menu()
            opcion = self.obtener_opcion_usuario()
            if opcion == 1:
                self.crearServicio()
            elif opcion == 2:
                self.listarServicios()
            elif opcion == 3:
                self.buscarServicio()
            elif opcion == 4:
                self.actualizarServicio()
            elif opcion == 5:
                self.eliminarServicio()
            elif opcion == 6:
                self.agregarServicioRealizado()
            elif opcion == 7:
                self.eliminarServicioRealizado()
            elif opcion == 8:
                print("Saliendo del menú...")
                break
            else:
                print("Opción no válida, por favor elija una opción del 1 al 8.")

    def mostrar_menu(self):
        print("\nServicio")
        print("1. Crear Servicio")
        print("2. Listar Servicios")
        print("3. Buscar Servicio")
        print("4. Actualizar Servicio")
        print("5. Eliminar Servicio")
        print("6. Agregar ServicioRealizado a Servicio")
        print("7. Eliminar ServicioRealizado a Servicio")
        print("8. Salir")

    def obtener_opcion_usuario(self) -> int:
        while True:
            try:
                return int(input("Elija una opción: "))
            except ValueError:
                print("Error: Ingrese un número válido.")

    def crearServicio(self):
        tipo = input("Ingrese el tipo de Cuerpo (Guardia, Imaginaria, Cuartelero): ").lower()
        idServicio = input("Ingrese el ID del Cuerpo: ")
        descripcion = input("Ingrese la descripción del Servicio: ")

        if tipo == 'guardia':
            atributo1 = input("Ingrese el primer atributo adicional (Tipo de Guardia): ")
            atributo2 = int(input("Ingrese el segundo atributo adicional (Duración): "))
            cuerpo = Guardia(idServicio, descripcion, atributo1, atributo2)
        elif tipo == 'imaginaria':
            atributo1 = input("Ingrese el primer atributo adicional (Frecuencia): ")
            atributo2 = input("Ingrese el segundo atributo adicional (Tipo): ")
            cuerpo = Imaginaria(idServicio, descripcion, atributo1, atributo2)
        elif tipo == 'cuartelero':
            atributo1 = input("Ingrese el primer atributo adicional (Turno): ")
            atributo2 = input("Ingrese el segundo atributo adicional (Ubicación): ")
            cuerpo = Cuartelero(idServicio,descripcion, atributo1, atributo2)
        else:
            print("Tipo de servicio no válido.")
            return

        self.controladorServicio.create(cuerpo)
        print("Servicio creado exitosamente.")
        self.guardarServicios()

    def listarServicios(self):
        servicios = self.controladorServicio.index()
        if servicios:
            for servicio in servicios:
                print(servicio.toStr())
        else:
            print("No hay servicios registrados.")

    def buscarServicio(self):
        idServicio = input("Ingrese el ID del Servicio: ")
        servicio = self.controladorServicio.get(idServicio)
        if servicio is not None:
            print(servicio.toStr())
        else:
            print("Servicio no encontrado.")

    def actualizarServicio(self):
        tipo = input("Ingrese el tipo de Cuerpo (Guardia, Imaginaria, Cuartelero): ").lower()
        idServicio = input("Ingrese el ID del Cuerpo: ")
        descripcion = input("Ingrese la descripción del Servicio: ")

        if tipo == 'guardia':
            atributo1 = input("Ingrese el primer atributo adicional (Tipo de Guardia): ")
            atributo2 = int(input("Ingrese el segundo atributo adicional (Duración): "))
            cuerpo = Guardia(idServicio, descripcion, atributo1, atributo2)
        elif tipo == 'imaginaria':
            atributo1 = input("Ingrese el primer atributo adicional (Frecuencia): ")
            atributo2 = input("Ingrese el segundo atributo adicional (Tipo): ")
            cuerpo = Imaginaria(idServicio, descripcion, atributo1, atributo2)
        elif tipo == 'Cuartelero':
            atributo1 = input("Ingrese el primer atributo adicional (Turno): ")
            atributo2 = input("Ingrese el segundo atributo adicional (Ubicación): ")
            cuerpo = Cuartelero(idServicio, descripcion, atributo1, atributo2)
        else:
            print("Tipo de servicio no válido.")
            return

        servicio_actualizado = self.controladorServicio.update(cuerpo)
        if servicio_actualizado:
            print("Servicio actualizado exitosamente.")
            self.guardarServicios()
        else:
            print("Servicio no encontrado.")

    def eliminarServicio(self):
        idServicio = input("Ingrese el ID del Servicio: ")
        eliminado = self.controladorServicio.delete(idServicio)
        if eliminado:
            print("Servicio eliminado exitosamente.")
            self.guardarServicios()
        else:
            print("Servicio no encontrado.")

    def agregarServicioRealizado(self):
        idServicio = input("Ingrese el ID del Servicio: ")
        idServicioRealizado = input("Ingrese el ID del ServicioRealizado: ")

        servicio = self.controladorServicio.get(idServicio)
        servicioRealizado = self.controladorServicioRealizado.get(idServicioRealizado)

        if servicio is not None:
            servicio.agregarServicioRealizado(servicioRealizado)
            print("ServicioRealizado agregado exitosamente.")
            self.guardarServicios()
        else:
            print("Servicio no encontrado.")

    def eliminarServicioRealizado(self):
        idServicio = input("Ingrese el ID del Servicio: ")
        idServicioRealizado = input("Ingrese el ID del ServicioRealizado: ")

        servicio = self.controladorServicio.get(idServicio)
        servicioRealizado = self.controladorServicioRealizado.get(idServicioRealizado)

        if servicio is not None:
            servicio.eliminarServicioRealizado(servicioRealizado)
            print("ServicioRealizado eliminado exitosamente.")
            self.guardarServicios()
        else:
            print("Servicio no encontrado.")

    def guardarServicios(self):
        self.controladorServicio.guardar(self.archivo)

    def cargarServicios(self):
        self.controladorServicio.cargar(self.archivo)
