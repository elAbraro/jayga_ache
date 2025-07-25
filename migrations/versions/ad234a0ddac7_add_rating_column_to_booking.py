"""Add rating column to Booking

Revision ID: ad234a0ddac7
Revises: 1df1ee390495
Create Date: 2025-01-08 01:50:03.297981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad234a0ddac7'
down_revision = '1df1ee390495'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.drop_column('rating')

    # ### end Alembic commands ###
