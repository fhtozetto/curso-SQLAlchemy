from conf.db_session import create_session
from models.revendedor import Revendedor


def insert() -> None:
    print('Cadastrando de Revendedores')

    cnpj: str = input('Informe o CNPJ do revendedor: ')
    razao_social: str = input('Informe razão social do revendedor: ')
    contato: str = input('Informe o contato do revendedor: ')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()

    print('Revendedor cadastrado com sucesso!')
    print(f'          ID: {revendedor.id}')
    print(f'        Data: {revendedor.data_criacao}')
    print(f'        CNPJ: {revendedor.cnpj}')
    print(f'Razão Social: {revendedor.razao_social}')
    print(f'     Contato: {revendedor.contato}')


if __name__ == '__main__':
    insert()
