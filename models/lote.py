import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List
from datetime import datetime

from models.model_base import ModelBase
from models.tipos_picole import TipoPicole
from models.nota_fiscal import NotaFiscal


class Lote(ModelBase):
    __tablename__: str = 'lotes'

    id: orm.Mapped[int] = orm.mapped_column(
        sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, default=datetime.now, index=True)
    quantidade: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False)

    id_tipo_picole: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey('tipos_picole.id'), nullable=False)
    tipo_picole: orm.Mapped['TipoPicole'] = orm.relationship(
        back_populates='lotes', lazy='joined')

    notas_fiscais: orm.Mapped[List['NotaFiscal']] = orm.relationship(
        secondary='lotes_nota_fiscal', back_populates='lotes', lazy='dynamic')


def __repr__(self) -> str:
    return f'<Lote: {self.id}>'
