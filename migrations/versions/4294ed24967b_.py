"""empty message

Revision ID: 4294ed24967b
Revises: c5d00c1a8ceb
Create Date: 2021-12-19 02:05:48.054048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4294ed24967b"
down_revision = "c5d00c1a8ceb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, "promotors", "states", ["state"], ["id"])
    op.create_foreign_key(None, "people", "venue", ["venuefk"], ["id"])
    op.create_foreign_key(None, "people", "promotors", ["promotorfk"], ["id"])
    op.create_foreign_key(None, "seating_compasity", "venue", ["venuefk"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "seating_compasity", type_="foreignkey")
    op.drop_constraint(None, "people", type_="foreignkey")
    op.drop_constraint(None, "people", type_="foreignkey")
    op.drop_constraint(None, "promotors", type_="foreignkey")
    # ### end Alembic commands ###
