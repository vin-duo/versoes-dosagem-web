"""empty message

Revision ID: 64ed115bbb3f
Revises: 960ad287dfd5
Create Date: 2021-09-11 23:36:56.305875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64ed115bbb3f'
down_revision = '960ad287dfd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('parametros', 'b_acr')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parametros', sa.Column('b_acr', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
