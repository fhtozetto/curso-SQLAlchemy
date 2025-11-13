from conf.db_session import create_session
from models.sabor import Sabor


def insert() -> None:
    print('Cadastrando de Sabores')

    nome: str = input('Informe o nome do sabor: ')

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)
        session.commit()

    print('Sabor cadastrado com sucesso!')
    print(f'     ID: {sabor.id}')
    print(f'   Data: {sabor.data_criacao}')
    print(f'   Nome: {sabor.nome}')


if __name__ == '__main__':
    insert()
