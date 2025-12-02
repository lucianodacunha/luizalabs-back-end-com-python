class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas if paginas >0 else 1

    def __str__(self):
        return (f"Titulo: {self.titulo}, Autor: {self.autor}, "
                f"Paginas: {self.paginas}")


def main():
    livro = Livro("Dominando Python", "Luciano da Cunha", 300)
    print(livro)


if __name__ == "__main__":
    main()
    