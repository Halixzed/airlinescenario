"""Initial migration

Revision ID: 38339e3fcd07
Revises: 
Create Date: 2024-05-20 00:56:47.833745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38339e3fcd07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('airplane',
    sa.Column('numser', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=80), nullable=False),
    sa.Column('model', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('numser')
    )
    op.create_table('city',
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('city_name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('city_id')
    )
    op.create_table('passenger',
    sa.Column('passenger_id', sa.Integer(), nullable=False),
    sa.Column('surname', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('passenger_id')
    )
    op.create_table('staff',
    sa.Column('empnum', sa.Integer(), nullable=False),
    sa.Column('surname', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('salary', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('empnum')
    )
    op.create_table('flight',
    sa.Column('flight_id', sa.Integer(), nullable=False),
    sa.Column('flight_num', sa.String(length=20), nullable=False),
    sa.Column('origin', sa.String(length=80), nullable=False),
    sa.Column('destination', sa.String(length=80), nullable=False),
    sa.Column('flight_date', sa.Date(), nullable=False),
    sa.Column('dep_time', sa.Time(), nullable=False),
    sa.Column('arr_time', sa.Time(), nullable=False),
    sa.Column('airplane_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['airplane_id'], ['airplane.numser'], ),
    sa.PrimaryKeyConstraint('flight_id')
    )
    op.create_table('passenger_contact',
    sa.Column('passenger_id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['passenger_id'], ['passenger.passenger_id'], ),
    sa.PrimaryKeyConstraint('passenger_id')
    )
    op.create_table('pilot',
    sa.Column('pilot_id', sa.Integer(), nullable=False),
    sa.Column('empnum', sa.Integer(), nullable=True),
    sa.Column('type_rating', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['empnum'], ['staff.empnum'], ),
    sa.PrimaryKeyConstraint('pilot_id')
    )
    op.create_table('booking',
    sa.Column('booking_id', sa.Integer(), nullable=False),
    sa.Column('passenger_id', sa.Integer(), nullable=True),
    sa.Column('flight_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['flight_id'], ['flight.flight_id'], ),
    sa.ForeignKeyConstraint(['passenger_id'], ['passenger.passenger_id'], ),
    sa.PrimaryKeyConstraint('booking_id')
    )
    op.create_table('crew_assignment',
    sa.Column('crew_assign_id', sa.Integer(), nullable=False),
    sa.Column('flight_id', sa.Integer(), nullable=True),
    sa.Column('empnum', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['empnum'], ['staff.empnum'], ),
    sa.ForeignKeyConstraint(['flight_id'], ['flight.flight_id'], ),
    sa.PrimaryKeyConstraint('crew_assign_id')
    )
    op.create_table('flight_intermediate_city',
    sa.Column('flight_inter_city_id', sa.Integer(), nullable=False),
    sa.Column('flight_id', sa.Integer(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('sequence_num', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['city.city_id'], ),
    sa.ForeignKeyConstraint(['flight_id'], ['flight.flight_id'], ),
    sa.PrimaryKeyConstraint('flight_inter_city_id')
    )
    op.create_table('pilot_assignment',
    sa.Column('assign_id', sa.Integer(), nullable=False),
    sa.Column('flight_id', sa.Integer(), nullable=True),
    sa.Column('pilot_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['flight_id'], ['flight.flight_id'], ),
    sa.ForeignKeyConstraint(['pilot_id'], ['pilot.pilot_id'], ),
    sa.PrimaryKeyConstraint('assign_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pilot_assignment')
    op.drop_table('flight_intermediate_city')
    op.drop_table('crew_assignment')
    op.drop_table('booking')
    op.drop_table('pilot')
    op.drop_table('passenger_contact')
    op.drop_table('flight')
    op.drop_table('staff')
    op.drop_table('passenger')
    op.drop_table('city')
    op.drop_table('airplane')
    # ### end Alembic commands ###
