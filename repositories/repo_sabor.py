from conf.db_session import create_session
from models.sabor import Sabor


def insert() -> Sabor:
    print('Cadastrando de Sabores')

    nome: str = input('Informe o nome do sabor: ')

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)
        session.commit()

        return sabor


if __name__ == '__main__':
    sab = insert()

    print('Sabor cadastrado com sucesso!')
    print(f'     ID: {sab.id}')
    print(f'   Data: {sab.data_criacao}')
    print(f'   Nome: {sab.nome}')
