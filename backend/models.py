from backend import db

class Passenger(db.Model):
    passenger_id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)

    contact = db.relationship('PassengerContact', backref='passenger', uselist=False)
    bookings = db.relationship('Booking', backref='passenger')

    def to_dict(self):
        return {
            'passenger_id': self.passenger_id,
            'surname': self.surname,
            'name': self.name,
            'contact': self.contact.to_dict() if self.contact else None
        }

class PassengerContact(db.Model):
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.passenger_id'), primary_key=True)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'address': self.address,
            'phone': self.phone
        }

class Flight(db.Model):
    flight_id = db.Column(db.Integer, primary_key=True)
    flight_num = db.Column(db.String(20), nullable=False)
    origin = db.Column(db.String(80), nullable=False)
    destination = db.Column(db.String(80), nullable=False)
    flight_date = db.Column(db.Date, nullable=False)
    dep_time = db.Column(db.Time, nullable=False)
    arr_time = db.Column(db.Time, nullable=False)

    airplane_id = db.Column(db.Integer, db.ForeignKey('airplane.numser'))
    airplane = db.relationship('Airplane', backref='flights')

    def to_dict(self):
        return {
            'flight_id': self.flight_id,
            'flight_num': self.flight_num,
            'origin': self.origin,
            'destination': self.destination,
            'flight_date': self.flight_date,
            'dep_time': self.dep_time,
            'arr_time': self.arr_time,
            'airplane': self.airplane.to_dict() if self.airplane else None
        }

class Booking(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.passenger_id'))
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.flight_id'))

    def to_dict(self):
        return {
            'booking_id': self.booking_id,
            'passenger_id': self.passenger_id,
            'flight_id': self.flight_id
        }

class Staff(db.Model):
    empnum = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Numeric, nullable=False)

    def to_dict(self):
        return {
            'empnum': self.empnum,
            'surname': self.surname,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'salary': str(self.salary)
        }

class Pilot(db.Model):
    pilot_id = db.Column(db.Integer, primary_key=True)
    empnum = db.Column(db.Integer, db.ForeignKey('staff.empnum'))
    type_rating = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            'pilot_id': self.pilot_id,
            'empnum': self.empnum,
            'type_rating': self.type_rating
        }

class Airplane(db.Model):
    numser = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            'numser': self.numser,
            'manufacturer': self.manufacturer,
            'model': self.model
        }

class City(db.Model):
    city_id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            'city_id': self.city_id,
            'city_name': self.city_name
        }

class FlightIntermediateCity(db.Model):
    flight_inter_city_id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.flight_id'))
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'))
    sequence_num = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'flight_inter_city_id': self.flight_inter_city_id,
            'flight_id': self.flight_id,
            'city_id': self.city_id,
            'sequence_num': self.sequence_num
        }

class CrewAssignment(db.Model):
    crew_assign_id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.flight_id'))
    empnum = db.Column(db.Integer, db.ForeignKey('staff.empnum'))

    def to_dict(self):
        return {
            'crew_assign_id': self.crew_assign_id,
            'flight_id': self.flight_id,
            'empnum': self.empnum
        }

class PilotAssignment(db.Model):
    assign_id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.flight_id'))
    pilot_id = db.Column(db.Integer, db.ForeignKey('pilot.pilot_id'))

    def to_dict(self):
        return {
            'assign_id': self.assign_id,
            'flight_id': self.flight_id,
            'pilot_id': self.pilot_id
        }
