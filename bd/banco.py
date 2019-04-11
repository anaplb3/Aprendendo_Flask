import MySQLdb

print("Conectando...")

conn = MySQLdb.connect(user="root", passwd="anaehtop")

conn.cursor().execute("DROP DATABASE `dados`;")

print("Conectado")

criar_tabela = '''SET NAMES utf8;
                CREATE DATABASE `dados`; 
                USE `dados`;
                CREATE TABLE `empresa` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `nome` varchar(100) COLLATE utf8_bin NOT NULL,
                `cnpj` varchar(100) NOT NULL,
                PRIMARY KEY (`id`)
                ) ENGINE =InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
                CREATE TABLE `pessoa` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `nome` varchar(100) COLLATE utf8_bin NOT NULL,
                `cpf` varchar(100) NOT NULL,
                PRIMARY KEY (`id`)
                ) ENGINE =InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
                '''

conn.cursor().execute(criar_tabela)

cursor = conn.cursor()

# Upando empresas
cursor.executemany(
    "INSERT INTO empresa (nome, cnpj) VALUES (%s, %s)",
    [
        ("Guaraves", "12.727.145/0001-78"),
        ("Cacau Show", "61.472.205/0001-64"),
        ("Lojas Americanas", "33.014.556/0001-96"),
    ],
)

# Upando pessoas
cursor.executemany(
    "INSERT INTO pessoa (nome, cpf) VALUES (%s, %s)",
    [
        ("Ana Paula", "228.713.320-88"),
        ("Ronaldo Neves", "690.871.530-23"),
        ("Pedro Henrique Sousa", "756.122.550-47"),
    ],
)
# Printando empresas
cursor.execute("select * from empresa")
print("------------- Empresas ----------")
for empresa in cursor.fetchall():
    print(empresa[1])

# Printando pessoas
cursor.execute("select * from pessoa")
print("------------- Pessoas ----------")
for pessoa in cursor.fetchall():
    print(pessoa[1])

conn.commit()
cursor.close()