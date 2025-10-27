import sqlalchemy as sa

from models.model_base import ModelBase


# Picole pode ter vários conservante
conservantes_picole = sa.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.ForeignKey('picoles.id'), primary_key=True),
    sa.Column('id_conservante', sa.ForeignKey('conservantes.id'), primary_key=True)
)
