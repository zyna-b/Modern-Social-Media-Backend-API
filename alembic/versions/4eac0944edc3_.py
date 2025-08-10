"""empty message

Revision ID: 4eac0944edc3
Revises: 3de59fce53ec
Create Date: 2025-08-10 16:06:20.360707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4eac0944edc3'
down_revision: Union[str, Sequence[str], None] = '3de59fce53ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    try:
        op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
        print("Content column added successfully")
    except Exception as e:
        print(f"Error adding content column: {e}")


def downgrade() -> None:
    """Downgrade schema."""     
    try:
        op.drop_column('posts', 'content')
        print("Content column dropped successfully")
    except Exception as e:
        print(f"Error dropping content column: {e}")
