"""empty message

Revision ID: adc0c6d39b18
Revises: 0a7f250bf9c3
Create Date: 2020-05-30 20:14:27.638601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adc0c6d39b18'
down_revision = '0a7f250bf9c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'comments', 'courses', ['course_id'], ['id'])
    op.create_foreign_key(None, 'courses', 'admins', ['admin_id'], ['id'])
    op.create_foreign_key(None, 'courses', 'modules', ['module_id'], ['id'])
    op.create_foreign_key(None, 'scores', 'courses', ['course_id'], ['id'])
    op.create_foreign_key(None, 'scores', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'user_course', 'courses', ['course_id'], ['id'])
    op.create_foreign_key(None, 'user_course', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'user_search_histories', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_search_histories', type_='foreignkey')
    op.drop_constraint(None, 'user_course', type_='foreignkey')
    op.drop_constraint(None, 'user_course', type_='foreignkey')
    op.drop_constraint(None, 'scores', type_='foreignkey')
    op.drop_constraint(None, 'scores', type_='foreignkey')
    op.drop_constraint(None, 'courses', type_='foreignkey')
    op.drop_constraint(None, 'courses', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    # ### end Alembic commands ###
