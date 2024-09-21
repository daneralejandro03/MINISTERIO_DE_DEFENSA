from Controlador import ControladorCuartel
from Modelo.Cuartel import Cuartel
from Vista.VistaDespliegue import VistaDespliegue
from Controlador.ControladorDespliegue import ControladorDespliegue

class VistaCuartel:

    controladorDespliegue = ControladorDespliegue()
    vistaDespliegue = VistaDespliegue(controladorDespliegue)

    def __init__(self, controladorcuartel: ControladorCuartel):
        self.controladorcuartel = controladorcuartel  # Usa la instancia pasada correctamente
        self.archivo = "cuarteles.json"
        self.cargarCuarteles()
        self.vistaDespliegue.cargarDespliegue()

    def menu(self):
        while True:
            try:
                print("\nCuartel")
                print("1. Crear Cuartle")
                print("2. Listar Cuarteles")
                print("3. Buscar Cuartel")
                print("4. Actualizar Cuartel")
                print("5. Eliminar Cuartel")
                print("6. Agregar Despliegue a Cuartel")
                print("7. Eliminar Despliegue de Cuartel")
                print("8. Salir")
                opcion = int(input("Elija una opción: "))

                if opcion == 1:
                    self.crearCuartel()
                elif opcion == 2:
                    self.listarCuarteles()
                elif opcion == 3:
                    self.buscarCuartel()
                elif opcion == 4:
                    self.actualizarcuartel()
                elif opcion == 5:
                    self.eliminarCuartel()
                elif opcion == 6:
                    self.agregarDespliegueCuartel()
                elif opcion == 7:
                    self.eliminarDespliegueCuartel()
                elif opcion == 8:
                    print("Saliendo del menú...")
                    break
                else:
                    print("Opción no válida, por favor elija una opción del 1 al 8.")
            except ValueError:
                print("Error: Ingrese un número válido.")

    def crearCuartel(self):
        idCuartel = input("Ingrese el ID del Cuartel: ")
        nombre = input("Ingrese el nombre del Cuartel: ")
        informacion = input("Ingrese la ubicación del Cuartel: ")

        cuartel = Cuartel(idCuartel, nombre, informacion)
        self.controladorcuartel.create(cuartel)
        print("Cuartel creado exitosamente.")
        self.guardarCuarteles()

    def listarCuarteles(self):
        cuarteles = self.controladorcuartel.index()
        if cuarteles:
            for cuartel in cuarteles:
                print(cuartel.toStr())
        else:
            print("No hay cuarteles registrados.")


    def buscarCuartel(self):
        idCuartel = input("Ingrese el ID del Cuartel: ")
        cuartel = self.controladorcuartel.get(idCuartel)
        if cuartel:
            print(cuartel.toStr())
        else:
            print("Cuartel no encontrado.")


    def actualizarcuartel(self):
        idCuartel = input("Ingrese el ID del Cuartel: ")
        nombre = input("Ingrese el nombre del Cuartel: ")
        informacion = input("Ingrese la información del Cuartel: ")

        cuartel = Cuartel(idCuartel, nombre, informacion)
        actualizado = self.controladorcuartel.update(cuartel)
        if actualizado:
            print("Cuartel actualizado exitosamente.")
            self.guardarCuarteles()
        else:
            print("Cuartel no encontrado.")


    def eliminarCuartel(self):
        idCuartel = input("Ingrese el ID del Cuartel: ")
        eliminado = self.controladorcuartel.delete(idCuartel)
        if eliminado:
            print("Cuartel eliminado exitosamente.")
            self.guardarCuarteles()
        else:
            print("Cuartel no encontrado.")

    def agregarDespliegueCuartel(self):
        idCuartel = input("Ingrese el ID del Cuartel: ")
        idDespliegue = input("Ingrese el ID del Despliegue: ")

        cuartel = self.controladorcuartel.get(idCuartel)
        despliegue = self.controladorDespliegue.get(idDespliegue)
        if cuartel is not None:
            cuartel.agregarDespliegue(despliegue)
            print("Despliegue agregado exitosamente.")
            self.guardarCuarteles()
        else:
            print("Cuartel no encontrado.")

    def eliminarDespliegueCuartel(self):
        idCuartel = input("Ingrese el ID del Cuartel: ")
        idDespliegue = input("Ingrese el ID del Despliegue: ")

        cuartel = self.controladorcuartel.get(idCuartel)
        despliegue = self.controladorDespliegue.get(idDespliegue)
        if cuartel is not None:
            cuartel.eliminarDespliegue(despliegue)
            print("Despliegue eliminado exitosamente.")
            self.guardarCuarteles()
        else:
            print("Cuartel no encontrado.")

    # Métodos para guardar y cargar automáticamente
    def guardarCuarteles(self):
        """Guarda automáticamente los soldados al realizar una acción."""
        self.controladorcuartel.guardar(self.archivo)

    def cargarCuarteles(self):
        """Carga automáticamente los soldados al iniciar la aplicación."""
        self.controladorcuartel.cargar(self.archivo)
