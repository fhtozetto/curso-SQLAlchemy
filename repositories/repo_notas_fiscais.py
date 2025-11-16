from conf.db_session import create_session
from models.nota_fiscal import NotaFiscal

from decimal import Decimal


def insert() -> None:
    print('Cadastrando de Lote de Picoles')

    valor: Decimal = Decimal(input('Informe o valor da NF: '))
    numero_serie: str = input('Informe o nº de serie: ')
    descricao: str = input('Informe a descrição: ')
    id_revendedor: int = int(input('Informe o ID do fornecedor: '))


    nota_fiscal: NotaFiscal = NotaFiscal(
        valor=valor,
        numero_serie=numero_serie, 
        descricao=descricao, 
        id_revendedor=id_revendedor
    )

    with create_session() as session:
        session.add(nota_fiscal)
        session.commit()

    print('Nota Fiscal cadastrada com sucesso!')
    print(f'              ID: {nota_fiscal.id}')
    print(f'            Data: {nota_fiscal.data_criacao}')
    print(f'           Valor: {nota_fiscal.valor}')
    print(f' Numero de Serie: {nota_fiscal.numero_serie}')
    print(f'       Descrição: {nota_fiscal.descricao}')
    print(f'ID do Revendedor: {nota_fiscal.id_revendedor}')


if __name__ == '__main__':
    insert()
