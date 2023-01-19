"""add content to posts table

Revision ID: 1903b7ed2fc5
Revises: 27465ac26c9e
Create Date: 2023-01-19 15:10:40.888451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1903b7ed2fc5'
down_revision = '27465ac26c9e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
