from Controlador import ControladorSoldado
from Controlador.ControladorServicioRealizado import ControladorServicioRealizado  # Asegúrate de importar la clase
from Modelo.Soldado import Soldado
from Vista.VistaServicioRealizado import VistaServicioRealizado


class VistaSoldado:

    controladorServicioRealizado = ControladorServicioRealizado()  # Crea una instancia del controlador
    vistaServicioRealizado = VistaServicioRealizado(controladorServicioRealizado)

    def __init__(self, controladorsoldado: ControladorSoldado):
        self.controladorsoldado = controladorsoldado  # Usa la instancia pasada correctamente
        self.archivo = "soldados.json"
        self.cargarSoldados()
        self.vistaServicioRealizado.cargarServicioRealizaodo()

    def menu(self):
        while True:
            try:
                print("\nSOLDADO")
                print("1. Crear Soldado")
                print("2. Listar Soldados")
                print("3. Buscar Soldado")
                print("4. Actualizar Soldado")
                print("5. Eliminar Soldado")
                print("6. Agregar Servicio Realizado a Soldado")
                print("7. Eliminar Servicio Realizado de Soldado")
                print("8. Salir")
                opcion = int(input("Elija una opción: "))

                if opcion == 1:
                    self.crearSoldado()
                elif opcion == 2:
                    self.listarSoldados()
                elif opcion == 3:
                    self.buscarSoldado()
                elif opcion == 4:
                    self.actualizarSoldado()
                elif opcion == 5:
                    self.eliminarSoldado()
                elif opcion == 6:
                    self.agregarServicioRealizadoSoldado()
                elif opcion == 7:
                    self.eliminarServicioRealizadoSoldado()
                elif opcion == 8:
                    print("Saliendo del menú...")
                    break
                else:
                    print("Opción no válida, por favor elija una opción del 1 al 6.")
            except ValueError:
                print("Error: Ingrese un número válido.")

    def crearSoldado(self):
        idSoldado = input("Ingrese el ID del Soldado: ")
        nombre = input("Ingrese el nombre del Soldado: ")
        informacion = input("Ingrese la información del Soldado: ")

        soldado = Soldado(idSoldado, nombre, informacion)
        self.controladorsoldado.create(soldado)
        print("Soldado creado exitosamente.")
        self.guardarSoldados()

    def listarSoldados(self):
        soldados = self.controladorsoldado.index()
        if soldados:
            for soldado in soldados:
                print(soldado.toStr()) # Uso correcto de toStr
        else:
            print("No hay soldados registrados.")

    def buscarSoldado(self):
        idSoldado = input("Ingrese el ID del Soldado: ")
        soldado = self.controladorsoldado.get(idSoldado)
        print(soldado)
        if soldado is not None:
            print(soldado.toStr())  # Uso correcto de toStr
        else:
            print("Soldado no encontrado.")

    def actualizarSoldado(self):
        idSoldado = input("Ingrese el ID del Soldado: ")
        nombre = input("Ingrese el nuevo nombre del Soldado: ")
        informacion = input("Ingrese la nueva información del Soldado: ")

        soldado = Soldado(idSoldado, nombre, informacion)
        actualizado = self.controladorsoldado.update(soldado)
        if actualizado:
            print("Soldado actualizado exitosamente.")
            self.guardarSoldados()
        else:
            print("Soldado no encontrado.")

    def eliminarSoldado(self):
        idSoldado = input("Ingrese el ID del Soldado: ")
        eliminado = self.controladorsoldado.delete(idSoldado)
        if eliminado:
            print("Soldado eliminado exitosamente.")
            self.guardarSoldados()
        else:
            print("Soldado no encontrado.")

    def agregarServicioRealizadoSoldado(self):
        idSoldado = input("Ingrese el ID del Soldado: ")
        idServicioRealizado = input("Ingrese el ID del Servicio Realizado: ")

        soldado = self.controladorsoldado.get(idSoldado)
        servicioRealizado = self.controladorServicioRealizado.get(idServicioRealizado)

        if soldado is not None:
            soldado.agregarServicioRealizado(servicioRealizado)
            print("Servicio Realizado agregado exitosamente.")
            self.guardarSoldados()
        else:
            print("Soldado no encontrado.")

    def eliminarServicioRealizadoSoldado(self):
        idSoldado = input("Ingrese el ID del Soldado: ")
        idServicioRealizado = input("Ingrese el ID del Servicio Realizado: ")

        soldado = self.controladorsoldado.get(idSoldado)
        if soldado is not None:
            soldado.eliminarServicioRealizado(idServicioRealizado)
            print("Servicio Realizado eliminado exitosamente.")
            self.guardarSoldados()
        else:
            print("Soldado no encontrado.")


    # Métodos para guardar y cargar automáticamente
    def guardarSoldados(self):
        """Guarda automáticamente los soldados al realizar una acción."""
        self.controladorsoldado.guardar(self.archivo)

    def cargarSoldados(self):
        """Carga automáticamente los soldados al iniciar la aplicación."""
        self.controladorsoldado.cargar(self.archivo)
