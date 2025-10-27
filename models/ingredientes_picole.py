import sqlalchemy as sa

from models.model_base import ModelBase


# Picole pode ter vários ingredientes
ingredientes_picole = sa.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey(
        'picoles.id'), primary_key=True),
    sa.Column('id_ingrediente', sa.Integer, sa.ForeignKey(
        'ingredientes.id'), primary_key=True)
)
