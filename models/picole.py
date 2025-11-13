from __future__ import annotations

import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List, Optional, TYPE_CHECKING
from decimal import Decimal
from datetime import datetime

from models.model_base import ModelBase

from models.conservantes_picole import conservantes_picole  # noqa: F401
from models.aditivos_nutritivos_picole import aditivos_nutritivos_picole  # noqa: F401
from models.ingredientes_picole import ingredientes_picole  # noqa: F401

if TYPE_CHECKING:
    from models.sabor import Sabor
    from models.tipos_embalagem import TipoEmbalagem
    from models.tipos_picole import TipoPicole
    from models.conservante import Conservante
    from models.aditivo_nutritivo import AditivoNutritivo
    from models.ingrediente import Ingrediente


class Picole(ModelBase):
    __tablename__: str = 'picoles'

    id: orm.Mapped[int] = orm.mapped_column(
        sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, default=datetime.now, index=True)

    preco: orm.Mapped[Decimal] = orm.mapped_column(
        sa.Numeric(8, 2), nullable=False)

    id_sabor: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey('sabores.id'), nullable=False)
    sabor: orm.Mapped['Sabor'] = orm.relationship(back_populates='picoles', lazy='joined')

    id_tipo_embalagem: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey('tipos_embalagem.id'), nullable=False)
    tipos_embalagem: orm.Mapped['TipoEmbalagem'] = orm.relationship(back_populates='picoles')

    id_tipo_picole: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey('tipos_picole.id'), nullable=False)
    tipo_picole: orm.Mapped['TipoPicole'] = orm.relationship(back_populates='picoles')

    # Um picole pode ter vários ingredientes
    ingredientes: orm.Mapped[List['Ingrediente']] = orm.relationship(
        secondary='ingredientes_picole', back_populates='picoles')

    # Um picole pode ter vários conservantes ou mesmo nenhum
    conservantes: orm.Mapped[Optional[List['Conservante']]] = orm.relationship(
        secondary='conservantes_picole', back_populates='picoles')

    # Um picole pode ter vários aditivos nutritivos ou nenhum
    aditivos_nutritivos: orm.Mapped[Optional[List['AditivoNutritivo']]] = orm.relationship(
        secondary='aditivos_nutritivos_picole', back_populates='picoles')


    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'
