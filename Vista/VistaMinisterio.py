from Controlador import ControladorMinisterio
from Modelo.Ministerio import Ministerio
from Controlador.ControladorCuerpo import ControladorCuerpo
from Vista.VistaCuerpo import VistaCuerpo

class VistaMinisterio:

    controladorcuerpo = ControladorCuerpo()
    vistacuerpo = VistaCuerpo(controladorcuerpo)

    def __init__(self, controladorministerio: ControladorMinisterio):
        self.controladorministerio = controladorministerio
        self.archivo = "ministerios.json"
        self.cargarMinisterios()  # Cargar ministerios automáticamente al iniciar
        self.vistacuerpo.cargarCuerpos()  # Cargar cuerpos automáticamente al iniciar


    def menu(self):
        while True:
            try:
                print("\nMINISTERIO")
                print("1. Crear Ministerio")
                print("2. Listar Ministerios")
                print("3. Buscar Ministerio")
                print("4. Actualizar Ministerio")
                print("5. Eliminar Ministerio")
                print("6. Agregar Cuerpo a Ministerio")
                print("7. Eliminar Cuerpo de Ministerio")
                print("8. Salir")
                opcion = int(input("Elija una opción: "))

                if opcion == 1:
                    self.crearMinisterio()
                elif opcion == 2:
                    self.listarMinisterios()
                elif opcion == 3:
                    self.buscarMinisterio()
                elif opcion == 4:
                    self.actualizarMinisterio()
                elif opcion == 5:
                    self.eliminarMinisterio()
                elif opcion == 6:
                    self.agregarCuerpoMinisterio()
                elif opcion == 7:
                    self.eliminarCuerpoMinisterio()
                elif opcion == 8:
                    print("Saliendo del menú...")
                    break
                else:
                    print("Opción no válida, por favor elija una opción del 1 al 8.")
            except ValueError:
                print("Error: Ingrese un número válido.")

    def crearMinisterio(self):
        idMinisterio = input("Ingrese el ID del Ministerio: ")
        nombre = input("Ingrese el nombre del Ministerio: ")
        informacion = input("Ingrese la información del Ministerio: ")

        ministerio = Ministerio(idMinisterio, nombre, informacion)
        self.controladorministerio.create(ministerio)
        print("Ministerio creado exitosamente.")
        self.guardarMinisterios()  # Guardar automáticamente después de crear

    def listarMinisterios(self):
        ministerios = self.controladorministerio.index()
        if ministerios:
            for ministerio in ministerios:
                print(ministerio.toStr())
        else:
            print("No hay ministerios registrados.")

    def buscarMinisterio(self):
        idMinisterio = input("Ingrese el ID del Ministerio: ")
        ministerio = self.controladorministerio.get(idMinisterio)
        if ministerio is not None:
            print(ministerio.toStr())
        else:
            print("Ministerio no encontrado.")

    def actualizarMinisterio(self):
        idMinisterio = input("Ingrese el ID del Ministerio: ")
        nombre = input("Ingrese el nombre del Ministerio: ")
        informacion = input("Ingrese la información del Ministerio: ")

        ministerio = Ministerio(idMinisterio, nombre, informacion)
        ministerio_actualizado = self.controladorministerio.update(ministerio)
        if ministerio_actualizado is not None:
            print("Ministerio actualizado exitosamente.")
            self.guardarMinisterios()  # Guardar automáticamente después de actualizar
        else:
            print("Ministerio no encontrado.")

    def eliminarMinisterio(self):
        idMinisterio = input("Ingrese el ID del Ministerio: ")
        eliminado = self.controladorministerio.delete(idMinisterio)
        if eliminado:
            print("Ministerio eliminado exitosamente.")
            self.guardarMinisterios()  # Guardar automáticamente después de eliminar
        else:
            print("Ministerio no encontrado.")

    def agregarCuerpoMinisterio(self):
        idMinisterio = input("Ingrese el ID del Ministerio: ")
        idCuerpo = input("Ingrese el ID del Cuerpo: ")

        cuerpo = self.controladorcuerpo.get(idCuerpo)
        ministerio = self.controladorministerio.get(idMinisterio)

        if ministerio is not None:
            ministerio.agregarCuerpo(cuerpo)
            print("Cuerpo agregado exitosamente.")
            self.guardarMinisterios()  # Guardar automáticamente después de agregar un cuerpo
        else:
            print("Ministerio no encontrado.")

    def eliminarCuerpoMinisterio(self):
        idMinisterio = input("Ingrese el ID del Ministerio: ")
        idCuerpo = input("Ingrese el ID del Cuerpo: ")

        ministerio = self.controladorministerio.get(idMinisterio)
        if ministerio is not None:
            ministerio.eliminarCuerpo(idCuerpo)
            print("Cuerpo eliminado exitosamente.")
            self.guardarMinisterios()

    # Métodos para guardar y cargar automáticamente
    def guardarMinisterios(self):
        """Guarda los ministerios automáticamente."""
        self.controladorministerio.guardar(self.archivo)

    def cargarMinisterios(self):
        """Carga los ministerios automáticamente al iniciar el programa."""
        self.controladorministerio.cargar(self.archivo)
