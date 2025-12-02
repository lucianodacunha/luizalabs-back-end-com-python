class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return (f"Produto: {self.nome} | Preço: {self.preco} | "
                f"Quantidade: {self.quantidade}")


def main():
    produto = Produto("Computador", 5000.0, 10)
    print(produto)


if __name__ == "__main__":
    main()
