import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime

from models.model_base import ModelBase


class Revendedor(ModelBase):
    __tablename__: str = 'revendedores'

    id: orm.Mapped[int] = orm.mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, default=datetime.now, index=True)
    cnpj: orm.Mapped[str] = orm.mapped_column(sa.String(45), unique=True, nullable=False)
    razao_social: orm.Mapped[str] = orm.mapped_column(sa.String(100), unique=True, nullable=False)
    contato: orm.Mapped[str] = orm.mapped_column(sa.String(100), nullable=False)


def __repr__(self) -> str:
    return f'<Revendedor: {self.razao_social}>'
