import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime

from models.model_base import ModelBase
from models.lote import Lote


class TipoPicole(ModelBase):
    __tablename__: str = 'tipos_picole'

    id: orm.Mapped[int] = orm.mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, default=datetime.now, index=True)
    nome: orm.Mapped[str] = orm.mapped_column(sa.String(45), unique=True, nullable=False)

    lote: orm.Mapped['Lote'] = orm.Relationship(back_populates='tipo_picole')


def __repr__(self) -> str:
    return f'<Tipo Picole: {self.nome}>'
