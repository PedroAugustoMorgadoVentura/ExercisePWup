class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade}")


class ProdutoImportado(Produto):
    def __init__(self, nome, preco, quantidade, imposto):
        super().__init__(nome, preco, quantidade)
        self.imposto = imposto

    def preco_final(self):
        preco_total = self.preco + (self.preco * self.imposto / 100)
        return preco_total


produto_importado = ProdutoImportado("Computador", 2500, 10, 15)
produto_importado.mostrar_dados()
print(f"Preço final com imposto: R${produto_importado.preco_final():.2f}")
