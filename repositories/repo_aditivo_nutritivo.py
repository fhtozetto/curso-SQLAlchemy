from conf.db_session import create_session
from sqlalchemy import select  # , func

from typing import Sequence

from models.aditivo_nutritivo import AditivoNutritivo
# from conf.helpers import formata_data


def insert() -> AditivoNutritivo:
    print('Cadastrando aditivo nutritivo')

    nome: str = input('Informe o nome o aditivo nutritivo: ')
    formula_quimica: str = input('Informe a formula quimica do aditivo: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()

        return an


# select * from aditivos_nutritivos
def get_todos_aditivos_nutritivos() -> Sequence[AditivoNutritivo]:
    with create_session() as session:
        stmt = select(AditivoNutritivo)
        result = session.execute(stmt)
        return result.scalars().all()


# select * from aditivos_nutritivos where id = 1
def get_sabor_por_id(id_sabor: int) -> AditivoNutritivo | None:
    with create_session() as session:
        stmt = select(AditivoNutritivo).where(AditivoNutritivo.id == id_sabor)
        result = session.execute(stmt)
        return result.scalars().first()


if __name__ == '__main__':
    # # Inserindo dados
    # an = insert()

    # print('Aditivo nutritivo cadastrado com sucesso!')
    # print(f'     ID: {an.id}')
    # print(f'   Data: {an.data_criacao}')
    # print(f'   Nome: {an.nome}')
    # print(f'Formula: {an.formula_quimica}')

    # # Seleciona todos
    # an = get_todos_aditivos_nutritivos()
    # for i in an:
    #     print(f'ID: {i.id}, nome: {i.nome}, formula: {i.formula_quimica}')

    # Seleciona por id
    an = get_sabor_por_id(id_sabor=10)
    if an is not None:
        print(f'ID: {an.id}, nome: {an.nome}, formula: {an.formula_quimica}')
    else:
        print('Registro não encontrado')
