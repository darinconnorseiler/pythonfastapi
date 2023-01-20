"""add content column to posts table

Revision ID: be6f87b72b1d
Revises: 6d9c8e172b36
Create Date: 2023-01-20 11:35:48.307462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be6f87b72b1d'
down_revision = '6d9c8e172b36'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
