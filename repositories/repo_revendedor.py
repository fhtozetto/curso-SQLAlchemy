from conf.db_session import create_session
from models.revendedor import Revendedor


def insert() -> Revendedor:
    print('Cadastrando de Revendedores')

    cnpj: str = input('Informe o CNPJ do revendedor: ')
    razao_social: str = input('Informe razão social do revendedor: ')
    contato: str = input('Informe o contato do revendedor: ')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()

        return revendedor


if __name__ == '__main__':
    rev = insert()

    print('Revendedor cadastrado com sucesso!')
    print(f'          ID: {rev.id}')
    print(f'        Data: {rev.data_criacao}')
    print(f'        CNPJ: {rev.cnpj}')
    print(f'Razão Social: {rev.razao_social}')
    print(f'     Contato: {rev.contato}')
