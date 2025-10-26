import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List
from decimal import Decimal
from datetime import datetime

from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote

# Nota fiscal pode ter vários lotes
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.Integer, sa.ForeignKey(
        'notas_fiscais.id'), primary_key=True),
    sa.Column('id_lote', sa.Integer, sa.ForeignKey('lotes.id'), primary_key=True),
)


class NotaFiscal(ModelBase):
    __tablename__: str = 'notas_fiscais'

    id: orm.Mapped[int] = orm.mapped_column(
        sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, default=datetime.now, index=True)

    valor: orm.Mapped[Decimal] = orm.mapped_column(
        sa.Numeric(8, 2), nullable=False)
    numero_serie: orm.Mapped[str] = orm.mapped_column(
        sa.String(45), nullable=False, unique=True)
    descricao: orm.Mapped[str] = orm.mapped_column(
        sa.String(200), nullable=False)

    id_revendedor: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey('revendedores.id'), nullable=False)
    revendedor: orm.Mapped['Revendedor'] = orm.relationship(back_populates='notas_fiscais', lazy='joined')

    # Uma nota fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal
    lotes: orm.Mapped[List['Lote']] = orm.relationship(
        secondary='lotes_nota_fiscal', back_populates='notas_fiscais', lazy='dynamic')


def __repr__(self) -> str:
    return f'<Nota Fiscal: {self.numero_serie}>'
