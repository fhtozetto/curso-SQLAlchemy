from conf.db_session import create_session
from models.ingrediente import Ingrediente


def insert() -> Ingrediente:
    print('Cadastrando de Ingrediente')

    nome: str = input('Informe o nome do ingrediente: ')

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()

        return ingrediente


if __name__ == '__main__':
    ing = insert()

    print('Ingrediente cadastrado com sucesso!')
    print(f'     ID: {ing.id}')
    print(f'   Data: {ing.data_criacao}')
    print(f'   Nome: {ing.nome}')
