# Programação Orientada a Objetos
# AC03 ADS-EaD - Implementação de classes, herança, polimorfismo e lançamento de exceções.
# Email Impacta: victor.jurado@aluno.faculdadeimpacta.com.br


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @nome.setter
    def nome(self, novo_nome):

        if len(novo_nome) > 0:
            self.__nome = novo_nome

        if len(novo_nome) == 0:
            raise ValueError

    @preco.setter
    def preco(self, novo_preco):
        if not isinstance(novo_preco, (int, float)):
            raise TypeError
        elif novo_preco <= 0:
            raise ValueError
        elif isinstance(novo_preco, (int, float)):
            self.__preco = novo_preco


    def calcular_preco_com_frete(self):
        return self.__preco


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.peso = peso

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, novo_peso):
        if isinstance(novo_peso, int):
            if novo_peso > 0:
                self.__peso = novo_peso
            elif novo_peso <= 0:
                raise ValueError
        elif not isinstance(novo_peso, int):
            raise TypeError

    def peso_em_kg(self):
        return self.__peso / 1000

    def calcular_preco_com_frete(self):
        return self.peso_em_kg() * 5 + self.preco


class ProdutoEletronico(ProdutoFisico):
    def __init__(self, nome, preco, peso, tensao, tempo_garantia):
        super().__init__(nome, preco, peso)
        self.tensao = tensao
        self.__tempo_garantia = tempo_garantia

    @property
    def tensao(self):
        return self.__tensao

    @property
    def tempo_garantia(self):
        return self.__tempo_garantia

    @tensao.setter
    def tensao(self, nova_tensao):
        if isinstance(nova_tensao, int):
            if nova_tensao == 0 or nova_tensao == 127 or nova_tensao == 220:
                self.__tensao = nova_tensao
            else:
                raise ValueError
        else:
            raise TypeError

    def calcular_preco_com_frete(self):
        return super().calcular_preco_com_frete() * 1.01


class Ebook(Produto):
    def __init__(self, nome, preco, autor, numero_paginas):
        self.__autor = autor
        self.numero_paginas = numero_paginas
        super().__init__(nome, preco)

    @property
    def nome_exibicao(self):
        return (f'{self.nome} ({self.autor})')

    @property
    def autor(self):
        return self.__autor

    @property
    def numero_paginas(self):
        return self.__numero_paginas

    @numero_paginas.setter
    def numero_paginas(self, valor):
        if valor > 0:
            self.__numero_paginas = valor
        elif valor <= 0:
            raise ValueError