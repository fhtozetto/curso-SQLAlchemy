import sqlalchemy as sa

from models.model_base import ModelBase


# Picole pode ter vários aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.ForeignKey('picoles.id'), primary_key=True),
    sa.Column('id_aditivo_nutritivo', sa.ForeignKey('aditivos_nutritivos.id'), primary_key=True)
)
