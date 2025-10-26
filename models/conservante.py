import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List
from datetime import datetime

from models.model_base import ModelBase
from models.picole import Picole


class Conservante(ModelBase):
    __tablename__: str = 'conservantes'

    id: orm.Mapped[int] = orm.mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, default=datetime.now, index=True)
    nome: orm.Mapped[str] = orm.mapped_column(sa.String(45), unique=True, nullable=False)
    descricao: orm.Mapped[str] = orm.mapped_column(sa.String(45), nullable=False)

    picoles: orm.Mapped[List['Picole']] = orm.relationship(
        secondary='conservantes_picole', back_populates='conservantes', lazy='dynamic')


def __repr__(self) -> str:
    return f'<Conservante: {self.nome}>'
