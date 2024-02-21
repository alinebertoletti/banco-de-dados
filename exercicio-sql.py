import sqlite3

conexao = sqlite3.connect('banco de dados')
cursor  = conexao.cursor()

#1: criar a tabela alunos e incluir id, nome, idade e curso
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2: inserir pelo menos 5 registros
#cursor.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Isadora", "18", "Biologia")')
#cursor.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Marcos", "19", "Pedagogia")')
#cursor.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Diego", "17", "Fisioterapia")')
#cursor.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Maria", "20", "Medicina")')
#cursor.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Ísis", "18", "Engenharia de Software")')

#3.a: selecionar todos os registros da tabela
#dados = cursor.execute('SELECT * FROM alunos')
#for usuario in dados:
 #   print (usuario)

#3.b: seelcionar nome e idade para os alunos com mais de 20 anos
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
#for usuario in dados:
 #   print (usuario)

#3.c: selecionar os alunos do curso de engenharia em ordem alfabetica
#dados = cursor.execute('SELECT curso FROM alunos WHERE curso = "Engenharia" ORDER BY nome ')
#for usuario in dados:
 #   print (usuario)

#3.d:contar numero total de alunos
#dados = cursor.execute('SELECT COUNT (*) FROM alunos')
#for usuario in dados:
 #   print (usuario)


# 4.a: atualizar a idade de um aluno específico na tabela
#cursor.execute('UPDATE alunos SET idade = 22 WHERE nome= "Maria"')

#4.b: remova um aluno pelo seu id:
#cursor.execute ('DELETE FROM alunos where id = 2')

#5: criar uma tabela chamada "clientes" com os campos: id, nome, idade e saldo. Inserir alguns dados
#cursor.execute('CREATE TABLE clientes(id INT primary key, nome VARCHAR(150), idade INT, saldo FLOAT);')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(11, "Vitória", "30", 12495)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(12, "Jéssica", "24", 10101)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(13, "Camila", "27", 1200)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(14, "Letícia", "36", 17654)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(15, "Giovanna", "32", 495)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(16, "Gabriela", "18", 1295)')

#cursor.execute('UPDATE clientes SET saldo = "12495" WHERE nome= "Vitória"')
#cursor.execute('UPDATE clientes SET saldo = "10101" WHERE nome= "Jéssica"')


#6.a: selecione o nome e a idade dos clientes com iadade superior a 30 anos
#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
#for usuario in dados:
 #   print (usuario)

#6.b: calcule o saldo médio dos clientes
#dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
#for usuario in dados:
 #   print (usuario)

#6.c: encontre o cliente com o saldo máximo
#dados = cursor.execute(' SELECT nome FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
#for usuario in dados:
#    print (usuario)

#6.d:  conte quantos clientes tem saldo acima de 1000:
#dados = cursor.execute ('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
#for usuario in dados:
 #   print (usuario)

# 7.a: atalize o saldo de um cliente específico:
#cursor.execute('UPDATE clientes SET saldo = "200" WHERE nome = "Camila"')

# 7.b: remova um cliente pelo seu ID:
#cursor.execute ('DELETE FROM clientes where id = 14')

#8: Juntando tabelas:
#cursor.execute('CREATE TABLE compras (id INT primary key, cliente_id INT, produto VARCHAR(250), valor FLOAT, CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes(id));')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) values (1, 11, "caderno", 14.50)')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) values (4, 16, "borracha", 2.75)')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) values (3, 13, "caneta", 2.0)')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) values (2, 12, "lapiseira", 4.20)')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) values (5, 11, "borracha", 2.75)')

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
#cledados = cursor.execute('SELECT c.nome, co.produto, co.valor from compras as co INNER JOIN clientes as c on c.id = co.cliente_id')
#for usuario in dados:
 #   print(usuario)

conexao.commit()
conexao.close