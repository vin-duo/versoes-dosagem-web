"""parametros

Revision ID: 43d5a5ebbf05
Revises: c1ceecd4f284
Create Date: 2021-09-11 15:44:12.738375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43d5a5ebbf05'
down_revision = 'c1ceecd4f284'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parametros', sa.Column('c_unitario', sa.Integer(), nullable=False))
    op.add_column('parametros', sa.Column('a_unitario', sa.Integer(), nullable=False))
    op.add_column('parametros', sa.Column('b_unitario', sa.Integer(), nullable=False))
    op.add_column('parametros', sa.Column('c_massa', sa.Integer(), nullable=False))
    op.add_column('parametros', sa.Column('a_massa', sa.Integer(), nullable=False))
    op.add_column('parametros', sa.Column('b_massa', sa.Integer(), nullable=False))
    op.add_column('parametros', sa.Column('c_acr', sa.Integer(), nullable=False))
    op.add_column('parametros', sa.Column('a_acr', sa.Integer(), nullable=False))
    op.add_column('parametros', sa.Column('b_acr', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('parametros', 'b_acr')
    op.drop_column('parametros', 'a_acr')
    op.drop_column('parametros', 'c_acr')
    op.drop_column('parametros', 'b_massa')
    op.drop_column('parametros', 'a_massa')
    op.drop_column('parametros', 'c_massa')
    op.drop_column('parametros', 'b_unitario')
    op.drop_column('parametros', 'a_unitario')
    op.drop_column('parametros', 'c_unitario')
    # ### end Alembic commands ###