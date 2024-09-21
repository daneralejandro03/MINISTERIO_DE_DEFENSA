from datetime import datetime

from Controlador import ControladorDespliegue
from Modelo.Despliegue import Despliegue

class VistaDespliegue:

    def __init__(self, controladordespliegue: ControladorDespliegue):
        self.controladordespliegue = controladordespliegue
        self.archivo = "despliegues.json"
        self.cargarDespliegue()

    def menu(self):
        while True:
            try:
                print("\nDespliegue")
                print("1. Crear Despliegue")
                print("2. Listar Despliegues")
                print("3. Buscar Despliegues")
                print("4. Actualizar Despliegues")
                print("5. Eliminar Despliegues")
                print("6. Salir")
                opcion = int(input("Elija una opción: "))

                if opcion == 1:
                    self.crearDespliegue()
                elif opcion == 2:
                    self.listarDespliegues()
                elif opcion == 3:
                    self.buscarDespliegue()
                elif opcion == 4:
                    self.actualizarDespliegue()
                elif opcion == 5:
                    self.eliminarDespliegue()
                elif opcion == 6:
                    print("Saliendo del menú...")
                    break
                else:
                    print("Opción no válida, por favor elija una opción del 1 al 6.")
            except ValueError:
                print("Error: Ingrese un número válido.")

    def crearDespliegue(self):
        idDespliegue = input("Ingrese el ID del Despliegue: ")
        informacion = input("Ingrese la información del Despliegue: ")

        # Pedimos la fecha y la convertimos al formato datetime
        fecha_str = input("Ingrese la fecha del Despliegue (formato YYYY-MM-DD): ")
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return  # Se detiene si la fecha es incorrecta

        despliegue = Despliegue(idDespliegue, informacion, fecha)
        self.controladordespliegue.create(despliegue)
        print("Despliegue creado exitosamente.")
        self.guardarDespliegue()


    def listarDespliegues(self):
        despliegues = self.controladordespliegue.index()
        if despliegues:
            for despliegue in despliegues:
                print(despliegue.toStr())
        else:
            print("No hay despliegues registrados.")

    def buscarDespliegue(self):
        idDespliegue = input("Ingrese el ID del Despliegue: ")
        despliegue = self.controladordespliegue.get(idDespliegue)
        if despliegue:
            print(despliegue.toStr())
        else:
            print("Despliegue no encontrado.")

    def actualizarDespliegue(self):
        idDespliegue = input("Ingrese el ID del Despliegue: ")
        informacion = input("Ingrese la nueva información del Despliegue: ")

        # Pedimos la fecha y la convertimos al formato datetime
        fecha_str = input("Ingrese la nueva fecha del Despliegue (formato YYYY-MM-DD): ")
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return

        despliegue = Despliegue(idDespliegue, informacion, fecha)
        actualizado = self.controladordespliegue.update(despliegue)
        if actualizado:
            print("Despliegue actualizado exitosamente.")
            self.guardarDespliegue()
        else:
            print("Despliegue no encontrado.")

    def eliminarDespliegue(self):
        idDespliegue = input("Ingrese el ID del Despliegue: ")
        eliminado = self.controladordespliegue.delete(idDespliegue)
        if eliminado:
            print("Despliegue eliminado exitosamente.")
            self.guardarDespliegue()
        else:
            print("Despliegue no encontrado.")


    # Métodos para guardar y cargar automáticamente
    def guardarDespliegue(self):
        """Guarda automáticamente las compañías al salir de la aplicación."""
        self.controladordespliegue.guardar(self.archivo)

    def cargarDespliegue(self):
        """Carga automáticamente las compañías al iniciar la aplicación."""
        self.controladordespliegue.cargar(self.archivo)


