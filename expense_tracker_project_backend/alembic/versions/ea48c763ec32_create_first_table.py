"""create first table

Revision ID: ea48c763ec32
Revises: 
Create Date: 2024-07-25 20:24:11.722374

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea48c763ec32'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'my_new_table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('description', sa.String(length=200)),
        sa.Column('created_at', sa.DateTime, default=sa.func.current_timestamp())
    )


def downgrade() -> None:
    op.drop_table('my_new_table')
