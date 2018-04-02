"""Init

Revision ID: 4e6a06bad7a8
Revises: None
Create Date: 2015-09-21 17:30:38.442998

"""

# revision identifiers, used by Alembic.
revision = '4e6a06bad7a8'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clusters',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cluster_name', sa.String(length=250), nullable=True),
    sa.Column('coordinator_host', sa.String(length=255), nullable=True),
    sa.Column('coordinator_port', sa.Integer(), nullable=True),
    sa.Column('coordinator_endpoint', sa.String(length=255), nullable=True),
    sa.Column('broker_host', sa.String(length=255), nullable=True),
    sa.Column('broker_port', sa.Integer(), nullable=True),
    sa.Column('broker_endpoint', sa.String(length=255), nullable=True),
    sa.Column('metadata_last_refreshed', sa.DateTime(), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cluster_name')
    )
    op.create_table('dashboards',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dashboard_title', sa.String(length=500), nullable=True),
    sa.Column('position_json', sa.Text(), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dbs',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('database_name', sa.String(length=250), nullable=True),
    sa.Column('sqlalchemy_uri', sa.String(length=1024), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('database_name')
    )
    op.create_table('datasources',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datasource_name', sa.String(length=255), nullable=True),
    sa.Column('is_featured', sa.Boolean(), nullable=True),
    sa.Column('is_hidden', sa.Boolean(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('default_endpoint', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.Column('cluster_name', sa.String(length=250), sa.ForeignKey("clusters.cluster_name"), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('datasource_name')
    )
    op.create_table('tables',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_name', sa.String(length=250), nullable=True),
    sa.Column('main_dttm_col', sa.String(length=250), nullable=True),
    sa.Column('default_endpoint', sa.Text(), nullable=True),
    sa.Column('database_id', sa.String(length= 1024), sa.ForeignKey("dbs.sqlalchemy_uri"), nullable=False),
    sa.Column('created_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('table_name')
    )
    op.create_table('columns',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datasource_name', sa.String(length=255), nullable=True),
    sa.Column('column_name', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('type', sa.String(length=32), nullable=True),
    sa.Column('groupby', sa.Boolean(), nullable=True),
    sa.Column('count_distinct', sa.Boolean(), nullable=True),
    sa.Column('sum', sa.Boolean(), nullable=True),
    sa.Column('max', sa.Boolean(), nullable=True),
    sa.Column('min', sa.Boolean(), nullable=True),
    sa.Column('filterable', sa.Boolean(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('metrics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('metric_name', sa.String(length=512), nullable=True),
    sa.Column('verbose_name', sa.String(length=1024), nullable=True),
    sa.Column('metric_type', sa.String(length=32), nullable=True),
    sa.Column('datasource_name', sa.String(length=255), sa.ForeignKey("datasources.datasource_name"), nullable=True),
    sa.Column('json', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['datasource_name'], ['datasources.datasource_name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('slices',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slice_name', sa.String(length=250), nullable=True),
    sa.Column('druid_datasource_id', sa.Integer(), sa.ForeignKey("datasources.id"), nullable=True),
    sa.Column('table_id', sa.Integer(), sa.ForeignKey("tables.id"), nullable=True),
    sa.Column('datasource_type', sa.String(length=200), nullable=True),
    sa.Column('datasource_name', sa.String(length=2000), nullable=True),
    sa.Column('viz_type', sa.String(length=250), nullable=True),
    sa.Column('params', sa.Text(), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sql_metrics',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('metric_name', sa.String(length=512), nullable=True),
    sa.Column('verbose_name', sa.String(length=1024), nullable=True),
    sa.Column('metric_type', sa.String(length=32), nullable=True),
    sa.Column('table_id', sa.Integer(), sa.ForeignKey("tables.id"), nullable=True),
    sa.Column('expression', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('table_columns',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), sa.ForeignKey("tables.id"), nullable=True),
    sa.Column('column_name', sa.String(length=255), nullable=True),
    sa.Column('is_dttm', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('type', sa.String(length=32), nullable=True),
    sa.Column('groupby', sa.Boolean(), nullable=True),
    sa.Column('count_distinct', sa.Boolean(), nullable=True),
    sa.Column('sum', sa.Boolean(), nullable=True),
    sa.Column('max', sa.Boolean(), nullable=True),
    sa.Column('min', sa.Boolean(), nullable=True),
    sa.Column('filterable', sa.Boolean(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), sa.ForeignKey("ab_user.id"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dashboard_slices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dashboard_id', sa.Integer(), sa.ForeignKey("dashboards.id"), nullable=True),
    sa.Column('slice_id', sa.Integer(), sa.ForeignKey("slices.id"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dashboard_slices')
    op.drop_table('table_columns')
    op.drop_table('sql_metrics')
    op.drop_table('slices')
    op.drop_table('metrics')
    op.drop_table('columns')
    op.drop_table('tables')
    op.drop_table('datasources')
    op.drop_table('dbs')
    op.drop_table('dashboards')
    op.drop_table('clusters')
    ### end Alembic commands ###
