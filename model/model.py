class Empresa:
    def __init__(self, nome, cnpj, id=None):
        self.nome = nome
        self.cnpj = cnpj
        self.id = id


class Pessoa:
    def __init__(self, nome, cpf, id=None):
        self.nome = nome
        self.cpf = cpf
        self.id = id
