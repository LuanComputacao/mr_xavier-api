"""including question type

Revision ID: fbed0f0ca3db
Revises: eebf14afce81
Create Date: 2020-09-20 00:56:14.422638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbed0f0ca3db'
down_revision = 'eebf14afce81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('type', sa.Integer(), server_default='1', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'type')
    # ### end Alembic commands ###