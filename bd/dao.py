from model import model

SQL_DELETA = "delete from %s where id = %s"
SQL_EMPRESA_POR_ID = "SELECT id, nome, cnpj from empresa where id = %s"
SQL_PESSOA_POR_ID = "SELECT id, nome, cpf from pessoa where id = %s"
SQL_ATUALIZA_EMPRESA = "UPDATE empresa SET nome= %s, cnpj = %s where id= %s"
SQL_ATUALIZA_PESSOA = "UPDATE pessoa SET nome= %s, cpf = %s where id= %s"
SQL_BUSCA_EMPRESA = "SELECT id, nome, cnpj from empresa"
SQL_BUSCA_PESSOA = "SELECT id, nome, cpf from pessoa"
SQL_CRIA_EMPRESA = "INSERT into empresa (nome, cnpj) values (%s, %s)"
SQL_CRIA_PESSOA = "INSERT into pessoa (nome, cpf) values (%s, %s)"

class EmpresaDao:
    def __init__(self, db):
        self.db = db

    def salvar(self, empresa):
        cursor = self.db.connection.cursor()

        if empresa.id:
            cursor.execute(SQL_ATUALIZA_EMPRESA, (empresa.nome, empresa.cnpj))

        else:
            cursor.execute(SQL_CRIA_EMPRESA, (empresa.nome, empresa.cnpj))
            empresa.id = cursor.lastrowid

        self.db.connection.commit()

        return empresa

    def listar(self):
        cursor = self.db.connection.cursor()
        cursor.execute(SQL_BUSCA_EMPRESA)
        empresas = EmpresaDao.traduz_empresa(cursor.fetchall())
        return empresas

    def buscar_por_id(self, id):
        cursor = self.db.connection.cursor()
        cursor.execute(SQL_EMPRESA_POR_ID, (id, ))
        tupla = cursor.fetchone()
        return model.Empresa(tupla[1], tupla[2], id=tupla[0])


    def deletar(self, id):
        self.db.connection.cursor.execute(SQL_DELETA, ("empresa", id))
        self.db.connection.commit()


    def traduz_empresa(empresas):
        def cria_empresa_com_tupla(tupla):
            return model.Empresa(tupla[1], tupla[2], id=tupla[0])
        return list(map(cria_empresa_com_tupla, empresas))


class PessoaDao:
    def __init__(self, db):
        self.db = db

    def salvar(self, pessoa):
        cursor = self.db.connection.cursor()

        if pessoa.id:
            cursor.execute(SQL_ATUALIZA_PESSOA, (pessoa.nome, pessoa.cpf))

        else:
            cursor.execute(SQL_CRIA_PESSOA, (pessoa.nome, pessoa.cpf))
            pessoa.id = cursor.lastrowid

        self.db.connection.commit()

        return pessoa

    def listar(self):
        cursor = self.db.connection.cursor()
        cursor.execute(SQL_BUSCA_PESSOA)
        pessoas = PessoaDao.traduz_pessoa(cursor.fetchall())
        return pessoas

    def buscar_por_id(self, id):
        cursor = self.db.connection.cursor()
        cursor.execute(SQL_PESSOA_POR_ID, (id,))
        tupla = cursor.fetchone()
        return model.Pessoa(tupla[1], tupla[2], id=tupla[0] )

    def deletar(self, id):
        self.db.connection.cursor.execute(SQL_DELETA, ("pessoa", id))
        self.db.connection.commit()

    def traduz_pessoa(pessoas):
        def cria_empresa_com_tupla(tupla):
            return model.Pessoa(tupla[1], tupla[2], id=tupla[0])

        return list(map(cria_empresa_com_tupla, pessoas))
