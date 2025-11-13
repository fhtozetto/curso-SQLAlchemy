from conf.db_session import create_session
from models.tipos_picole import TipoPicole


def insert() -> None:
    print('Cadastrando de Tipo de Picoles')

    nome: str = input('Informe o tipo de picole: ')

    tipo_picole: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tipo_picole)
        session.commit()

    print('Tipo de picole cadastrado com sucesso!')
    print(f'     ID: {tipo_picole.id}')
    print(f'   Data: {tipo_picole.data_criacao}')
    print(f'   Nome: {tipo_picole.nome}')


if __name__ == '__main__':
    insert()
