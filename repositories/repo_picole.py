from conf.db_session import create_session
from models.picole import Picole

from decimal import Decimal


def insert() -> Picole:
    print('Cadastrando de Lote de Picoles')

    preco: Decimal = Decimal(input('Informe o preço do picole: '))
    id_sabor: int = int(input('Informe o ID do sabor: '))
    id_tipo_embalagem: int = int(input('Informe o ID do tipo de embalagem: '))
    id_tipo_picole: int = int(input('Informe o ID do tipo de picole: '))


    picole: Picole = Picole(
        preco=preco, 
        id_sabor=id_sabor, 
        id_tipo_embalagem=id_tipo_embalagem, 
        id_tipo_picole=id_tipo_picole
    )

    with create_session() as session:
        session.add(picole)
        session.commit()

        return picole


if __name__ == '__main__':
    pi = insert()

    print('Tipo de picole cadastrado com sucesso!')
    print(f'               ID: {pi.id}')
    print(f'             Data: {pi.data_criacao}')
    print(f'            Preço: {pi.preco}')
    print(f'         ID Sabor: {pi.id_sabor}')
    print(f'ID Tipo Embalagem: {pi.id_tipo_embalagem}')
    print(f'   ID Tipo Picole: {pi.id_tipo_picole}')
