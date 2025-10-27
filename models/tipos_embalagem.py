from __future__ import annotations

import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List, TYPE_CHECKING
from datetime import datetime

from models.model_base import ModelBase

if TYPE_CHECKING:
    from models.picole import Picole


class TipoEmbalagem(ModelBase):
    __tablename__: str = 'tipos_embalagem'

    id: orm.Mapped[int] = orm.mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, default=datetime.now, index=True)
    nome: orm.Mapped[str] = orm.mapped_column(sa.String(45), unique=True, nullable=False)

    picoles: orm.Mapped[List['Picole']] = orm.relationship(back_populates='tipos_embalagem')


def __repr__(self) -> str:
    return f'<Tipo Embalagem: {self.nome}>'
