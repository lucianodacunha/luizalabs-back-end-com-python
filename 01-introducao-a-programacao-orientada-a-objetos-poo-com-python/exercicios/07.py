class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return (self.largura * 2) + (self.altura * 2)

    
def main():
    ret = Retangulo(largura=2, altura=3)
    print(f"Area: {ret.area()}")
    print(f"Perimetro: {ret.perimetro()}")


if __name__ == "__main__":
    main()
