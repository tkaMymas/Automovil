class autoMovil:
    def __init__(self, marca):
        self.marca = marca

# Apartado de Acelerar

    def acelerarAudi(self, marca):
        if marca == "Audi":
            for i in range(0, 355, 15):
                print("Su", marca, "esta llendo a", i, "Km/h")
                if i == 350:
                    print()
                    print("Estas llendo a mucha velocidad, puede ser peligroso.")
                    print()

    def acelerarHonda(self, marca):
        if marca == "Honda":
            for i in range(0, 295, 10):
                print("Su", marca, "esta llendo a", i, "Km/h")
                if i == 290:
                    print()
                    print("Estas llendo a mucha velocidad, puede ser peligroso.")
                    print()

    def acelerarMercedes(self, marca):
        if marca == "Mercedes":
            for i in range(0, 325, 20):
                print("Su", marca, "esta llendo a", i, "Km/h")
                if i == 320:
                    print()
                    print("Estas llendo a mucha velocidad, puede ser peligroso.")
                    print()

# Apartado de Desacelerar

    def desacelerarAudi(self, marca):
        for i in range(355, 0, -25):
            print("Su auto", marca, "esta llendo a", i, "Km/h")

    def desacelerarHonda(self, marca):
        for i in range(295, 0, -15):
            print("Su auto", marca, "esta llendo a", i, "Km/h")

    def desacelerarMercedes(self, marca):
        for i in range(325, 0, -20):
            print("Su auto", marca, "esta llendo a", i, "Km/h")

while True:
    marca = str(input("Elija un auto para conducir (Audi, Honda, Mercedes): "))
    if not marca == "":
        break
    else:
        print("Ingrese un auto valido.")
        print()

autoMoviles = autoMovil(marca)

while True:
    print()
    menu = input("¿Que opción desea hacer? (Acelerar, Desacelerar, Salir): ")
    if menu == "Acelerar":
        if marca == "Audi":
            autoMoviles.acelerarAudi(marca)
        if marca == "Honda":
            autoMoviles.acelerarHonda(marca)
        if marca == "Mercedes":
            autoMoviles.acelerarMercedes(marca)
    elif menu == "Desacelerar":
        if marca == "Audi":
            autoMoviles.desacelerarAudi(marca)
        if marca == "Honda":
            autoMoviles.desacelerarHonda(marca)
        if marca == "Mercedes":
            autoMoviles.desacelerarMercedes(marca)
    elif menu == "Salir":
        print("Se va a detener la prueba de autos...")
        break
    else:
        print("Ingrese una opción valida.")