from conf.db_session import create_session
from models.conservante import Conservante


def insert() -> None:
    print('Cadastrando de Conservantes')

    nome: str = input('Informe o nome do conservantes: ')
    descricao: str = input('Informe a descrição do conservante: ')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conservante)
        session.commit()

    print('Conservante cadastrado com sucesso!')
    print(f'       ID: {conservante.id}')
    print(f'     Data: {conservante.data_criacao}')
    print(f'     Nome: {conservante.nome}')
    print(f'Descrição: {conservante.descricao}')


if __name__ == '__main__':
    insert()
