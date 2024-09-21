from Controlador import ControladorCompania
from Modelo.Compania import Compania
from Vista.VistaSoldado import VistaSoldado
from Controlador.ControladorSoldado import ControladorSoldado
from Controlador.ControladorDespliegue import ControladorDespliegue
from Vista.VistaDespliegue import VistaDespliegue

class VistaCompania:

    controladorSoldado = ControladorSoldado()
    vistaSoldado = VistaSoldado(controladorSoldado)

    controladorDespliegue = ControladorDespliegue()
    vistaDespliegue = VistaDespliegue(controladorDespliegue)

    def __init__(self, controladorcompania: ControladorCompania):
        self.controladorcompania = controladorcompania
        self.archivo = "companias.json"
        self.cargarCompania()
        self.vistaSoldado.cargarSoldados()
        self.vistaDespliegue.cargarDespliegue()


    def menu(self):
        while True:
            try:
                print("\nCompañía")
                print("1. Crear Compañia")
                print("2. Listar Compañias")
                print("3. Buscar Compañia")
                print("4. Actualizar Compañia")
                print("5. Eliminar Compañia")
                print("6. Agregar Soldado a Compañia")
                print("7. Eliminar Soldado de Compañia")
                print("8. Agregar Despliegue a Compañia")
                print("9. Eliminar Despliegue de Compañia")
                print("10. Salir")
                opcion = int(input("Elija una opción: "))

                if opcion == 1:
                    self.crearCompania()
                elif opcion == 2:
                    self.listarCompanias()
                elif opcion == 3:
                    self.buscarCompania()
                elif opcion == 4:
                    self.actualizarCompania()
                elif opcion == 5:
                    self.eliminarCompania()
                elif opcion == 6:
                    self.agregarSoldadoCompania()
                elif opcion == 7:
                    self.eliminarSoldadoCompania()
                elif opcion == 8:
                    self.agregarDespliegueCompania()
                elif opcion == 9:
                    self.eliminarDespliegueCompania()
                elif opcion == 10:
                    print("Saliendo del menú...")
                    break
                else:
                    print("Opción no válida, por favor elija una opción del 1 al 10.")
            except ValueError:
                print("Error: Ingrese un número válido.")

    def crearCompania(self):
        idCompania = input("Ingrese el ID de la Compañía: ")
        nombre = input("Ingrese el nombre de la Compañía: ")
        informacion = input("Ingrese la Actividad de la Compañía: ")

        compania = Compania(idCompania, nombre, informacion)
        self.controladorcompania.create(compania)
        print("Compañía creada exitosamente.")
        self.guardarCompania()

    def listarCompanias(self):
        companias = self.controladorcompania.index()
        if companias:
            for compania in companias:
                print(compania.toStr())
        else:
            print("No hay compañías registradas.")

    def buscarCompania(self):
        idCompania = input("Ingrese el ID de la Compañía: ")
        compania = self.controladorcompania.get(idCompania)
        if compania:
            print(compania.toStr())
        else:
            print("Compañía no encontrada.")

    def actualizarCompania(self):
        idCompania = input("Ingrese el ID de la Compañía: ")
        nombre = input("Ingrese el nuevo nombre de la Compañía: ")
        informacion = input("Ingrese la nueva Actividad de la Compañía: ")

        compania = Compania(idCompania, nombre, informacion)
        actualizado = self.controladorcompania.update(compania)
        if actualizado:
            print("Compañía actualizada exitosamente.")
            self.guardarCompania()
        else:
            print("Compañía no encontrada.")

    def eliminarCompania(self):
        idCompania = input("Ingrese el ID de la Compañía: ")
        eliminado = self.controladorcompania.delete(idCompania)
        if eliminado:
            print("Compañía eliminada exitosamente.")
            self.guardarCompania()
        else:
            print("Compañía no encontrada.")

    def agregarSoldadoCompania(self):
        idCompania = input("Ingrese el ID de la Compañía: ")
        idSoldado = input("Ingrese el ID del Soldado: ")

        compania = self.controladorcompania.get(idCompania)
        soldado = self.controladorSoldado.get(idSoldado)

        if compania is not None:
            compania.agregarSoldado(soldado)
            print("Soldado agregado exitosamente.")
            self.guardarCompania()
        else:
            print("Compañía no encontrada.")


    def eliminarSoldadoCompania(self):
        idCompania = input("Ingrese el ID de la Compañía: ")
        idSoldado = input("Ingrese el ID del Soldado: ")

        compania = self.controladorcompania.get(idCompania)
        if compania is not None:
            compania.eliminarSoldado(idSoldado)
            print("Soldado eliminado exitosamente.")
            self.guardarCompania()
        else:
            print("Compañía no encontrada.")

    def agregarDespliegueCompania(self):
        idCompania = input("Ingrese el ID de la Compañía: ")
        idDespliegue = input("Ingrese el ID del Despliegue: ")

        compania = self.controladorcompania.get(idCompania)
        despliegue = self.controladorDespliegue.get(idDespliegue)
        if compania is not None:
            compania.agregarDespliegue(despliegue)
            print("Despliegue agregado exitosamente.")
            self.guardarCompania()
        else:
            print("Compañía no encontrada.")

    def eliminarDespliegueCompania(self):
        idCompania = input("Ingrese el ID de la Compañía: ")
        idDespliegue = input("Ingrese el ID del Despliegue: ")

        compania = self.controladorcompania.get(idCompania)
        despliegue = self.controladorDespliegue.get(idDespliegue)
        if compania is not None:
            compania.eliminarDespliegue(despliegue)
            print("Despliegue eliminado exitosamente.")
            self.guardarCompania()
        else:
            print("Compañía no encontrada.")


    # Métodos para guardar y cargar automáticamente
    def guardarCompania(self):
        """Guarda automáticamente las compañías al salir de la aplicación."""
        self.controladorcompania.guardar(self.archivo)

    def cargarCompania(self):
        """Carga automáticamente las compañías al iniciar la aplicación."""
        self.controladorcompania.cargar(self.archivo)
