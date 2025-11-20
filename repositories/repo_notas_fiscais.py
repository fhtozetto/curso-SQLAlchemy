from conf.db_session import create_session
from models.nota_fiscal import NotaFiscal

from decimal import Decimal


def insert() -> NotaFiscal:
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

        return nota_fiscal


if __name__ == '__main__':
    nf = insert()

    print('Nota Fiscal cadastrada com sucesso!')
    print(f'              ID: {nf.id}')
    print(f'            Data: {nf.data_criacao}')
    print(f'           Valor: {nf.valor}')
    print(f' Numero de Serie: {nf.numero_serie}')
    print(f'       Descrição: {nf.descricao}')
    print(f'ID do Revendedor: {nf.id_revendedor}')
