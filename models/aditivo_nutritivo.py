import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime

from models.model_base import ModelBase


class AditivoNutritivo(ModelBase):
    __tablename__: str = 'aditivos_nutritivos'

    id: orm.Mapped[int] = orm.mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, default=datetime.now, index=True)
    nome: orm.Mapped[str] = orm.mapped_column(sa.String(45), unique=True, nullable=False)
    formula_quimica: orm.Mapped[str] = orm.mapped_column(sa.String(45), unique=True, nullable=False)


def __repr__(self) -> str:
    return f'<Aditivo Nutritivo: {self.nome}>'
