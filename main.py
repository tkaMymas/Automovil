class autoMovil:
    def __init__(self):
        self.marca = ""

    def menuAutos(self):
        while True:
            print()
            menu = input("¿Que opción desea hacer? (Acelerar, Desacelerar, Salir): ")
            if menu == "Acelerar":
                if marca == "Audi":
                    autoMovil.acelerarAudi()
                    break
                elif marca == "Honda":
                    autoMovil.acelerarHonda()
                    break
                elif marca == "Mercedes":
                    autoMovil.acelerarMercedes()
                    break
            # elif menu == "Desacelerar":
            #     if marca == "Audi":
            #         #autoMovil.acelerarAudi()
            #         break
            #     elif marca == "Honda":
            #         #autoMovil.acelerarHonda()
            #         break
            #     elif marca == "Mercedes":
            #         #autoMovil.acelerarMercedes()
            #         break
            elif menu == "Salir":
                print("Se va a detener la prueba de autos...")
                break
            else:
                print("Ingrese una opción valida.")

# Apartado de Acelerar

    def acelerarAudi(self):
        for i in range(0, 355, 15):
            print("Su", marca, "esta llendo a", i, "Km/h")
            if i == 350:
                print()
                print("Estas llendo a mucha velocidad, puede ser peligroso.")
                print()

    def acelerarHonda(self):
        for i in range(0, 295, 10):
            print("Su", marca, "esta llendo a", i, "Km/h")
            if i == 290:
                print()
                print("Estas llendo a mucha velocidad, puede ser peligroso.")
                print()

    def acelerarMercedes(self):
        for i in range(0, 325, 20):
            print("Su", marca, "esta llendo a", i, "Km/h")
            if i == 320:
                print()
                print("Estas llendo a mucha velocidad, puede ser peligroso.")
                print()

# Apartado de Desacelerar

    def desacelerarAudi(self):
        for i in range(355, 0, -25):
            print("Su auto", marca, "esta desacelerando a", i, "Km/h")

    def desacelerarHonda(self):
        for i in range(295, 0, -15):
            print("Su auto", marca, "esta desacelerando a", i, "Km/h")

    def desacelerarMercedes(self):
        for i in range(325, 0, -20):
            print("Su auto", marca, "esta desacelerando a", i, "Km/h")

autoMoviles = autoMovil()

while True:
    marca = input("Seleccione una marca de auto (Audi, Honda, Mercedes): ")
    if marca == "Audi":
        autoMoviles.marca
        autoMoviles.menuAutos()
        break
    elif marca == "Honda":
        autoMoviles.marca
        autoMoviles.menuAutos()
        break
    elif marca == "Mercedes":
        autoMoviles.marca
        autoMoviles.menuAutos()
        break
    else:
        print("Seleccione una marca de auto valida por favor.")
        print()