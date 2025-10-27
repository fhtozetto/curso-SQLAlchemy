import sqlalchemy as sa

from models.model_base import ModelBase


# Nota fiscal pode ter vários lotes
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.ForeignKey('notas_fiscais.id'), primary_key=True),
    sa.Column('id_lote', sa.ForeignKey('lotes.id'), primary_key=True),
)
