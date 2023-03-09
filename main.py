import time

class autoMovil:
    def __init__(self):
        self.marca = ""
        self.velocidad = 0

    def conducirAuto(self):
        print("Vamos a acelerar el auto.")
        time.sleep(2)
        auto.acelerarAuto()

    def acelerarAuto(self):
        for i in range(0, 185, 5):
            print("Su auto", marca, "esta acelerando a", i, "Km/h")
            if i == 125:
                print()
                print("Estas pasando el limite de velocidad en la carretera, puede ser peligroso.")
                print()
                while True:
                    quererDesacelerar = input(
                        "Ingrese SI, para desacelerar el auto, si no el auto seguira acelerando: ")
                    if quererDesacelerar.upper() == "SI":
                        print("Desacelerando...")
                        time.sleep(1)
                        auto.desacelerarAuto()
                        break
                    else:
                        print("Por favor se prudente.")

    def desacelerarAuto(self):
        for i in range(185, 0, -5):
            print("Su auto", marca, "esta acelerando a", i, "Km/h")
            if i == 10:
                print("El auto esta llendo muy lento.")
                print()
                quererAcelerar = input("Ingrese SI, para acelerar el auto: ")
                if quererAcelerar.upper() == "SI":
                    print("Acelerando...")
                    time.sleep(1)
                    auto.acelerarAuto()

auto = autoMovil()

while True:
    marca = input("Ingrese una marca de auto: ")
    if marca == "":
        print("Ingrese una marca valida por favor.")
        print()
    else:
        auto.marca
        auto.conducirAuto()
        print()
        break