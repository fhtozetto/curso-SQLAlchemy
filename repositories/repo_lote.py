from conf.db_session import create_session
from models.lote import Lote


def insert() -> Lote:
    print('Cadastrando de Lote de Picoles')

    id_tipo_picole: int = int(input('Informe o ID do tipo de picole: '))
    quantidade: int = int(input('Informe a quantidade de picoles: '))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:
        session.add(lote)
        session.commit()

        return lote


if __name__ == '__main__':
    lo = insert()

    print('Tipo de picole cadastrado com sucesso!')
    print(f'            ID: {lo.id}')
    print(f'          Data: {lo.data_criacao}')
    print(f'ID Tipo Picole: {lo.id_tipo_picole}')
    print(f'    Quantidade: {lo.quantidade}')
