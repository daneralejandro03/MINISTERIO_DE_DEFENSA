from datetime import datetime

from Modelo.Armada import Armada
from Modelo.Artilleria import Artilleria
from Modelo.Compania import Compania
from Modelo.Cuartel import Cuartel
from Modelo.Despliegue import Despliegue
from Modelo.Ministerio import Ministerio
from Modelo.Infanteria import Infanteria
from Modelo.Soldado import Soldado


def main():

    ministerio = Ministerio("1", "Ministerio de Defensa", "El ministerios de los chingasos")

    cuerpo1 = Infanteria("1", "Infanteria", "Cuerpo de infanteria", "Ingenieros", "Combate Terrestre")
    cuerpo2 = Artilleria("2", "Artilleria", "Cuerpo de artilleria", "Pesada", "Lo necesario")
    cuerpo3 = Armada("3", "Armada", "Cuerpo de armada", "De las que flotan", "El charcos")

    compañia1 = Compania("1", "Compañía de Infantería #1", "Combate Terrestre")
    compañia2 = Compania("2", "Compañía de Infantería #2", "Operaciones Especiales")
    compañia3 = Compania("3", "Compañía de Comunicaciones #1", "Comunicaciones y Señales")
    compañia4 = Compania("4", "Compañía de Inteligencia #1", "Operaciones de Inteligencia")
    compañia5 = Compania("5", "Compañía de Infantería #3", "Combate en Terreno Urbano")
    compañia6 = Compania("6", "Compañía de Ingenieros #2", "Desminado Humanitario")
    compañia7 = Compania("7", "Compañía de Comunicaciones #2", "Guerra Electrónica")
    compañia8 = Compania("8", "Compañía de Infantería #6", "Combate en Desierto")
    compañia9 = Compania("9", "Compañía de Transporte #1", "Logística y Abastecimiento")
    compañia10 = Compania("10", "Compañía de Inteligencia #2", "Ciberseguridad")

    cuartel1 = Cuartel("1", "Cuartel de Infantería #1", "Caldas")
    cuartel2 = Cuartel("2", "Cuartel de Infantería #2", "Antioquia")
    cuartel3 = Cuartel("3", "Cuartel de Artillería #3", "Valle del Cauca")
    cuartel4 = Cuartel("4", "Cuartel de Ingenieros #4", "Cundinamarca")
    cuartel5 = Cuartel("5", "Cuartel de Caballería #5", "Atlántico")
    cuartel6 = Cuartel("6", "Cuartel de Logística #6", "Santander")
    cuartel7 = Cuartel("7", "Cuartel de Comunicaciones #7", "Nariño")
    cuartel8 = Cuartel("8", "Cuartel de Sanidad #8", "Bolívar")
    cuartel9 = Cuartel("9", "Cuartel de Policía Militar #9", "Huila")
    cuartel10 = Cuartel("10", "Cuartel de Mantenimiento #10", "Sucre")
    cuartel11 = Cuartel("11", "Cuartel de Operaciones Especiales #11", "Magdalena")
    cuartel12 = Cuartel("12", "Cuartel de Protección Civil #12", "Tolima")
    cuartel13 = Cuartel("13", "Cuartel de Reposición #13", "Cesar")
    cuartel14 = Cuartel("14", "Cuartel de Control de Fronteras #14", "La Guajira")
    cuartel15 = Cuartel("15", "Cuartel de Estrategia #15", "Quindío")
    cuartel16 = Cuartel("16", "Cuartel de Inteligencia #16", "Risaralda")
    cuartel17 = Cuartel("17", "Cuartel de Evaluación y Control #17", "Chocó")
    cuartel18 = Cuartel("18", "Cuartel de Seguridad Nacional #18", "Caquetá")
    cuartel19 = Cuartel("19", "Cuartel de Asuntos Civiles #19", "Vaupés")
    cuartel20 = Cuartel("20", "Cuartel de Operaciones Aéreas #20", "Vichada")

    soldado1 = Soldado("1", "Salazar", "Manizales")
    soldado2 = Soldado("2", "Gómez", "Medellín")
    soldado3 = Soldado("3", "Martínez", "Cali")
    soldado4 = Soldado("4", "Rodríguez", "Bogotá")
    soldado5 = Soldado("5", "Pérez", "Barranquilla")
    soldado6 = Soldado("6", "Torres", "Bucaramanga")
    soldado7 = Soldado("7", "Hernández", "Cúcuta")
    soldado8 = Soldado("8", "Ramírez", "Cartagena")
    soldado9 = Soldado("9", "Mendoza", "Pereira")
    soldado10 = Soldado("10", "Sánchez", "Santa Marta")
    soldado11 = Soldado("11", "Vásquez", "Ibagué")
    soldado12 = Soldado("12", "Suárez", "Neiva")
    soldado13 = Soldado("13", "Ospina", "Tunja")
    soldado14 = Soldado("14", "Castro", "Villavicencio")
    soldado15 = Soldado("15", "Cano", "Quibdó")
    soldado16 = Soldado("16", "Patiño", "Popayán")
    soldado17 = Soldado("17", "García", "Yopal")
    soldado18 = Soldado("18", "Márquez", "San Andrés")
    soldado19 = Soldado("19", "Silva", "Leticia")
    soldado20 = Soldado("20", "Ríos", "El Banco")

    despliegue1 = Despliegue("1", "Despliegue de Infantería #1", datetime(2021, 5, 1))
    despliegue2 = Despliegue("2", "Despliegue de Artillería #1", datetime(2021, 6, 15))
    despliegue3 = Despliegue("3", "Despliegue de Caballería #1", datetime(2021, 7, 10))
    despliegue4 = Despliegue("4", "Despliegue de Ingenieros #1", datetime(2021, 8, 20))
    despliegue5 = Despliegue("5", "Despliegue de Comunicaciones #1", datetime(2021, 9, 5))

    #Cuerpos del Ministerio
    ministerio.agregarCuerpo(cuerpo1)
    ministerio.agregarCuerpo(cuerpo2)
    ministerio.agregarCuerpo(cuerpo3)

    #Cuarteles de los cuerpos
    cuerpo1.agregarCuartel(cuartel1)
    cuerpo1.agregarCuartel(cuartel2)
    cuerpo1.agregarCuartel(cuartel4)
    cuerpo1.agregarCuartel(cuartel11)
    cuerpo1.agregarCuartel(cuartel12)
    cuerpo1.agregarCuartel(cuartel16)
    cuerpo1.agregarCuartel(cuartel19)

    cuerpo2.agregarCuartel(cuartel3)
    cuerpo2.agregarCuartel(cuartel5)
    cuerpo2.agregarCuartel(cuartel9)
    cuerpo2.agregarCuartel(cuartel10)
    cuerpo2.agregarCuartel(cuartel13)
    cuerpo2.agregarCuartel(cuartel17)
    cuerpo2.agregarCuartel(cuartel20)

    cuerpo3.agregarCuartel(cuartel6)
    cuerpo3.agregarCuartel(cuartel7)
    cuerpo3.agregarCuartel(cuartel8)
    cuerpo3.agregarCuartel(cuartel14)
    cuerpo3.agregarCuartel(cuartel15)
    cuerpo3.agregarCuartel(cuartel18)

    #Soldados de los cuerpos
    cuerpo1.agregarSoldado(soldado1)
    cuerpo1.agregarSoldado(soldado2)
    cuerpo1.agregarSoldado(soldado3)
    cuerpo1.agregarSoldado(soldado4)
    cuerpo1.agregarSoldado(soldado5)
    cuerpo1.agregarSoldado(soldado6)
    cuerpo1.agregarSoldado(soldado7)

    cuerpo2.agregarSoldado(soldado8)
    cuerpo2.agregarSoldado(soldado9)
    cuerpo2.agregarSoldado(soldado10)
    cuerpo2.agregarSoldado(soldado11)
    cuerpo2.agregarSoldado(soldado12)
    cuerpo2.agregarSoldado(soldado13)
    cuerpo2.agregarSoldado(soldado14)

    cuerpo3.agregarSoldado(soldado15)
    cuerpo3.agregarSoldado(soldado16)
    cuerpo3.agregarSoldado(soldado17)
    cuerpo3.agregarSoldado(soldado18)
    cuerpo3.agregarSoldado(soldado19)
    cuerpo3.agregarSoldado(soldado20)

    #Soldados de las compañias
    compañia1.agregarSoldado(soldado1)
    compañia1.agregarSoldado(soldado2)
    compañia2.agregarSoldado(soldado3)
    compañia2.agregarSoldado(soldado4)
    compañia3.agregarSoldado(soldado5)
    compañia3.agregarSoldado(soldado6)
    compañia4.agregarSoldado(soldado7)
    compañia4.agregarSoldado(soldado8)
    compañia5.agregarSoldado(soldado9)
    compañia5.agregarSoldado(soldado10)
    compañia6.agregarSoldado(soldado11)
    compañia6.agregarSoldado(soldado12)
    compañia7.agregarSoldado(soldado13)
    compañia7.agregarSoldado(soldado14)
    compañia8.agregarSoldado(soldado15)
    compañia8.agregarSoldado(soldado16)
    compañia9.agregarSoldado(soldado17)
    compañia9.agregarSoldado(soldado18)
    compañia10.agregarSoldado(soldado19)
    compañia10.agregarSoldado(soldado20)

    #Despliegues del cuartel
    cuartel1.agregarDespliegue(despliegue1)
    cuartel2.agregarDespliegue(despliegue2)
    cuartel3.agregarDespliegue(despliegue3)
    cuartel4.agregarDespliegue(despliegue4)
    cuartel5.agregarDespliegue(despliegue5)

    #Despliegues de las compañias
    compañia1.agregarDespliegue(despliegue1)
    compañia2.agregarDespliegue(despliegue2)
    compañia3.agregarDespliegue(despliegue3)
    compañia4.agregarDespliegue(despliegue4)
    compañia5.agregarDespliegue(despliegue5)

    cuerpo1.saberlosdesplieguesdeloscuerpos()


if __name__ == "__main__":
    main()






