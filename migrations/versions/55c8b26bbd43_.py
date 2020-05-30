"""empty message

Revision ID: 55c8b26bbd43
Revises: adc0c6d39b18
Create Date: 2020-05-30 20:16:51.385007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55c8b26bbd43'
down_revision = 'adc0c6d39b18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'comments', 'courses', ['course_id'], ['id'])
    op.create_foreign_key(None, 'courses', 'admins', ['admin_id'], ['id'])
    op.create_foreign_key(None, 'courses', 'modules', ['module_id'], ['id'])
    op.create_foreign_key(None, 'scores', 'courses', ['course_id'], ['id'])
    op.create_foreign_key(None, 'scores', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'user_course', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'user_course', 'courses', ['course_id'], ['id'])
    op.create_unique_constraint(None, 'user_search_histories', ['content'])
    op.create_foreign_key(None, 'user_search_histories', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_search_histories', type_='foreignkey')
    op.drop_constraint(None, 'user_search_histories', type_='unique')
    op.drop_constraint(None, 'user_course', type_='foreignkey')
    op.drop_constraint(None, 'user_course', type_='foreignkey')
    op.drop_constraint(None, 'scores', type_='foreignkey')
    op.drop_constraint(None, 'scores', type_='foreignkey')
    op.drop_constraint(None, 'courses', type_='foreignkey')
    op.drop_constraint(None, 'courses', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    # ### end Alembic commands ###
