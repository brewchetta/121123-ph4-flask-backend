"""empty message

Revision ID: 211257f3d159
Revises: 
Create Date: 2024-02-21 14:04:14.543640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '211257f3d159'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('raccoons_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('has_rabies', sa.Boolean(), nullable=True),
    sa.Column('img_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('raccoons_table')
    # ### end Alembic commands ###
