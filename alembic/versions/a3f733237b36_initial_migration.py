"""Initial migration

Revision ID: a3f733237b36
Revises:
Create Date: 2025-07-23 22:30:36.193179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3f733237b36'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'bookmarks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=100), nullable=True),
        sa.Column('url', sa.String(length=255), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('tags', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bookmarks_url'), 'bookmarks', ['url'], unique=True)
    op.create_index(op.f('ix_bookmarks_title'), 'bookmarks', ['title'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_bookmarks_title'), table_name='bookmarks')
    op.drop_index(op.f('ix_bookmarks_url'), table_name='bookmarks')
    op.drop_table('bookmarks')
