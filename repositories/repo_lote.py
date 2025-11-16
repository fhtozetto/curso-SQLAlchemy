from conf.db_session import create_session
from models.lote import Lote


def insert() -> None:
    print('Cadastrando de Lote de Picoles')

    id_tipo_picole: int = int(input('Informe o ID do tipo de picole: '))
    quantidade: int = int(input('Informe a quantidade de picoles: '))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:
        session.add(lote)
        session.commit()

    print('Tipo de picole cadastrado com sucesso!')
    print(f'            ID: {lote.id}')
    print(f'          Data: {lote.data_criacao}')
    print(f'ID Tipo Picole: {lote.id_tipo_picole}')
    print(f'    Quantidade: {lote.quantidade}')


if __name__ == '__main__':
    insert()
