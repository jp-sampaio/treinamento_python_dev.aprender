import sqlite3

with sqlite3.connect('animes.db') as conexao:
    # Criar uma conexão com o banco de dados
    sql = conexao.cursor()
    # Rodar comando sql
    sql.execute('create table if not exists animes(nome text, genero text, temporadas interger);')
    # Exemplo de inserir dados
    sql.execute('insert into animes(nome, genero, temporadas) values("naruto", "shounen", 12)')
    # Exemplo de usar dados da minha aplicação em um comando SQL
    nome = input('Nome do anime: ')
    genero = input('Genêro do anime: ')
    temporadas = int(input('Total de temporadas: '))

    sql.execute('insert into animes values(?,?,?)', [nome, genero, temporadas])

    # Salvando alterações no banco de dados
    conexao.commit()

    # Exibir dados no console python (terminal)
    animes = sql.execute('select * from animes;')
    for anime in animes:
        print(anime)