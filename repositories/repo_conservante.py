from conf.db_session import create_session
from models.conservante import Conservante


def insert() -> Conservante:
    print('Cadastrando de Conservantes')

    nome: str = input('Informe o nome do conservantes: ')
    descricao: str = input('Informe a descrição do conservante: ')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conservante)
        session.commit()

        return conservante


if __name__ == '__main__':
    con = insert()

    print('Conservante cadastrado com sucesso!')
    print(f'       ID: {con.id}')
    print(f'     Data: {con.data_criacao}')
    print(f'     Nome: {con.nome}')
    print(f'Descrição: {con.descricao}')
