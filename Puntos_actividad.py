import math

# Punto: 1
class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje


# Punto: 2
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def calcular_distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)


# Punto: 3
class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def calcular_perimetro(self):
        base = abs(self.esquina2.x - self.esquina1.x)
        altura = abs(self.esquina2.y - self.esquina1.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina2.x - self.esquina1.x)
        altura = abs(self.esquina2.y - self.esquina1.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina2.x - self.esquina1.x)
        altura = abs(self.esquina2.y - self.esquina1.y)
        return base == altura


# Punto: 4
class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_centro_punto = self.centro.calcular_distancia(punto)
        return distancia_centro_punto <= self.radio


# Punto: 5
class Carta:
    PINTAS = ['Pica', 'Corazón', 'Diamante', 'Trébol']

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta


# Punto: 6
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
        else:
            print("Saldo insuficiente.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota

    def mostrar_detalles(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance actual: ${self.balance:.2f}")


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear un vehículo
    vehiculo = Vehiculo(200, 5000)

    # Crear dos puntos
    punto1 = Punto(0, 0)
    punto2 = Punto(3, 4)

    # Crear un rectángulo con los puntos anteriores
    rectangulo = Rectangulo(punto1, punto2)

    # Crear un círculo
    centro_circulo = Punto(1, 1)
    circulo = Circulo(centro_circulo, 5)

    # Crear una carta
    carta = Carta('As', Carta.PINTAS[0])

    # Crear una cuenta bancaria
    cuenta_bancaria = CuentaBancaria("123456", ["Juan", "María"], 1000)

    # Ejemplos de uso: métodos
    punto1.mostrar()
    punto2.mover(1, 2)
    distancia = punto1.calcular_distancia(punto2)
    print(f"Distancia entre los puntos: {distancia}")
    print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")
    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
    print(f"¿El rectángulo es un cuadrado? {rectangulo.es_cuadrado()}")
    print(f"Área del círculo: {circulo.calcular_area()}")
    print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")
    print(f"¿El punto pertenece al círculo? {circulo.punto_pertenece(Punto(6, 2))}")
    print(f"Valor de la carta: {carta.valor}, Pinta de la carta: {carta.pinta}")
    cuenta_bancaria.depositar(500)
    cuenta_bancaria.retirar(200)
    cuenta_bancaria.aplicar_cuota_manejo()
    cuenta_bancaria.mostrar_detalles()
