"""empty message

Revision ID: 4630383cacef
Revises: 
Create Date: 2018-03-03 13:53:55.049830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4630383cacef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bio', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'bio')
    # ### end Alembic commands ###
