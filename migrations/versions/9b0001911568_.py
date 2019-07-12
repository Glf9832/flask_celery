"""empty message

Revision ID: 9b0001911568
Revises: 
Create Date: 2019-07-10 19:33:18.319939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b0001911568'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=80), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
