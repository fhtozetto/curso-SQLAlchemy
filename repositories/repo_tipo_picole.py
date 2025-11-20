from conf.db_session import create_session
from models.tipos_picole import TipoPicole


def insert() -> TipoPicole:
    print('Cadastrando de Tipo de Picoles')

    nome: str = input('Informe o tipo de picole: ')

    tipo_picole: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tipo_picole)
        session.commit()

        return tipo_picole


if __name__ == '__main__':
    tp = insert()

    print('Tipo de picole cadastrado com sucesso!')
    print(f'     ID: {tp.id}')
    print(f'   Data: {tp.data_criacao}')
    print(f'   Nome: {tp.nome}')
