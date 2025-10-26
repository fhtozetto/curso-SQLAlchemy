import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List, Optional
from decimal import Decimal
from datetime import datetime

from models.model_base import ModelBase
from models.sabor import Sabor
from models.tipos_embalagem import TipoEmbalagem
from models.tipos_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo


# Picole pode ter vários ingredientes
igredientes_picole = sa.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey(
        'picoles.id'), primary_key=True),
    sa.Column('id_ingrediente', sa.Integer, sa.ForeignKey(
        'ingredientes.id'), primary_key=True)
)

# Picole pode ter vários conservante
conservantes_picole = sa.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey(
        'picoles.id'), primary_key=True),
    sa.Column('id_conservante', sa.Integer, sa.ForeignKey(
        'conservantes.id'), primary_key=True)
)

# Picole pode ter vários aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey(
        'picoles.id'), primary_key=True),
    sa.Column('id_aditivo_nutritivo', sa.Integer, sa.ForeignKey(
        'aditivos_nutritivos.id'), primary_key=True)
)


class Picole(ModelBase):
    __tablename__: str = 'picoles'

    id: orm.Mapped[int] = orm.mapped_column(
        sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, default=datetime.now, index=True)

    preco: orm.Mapped[Decimal] = orm.mapped_column(
        sa.Numeric(8, 2), nullable=False)

    id_sabor: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey('sabores.id'), nullable=False)
    sabor: orm.Mapped['Sabor'] = orm.relationship(
        back_populates='picoles', lazy='joined')

    id_tipo_embalagem: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey('tipos_embalagem.id'), nullable=False)
    tipo_embalagem: orm.Mapped['TipoEmbalagem'] = orm.relationship(
        back_populates='picoles', lazy='joined')

    id_tipo_picole: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey('tipos_picole.id'), nullable=False)
    tipo_picole: orm.Mapped['TipoPicole'] = orm.relationship(
        back_populates='picoles', lazy='joined')

    # Um picole pode ter vários ingredientes
    ingredientes: orm.Mapped[List['Ingrediente']] = orm.relationship(
        secondary='ingredientes_picole', back_populates='ingredientes', lazy='dynamic')

    # Um picole pode ter vários conservantes ou mesmo nenhum
    conservantes: Optional[orm.Mapped[List['Conservante']]] = orm.relationship(
        secondary='conservantes_picole', back_populates='conservantes', lazy='dynamic')

    # Um picole pode ter vários aditivos nutritivos ou nenhum
    aditivos_nutritivos: Optional[orm.Mapped[List['AditivoNutritivo']]] = orm.relationship(
        secondary='aditivos_nutritivos_picole', back_populates='aditivos_nutritivos', lazy='dynamic')


def __repr__(self) -> str:
    return f'<Lote: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'
