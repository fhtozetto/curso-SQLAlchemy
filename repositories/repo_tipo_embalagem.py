from conf.db_session import create_session
from models.tipos_embalagem import TipoEmbalagem


def insert() -> TipoEmbalagem:
    print('Cadastrando de Tipo de Embalagens')

    nome: str = input('Informe o tipo de embalagem: ')

    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tipo_embalagem)
        session.commit()

        return tipo_embalagem


if __name__ == '__main__':
    te = insert()

    print('Tipo de embalagem cadastrado com sucesso!')
    print(f'     ID: {te.id}')
    print(f'   Data: {te.data_criacao}')
    print(f'   Nome: {te.nome}')
