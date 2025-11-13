from conf.db_session import create_session
from models.tipos_embalagem import TipoEmbalagem


def insert() -> None:
    print('Cadastrando de Tipo de Embalagens')

    nome: str = input('Informe o tipo de embalagem: ')

    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tipo_embalagem)
        session.commit()

    print('Tipo de embalagem cadastrado com sucesso!')
    print(f'     ID: {tipo_embalagem.id}')
    print(f'   Data: {tipo_embalagem.data_criacao}')
    print(f'   Nome: {tipo_embalagem.nome}')


if __name__ == '__main__':
    insert()
