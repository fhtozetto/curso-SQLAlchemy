from __future__ import annotations

import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List, TYPE_CHECKING
from datetime import datetime

from models.model_base import ModelBase
from models.lote import Lote

if TYPE_CHECKING:
    from models.picole import Picole


class TipoPicole(ModelBase):
    __tablename__: str = 'tipos_picole'

    id: orm.Mapped[int] = orm.mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, default=datetime.now, index=True)
    nome: orm.Mapped[str] = orm.mapped_column(sa.String(45), unique=True, nullable=False)

    lotes: orm.Mapped[List['Lote']] = orm.relationship(back_populates='tipo_picole')
    picoles: orm.Mapped[List['Picole']] = orm.relationship(back_populates='tipo_picole')


def __repr__(self) -> str:
    return f'<Tipo Picole: {self.nome}>'
