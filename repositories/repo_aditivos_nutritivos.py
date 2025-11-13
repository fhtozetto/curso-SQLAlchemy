from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo


def insert() -> None:
    print('Cadastrando aditivo nutritivo')

    nome: str = input('Informe o nome o aditivo nutritivo: ')
    formula_quimica: str = input('Informe a formula quimica do aditivo: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()

    print('Aditivo nutritivo cadastrado com sucesso!')
    print(f'     ID: {an.id}')
    print(f'   Data: {an.data_criacao}')
    print(f'   Nome: {an.nome}')
    print(f'Formula: {an.formula_quimica}')


if __name__ == '__main__':
    insert()
