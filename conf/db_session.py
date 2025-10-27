import os
from distutils.util import strtobool  # type: ignore
import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from models.model_base import ModelBase

from pathlib import Path  # Usado no SQLite
from typing import Optional
from dotenv import load_dotenv


# Carrega as variáveis do .env
load_dotenv()

# Pega as variáveis do ambiente
__DB_USER = os.getenv("DB_USER")
__DB_PASSWORD = os.getenv("DB_PASSWORD")
__DB_HOST = os.getenv("DB_HOST")
__DB_PORT = os.getenv("DB_PORT")
__DB_NAME = os.getenv("DB_NAME")

# Comportamento do sistema
__SQLITE = bool(strtobool(os.getenv('SQLITE', 'false')))
__DROP_TABLES = bool(strtobool(os.getenv('DROP_TABLES', 'false')))
__CREATE_TABLES = bool(strtobool(os.getenv('CREATE_TABLES', 'false')))

__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    '''
    Função para configurar uma conexão com o banco de dados escolhido
    '''
    global __engine

    if __engine:
        return __engine

    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={
                                    'check_same_thread': False})
    else:
        conn_str = f'postgresql+psycopg2://{__DB_USER}:{__DB_PASSWORD}@{__DB_HOST}:{__DB_PORT}/{__DB_NAME}'
        __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    '''
    Função responsável por criar uma seção de conexão com o Banco de Dados
    '''
    global __engine

    if not __engine:
        create_engine(sqlite=__SQLITE)  # Para rodar com SQLite / create_engine(sqlite=True)

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()

    return session


def create_tables() -> None:
    '''
    Função responsável por criar as tabelas no Banco de Dados
    '''
    global __engine

    if not __engine:
        create_engine(sqlite=__SQLITE)  # Para rodar com SQLite / create_engine(sqlite=True)

    # import models.__all_models  # noqa: F401
    if __DROP_TABLES:
        ModelBase.metadata.drop_all(__engine)
    if __CREATE_TABLES:
        ModelBase.metadata.create_all(__engine)
