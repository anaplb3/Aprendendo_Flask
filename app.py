from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL
from bd import dao
from model import model

app = Flask(__name__)

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "anaehtop"
app.config["MYSQL_DB"] = "dados"

db = MySQL(app)

daoEmpresa = dao.EmpresaDao(db)
daoPessoa = dao.PessoaDao(db)

@app.route('/')
def hello_world():
    return render_template("inicio.html")


# Mostra as empresas cadastradas
@app.route("/empresas")
def listarEmpresas():
    lista_empresas = daoEmpresa.listar()
    return render_template("empresas.html", empresas=lista_empresas)


# Mostra as pessoas cadastradas
@app.route("/pessoas")
def listarPessoas():
    lista_pessoas = daoPessoa.listar()
    return render_template("pessoas.html", pessoas=lista_pessoas)


# Redireciona para a página de cadastro de pessoas
@app.route("/cadastroEmpresas")
def cadastro_empresa():

    return render_template("cadastro_empresa.html")


# Redireciona para a página de cadastro de pessoas
@app.route("/cadastroPessoas")
def cadastro_pessoa():

    return render_template("cadastro_pessoa.html")


# Pega as informações de cadastro, coloca no banco e redireciona para a página de empresas
@app.route("/criar_empresa", methods=["POST"])
def cadastro_empresas():
    nome = request.form["nome"]
    cnpj = request.form["cnpj"]

    daoEmpresa.salvar(model.Empresa(nome, cnpj))
    return redirect("/empresas")


# Cadastra no banco e redireciona para a pagina de pessoas
@app.route("/criar_pessoa", methods=["POST"])
def cadastro_pessoas():
    nome = request.form["nome"]
    cpf = request.form["cpf"]

    daoPessoa.salvar(model.Pessoa(nome, cpf))
    return redirect("/pessoas")


if __name__ == '__main__':
    app.run()
