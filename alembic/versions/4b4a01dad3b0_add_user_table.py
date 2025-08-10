"""add user table

Revision ID: 4b4a01dad3b0
Revises: 4eac0944edc3
Create Date: 2025-08-10 16:13:55.737428

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b4a01dad3b0'
down_revision: Union[str, Sequence[str], None] = '4eac0944edc3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    try:
        op.create_table(
            'users',
            sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
            sa.Column('email', sa.String(), nullable=False, unique=True),
            sa.Column('password', sa.String(), nullable=False),
            sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False)
        )
        print("User table created successfully")
    except Exception as e:
        print(f"Error creating user table: {e}")


def downgrade() -> None:
    """Downgrade schema."""
    try:
        op.drop_table('users')
        print("User table dropped successfully")
    except Exception as e:
        print(f"Error dropping user table: {e}")