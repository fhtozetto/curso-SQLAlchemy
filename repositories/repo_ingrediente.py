from conf.db_session import create_session
from models.ingrediente import Ingrediente


def insert() -> None:
    print('Cadastrando de Ingrediente')

    nome: str = input('Informe o nome do ingrediente: ')

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()

    print('Ingrediente cadastrado com sucesso!')
    print(f'     ID: {ingrediente.id}')
    print(f'   Data: {ingrediente.data_criacao}')
    print(f'   Nome: {ingrediente.nome}')


if __name__ == '__main__':
    insert()
