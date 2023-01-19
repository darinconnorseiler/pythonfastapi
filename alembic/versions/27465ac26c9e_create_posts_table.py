"""create posts table

Revision ID: 27465ac26c9e
Revises: 
Create Date: 2023-01-19 15:01:12.741539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27465ac26c9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_table('posts')
    pass
