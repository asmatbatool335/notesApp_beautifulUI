"""rename note table to document

Revision ID: b45d2b02ecd9
Revises: 5bc195fb9597
Create Date: 2025-07-31 16:27:38.286676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b45d2b02ecd9'
down_revision = '5bc195fb9597'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('note', 'document')


def downgrade():
    op.rename_table('document', 'note')
